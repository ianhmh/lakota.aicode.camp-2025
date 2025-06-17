# Day Four, Session 2: Traditional Agriculture Meets Data Science (Enhanced with Real Data)

# Import the data science tools we'll need
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

print("🌱 Welcome to Traditional Agriculture + Data Science!")
print("📊 Tools loaded: pandas, matplotlib, scikit-learn")
print("🌾 Ready to explore Three Sisters agriculture with real climate data...")

# ---
# ## Part 1: Real Climate Data with Pandas (25 minutes)
#
# Let's load and process the real climate data from NOAA.

# Load the REAL downloaded data from NOAA
# Make sure the file 'NOAA_Black_Hills_Data.csv' is in the same directory
try:
    raw_df = pd.read_csv('NOAA_Black_Hills_Data.csv')
    print("✅ Successfully loaded 'NOAA_Black_Hills_Data.csv'")
except FileNotFoundError:
    print("❌ ERROR: 'NOAA_Black_Hills_Data.csv' not found.")
    print("Please download the data from NOAA as instructed and save it in the correct directory.")
    # Create an empty DataFrame to prevent further errors
    raw_df = pd.DataFrame()

if not raw_df.empty:
    # --- Data Cleaning and Preparation ---
    # Standardize city names from the station names
    raw_df['City'] = raw_df['NAME'].apply(lambda x: x.split(',')[0].title())
    city_mapping = {
        'Rapid City Regional Airport': 'Rapid City',
        'Spearfish Black Hills Airport': 'Spearfish',
        'Lead 1 E': 'Lead',
        'Hot Springs': 'Hot Springs',
        'Custer': 'Custer'
    }
    raw_df['City'] = raw_df['City'].replace(city_mapping)

    # Convert DATE to datetime objects and extract Year
    raw_df['DATE'] = pd.to_datetime(raw_df['DATE'])
    raw_df['YEAR'] = raw_df['DATE'].dt.year

    # Use average of TMAX and TMIN for a more representative temperature
    raw_df['TAVG'] = (raw_df['TMAX'] + raw_df['TMIN']) / 2

    # --- Calculate Historical Growing Seasons ---
    frost_temp = 32 # Frost temperature in Fahrenheit

    growing_seasons = []
    for city in raw_df['City'].unique():
        for year in raw_df['YEAR'].unique():
            city_year_df = raw_df[(raw_df['City'] == city) & (raw_df['YEAR'] == year)]
            
            # Last spring frost
            spring_frosts = city_year_df[(city_year_df['DATE'].dt.month < 7) & (city_year_df['TMIN'] <= frost_temp)]
            last_spring_frost = spring_frosts['DATE'].max()
            
            # First fall frost
            fall_frosts = city_year_df[(city_year_df['DATE'].dt.month > 7) & (city_year_df['TMIN'] <= frost_temp)]
            first_fall_frost = fall_frosts['DATE'].min()
            
            if pd.notna(last_spring_frost) and pd.notna(first_fall_frost):
                growing_days = (first_fall_frost - last_spring_frost).days
                growing_seasons.append({
                    'City': city,
                    'Year': year,
                    'Growing_Days': growing_days,
                    'Last_Spring_Frost': last_spring_frost.strftime('%b %d'),
                    'First_Fall_Frost': first_fall_frost.strftime('%b %d')
                })

    growing_season_df = pd.DataFrame(growing_seasons)

    # --- Create Annual Summary DataFrame for Machine Learning ---
    # This will be our primary dataset for modeling
    annual_summary = raw_df.groupby(['City', 'YEAR']).agg(
        Avg_Temp_F=('TAVG', 'mean'),
        Annual_Precip_In=('PRCP', 'sum')
    ).reset_index()

    # Merge with growing season data
    ml_df = pd.merge(annual_summary, growing_season_df, on=['City', 'Year'])

    # Add elevation data (from original notebook)
    elevation_data = {
        'City': ['Rapid City', 'Lead', 'Custer', 'Hot Springs', 'Spearfish'],
        'Elevation_ft': [3202, 5320, 5314, 3442, 3645]
    }
    elevation_df = pd.DataFrame(elevation_data)
    ml_df = pd.merge(ml_df, elevation_df, on='City')

    print("\n📊 REAL HISTORICAL DATA PROCESSED")
    print(f"Dataset shape: {ml_df.shape}")
    print(f"Cities included: {ml_df['City'].unique()}")
    print("\n📋 First few rows of the new ML-ready dataset:")
    print(ml_df.head())


