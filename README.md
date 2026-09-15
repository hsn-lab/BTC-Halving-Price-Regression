# Bitcoin Halving Price Regression

Analyzing Bitcoin's price patterns around halving events using logarithmic regression to project future price movements through 2036.

## Overview

This project fits logarithmic regression models to historical Bitcoin halving prices (2012-2024) and generates predictions for future halving cycles. The analysis reveals correlations between Bitcoin's programmed scarcity events and major price movements, providing data-driven insights into supply reduction impacts.

## Mathematical Model

### Core Formula
```
log₁₀(price) = a·ln(years - 2008) + b
```

Where:
- **a** = Exponential growth coefficient (orders of magnitude per unit time)
- **b** = Y-intercept constant (theoretical log₁₀(price) at year 2009)
- **years - 2008** = Time transformation to avoid ln(0) errors

### Methodology

1. **Time Transformation**: Converts halving years to x-values: [4, 8, 12, 16] (years since 2008)
2. **Price Logarithmic Conversion**: Transforms halving prices into log₁₀ values for linear fitting
3. **Polynomial Fitting**: Uses NumPy's least-squares method to determine optimal coefficients
4. **Future Projections**: Calculates predictions for 2028, 2032, and 2036 halvings
5. **Statistical Validation**: Computes R² and prediction accuracy metrics

## Historical Data

| Halving Year | Price (USD) | Log₁₀(Price) |
|---|---|---|
| 2012 | $12.33 | 1.091 |
| 2016 | $651.94 | 2.814 |
| 2020 | $8,591.65 | 3.934 |
| 2024 | $63,807 | 4.805 |

**Data Sources**:
- [Investing.com - Bitcoin Historical Data](https://www.investing.com/crypto/bitcoin/historical-data)
- [BitBo Rainbow Chart](https://charts.bitbo.io/rainbow/)

## Visualization Features

### V0.1
![ExtendedBTCHalvingPriceRegression version 1](https://github.com/user-attachments/assets/2390e71b-4195-4cde-8503-b4424208af4b)

### V0.2
![ExtendedBTCHalvingPriceRegression version 2](https://github.com/user-attachments/assets/091f5d91-5681-4f77-814f-c34bbad32db8)

### Chart Elements
- **Red dots**: Historical halving prices (solid) and projected future prices (hollow)
- **Blue trendline**: Logarithmic HPR model extending to 2040
- **Light coral line**: Actual Bitcoin weekly price movements (2012-August 2025)
- **Dashed prediction bands**: Timing uncertainty ranges
  - ±1-4 years: Color-coded bands (green, yellow, orange, red)
  - ±6 months: Blue offset lines
- **Vertical markers**: Halving event years on logarithmic scale

## Key Insights

- **Smooth Curve Generation**: 1,000 interpolated points (2012-2040) for smooth trendline visualization
- **Offset Band Mathematics**: Confidence bands calculated using temporal displacement (±0.5, ±1, ±2, ±3, ±4 years)
- **Prediction Framework**: Color-coded uncertainty ranges show timing confidence for future halvings
- **Growth Analysis**: Calculates percentage growth between halving periods with error metrics
- **Model Performance**: R² coefficient and percentage errors validate model accuracy against historical data

## Installation & Usage

```python
# Requirements
import numpy as np
import matplotlib.pyplot as plt

# Run analysis
python BTC_Halving_Price_Regression.py
```

## Limitations & Caveats

- External factors (regulation, adoption, market sentiment) may significantly impact actual prices
- Historical patterns do not guarantee future performance
- Model assumptions may not hold during unprecedented market conditions
- Predictions become less reliable with longer time horizons

## Future Projections

Expected halving prices based on current model (subject to market volatility):
- **2028 Halving**: [Model prediction]
- **2032 Halving**: [Model prediction]
- **2036 Halving**: [Model prediction]

## Attribution

- **Inspiration**: [BitBo Rainbow Chart](https://charts.bitbo.io/rainbow/)
- **Development**: Created with assistance from ChatGPT and Claude

**Current Version**: V0.2  
**Last Updated**: 2025
