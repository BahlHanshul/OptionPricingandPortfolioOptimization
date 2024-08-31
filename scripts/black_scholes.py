import numpy as np
from scipy.stats import norm

def black_scholes_call_price(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes call option price.
    S: Current stock price
    K: Option strike price
    T: Time to maturity in years
    r: Risk-free interest rate
    sigma: Volatility of the stock
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price


