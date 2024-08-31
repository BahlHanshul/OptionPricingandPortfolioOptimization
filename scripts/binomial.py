import numpy as np

def binomial_tree_option_price(S, K, T, r, sigma, steps=100):
    """
    Binomial tree option pricing model.
    S: Current stock price
    K: Option strike price
    T: Time to maturity in years
    r: Risk-free interest rate
    sigma: Volatility of the stock
    steps: Number of steps in the binomial tree
    """
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Initialize asset prices at maturity
    asset_prices = np.zeros(steps + 1)
    option_values = np.zeros(steps + 1)
    for i in range(steps + 1):
        asset_prices[i] = S * (u ** (steps - i)) * (d ** i)
        option_values[i] = max(0, asset_prices[i] - K)

    # Step back through the tree
    for j in range(steps - 1, -1, -1):
        for i in range(j + 1):
            option_values[i] = (p * option_values[i] + (1 - p) * option_values[i + 1]) * np.exp(-r * dt)

    return option_values[0]