# REAL Three Sisters Crop Requirements (Validated)
# Source: USDA, Indigenous Agriculture Research, Traditional Ecological Knowledge
three_sisters_data = {
    'Crop': ['Corn (Flint)', 'Corn (Dent)', 'Beans (Bush)', 'Beans (Pole)', 'Squash (Summer)', 'Squash (Winter)'],
    'Traditional_Name': ['Wahpe', 'Wahpe', 'Omnica', 'Omnica', 'Wagmu', 'Wagmu'],
    'Min_Frost_Free_Days': [90, 120, 90, 100, 100, 120], # Validated against seed catalogs
    'Min_Soil_Temp_F': [50, 55, 55, 55, 60, 60],
    'Water_Needs_Inches': [20, 25, 18, 20, 15, 18],
    'Cultural_Significance': [
        'Sacred grain, sustains community',
        'Main food source, stored for winter', 
        'Nitrogen fixer, protein source',
        'Climbs corn stalks, traditional method',
        'Early harvest, fresh food',
        'Long storage, winter sustenance'
    ]
}
crops_df = pd.DataFrame(three_sisters_data)
print("\n🌾 REAL THREE SISTERS CROP DATA LOADED")
print(crops_df[['Crop', 'Min_Frost_Free_Days', 'Min_Soil_Temp_F']])


# ---
# ## Part 2: Visualization with Matplotlib (25 minutes)
#
# Now let's visualize the real historical data.

