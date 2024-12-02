import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def train_model(df):
    """Train a regression model to predict total trips."""
    X = df[['Trips 1-3 Miles', 'Trips 10-25 Miles']]  # Features
    y = df['Total Trips']  # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Model Performance:\nMSE: {mse:.2f}, R2: {r2:.2f}")
    return model

if __name__ == "__main__":
    input_file = "data/categorized_dataset.csv"  # Replace with your input file path

    df = pd.read_csv(input_file)
    trained_model = train_model(df)
