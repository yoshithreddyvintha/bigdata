import pandas as pd
import dask.dataframe as dd
from time import time

# Serial processing using pandas
def process_data_pandas(df):
    """Perform data processing using pandas."""
    print("Processing data using pandas...")
    start_time = time()
    
    # Example processing: Calculate total trips and add a new column
    df['Total Trips'] = df['Trips 1-3 Miles'] + df['Trips 10-25 Miles']
    end_time = time()
    
    print(f"Time taken using pandas: {end_time - start_time:.2f} seconds")
    return df

# Parallel processing using dask
def process_data_dask(file_path):
    """Perform data processing using dask."""
    print("Processing data using dask...")
    start_time = time()
    
    ddf = dd.read_csv(file_path)
    ddf['Total Trips'] = ddf['Trips 1-3 Miles'] + ddf['Trips 10-25 Miles']
    ddf = ddf.compute()
    
    end_time = time()
    print(f"Time taken using dask: {end_time - start_time:.2f} seconds")
    return ddf

if __name__ == "__main__":
    input_file = "data/cleaned_dataset.csv"  # Replace with your input file path

    # Serial processing
    df = pd.read_csv(input_file)
    processed_data_pandas = process_data_pandas(df)

    # Parallel processing
    processed_data_dask = process_data_dask(input_file)
