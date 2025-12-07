import pandas as pd
import matplotlib.pyplot as plt

# Read sales data
data = pd.read_csv("sales.csv")

months = data['month']
sales = data['sales']

# Create a 1x3 subplot
plt.figure(figsize=(15, 4))

# -------- Line Plot --------
plt.subplot(1, 3, 1)
plt.plot(months, sales, marker='o')
plt.title("Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

# -------- Scatter Plot --------
plt.subplot(1, 3, 2)
plt.scatter(months, sales)
plt.title("Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

# -------- Bar Plot --------
plt.subplot(1, 3, 3)
plt.bar(months, sales)
plt.title("Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

# Show all three plots on one page
plt.tight_layout()
plt.show()
