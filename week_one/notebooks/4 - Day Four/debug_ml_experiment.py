#!/usr/bin/env python3
"""
Debug script for the Machine Learning Experiment cell
This recreates all dependencies and runs the ML experiment standalone
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def create_ml_dataset_from_weather_data():
    """Recreate the real_ml_df dataframe from the weather data"""
    
    # Load the weather data
    try:
        weather_df = pd.read_csv('rapid_city_weather.csv')
    except FileNotFoundError:
        print("Error: rapid_city_weather.csv not found in current directory")
        print("Please run this script from the same directory as the CSV file")
        return None
    
    # Clean and prepare the data
    weather_df['DATE'] = pd.to_datetime(weather_df['DATE'])
    weather_df['Year'] = weather_df['DATE'].dt.year
    weather_df['Month'] = weather_df['DATE'].dt.month
    weather_df['Day_of_Year'] = weather_df['DATE'].dt.dayofyear
    
    print("📊 Creating ML dataset from weather data...")
    
    # Calculate annual and growing season statistics for each year
    ml_data = []
    
    for year in range(2000, 2025):
        year_data = weather_df[weather_df['Year'] == year]
        
        if len(year_data) < 300:  # Skip years with insufficient data
            continue
            
        # Temperature statistics
        avg_temp = year_data['TAVG'].mean()
        max_temp = year_data['TMAX'].max()
        min_temp = year_data['TMIN'].min()
        
        # Precipitation statistics
        annual_precip = year_data['PRCP'].sum()
        
        # Growing season statistics (May-September)
        gs_data = year_data[year_data['Month'].isin([5, 6, 7, 8, 9])]
        gs_avg_temp = gs_data['TMAX'].mean()
        gs_precip = gs_data['PRCP'].sum()
        
        # Calculate frost dates and growing season length
        frost_data = year_data[year_data['TMIN'] <= 32]
        spring_frosts = frost_data[frost_data['Month'] <= 6]
        fall_frosts = frost_data[frost_data['Month'] >= 7]
        
        if not spring_frosts.empty and not fall_frosts.empty:
            last_spring_frost = spring_frosts['Day_of_Year'].max()
            first_fall_frost = fall_frosts['Day_of_Year'].min()
            growing_days = first_fall_frost - last_spring_frost
        else:
            # Handle edge cases
            last_spring_frost = 120  # April 30
            first_fall_frost = 280   # October 7
            growing_days = 160
        
        # Heat and water stress indicators
        heat_stress_days = (year_data['TMAX'] >= 95).sum()  # Days above 95°F
        drought_days = (year_data['PRCP'] <= 0.01).sum()    # Essentially dry days
        
        # Calculate crop suitability based on real requirements
        corn_suitability = min(1.0, growing_days / 90) * min(1.0, gs_precip / 12)
        bean_suitability = min(1.0, growing_days / 100) * min(1.0, gs_precip / 14)
        squash_suitability = min(1.0, growing_days / 120) * min(1.0, gs_precip / 15)
        
        # Overall season quality
        avg_suitability = (corn_suitability + bean_suitability + squash_suitability) / 3
        if avg_suitability >= 0.85:
            season_quality = 'Excellent'
        elif avg_suitability >= 0.70:
            season_quality = 'Good'
        elif avg_suitability >= 0.50:
            season_quality = 'Fair'
        else:
            season_quality = 'Challenging'
        
        ml_data.append({
            'Year': year,
            'Avg_Temp_F': round(avg_temp, 1),
            'Max_Temp_F': round(max_temp, 1),
            'Min_Temp_F': round(min_temp, 1),
            'Annual_Precip_In': round(annual_precip, 1),
            'GS_Avg_Temp_F': round(gs_avg_temp, 1),
            'GS_Precip_In': round(gs_precip, 1),
            'Last_Spring_Frost_Day': int(last_spring_frost),
            'First_Fall_Frost_Day': int(first_fall_frost),
            'Growing_Days': int(growing_days),
            'Heat_Stress_Days': int(heat_stress_days),
            'Drought_Days': int(drought_days),
            'Corn_Suitability': round(corn_suitability, 3),
            'Bean_Suitability': round(bean_suitability, 3),
            'Squash_Suitability': round(squash_suitability, 3),
            'Season_Quality': season_quality
        })
    
    # Create DataFrame
    real_ml_df = pd.DataFrame(ml_data)
    print(f"✅ ML dataset created: {real_ml_df.shape}")
    return real_ml_df

def run_ml_experiment(real_ml_df):
    """Run the machine learning experiment"""
    
    # 🤖 EXPERIMENT 2: Interactive Machine Learning
    # Build your own models to answer specific questions!
    
    # 🎯 CHOOSE WHAT TO PREDICT (target variable):
    target = 'Season_Quality'  # Try: 'Season_Quality', 'Growing_Days', 'Corn_Suitability', 'Bean_Suitability'
    
    # 🔧 CHOOSE YOUR FEATURES (what to predict FROM):
    # Pick features you think are most important for your prediction
    use_temperature = True        # Include temperature-related features
    use_precipitation = True      # Include precipitation-related features  
    use_growing_days = True      # Include growing season length
    use_stress_indicators = False # Include heat stress and drought indicators
    
    # 🧠 CHOOSE YOUR MODEL TYPE:
    model_type = 'random_forest'  # Options: 'random_forest', 'linear', 'logistic'
    
    # 📊 EXPERIMENT SETTINGS:
    test_size = 0.3              # Fraction of data to use for testing (0.1 to 0.5)
    show_feature_importance = True  # Show which features matter most
    show_predictions = True      # Show actual vs predicted values
    
    print(f"🎯 Predicting: {target}")
    print(f"🔧 Using model: {model_type}")
    print("=" * 50)
    
    # Build feature list based on your choices
    features = []
    if use_temperature:
        features.extend(['GS_Avg_Temp_F', 'Max_Temp_F', 'Min_Temp_F'])
    if use_precipitation:
        features.extend(['Annual_Precip_In', 'GS_Precip_In'])
    if use_growing_days:
        features.extend(['Growing_Days', 'Last_Spring_Frost_Day', 'First_Fall_Frost_Day'])
    if use_stress_indicators:
        features.extend(['Heat_Stress_Days', 'Drought_Days'])
    
    # Remove target from features if accidentally included
    if target in features:
        features.remove(target)
    
    print(f"📋 Features selected: {len(features)}")
    for i, feature in enumerate(features, 1):
        print(f"   {i}. {feature}")
    
    # Debug: Check if features exist in dataframe
    print(f"\n🔍 Debug - Available columns in real_ml_df:")
    print(list(real_ml_df.columns))
    
    missing_features = [f for f in features if f not in real_ml_df.columns]
    if missing_features:
        print(f"\n❌ Missing features: {missing_features}")
        return
    
    # Prepare data
    model_data = real_ml_df[features + [target]].dropna()
    X = model_data[features]
    y = model_data[target]
    
    print(f"\n📊 Data ready: {len(model_data)} samples, {len(features)} features")
    
    if len(model_data) == 0:
        print("❌ No data available after filtering!")
        return
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Choose and train model
    if model_type == 'random_forest':
        if target in ['Season_Quality']:  # Classification
            model = RandomForestClassifier(n_estimators=100, random_state=42)
        else:  # Regression
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            
    elif model_type == 'linear':
        if target in ['Season_Quality']:  # Logistic regression for categories
            model = LogisticRegression(random_state=42, max_iter=1000)
        else:  # Linear regression for numbers
            model = LinearRegression()
            
    elif model_type == 'logistic':
        model = LogisticRegression(random_state=42, max_iter=1000)
    
    # Train the model
    print(f"\n🚀 Training {model_type} model...")
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate performance
    print(f"\n📈 MODEL PERFORMANCE:")
    if target in ['Season_Quality']:  # Classification metrics
        accuracy = accuracy_score(y_test, y_pred)
        print(f"   Accuracy: {accuracy:.2f} ({accuracy*100:.1f}%)")
        
        print(f"\n📊 Detailed Results:")
        print(classification_report(y_test, y_pred))
        
    else:  # Regression metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        print(f"   R² Score: {r2:.3f} ({r2*100:.1f}% of variance explained)")
        print(f"   RMSE: {rmse:.2f}")
        print(f"   Average error: ±{rmse:.2f}")
    
    # Show feature importance
    if show_feature_importance and hasattr(model, 'feature_importances_'):
        print(f"\n🔍 FEATURE IMPORTANCE:")
        importances = model.feature_importances_
        feature_importance = list(zip(features, importances))
        feature_importance.sort(key=lambda x: x[1], reverse=True)
        
        for feature, importance in feature_importance:
            print(f"   {feature}: {importance:.3f}")
    
    # Show some predictions
    if show_predictions:
        print(f"\n🎯 SAMPLE PREDICTIONS:")
        print("Actual | Predicted | Year")
        print("-" * 30)
        
        # Get some test samples with their years
        test_indices = X_test.index
        for i in range(min(8, len(test_indices))):
            idx = test_indices[i]
            actual = y_test.iloc[i]
            predicted = y_pred[i]
            year = model_data.loc[idx, 'Year'] if 'Year' in model_data.columns else 'N/A'
            
            if target in ['Season_Quality']:
                print(f"{actual:>6} | {predicted:>9} | {year}")
            else:
                print(f"{actual:>6.1f} | {predicted:>9.1f} | {year}")
    
    # Experiment suggestions
    print(f"\n💡 EXPERIMENT IDEAS:")
    print(f"   🔄 Change target to predict different things")
    print(f"   🔧 Try different feature combinations:")
    print(f"      • Temperature only: What can temperature alone predict?")
    print(f"      • Precipitation only: How important is rainfall?")
    print(f"      • All features: Does more data = better predictions?")
    print(f"   🧠 Compare model types: Which works best for your question?")
    print(f"   📊 Try different test_size: How does training data amount affect performance?")
    
    print(f"\n🌾 AGRICULTURAL QUESTIONS TO EXPLORE:")
    print(f"   • Can we predict Three Sisters success from temperature alone?")
    print(f"   • Which weather factors best predict growing season quality?")
    print(f"   • How well can we predict next year's growing conditions?")
    print(f"   • What's the minimum data needed for good crop predictions?")

def main():
    """Main function to run the debug script"""
    print("🐛 DEBUG SCRIPT: Machine Learning Experiment")
    print("=" * 60)
    
    # Step 1: Create the ML dataset
    real_ml_df = create_ml_dataset_from_weather_data()
    
    if real_ml_df is None:
        print("❌ Failed to create dataset. Exiting.")
        return
    
    print(f"\n📋 Dataset info:")
    print(f"   Shape: {real_ml_df.shape}")
    print(f"   Columns: {list(real_ml_df.columns)}")
    print(f"   Sample data:")
    print(real_ml_df.head(3))
    
    # Step 2: Run the ML experiment
    print(f"\n" + "="*60)
    run_ml_experiment(real_ml_df)

if __name__ == "__main__":
    main()