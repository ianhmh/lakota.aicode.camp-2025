#!/usr/bin/env python3
"""
black_hills_cdo_daily.py
---------------------------------
Download 25 years of daily observations (GHCND) for ten Black Hills COOP stations
and save everything into a single CSV.

Dependencies
------------
pip install requests tqdm

Usage
-----
python black_hills_cdo_daily.py                     # writes black_hills_daily.csv
python black_hills_cdo_daily.py --out mydata.csv    # custom output

Notes
-----
* Your CDO token is hard‑coded below for convenience; remove it if you prefer
  to read from an environment variable.
* CDO enforces 1 000 records per request and a modest rate limit.  The code
  paginates automatically and sleeps 0.2 s per page to stay polite.
"""

import requests, csv, time, argparse, datetime as dt
from pathlib import Path
from tqdm import tqdm

# -----------------------------------------------------------------------
TOKEN   = "AKWgGrxkShJYogEWTwALrQBAkWIxxbJo"        # << keep private >>
STATIONS = [
    "USC00390593",
    "USC00390990",
    "USC00391295",
    "USC00392115",
    "USC00392840",
    "USC00393322",
    "USC00394865",
    "USC00395877",
    "USC00396477",
    "USC00407602",
]
# -----------------------------------------------------------------------

BASE_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
HEADERS  = {"token": TOKEN}

END_DATE   = dt.date.today() - dt.timedelta(days=1)
START_DATE = dt.date(END_DATE.year - 25, 1, 1)

def fetch_station(station_id, start, end):
    sid = f"GHCND:{station_id}"
    params = {
        "datasetid": "GHCND",
        "stationid": sid,
        "startdate": start.isoformat(),
        "enddate":   end.isoformat(),
        "units": "metric",
        "limit": 1000,
        "offset": 1,
        "includemetadata": "false",
    }

    rows = []
    with tqdm(desc=station_id, unit="page") as bar:
        while True:
            r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=30)
            r.raise_for_status()
            chunk = r.json().get("results", [])
            if not chunk:
                break
            rows.extend(chunk)
            bar.update(1)
            params["offset"] += 1000
            time.sleep(0.2)  # be nice to NOAA
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="black_hills_daily.csv", help="output CSV")
    args = ap.parse_args()

    out_file = Path(args.out)
    first = True

    for sid in STATIONS:
        data = fetch_station(sid, START_DATE, END_DATE)
        if not data:
            print(f"[warn] no data for {sid}")
            continue

        keys = ["station", "date", "datatype", "value"]
        mode = "w" if first else "a"
        with out_file.open(mode, newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            if first:
                w.writeheader()
                first = False
            w.writerows(data)

    print(f"Done → {out_file.resolve()}")

if __name__ == "__main__":
    main()
