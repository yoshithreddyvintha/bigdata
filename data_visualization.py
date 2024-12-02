# File: data_visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path
file_path = "/Users/yoshithreddyvintha/Desktop/Trips_Full Data.csv"

# Load dataset
df = pd.read_csv(file_path)

# Visualization: Seasonal Variability in Travel Behavior
sns.boxplot(data=df, x='Month of Date', y='Total Trips', palette='Set2')
plt.title('Seasonal Variability in Travel Behavior')
plt.xlabel('Month')
plt.ylabel('Total Trips')
plt.show()

# Visualization: Bar Plot (Staying at Home vs. Traveling)
df['Traveling'] = df['People Not Staying at Home']
df['Staying at Home'] = df['Population Staying at Home']
staying_vs_traveling = df.groupby('Month of Date')[['Traveling', 'Staying at Home']].sum()
staying_vs_traveling.plot(kind='bar', figsize=(10, 6))
plt.title('Number of People Staying at Home vs. Traveling')
plt.xlabel('Month')
plt.ylabel('Total Count')
plt.legend(['Traveling', 'Staying at Home'])
plt.show()

# Save visualizations (optional)
plt.savefig("C:/Users/YourName/Documents/Project/output/seasonal_variability.png")
plt.savefig("C:/Users/YourName/Documents/Project/output/staying_vs_traveling.png")
