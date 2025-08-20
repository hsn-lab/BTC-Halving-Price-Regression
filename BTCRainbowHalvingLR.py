import numpy as np
import matplotlib.pyplot as plt

genesis = 2008

# Historical halving years and prices
years = np.array([2012, 2016, 2020, 2024])
prices = np.array([12.33, 651.94, 8591.65, 63807])

# Future halving years (approximately every 4 years)
future_years = np.array([2028, 2032, 2036])
all_years = np.concatenate([years, future_years])

# Create realistic Bitcoin price history data based on actual historical patterns
print("Creating Bitcoin price history...")

# Key Bitcoin historical price points (approximate monthly averages)
btc_historical_data = {
    2012: [5, 6, 5, 5, 5, 5, 7, 10, 12, 12, 13, 13],
    2013: [14, 20, 90, 140, 110, 100, 90, 110, 130, 200, 800, 650],
    2014: [600, 550, 450, 420, 440, 580, 620, 520, 480, 340, 380, 320],
    2015: [220, 240, 250, 220, 230, 220, 280, 270, 230, 270, 320, 430],
    2016: [380, 370, 410, 420, 450, 650, 600, 580, 610, 630, 750, 950],
    2017: [900, 1050, 1200, 1300, 2500, 2700, 2600, 4300, 4200, 6300, 9800, 14200],
    2018: [11000, 8500, 7000, 6900, 7500, 6400, 6200, 6000, 6600, 6300, 4200, 3700],
    2019: [3400, 3800, 4000, 5200, 8000, 11000, 9500, 10000, 8200, 7500, 7200, 7200],
    2020: [7200, 8500, 5000, 6800, 9000, 9500, 9200, 11500, 10800, 13800, 19500, 28900],
    2021: [32000, 45000, 50000, 58000, 35000, 32000, 30000, 47000, 43000, 61000, 57000, 46000],
    2022: [38000, 39000, 45000, 38000, 30000, 20000, 19000, 20000, 19000, 20500, 16000, 16500],
    2023: [16800, 23000, 28000, 30000, 27000, 26500, 29000, 26000, 26500, 35000, 37000, 42000],
    2024: [42500, 51000, 69000, 66000, 62000, 70000, 58000, 60000],
    2025: [94536, 84381, 82549, 94184, 104598, 107171, 115765, 113322]  # Jan-Aug 2025
}

# Convert to arrays with weekly interpolation
btc_years = []
btc_prices = []

for year, monthly_prices in btc_historical_data.items():
    months = np.linspace(0, 11, len(monthly_prices))
    # Create weekly points (approximately 4 weeks per month)
    for month_idx, month_price in enumerate(monthly_prices):
        for week in range(4):
            week_fraction = month_idx + week/4.0
            year_fraction = year + week_fraction/12.0
            # Add some realistic volatility (±15%)
            volatility = np.random.uniform(0.85, 1.15)
            btc_years.append(year_fraction)
            btc_prices.append(month_price * volatility)

btc_years = np.array(btc_years)
btc_prices = np.array(btc_prices)

print(f"Created {len(btc_years)} weekly Bitcoin price points from 2012-2024")

# Fit logarithmic regression: log10(price) = a*ln(years - 2010) + b
# Using 2010 as base year to better align the regression line
x_fit = years - genesis  # shift to avoid log(0) and improve alignment
y_log = np.log10(prices)
coeffs = np.polyfit(np.log(x_fit), y_log, 1)
a, b = coeffs
print(f"log10(price) = {a:.4f} * ln(x-genesis) + {b:.4f}")

# Calculate future prices based on the model
future_x_fit = future_years - genesis
future_y_log = a * np.log(future_x_fit) + b
future_prices = 10**future_y_log

print("\nProjected future halving prices:")
for year, price in zip(future_years, future_prices):
    print(f"{year}: ${price:,.0f}")

# Extended smooth trendline (from 2012 to 2040)
x_plot_extended = np.linspace(2, 30, 1000)  # 2012 to 2040 (years since 2010)
y_plot_extended = a * np.log(x_plot_extended) + b
prices_plot_extended = 10**y_plot_extended

# Create the extended plot
plt.figure(figsize=(14, 8))

# Plot historical halving prices
plt.plot(years, prices, 'ro', markersize=10, label="Historical halving prices", zorder=5)

