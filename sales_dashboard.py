import pandas as pd
import matplotlib.pyplot as plt

# Sample sales dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [1500, 1800, 2200, 2100, 2500],
    'Revenue': [30000, 36000, 44000, 42000, 50000]
}

df = pd.DataFrame(data)

print(df)

# Sales Trend Chart
plt.plot(df['Month'], df['Sales'])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()

# Revenue Trend Chart
plt.plot(df['Month'], df['Revenue'])
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Revenue Trend")
plt.show()
