import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Food", "Travel", "Shopping", "Bills"],
    "Amount": [2500, 1200, 3000, 1800]
}

df = pd.DataFrame(data)

print("Total Expense =", df["Amount"].sum())

plt.pie(df["Amount"], labels=df["Category"], autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()
