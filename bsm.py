import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import streamlit.components.v1 as components

# ---------- Option Pricing Functions ----------
def blackScholes(S, K, r, T, sigma, type="c"):
    d1 = (np.log(S/K) + (r + sigma**2/2)* T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    try:
        if type == "c":
            price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return price
    except:
        st.sidebar.error("Please confirm all option parameters!")

def optionDelta (S, K, r, T, sigma, type="c"):
    d1 = (np.log(S/K) + (r + sigma**2/2)* T)/(sigma*np.sqrt(T))
    try:
        return norm.cdf(d1, 0, 1) if type == "c" else -norm.cdf(-d1, 0, 1)
    except:
        st.sidebar.error("Please confirm all option parameters!")

def optionGamma (S, K, r, T, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)* T)/(sigma*np.sqrt(T))
    try:
        return norm.pdf(d1, 0, 1)/ (S * sigma * np.sqrt(T))
    except:
        st.sidebar.error("Please confirm all option parameters!")

def optionTheta(S, K, r, T, sigma, type="c"):
    d1 = (np.log(S/K) + (r + sigma**2/2)* T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "c":
            theta = - ((S * norm.pdf(d1, 0, 1) * sigma) / (2 * np.sqrt(T))) - r * K * np.exp(-r*T) * norm.cdf(d2, 0, 1)
        elif type == "p":
            theta = - ((S * norm.pdf(d1, 0, 1) * sigma) / (2 * np.sqrt(T))) + r * K * np.exp(-r*T) * norm.cdf(-d2, 0, 1)
        return theta/365
    except:
        st.sidebar.error("Please confirm all option parameters!")
 
def optionVega (S, K, r, T, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)* T)/(sigma*np.sqrt(T))
    try:
        return S * np.sqrt(T) * norm.pdf(d1, 0, 1) * 0.01
    except:
        st.sidebar.error("Please confirm all option parameters!")

def optionRho(S, K, r, T, sigma, type="c"):
    d1 = (np.log(S/K) + (r + sigma**2/2)* T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "c":
            return 0.01 * K * T * np.exp(-r*T) * norm.cdf(d2, 0, 1)
        elif type == "p":
            return -0.01 * K * T * np.exp(-r*T) * norm.cdf(-d2, 0, 1)
    except:
        st.sidebar.error("Please confirm all option parameters!")

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Black-Scholes Model", layout="centered")

st.title("📈 Black-Scholes Option Price Calculator")
st.markdown("Developed by **Utkarsh Sonpipre**")
st.markdown("""
🔗 [GitHub Profile](https://github.com/utkarshsonpipre)  
🔗 [Project Repository](https://github.com/utkarshsonpipre?tab=repositories)
""")

st.info("Use the sidebar to input parameters. The app will calculate the Option Price and Greeks.")

# ---------- Sidebar Inputs ----------
st.sidebar.header("Black-Scholes Parameters")
r = st.sidebar.number_input("Risk-Free Rate", min_value=0.000, max_value=1.000, step=0.001, value=0.030)
S = st.sidebar.number_input("Underlying Asset Price", min_value=1.00, step=0.10, value=30.00)
K = st.sidebar.number_input("Strike Price", min_value=1.00, step=0.10, value=50.00)
days_to_expiry = st.sidebar.number_input("Time to Expiry Date (in days)", min_value=1, step=1, value=250)
sigma = st.sidebar.number_input("Volatility", min_value=0.000, max_value=1.000, step=0.01, value=0.30)
type_input = st.sidebar.selectbox("Option Type",["Call", "Put"])

type = "c" if type_input == "Call" else "p"
T = days_to_expiry/365

# ---------- Calculations ----------
spot_prices = [i for i in range(0, int(S)+50 + 1)]
prices = [blackScholes(i, K, r, T, sigma, type) for i in spot_prices]
deltas = [optionDelta(i, K, r, T, sigma, type) for i in spot_prices]
gammas = [optionGamma(i, K, r, T, sigma) for i in spot_prices]
thetas = [optionTheta(i, K, r, T, sigma, type) for i in spot_prices]
vegas = [optionVega(i, K, r, T, sigma) for i in spot_prices]
rhos = [optionRho(i, K, r, T, sigma, type) for i in spot_prices]

# ---------- Results Display ----------
st.subheader("🧮 Option Prices")
col1, col2 = st.columns(2)
col1.metric("Call Price", f"{blackScholes(S, K, r, T, sigma, 'c'):.3f}")
col2.metric("Put Price", f"{blackScholes(S, K, r, T, sigma, 'p'):.3f}")

st.subheader("📊 Option Greeks")
g1, g2, g3, g4, g5 = st.columns(5)
g1.metric("Delta", f"{optionDelta(S, K, r, T, sigma, 'c'):.3f}")
g2.metric("Gamma", f"{optionGamma(S, K, r, T, sigma):.3f}")
g3.metric("Theta", f"{optionTheta(S, K, r, T, sigma, 'c'):.3f}")
g4.metric("Vega", f"{optionVega(S, K, r, T, sigma):.3f}")
g5.metric("Rho", f"{optionRho(S, K, r, T, sigma, 'c'):.3f}")

# ---------- Visuals ----------
sns.set_style("whitegrid")

def build_plot(y, label):
    fig, ax = plt.subplots()
    sns.lineplot(x=spot_prices, y=y)
    ax.set_xlabel("Underlying Asset Price")
    ax.set_ylabel(label)
    ax.set_title(f"{label} vs Spot Price")
    fig.tight_layout()
    return fig

st.subheader("📈 Visualization of Greeks")
with st.expander("📍 Option Price Curve"):
    st.pyplot(build_plot(prices, "Option Price"))

with st.expander("📍 Delta"):
    st.pyplot(build_plot(deltas, "Delta"))

with st.expander("📍 Gamma"):
    st.pyplot(build_plot(gammas, "Gamma"))

with st.expander("📍 Theta"):
    st.pyplot(build_plot(thetas, "Theta"))

with st.expander("📍 Vega"):
    st.pyplot(build_plot(vegas, "Vega"))

with st.expander("📍 Rho"):
    st.pyplot(build_plot(rhos, "Rho"))
