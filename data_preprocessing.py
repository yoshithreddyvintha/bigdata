import pandas as pd

# Load dataset
def load_data(file_path):
    """Load dataset from a CSV file."""
    try:
        df = pd.read_csv(/Users/yoshithreddyvintha/Desktop/Trips_Full Data.csv)
        print("Data successfully loaded!")
        return df
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return None

# Basic cleaning
def clean_data(df):
    """Clean dataset by handling missing values and duplicates."""
    print("Initial shape:", df.shape)
    
    # Drop duplicates
    df = df.drop_duplicates()
    print("Shape after dropping duplicates:", df.shape)
    
    # Fill missing numeric values with median
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Fill missing categorical values with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    print("Missing values handled.")
    return df

# Save cleaned data
def save_clean_data(df, output_path):
    """Save cleaned data to a new CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

# Main execution
if __name__ == "__main__":
    input_file = "data/raw_dataset.csv"  # Replace with your input file path
    output_file = "data/cleaned_dataset.csv"  # Replace with your output file path

    data = load_data(input_file)
    if data is not None:
        cleaned_data = clean_data(data)
        save_clean_data(cleaned_data, output_file)
