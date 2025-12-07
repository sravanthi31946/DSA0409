import matplotlib.pyplot as plt

# Monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 27, 30, 32, 34, 33, 32, 30, 28, 25, 23]  # Example temps
rainfall = [80, 60, 50, 40, 30, 20, 10, 15, 40, 70, 90, 100]   # Example rainfall

# Create figure (two graphs in one page)
plt.figure(figsize=(12, 6))

# --- 1. Line Plot for Temperature ---
plt.subplot(1, 2, 1)  # 1 row, 2 columns, graph 1
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")

# --- 2. Scatter Plot for Rainfall ---
plt.subplot(1, 2, 2)  # 1 row, 2 columns, graph 2
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")

# Show all plots
plt.tight_layout()
plt.show()