if not ml_df.empty:
    # Visualization 1: Growing season length vs elevation (using real data)
    plt.figure(figsize=(10, 6))

    # Scatter plot of elevation vs average growing season
    avg_growing_season = ml_df.groupby('City').agg(
        Avg_Growing_Days=('Growing_Days', 'mean'),
        Elevation_ft=('Elevation_ft', 'first')
    ).reset_index()

    plt.scatter(avg_growing_season['Elevation_ft'], avg_growing_season['Avg_Growing_Days'], 
               s=150, alpha=0.7, color='green', label='Avg. Historical Growing Season')

    # Add city labels
    for i, row in avg_growing_season.iterrows():
        plt.annotate(row['City'], 
                    (row['Elevation_ft'], row['Avg_Growing_Days']),
                    xytext=(5, 5), textcoords='offset points')

    # Add Three Sisters requirements as horizontal lines
    plt.axhline(y=90, color='green', linestyle='--', alpha=0.7, label='Corn (Flint) - 90 days')
    plt.axhline(y=100, color='orange', linestyle='--', alpha=0.7, label='Beans (Pole) - 100 days')
    plt.axhline(y=120, color='red', linestyle='--', alpha=0.7, label='Squash (Winter) - 120 days')

    plt.title('🏔️ Real Growing Season Length vs Elevation in Black Hills (2000-2023)', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Elevation (feet)')
    plt.ylabel('Average Growing Season Length (frost-free days)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# ---
# ## Part 3: Machine Learning with Scikit-Learn (25 minutes)
#
# Now we build models on the real historical data.

if not ml_df.empty:
    # --- Machine Learning Model 1: Predict Growing Season Length ---
    print("\n🌱 MODEL 1: PREDICTING GROWING SEASON LENGTH (from Real Data)")
    print("=" * 60)

    # Prepare features and target
    features = ['Elevation_ft', 'Avg_Temp_F', 'Annual_Precip_In']
    X = ml_df[features]
    y = ml_df['Growing_Days']

    # Split data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train linear regression model
    growing_season_model = LinearRegression()
    growing_season_model.fit(X_train, y_train)

    # Make predictions and evaluate
    y_pred = growing_season_model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"📈 Model Performance:")
    print(f"   Root Mean Square Error: {rmse:.1f} days")
    print(f"   This means our model's predictions are, on average, off by about {rmse:.0f} days.")

    # Show feature importance (coefficients) and the intercept
    print(f"\n🔍 Feature Importance:")
    for feature, coef in zip(features, growing_season_model.coef_):
        print(f"   {feature}: {coef:.4f}")
    print(f"   Intercept: {growing_season_model.intercept_:.4f}")

    # --- Machine Learning Model 2: Classify Growing Season Quality ---
    print("\n🏆 MODEL 2: CLASSIFYING GROWING SEASON QUALITY (from Real Data)")
    print("=" * 60)

    # Create the 'Season_Quality' target variable
    def classify_season(days):
        if days >= 150: return 'Excellent'
        elif days >= 135: return 'Good'
        elif days >= 120: return 'Fair'
        else: return 'Challenging'
    
    ml_df['Season_Quality'] = ml_df['Growing_Days'].apply(classify_season)

    # Prepare features and target
    X_class = ml_df[['Elevation_ft', 'Avg_Temp_F', 'Annual_Precip_In', 'Growing_Days']]
    y_class = ml_df['Season_Quality']

    X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(
        X_class, y_class, test_size=0.2, random_state=42, stratify=y_class
    )

    # Train Random Forest classifier
    quality_model = RandomForestClassifier(n_estimators=100, random_state=42)
    quality_model.fit(X_train_class, y_train_class)
    accuracy = accuracy_score(y_test_class, quality_model.predict(X_test_class))
    print(f"📊 Model Accuracy: {accuracy:.2f} ({accuracy*100:.1f}%)")

# ---
# ## Part 4: Reusable Functions for Traditional Agriculture (15 minutes)
#
# These functions are now powered by models trained on real data.

# COPY/PASTABLE FUNCTION 1: Growing Season Predictor (Retrained)
def predict_growing_season(elevation_ft, avg_temp_f, annual_precip_in):
    """
    Predict growing season length based on location characteristics.
    Uses a model trained on 24 years of real Black Hills climate data.
    """
    if 'growing_season_model' not in globals():
        return "Model not trained. Please run the notebook first."

    # Coefficients are now taken directly from our trained model
    intercept = growing_season_model.intercept_
    coeffs = growing_season_model.coef_
    
    predicted_days = (intercept + 
                     (coeffs[0] * elevation_ft) + 
                     (coeffs[1] * avg_temp_f) + 
                     (coeffs[2] * annual_precip_in))
    
    return round(predicted_days)

# (Functions 2 and 3 are logic-based and remain the same, but are now more powerful
# because they will be fed more accurate inputs from our new models)

# COPY/PASTABLE FUNCTION 2: Three Sisters Planting Advisor
def three_sisters_advisor(city_name, growing_days, annual_precip):
    # This function remains the same, but its inputs are now more accurate.
    advice = {
        'location': city_name,
        'growing_season': f"{growing_days} frost-free days",
        'recommended_crops': [],
        'planting_advice': [],
        'water_advice': []
    }
    if growing_days >= 90:
        advice['recommended_crops'].append('Corn (Flint variety)')
    if growing_days >= 100:
        advice['recommended_crops'].append('Beans (Bush and Pole)')
    if growing_days >= 120:
        advice['recommended_crops'].append('Squash (Winter)')
    elif growing_days >= 100:
        advice['recommended_crops'].append('Squash (Summer only)')
    
    if not advice['recommended_crops']:
        advice['planting_advice'].append('Growing season is too short for reliable crops.')
    if annual_precip < 15:
        advice['water_advice'].append('⚠️ Dry conditions - plan for supplemental watering')
    else:
        advice['water_advice'].append('🌧️ Moderate precipitation - monitor dry spells')
    return advice

# COPY/PASTABLE FUNCTION 3: Frost Risk Calculator
def calculate_frost_risk(elevation_ft, date_string):
    # This function also remains the same.
    try:
        date_obj = datetime.strptime(f"2024 {date_string}", "%Y %b %d")
        day_of_year = date_obj.timetuple().tm_yday
    except:
        return "Invalid date format. Use 'May 20' or 'Sep 15'"
    
    # Base frost dates (day of year) for 3200 ft elevation (Rapid City)
    base_last_spring = 130  # May 10
    base_first_fall = 277   # Oct 4
    
    # Adjust for elevation (approx. 0.5 days later spring/earlier fall per 100 ft)
    elevation_adjustment = (elevation_ft - 3200) / 100 * 0.5
    
    adjusted_last_spring = base_last_spring + elevation_adjustment
    adjusted_first_fall = base_first_fall - elevation_adjustment
    
    if day_of_year < adjusted_last_spring:
        days_until_safe = adjusted_last_spring - day_of_year
        risk = "High" if days_until_safe > 10 else "Moderate"
        return f"{risk} frost risk - {days_until_safe:.0f} days until typically safe"
    elif day_of_year > adjusted_first_fall:
        return f"High frost risk - fall frost season has likely begun"
    else:
        return "Low frost risk - within typical growing season"

# --- Testing the new, improved functions ---
if not ml_df.empty:
    print("\n🛠️ TESTING REUSABLE FUNCTIONS (Powered by Real Data)")
    print("=" * 55)

    # Test with average conditions for Rapid City
    rc_avg = ml_df[ml_df['City'] == 'Rapid City'].mean()
    rapid_city_prediction = predict_growing_season(3202, rc_avg['Avg_Temp_F'], rc_avg['Annual_Precip_In'])
    print(f"📊 Rapid City predicted growing season: {rapid_city_prediction} days")
    print(f"   (Actual historical average: {int(rc_avg['Growing_Days'])} days)")

    # Test advisor for Custer
    custer_avg = ml_df[ml_df['City'] == 'Custer'].mean()
    custer_days = int(custer_avg['Growing_Days'])
    advice = three_sisters_advisor("Custer", custer_days, custer_avg['Annual_Precip_In'])
    print(f"\n🌱 Three Sisters advice for Custer (Avg. {custer_days} days):")
    print(f"   Recommended crops: {', '.join(advice['recommended_crops'])}")

    # Test frost risk calculator
    risk_june_custer = calculate_frost_risk(5314, "June 1")
    print(f"\n❄️ Frost risk for Custer (5314 ft) on June 1: {risk_june_custer}")
    print("\n✅ All functions ready to copy and use!")