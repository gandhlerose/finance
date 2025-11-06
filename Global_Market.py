import pandas as pd

# Sample data for three major stock indices
data = {
    "Market": ["US", "Europe", "Asia", "US", "Europe", "Asia"],
    "Index": ["S&P 500", "STOXX 600", "Nikkei 225", "S&P 500", "STOXX 600", "Nikkei 225"],
    "Month": ["August", "August", "August", "September", "September", "September"],
    "Return (%)": [2.5, 1.8, 3.2, -1.1, 0.5, 2.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("=== Global Market Monthly Returns ===")
print(df)

# Calculate average return by region
avg_returns = df.groupby("Market")["Return (%)"].mean().reset_index()
print("\n=== Average Monthly Return by Market ===")
print(avg_returns)

# Identify which market performed best overall
best_market = avg_returns.loc[avg_returns["Return (%)"].idxmax()]
print(f"\nBest performing market: {best_market['Market']} ({best_market['Return (%)']}%)")

# Analyze month-over-month change for each index
pivot = df.pivot(index="Index", columns="Month", values="Return (%)")
pivot["Change (%)"] = pivot["September"] - pivot["August"]
print("\n=== Month-over-Month Change in Returns ===")
print(pivot)

# Identify the most improved index
most_improved = pivot["Change (%)"].idxmax()
print(f"\nMost improved index: {most_improved}")
