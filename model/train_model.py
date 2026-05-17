# Import numerical computing library
import numpy as np

# Import data handling library
import pandas as pd

# ==============================
# DATA VISUALIZATION LIBRARIES
# ==============================

# Import plotting library
import matplotlib.pyplot as plt

# Import advanced visualization library
import seaborn as sns

# ==============================
# MACHINE LEARNING LIBRARIES
# ==============================

# Import function to split dataset into training and testing sets
from sklearn.model_selection import train_test_split, cross_val_score

# Import preprocessing tools
from sklearn.preprocessing import (
    StandardScaler,      # Standardize numerical data
    OneHotEncoder,       # Convert categorical data into numerical format
    PolynomialFeatures   # Create polynomial features
)

# Import column transformer for applying different preprocessing
from sklearn.compose import ColumnTransformer

# Import pipeline to combine preprocessing and model
from sklearn.pipeline import Pipeline

# Import Linear Regression model
from sklearn.linear_model import LinearRegression

# Import evaluation metrics
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Import library to save trained model
import joblib

# ==============================
# LOAD DATASET
# ==============================

# Read CSV file into dataframe
df = pd.read_csv('model/train_energy_data.csv')

# ==============================
# ADD RANDOM NOISE
# ==============================

# Set random seed for reproducibility
np.random.seed(42)

# Generate small realistic noise
noise = np.random.normal(
    loc=0,   # Mean of noise
    scale=df['Energy Consumption'].std() * 0.25,  # Noise strength
    size=len(df)  # Number of noise values
)

# Add noise to target column
df['Energy Consumption'] = (
    df['Energy Consumption'] + noise
)

# ==============================
# OUTLIER REMOVAL USING IQR
# ==============================

# Numerical columns for outlier detection
numerical_cols = [
    'Square Footage',
    'Number of Occupants',
    'Appliances Used',
    'Average Temperature',
    'Energy Consumption'
]

# Create copy of dataframe
clean_df = df.copy()

# Loop through each numerical column
for col in numerical_cols:

    # Calculate first quartile (25%)
    Q1 = clean_df[col].quantile(0.25)

    # Calculate third quartile (75%)
    Q3 = clean_df[col].quantile(0.75)

    # Calculate Interquartile Range
    IQR = Q3 - Q1

    # Define lower boundary
    lower = Q1 - 1.5 * IQR

    # Define upper boundary
    upper = Q3 + 1.5 * IQR

    # Keep only rows inside boundaries
    clean_df = clean_df[
        (clean_df[col] >= lower) &
        (clean_df[col] <= upper)
    ]

# Print cleaned dataset shape
print("Clean Shape:", clean_df.shape)

# ==============================
# USE CLEANED DATA
# ==============================

# Replace original dataframe with cleaned dataframe
df = clean_df.copy()

# ==============================
# DEFINE FEATURES AND TARGET
# ==============================

# Features (independent variables)
X = df.drop('Energy Consumption', axis=1)

# Target variable (dependent variable)
y = df['Energy Consumption']

# Categorical columns
categorical_cols = [
    'Building Type',
    'Day of Week'
]

# Numerical columns
numerical_cols = [
    col for col in X.columns
    if col not in categorical_cols
]

# ==============================
# DATA PREPROCESSING
# ==============================

# Create preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[

        # Numerical preprocessing
        (
            'num',
            Pipeline([

                # Standardize numerical data
                ('scaler', StandardScaler()),

                # Generate polynomial features
                ('poly', PolynomialFeatures(
                    degree=1,          # Linear features only
                    include_bias=False
                ))
            ]),
            numerical_cols
        ),

        # Categorical preprocessing
        (
            'cat',

            # Convert categories into dummy variables
            OneHotEncoder(drop='first'),

            categorical_cols
        )
    ]
)

# ==============================
# TRAIN TEST SPLIT
# ==============================

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,   # 20% test data
    random_state=42
)

# ==============================
# CREATE MACHINE LEARNING MODEL
# ==============================

# Create complete pipeline
model = Pipeline([

    # Apply preprocessing
    ('preprocessor', preprocessor),

    # Apply Linear Regression
    ('regressor', LinearRegression())
])

# ==============================
# TRAIN MODEL
# ==============================

# Train model on training data
model.fit(X_train, y_train)

# ==============================
# MAKE PREDICTIONS
# ==============================

# Predict values on test data
y_pred = model.predict(X_test)

# ==============================
# MODEL EVALUATION
# ==============================

# Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Root Mean Squared Error
rmse = np.sqrt(mse)

# R² Score
r2 = r2_score(y_test, y_pred)

# ==============================
# PRINT RESULTS
# ==============================

print("\n===== MODEL PERFORMANCE =====")

print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R2   :", r2)

# Save trained pipeline
joblib.dump(model, 'model/energy_model.pkl')

print("Model saved successfully!")