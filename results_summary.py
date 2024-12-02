
import pandas as pd

# File path
file_path = "/Users/yoshithreddyvintha/Desktop/Trips_Full Data.csv"

# Read results
correlation_results = pd.read_csv(file_path + "correlation_results.csv")

# Summarize results
print("Summary of Results:")
print(correlation_results)
