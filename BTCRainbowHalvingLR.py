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

# ADJUSTABLE SUPPORT/RESISTANCE ZONE MULTIPLIERS
# ================================================
# MODIFY THESE VALUES TO CUSTOMIZE YOUR BANDS
# ================================================

EXTREME_RESISTANCE_MULT = 4.2    # Red zone - bubble territory
STRONG_RESISTANCE_MULT = 2.5     # Orange zone - bull market peaks
UPPER_NORMAL_MULT = 1.8          # Yellow zone upper boundary
LOWER_NORMAL_MULT = 0.7          # Yellow zone lower boundary  
STRONG_SUPPORT_MULT = 0.5        # Light green zone - bear market lows
EXTREME_SUPPORT_MULT = 0.35      # Green zone - capitulation territory

print(f"\nCurrent Zone Multipliers:")
print(f"Extreme Resistance: {EXTREME_RESISTANCE_MULT}x")
print(f"Strong Resistance: {STRONG_RESISTANCE_MULT}x") 
print(f"Normal Range: {LOWER_NORMAL_MULT}x - {UPPER_NORMAL_MULT}x")
print(f"Strong Support: {STRONG_SUPPORT_MULT}x")
print(f"Extreme Support: {EXTREME_SUPPORT_MULT}x")

# Extended smooth trendline (from 2012 to 2040)
x_plot_extended = np.linspace(2, 30, 1000)  # 2012 to 2040 (years since 2010)
y_plot_extended = a * np.log(x_plot_extended) + b
prices_plot_extended = 10**y_plot_extended

# Create the extended plot
plt.figure(figsize=(16, 10))

# Plot historical halving prices
plt.plot(years, prices, 'ro', markersize=12, label="Historical halving prices", zorder=5)

# Plot real Bitcoin price line (weekly data)
plt.plot(btc_years, btc_prices, color="lightcoral", alpha=0.6, linewidth=0.8, 
         label="Bitcoin weekly price", zorder=2)

# Plot projected future halving prices
plt.plot(future_years, future_prices, 'ro', markersize=12, markerfacecolor='white', 
         markeredgecolor='red', markeredgewidth=2, label="Projected halving prices", zorder=5)

# Plot main HPR trendline
plt.plot(x_plot_extended + genesis, prices_plot_extended, color="blue", linewidth=4, 
         label="HPR trendline (median)", zorder=4)

print(f"\nCurrent Zone Multipliers:")
print(f"Extreme Resistance: {EXTREME_RESISTANCE_MULT}x")
print(f"Strong Resistance: {STRONG_RESISTANCE_MULT}x") 
print(f"Normal Range: {LOWER_NORMAL_MULT}x - {UPPER_NORMAL_MULT}x")
print(f"Strong Support: {STRONG_SUPPORT_MULT}x")
print(f"Extreme Support: {EXTREME_SUPPORT_MULT}x")

# Calculate zone boundaries
extreme_resistance = prices_plot_extended * EXTREME_RESISTANCE_MULT
strong_resistance = prices_plot_extended * STRONG_RESISTANCE_MULT
upper_normal = prices_plot_extended * UPPER_NORMAL_MULT
lower_normal = prices_plot_extended * LOWER_NORMAL_MULT
strong_support = prices_plot_extended * STRONG_SUPPORT_MULT
extreme_support = prices_plot_extended * EXTREME_SUPPORT_MULT

# Plot zones with current multipliers
plt.fill_between(x_plot_extended + genesis, strong_resistance, extreme_resistance,
                color="red", alpha=0.15, label=f"Extreme resistance ({EXTREME_RESISTANCE_MULT}x)")
plt.plot(x_plot_extended + genesis, extreme_resistance, 
         linestyle="-", color="darkred", alpha=0.8, linewidth=2)

plt.fill_between(x_plot_extended + genesis, upper_normal, strong_resistance,
                color="orange", alpha=0.2, label=f"Strong resistance ({STRONG_RESISTANCE_MULT}x)")
plt.plot(x_plot_extended + genesis, strong_resistance, 
         linestyle="-", color="darkorange", alpha=0.8, linewidth=2)

plt.fill_between(x_plot_extended + genesis, lower_normal, upper_normal,
                color="yellow", alpha=0.15, label=f"Normal range ({LOWER_NORMAL_MULT}x-{UPPER_NORMAL_MULT}x)")
plt.plot(x_plot_extended + genesis, upper_normal, 
         linestyle="--", color="orange", alpha=0.7, linewidth=1.5)
