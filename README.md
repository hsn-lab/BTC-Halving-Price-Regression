# Bitcoin Halving Price Regression

• **Core Functionality**: Bitcoin Halving Price Regression (HPR) analysis fitting logarithmic models to halving prices (2012-2024) and projecting future halvings through 2036

• **Logarithmic Regression Model**: Employs log10(price) = a*ln(years-2008) + b where 'a' represents the exponential growth coefficient and 'b' the y-intercept constant, transforming exponential price growth into linear relationship

• **Time Transformation**: Subtracts 2008 from halving years to create x_fit = [4, 8, 12, 16] corresponding to years since Bitcoin's conceptual origin, avoiding ln(0) mathematical errors

• **Price Logarithmic Conversion**: Transforms halving prices [12.33, 651.94, 8591.65, 63807] into log10 values [1.091, 2.814, 3.934, 4.805] for linear fitting

• **Polynomial Fitting**: Uses numpy.polyfit(ln(x_fit), y_log, 1) implementing least squares method to determine optimal coefficients minimising sum of squared residuals

• **Coefficient Interpretation**: Coefficient 'a' indicates how many orders of magnitude price increases per natural log unit of time; 'b' represents theoretical log10(price) at year 2009

• **Future Price Calculation**: For projected years, computes future_x_fit = future_years - 2008, then future_y_log = a * ln(future_x_fit) + b, finally exponentiating: future_prices = 10^future_y_log

• **Smooth Curve Generation**: Creates 1000 interpolated points using linspace(4, 32) representing 2012-2040, ensuring smooth trendline visualization across extended timeframe

• **Offset Band Mathematics**: Prediction bands calculated as 10^(a * ln(x_plot + offset) + b) where offset represents temporal displacement (±0.5, ±1, ±2, ±3, ±4 years)

• **Statistical Validation**: R-squared coefficient calculated as correlation between observed log10(prices) and predicted values squared, measuring model's explanatory power

• **Error Analysis**: Percentage errors computed as |predicted - actual| / actual * 100, quantifying model accuracy for each historical halving event

• **Historical Data Integration**: Incorporates real Bitcoin weekly price movements from 2012-August 2025, including realistic monthly averages interpolated with market volatility

• **Visualisation Elements**: Red dots for halving prices (solid historical, hollow projected), blue HPR trendline extending to 2040, light coral weekly price line showing actual market fluctuations

• **Prediction Framework**: Coloured dashed bands showing timing uncertainty ranges (±1-4 years: green, yellow, orange, red; ±6 months: blue offset lines)

• **Future Projections**: Calculates expected prices for upcoming halving cycles (2028, 2032, 2036) whilst acknowledging external factors like regulation and adoption could impact results

• **Statistical Validation**: Includes R-squared values and prediction accuracy metrics for historical data, showing model performance against actual halving prices

• **Market Context**: Demonstrates correlation between Bitcoin's programmed scarcity events and major price movements, supporting supply reduction hypothesis

• **Technical Features**: Logarithmic scale visualisation effectively displays exponential growth across multiple orders of magnitude with vertical markers for halving years

• **Growth Analysis**: Provides percentage growth calculations between halving periods and compares actual versus predicted prices with error percentages for model validation

<img width="1440" height="816" alt="ExtendedBTCHalvingPriceRegression" src="https://github.com/user-attachments/assets/2390e71b-4195-4cde-8503-b4424208af4b" />
