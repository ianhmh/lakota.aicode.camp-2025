#!/usr/bin/env python3
"""
black_hills_cdo_daily_v2.py
---------------------------------
Download daily GHCND data (25 years) for ten Black Hills COOP stations.

CDO /data endpoint rejects requests where (enddate‑startdate) > 1 year,
so we loop year‑by‑year and paginate each slice.

Dependencies
------------
pip install requests tqdm

Usage
-----
python black_hills_cdo_daily_v2.py               # -> black_hills_daily.csv
python black_hills_cdo_daily_v2.py --years 10    # shorter window

Notes
-----
* Edit TOKEN or read from env var `CDO_TOKEN`.
* Sleeps 0.2 s between requests to stay within 5 req/s limit.
"""

import requests, csv, time, argparse, datetime as dt, os
from pathlib import Path
from tqdm import tqdm

# -----------------------------------------------------------------------
TOKEN = os.getenv("CDO_TOKEN", "AKWgGrxkShJYogEWTwALrQBAkWIxxbJo")
STATIONS = [
    "USC00390593","USC00390990","USC00391295","USC00392115","USC00392840",
    "USC00393322","USC00394865","USC00395877","USC00396477","USC00407602",
]
# -----------------------------------------------------------------------

BASE_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
HEADERS  = {"token": TOKEN}

END_DATE   = dt.date.today() - dt.timedelta(days=1)

def fetch_slice(station, start, end):
    params = {
        "datasetid": "GHCND",
        "stationid": f"GHCND:{station}",
        "startdate": start.isoformat(),
        "enddate":   end.isoformat(),
        "units": "metric",
        "limit": 1000,
        "offset": 1,
        "includemetadata": "false",
    }
    rows = []
    while True:
        r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=30)
        if r.status_code == 400:
            msg = r.json().get("message","400 error")
            raise RuntimeError(f"{station} {start}->{end}: {msg}")
        r.raise_for_status()
        chunk = r.json().get("results", [])
        if not chunk:
            break
        rows.extend(chunk)
        params["offset"] += 1000
        time.sleep(0.2)
    return rows

def yearly_chunks(years_back):
    this_year = END_DATE.year
    for yr in range(this_year - years_back, this_year + 1):
        start = dt.date(yr, 1, 1)
        end   = dt.date(yr, 12, 31)
        if end > END_DATE:
            end = END_DATE
        yield start, end

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="black_hills_daily.csv")
    p.add_argument("--years", type=int, default=25, help="years back from today")
    args = p.parse_args()

    out_path = Path(args.out)
    first = True
    for sid in STATIONS:
        for start, end in yearly_chunks(args.years):
            rows = fetch_slice(sid, start, end)
            if not rows:
                continue
            keys = ["station","date","datatype","value"]
            mode = "w" if first else "a"
            with out_path.open(mode, newline="") as f:
                w = csv.DictWriter(f, fieldnames=keys)
                if first:
                    w.writeheader()
                    first = False
                w.writerows(rows)
        print(f"{sid} done")

    print(f"All stations complete → {out_path.resolve()}")
    print("Tip: import into pandas with pd.read_csv(...) then pivot.")

if __name__ == "__main__":
    main()