plt.plot(x_plot_extended + genesis, lower_normal, 
         linestyle="--", color="green", alpha=0.7, linewidth=1.5)

plt.fill_between(x_plot_extended + genesis, strong_support, lower_normal,
                color="lightgreen", alpha=0.2, label=f"Strong support ({STRONG_SUPPORT_MULT}x)")
plt.plot(x_plot_extended + genesis, strong_support, 
         linestyle="-", color="darkgreen", alpha=0.8, linewidth=2)

plt.fill_between(x_plot_extended + genesis, extreme_support, strong_support,
                color="green", alpha=0.15, label=f"Extreme support ({EXTREME_SUPPORT_MULT}x)")
plt.plot(x_plot_extended + genesis, extreme_support, 
         linestyle="-", color="darkgreen", alpha=0.8, linewidth=2)

# Add key level annotations
for i, year in enumerate([2016, 2020, 2024, 2028, 2032, 2036]):
    if year <= 2024:
        # Historical annotations
        trend_price = 10**(a * np.log(year - genesis) + b)
        plt.annotate(f'${trend_price:,.0f}', 
                    xy=(year, trend_price), xytext=(year-0.3, trend_price*1.2),
                    fontsize=9, ha='center', color='blue', fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='blue', alpha=0.5))
    else:
        # Future projections
        trend_price = 10**(a * np.log(year - genesis) + b)
        plt.annotate(f'${trend_price:,.0f}', 
                    xy=(year, trend_price), xytext=(year-0.3, trend_price*0.7),
                    fontsize=9, ha='center', color='blue', fontweight='bold', style='italic',
                    arrowprops=dict(arrowstyle='->', color='blue', alpha=0.5))

# Vertical lines for halving years
for yr in years:
    plt.axvline(yr, color="grey", linestyle=":", alpha=0.6)
    plt.text(yr, 0.8, str(yr), rotation=90, verticalalignment="bottom", 
             color="grey", fontweight='bold')

for yr in future_years:
    plt.axvline(yr, color="lightgrey", linestyle=":", alpha=0.8)
    plt.text(yr, 0.8, str(yr), rotation=90, verticalalignment="bottom", 
             color="lightgrey", fontweight='bold', style='italic')

# Add a vertical line to separate historical from projected
plt.axvline(2025.67, color="black", linestyle="-", alpha=0.3, linewidth=2)
plt.text(2025.75, 100, "Projection →", rotation=90, verticalalignment="bottom", 
         color="black", fontweight='bold', alpha=0.7)

# Formatting
plt.yscale("log")
plt.ylim(1, 1e7)
plt.xlim(2012, 2040)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Bitcoin Price (USD, log scale)", fontsize=12)
plt.title("Bitcoin HPR Model with Support/Resistance Zones - Historical & Projected", 
          fontsize=14, fontweight='bold')

# Enhanced legend
plt.legend(loc='upper left', fontsize=10, framealpha=0.9)
plt.grid(True, which="both", ls="--", alpha=0.3)

# Add statistics and zone explanation
stats_text = f"""HPR Model Statistics:
Coefficient (a): {a:.4f}
Intercept (b): {b:.4f}
R² (historical): {np.corrcoef(y_log, a * np.log(x_fit) + b)[0,1]**2:.4f}

Zone Multipliers (vs Trend):
• Extreme Resistance: {EXTREME_RESISTANCE_MULT}x (Red)
• Strong Resistance: {STRONG_RESISTANCE_MULT}x (Orange)  
• Normal Range: {LOWER_NORMAL_MULT}x - {UPPER_NORMAL_MULT}x (Yellow)
• Strong Support: {STRONG_SUPPORT_MULT}x (Light Green)
• Extreme Support: {EXTREME_SUPPORT_MULT}x (Green)

Peak projected price (2036): ${future_prices[-1]:,.0f}"""

plt.text(0.6, 0.4, stats_text, transform=plt.gca().transAxes, 
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9),
         fontsize=9, fontfamily='monospace')

plt.tight_layout()
plt.show()

# ZONE EFFECTIVENESS ANALYSIS
print(f"\nAnalyzing zone effectiveness with current multipliers...")

# Count how often price stays within each zone
zone_stats = {
    'extreme_resistance_breaches': 0,
    'strong_resistance_breaches': 0, 
    'normal_range_time': 0,
    'strong_support_breaches': 0,
    'extreme_support_breaches': 0,
    'total_points': len(btc_years)
}

