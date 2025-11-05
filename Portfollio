import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === 1. Create mock dataset  ===
data = {
    "Asset": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
    "Initial Price": [180, 320, 140, 125, 250],
    "Final Price": [195, 345, 165, 150, 290],
    "Shares Held": [30, 25, 20, 40, 15]
}

portfolio = pd.DataFrame(data)

# === 2. Calculate investment, returns, and percentages ===
portfolio["Initial Value"] = portfolio["Initial Price"] * portfolio["Shares Held"]
portfolio["Final Value"] = portfolio["Final Price"] * portfolio["Shares Held"]
portfolio["Return ($)"] = portfolio["Final Value"] - portfolio["Initial Value"]
portfolio["Return (%)"] = (portfolio["Return ($)"] / portfolio["Initial Value"]) * 100

# === 3. Portfolio summary ===
total_initial = portfolio["Initial Value"].sum()
total_final = portfolio["Final Value"].sum()
total_return = total_final - total_initial
total_return_pct = (total_return / total_initial) * 100

# === 4. Identify best and worst performing assets ===
best_asset = portfolio.loc[portfolio["Return (%)"].idxmax()]
worst_asset = portfolio.loc[portfolio["Return (%)"].idxmin()]

# === 5. Contribution to total portfolio performance ===
portfolio["Weight (%)"] = (portfolio["Initial Value"] / total_initial) * 100
portfolio["Contribution (%)"] = (portfolio["Weight (%)"] * portfolio["Return (%)"]) / 100

# === 6. Rank assets by contribution ===
ranked = portfolio.sort_values("Contribution (%)", ascending=False)

# === 7. Output ===
print("=== Portfolio Performance Summary ===")
print(portfolio[["Asset", "Initial Value", "Final Value", "Return ($)", "Return (%)", "Contribution (%)"]])

print("\n=== Key Portfolio Metrics ===")
print(f"Total Initial Investment: ${total_initial:,.2f}")
print(f"Total Final Value: ${total_final:,.2f}")
print(f"Total Return: ${total_return:,.2f} ({total_return_pct:.2f}%)")

print("\nBest Performing Asset:")
print(best_asset[["Asset", "Return (%)"]])

print("\nWorst Performing Asset:")
print(worst_asset[["Asset", "Return (%)"]])

print("\n=== Asset Contribution Ranking ===")
print(ranked[["Asset", "Contribution (%)"]])

# === 8. Visualizations  ===
plt.figure(figsize=(10,6))
sns.barplot(x="Asset", y="Return (%)", data=portfolio, palette="coolwarm")
plt.title("Portfolio Asset Returns (%)")
plt.ylabel("Return (%)")
plt.xlabel("Asset")
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x="Asset", y="Contribution (%)", data=ranked, palette="viridis")
plt.title("Portfolio Asset Contribution (%)")
plt.ylabel("Contribution (%)")
plt.xlabel("Asset")
plt.show()
