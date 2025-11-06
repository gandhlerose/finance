# Monte Carlo Simulation for Portfolio Risk and Performance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# === Step 1: Download historical stock data ===

tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']  # Example portfolio
start_date = '2022-01-01'
end_date = '2025-01-01'

data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']


# === Step 2: Compute daily returns ===

returns = data.pct_change().dropna()

# === Step 3: Portfolio initialization ===

initial_capital = 100000
weights = np.array([0.25, 0.25, 0.25, 0.25])  # Equal allocation
mean_returns = returns.mean()
cov_matrix = returns.cov()

# === Step 4: Monte Carlo Simulation Function ===
def monte_carlo_portfolio(weights, mean_returns, cov_matrix, num_simulations=1000, days=252):
    results = np.zeros((num_simulations, days))
    
    for i in range(num_simulations):
        daily_portfolio_value = initial_capital
        portfolio_history = [daily_portfolio_value]
        
        for _ in range(days):
            # Simulate daily returns from multivariate normal distribution
            simulated_returns = np.random.multivariate_normal(mean_returns, cov_matrix)
            portfolio_return = np.dot(simulated_returns, weights)
            daily_portfolio_value *= (1 + portfolio_return)
            portfolio_history.append(daily_portfolio_value)
        
        results[i, :] = portfolio_history[1:]
    
    return results

# === Step 5: Run Simulation ===
simulations = monte_carlo_portfolio(weights, mean_returns, cov_matrix, num_simulations=5000)

# === Step 6: Visualization ===
plt.figure(figsize=(14,7))
plt.plot(simulations.T, color='blue', alpha=0.01)
plt.title('Monte Carlo Simulation of Portfolio Performance (1 Year)')
plt.xlabel('Trading Days')
plt.ylabel('Portfolio Value ($)')
plt.grid(True)
plt.show()

# === Step 7: Simulation Metrics ===
ending_values = simulations[:, -1]
mean_end = np.mean(ending_values)
median_end = np.median(ending_values)
percentile_5 = np.percentile(ending_values, 5)
percentile_95 = np.percentile(ending_values, 95)

print("=== Monte Carlo Simulation Results ===")
print("Mean Ending Portfolio Value: $", round(mean_end, 2))
print("Median Ending Portfolio Value: $", round(median_end, 2))
print("5th Percentile Value (Worst Case): $", round(percentile_5, 2))
print("95th Percentile Value (Best Case): $", round(percentile_95, 2))
