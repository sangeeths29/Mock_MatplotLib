'''
Mock_MatplotLib
Problem 1 - https://tinyurl.com/MatplotlibInterviewQuestion
Imagine you are working for a travel agency named "Wanderlust Adventures." Your team has been assigned a project to analyze and visualize the travel data for the past year. The data includes information about various destinations, the number of travelers per month, and the revenue generated. As the data analyst, you decide to use Matplotlib to create insightful visualizations.
As a data analyst at "Wanderlust Adventures," you have been given a dataset containing monthly travel data for different destinations. The dataset includes information about the number of travelers and the revenue generated each month. Your task is to create three visualizations using Matplotlib: a line plot, a pie chart, and a scatter plot.

Line Plot: Create a line plot using Matplotlib that illustrates the trend of both traveler count and revenue over the past year. The x-axis should represent the months, while the y-axis should represent the traveler count and revenue, respectively. The line plot should display two lines, one for traveler count and another for revenue, showcasing their trends over time.
Pie Chart: Generate a pie chart using Matplotlib to display the distribution of traveler count among the top five destinations for the entire year. Each slice of the pie should represent a destination, and its size should correspond to the proportion of travelers visiting that particular destination.
Scatter Plot: Create a scatter plot using Matplotlib that demonstrates the relationship between the number of travelers and the revenue generated for each month. Each data point on the scatter plot should represent a month, with the x-coordinate representing the traveler count and the y-coordinate representing the revenue generated.
Note: Use the file called "travel.csv"
'''
# Step 1 - Import and Load Data
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
df = pd.read_csv("travel.csv")

# Step 2 - Line Plot
# Aggregate by month
monthly_totals = (
    df.groupby("Month", observed=True)[["Travelers", "Revenue"]]
      .sum(numeric_only=True)
      .sort_index()
)

# Plot (two lines on one chart)
plt.figure(figsize=(10, 6))
plt.plot(monthly_totals.index, monthly_totals["Travelers"], marker="o", label="Travelers")
plt.plot(monthly_totals.index, monthly_totals["Revenue"], marker="s", label="Revenue")
plt.title("Monthly Travelers and Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Count / Revenue")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 3 - Pie Chart
# Sum travelers per destination and take the top 5
top5_dest = (
    df.groupby("Destination")["Travelers"].sum().sort_values(ascending=False).head(5)
)

plt.figure(figsize=(8, 6))
plt.pie(
    top5_dest.values,
    labels=top5_dest.index,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Top 5 Destinations by Traveler Count (Yearly)")
plt.tight_layout()
plt.show()

# Step 4 - Scatter Plot
# Reuse monthly totals from the line plot
scatter_df = monthly_totals.reset_index()

plt.figure(figsize=(8, 6))
plt.scatter(scatter_df["Travelers"], scatter_df["Revenue"])

# Label each point with the month
for _, row in scatter_df.iterrows():
    plt.text(row["Travelers"] + 10, row["Revenue"], row["Month"])

plt.title("Travelers vs Revenue (Monthly)")
plt.xlabel("Travelers (Monthly Total)")
plt.ylabel("Revenue (Monthly Total)")
plt.grid(True)
plt.tight_layout()
plt.show()