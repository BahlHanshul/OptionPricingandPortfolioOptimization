import streamlit as st
from black_scholes import black_scholes_call_price
from monte_carlo import monte_carlo_option_price
from binomial import binomial_tree_option_price
from portfolio_optimizer import optimize_portfolio
import yfinance as yf
import numpy as np

st.title("Option Pricing and Portfolio Optimization")


model = st.sidebar.selectbox(
    "Select Option Pricing Model",
    ("Black-Scholes", "Monte Carlo", "Binomial Tree")
)


ticker = st.text_input("Enter Stock Ticker", "AAPL")
K = st.number_input("Strike Price", value=100.0)
T = st.number_input("Time to Maturity (years)", value=1.0)
r = st.number_input("Risk-Free Rate", value=0.05)
sigma = st.number_input("Volatility", value=0.2)


data = yf.Ticker(ticker)
S = data.history(period="1d")["Close"].iloc[-1]
st.write(f"Current Stock Price for {ticker}: ${S}")


if model == "Black-Scholes":
    price = black_scholes_call_price(S, K, T, r, sigma)
elif model == "Monte Carlo":
    price = monte_carlo_option_price(S, K, T, r, sigma)
else:
    price = binomial_tree_option_price(S, K, T, r, sigma)

st.write(f"Option Price using {model}: ${price:.2f}")


if st.button("Optimize Portfolio"):
    prices = [black_scholes_call_price(S, K, T, r, sigma),
              monte_carlo_option_price(S, K, T, r, sigma),
              binomial_tree_option_price(S, K, T, r, sigma)]
    weights = np.array([0.4, 0.3, 0.3])  # Initial weights
    returns = np.array([0.08, 0.10, 0.09])  # Expected returns

    optimized_value, optimized_weights = optimize_portfolio(prices, weights, returns)
    st.write(f"Optimized Portfolio Value: ${optimized_value:.2f}")
    st.write(f"Optimized Weights: {optimized_weights}")

    # Chart Visualization
    st.bar_chart(optimized_weights)
