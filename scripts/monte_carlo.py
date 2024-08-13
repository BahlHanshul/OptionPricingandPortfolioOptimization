import numpy as np

def monte_carlo_option_price(S, K, T, r, sigma, num_simulations=10000):
    """
    Monte Carlo simulation to estimate the option price.
    S: Current stock price
    K: Option strike price
    T: Time to maturity in years
    r: Risk-free interest rate
    sigma: Volatility of the stock
    num_simulations: Number of simulations to run
    """
    np.random.seed(42)  # For reproducibility
    payoffs = []
    
    for _ in range(num_simulations):
        ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * np.random.randn())
        payoff = max(ST - K, 0)  # Call option payoff
        payoffs.append(payoff)
    
    price = np.exp(-r * T) * np.mean(payoffs)
    return price

# Sample Input
#price = monte_carlo_option_price(S, K, T, r, sigma)
#print(f"Monte Carlo Call Price: {price}")
