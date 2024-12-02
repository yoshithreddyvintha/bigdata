import pandas as pd

def categorize_distances(df):
    """Categorize trips into distance bins."""
    bins = [0, 3, 10, 25, 50, 100]
    labels = ['1-3 Miles', '3-10 Miles', '10-25 Miles', '25-50 Miles', '50+ Miles']
    
    df['Distance Category'] = pd.cut(df['Trip Distance'], bins=bins, labels=labels, right=False)
    print("Distance categories added.")
    return df

if __name__ == "__main__":
    input_file = "data/cleaned_dataset.csv"  # Replace with your input file path
    output_file = "data/categorized_dataset.csv"  # Replace with your output file path
    
    df = pd.read_csv(input_file)
    categorized_data = categorize_distances(df)
    categorized_data.to_csv(output_file, index=False)
    print(f"Categorized data saved to {output_file}")
