import pandas as pd

df = pd.read_csv("customer_data.csv")

def segment(x):
    if x >= 50000:
        return "High Spender"
    elif x >= 20000:
        return "Medium Spender"
    else:
        return "Low Spender"

df["Segment"] = df["Total Spending"].apply(segment)

print(df.groupby("Segment")["Age"].mean())