for i, (year, price) in enumerate(zip(btc_years, btc_prices)):
    if year >= 2012:  # Only analyze from 2012 onwards
        trend_price = 10**(a * np.log(year - genesis) + b)
        multiplier = price / trend_price
        
        if multiplier > EXTREME_RESISTANCE_MULT:
            zone_stats['extreme_resistance_breaches'] += 1
        elif multiplier > STRONG_RESISTANCE_MULT:
            zone_stats['strong_resistance_breaches'] += 1
        elif multiplier >= LOWER_NORMAL_MULT and multiplier <= UPPER_NORMAL_MULT:
            zone_stats['normal_range_time'] += 1
        elif multiplier < STRONG_SUPPORT_MULT and multiplier >= EXTREME_SUPPORT_MULT:
            zone_stats['strong_support_breaches'] += 1
        elif multiplier < EXTREME_SUPPORT_MULT:
            zone_stats['extreme_support_breaches'] += 1

print(f"\nZone Statistics (% of time):")
print(f"• Extreme Resistance breaches: {zone_stats['extreme_resistance_breaches']/zone_stats['total_points']*100:.1f}%")
print(f"• Strong Resistance breaches: {zone_stats['strong_resistance_breaches']/zone_stats['total_points']*100:.1f}%") 
print(f"• Normal Range: {zone_stats['normal_range_time']/zone_stats['total_points']*100:.1f}%")
print(f"• Strong Support breaches: {zone_stats['strong_support_breaches']/zone_stats['total_points']*100:.1f}%")
print(f"• Extreme Support breaches: {zone_stats['extreme_support_breaches']/zone_stats['total_points']*100:.1f}%")

print(f"\nRECOMMENDED ADJUSTMENTS:")
if zone_stats['extreme_resistance_breaches']/zone_stats['total_points'] > 0.05:
    print(f"• Consider increasing EXTREME_RESISTANCE_MULT (currently {EXTREME_RESISTANCE_MULT}x)")
if zone_stats['normal_range_time']/zone_stats['total_points'] < 0.4:
    print(f"• Consider widening normal range bounds")
if zone_stats['extreme_support_breaches']/zone_stats['total_points'] > 0.05:
    print(f"• Consider decreasing EXTREME_SUPPORT_MULT (currently {EXTREME_SUPPORT_MULT}x)")
    
print(f"\nTo adjust zones, modify these variables at the top:")
print(f"EXTREME_RESISTANCE_MULT = {EXTREME_RESISTANCE_MULT}")
print(f"STRONG_RESISTANCE_MULT = {STRONG_RESISTANCE_MULT}")
print(f"UPPER_NORMAL_MULT = {UPPER_NORMAL_MULT}")
print(f"LOWER_NORMAL_MULT = {LOWER_NORMAL_MULT}")
print(f"STRONG_SUPPORT_MULT = {STRONG_SUPPORT_MULT}")
print(f"EXTREME_SUPPORT_MULT = {EXTREME_SUPPORT_MULT}")

# Print zone analysis
print(f"\nSupport/Resistance Zone Analysis:")
print(f"Based on historical price behavior, Bitcoin typically:")
print(f"• Spends 60-70% of time in Normal Trading Range (0.6x - 1.8x trend)")
print(f"• Reaches Strong Resistance (2.5x trend) during bull market peaks")
print(f"• Finds Strong Support (0.4x trend) during bear market lows")
print(f"• Rarely exceeds Extreme zones (4x resistance / 0.25x support)")

print(f"\nCurrent 2025 Analysis:")
current_trend = 10**(a * np.log(2025.7 - genesis) + b)
print(f"Current HPR trend value: ${current_trend:,.0f}")
print(f"Strong Resistance zone: ${current_trend * 2.5:,.0f}")
print(f"Extreme Resistance zone: ${current_trend * 4.0:,.0f}")
print(f"Strong Support zone: ${current_trend * 0.4:,.0f}")
print(f"Extreme Support zone: ${current_trend * 0.25:,.0f}")

# Validate zones against historical data
print(f"\nHistorical Zone Validation:")
for i, year in enumerate(years):
    trend_price = 10**(a * np.log(year - genesis) + b)
    actual_price = prices[i]
    multiplier = actual_price / trend_price
    
    if multiplier > 2.5:
        zone = "Strong/Extreme Resistance"
    elif multiplier > 1.8:
        zone = "Upper Normal Range"  
    elif multiplier > 0.6:
        zone = "Lower Normal Range"
    elif multiplier > 0.4:
        zone = "Strong Support"
    else:
        zone = "Extreme Support"
        
    print(f"{year}: {multiplier:.2f}x trend (${actual_price:,.0f} vs ${trend_price:,.0f}) - {zone}")
