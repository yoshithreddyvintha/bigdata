import matplotlib.pyplot as plt
import pandas as pd

# Define tasks and timelines
data = {
    "Task": [
        "Data Collection",
        "Data Cleaning",
        "Data Processing",
        "Model Building",
        "Model Testing",
        "Data Visualization",
        "Final Report"
    ],
    "Start": ["2024-11-12", "2024-11-16", "2024-11-23", "2024-11-27", "2024-11-30", "2024-12-01", "2024-12-02"],
    "End": ["2024-11-15", "2024-11-19", "2024-11-24", "2024-11-29", "2024-11-30", "2024-12-01", "2024-12-02"],
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])
df["Duration"] = (df["End"] - df["Start"]).dt.days

# Create Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))
for i, task in enumerate(df["Task"]):
    ax.barh(task, df["Duration"].iloc[i], left=df["Start"].iloc[i], color="skyblue")

ax.set_xlabel("Date")
ax.set_ylabel("Task")
ax.set_title("Project Timeline (Gantt Chart)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the Gantt chart
plt.savefig("output/gantt_chart.png")
plt.show()
