
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# File path
file_path = "C:/Users/YourName/Documents/Project/data/cleaned_data.csv"

# Load dataset
df = pd.read_csv(file_path)

# Example analysis: Correlation analysis between trip distances and total trips
distance_columns = ['Trips 1-3 Miles', 'Trips 10-25 Miles', 'Trips 100-250 Miles']
correlations = {}
for col in distance_columns:
    correlations[col] = pearsonr(df[col], df['Total Trips'])[0]

print("Correlation with Total Trips:")
for k, v in correlations.items():
    print(f"{k}: {v:.2f}")

# Save analysis results
correlation_path = "C:/Users/YourName/Documents/Project/output/correlation_results.csv"
pd.DataFrame(list(correlations.items()), columns=["Distance Category", "Correlation"]).to_csv(correlation_path, index=False)