# Plot real Bitcoin price line (weekly data)
plt.plot(btc_years, btc_prices, color="lightcoral", alpha=0.6, linewidth=0.8, 
         label="Bitcoin weekly price", zorder=2)

# Plot projected future halving prices
plt.plot(future_years, future_prices, 'ro', markersize=10, markerfacecolor='white', 
         markeredgecolor='red', markeredgewidth=2, label="Projected halving prices", zorder=5)

# Plot extended smooth trendline
plt.plot(x_plot_extended + genesis, prices_plot_extended, color="blue", linewidth=3, 
         label="HPR trendline (extended)", zorder=4)

# Plot dashed rainbow lines (straight offsets)
year_offsets = [1, 2, 3, 4]  # years ahead/behind
colors = ["green", "yellow", "orange", "red"]
labels = ["±1 year", "±2 years", "±3 years", "±4 years"]

for i, (offset, color) in enumerate(zip(year_offsets, colors)):
    plt.plot(x_plot_extended + genesis + offset, prices_plot_extended, 
             linestyle="--", color=color, alpha=0.7, linewidth=1.5,
             label=labels[i] if i == 0 else "")
    plt.plot(x_plot_extended + genesis - offset, prices_plot_extended, 
             linestyle="--", color=color, alpha=0.7, linewidth=1.5)

# ±6 months blue dashed lines
plt.plot(x_plot_extended + genesis + 0.5, prices_plot_extended, 
         linestyle="--", color="blue", alpha=0.5, linewidth=1, label="±6 months")
plt.plot(x_plot_extended + genesis - 0.5, prices_plot_extended, 
         linestyle="--", color="blue", alpha=0.5, linewidth=1)

# Vertical grey lines for all halving years (historical and future)
for yr in years:
    plt.axvline(yr, color="grey", linestyle=":", alpha=0.6)
    plt.text(yr, 1.8, str(yr), rotation=90, verticalalignment="bottom", 
             color="grey", fontweight='bold')

for yr in future_years:
    plt.axvline(yr, color="lightgrey", linestyle=":", alpha=0.8)
    plt.text(yr, 1.8, str(yr), rotation=90, verticalalignment="bottom", 
             color="lightgrey", fontweight='bold', style='italic')

# Add a vertical line to separate historical from projected
plt.axvline(2025.67, color="black", linestyle="-", alpha=0.3, linewidth=2)
plt.text(2025.75, 1e5, "Projection →", rotation=90, verticalalignment="bottom", 
         color="black", fontweight='bold', alpha=0.7)

# Formatting
plt.yscale("log")
plt.ylim(1, 1e7)
plt.xlim(2012, 2040)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Bitcoin Price (USD, log scale)", fontsize=12)
plt.title("Extended Bitcoin Halving Price Regression (HPR) - Historical & Projected", 
          fontsize=14, fontweight='bold')

# Enhanced legend (without the old rainbow key)
plt.grid(True, which="both", ls="--", alpha=0.3)

# Add some statistics text box
stats_text = f"""Model Statistics:
Coefficient (a): {a:.4f}
Intercept (b): {b:.4f}
R² (historical): {np.corrcoef(y_log, a * np.log(x_fit) + b)[0,1]**2:.4f}

Peak projected price (2036): ${future_prices[-1]:,.0f}"""

plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
         fontsize=9, fontfamily='monospace')

plt.tight_layout()
plt.show()

# Print additional analysis
print(f"\nModel R-squared (historical data): {np.corrcoef(y_log, a * np.log(x_fit) + b)[0,1]**2:.4f}")
print(f"\nActual vs Predicted (historical):")
predicted_historical = 10**(a * np.log(x_fit) + b)
for year, actual, predicted in zip(years, prices, predicted_historical):
    error_pct = abs(predicted - actual) / actual * 100
    print(f"{year}: Actual ${actual:,.0f}, Predicted ${predicted:,.0f} (Error: {error_pct:.1f}%)")

print(f"\nGrowth analysis:")
for i in range(len(future_years)):
    if i == 0:
        prev_price = prices[-1]  # 2024 price
        prev_year = years[-1]
    else:
        prev_price = future_prices[i-1]
        prev_year = future_years[i-1]
    
    current_price = future_prices[i]
    current_year = future_years[i]
    growth = (current_price / prev_price - 1) * 100
    
    print(f"{prev_year} to {current_year}: {growth:.1f}% growth (${prev_price:,.0f} → ${current_price:,.0f})")
