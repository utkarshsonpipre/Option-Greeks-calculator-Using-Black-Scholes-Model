# 📊 Black-Scholes Option Pricing and Greeks Calculator

The **Black-Scholes Option Pricing and Greeks Calculator** is a financial analytics tool built with **Streamlit**. It allows users to compute option prices and key sensitivities (Greeks) using the **Black-Scholes model**, a standard mathematical model for pricing European-style options. This interactive app is designed to help traders, quants, and learners visualize how different parameters impact the option price and its sensitivities.

---

## 📸 Live Preview

> [*Add your deployed app link here:*](https://option-greeks-calculator-using-black-nbhm.onrender.com/)

**[Launch App](#)**
![Screenshot_30-6-2025_213054_option-greeks-calculator-using-black-nbhm onrender com (1)](https://github.com/user-attachments/assets/c9022c6e-df5a-403c-9d33-05503396c832)
![Screenshot_30-6-2025_21311_option-greeks-calculator-using-black-nbhm onrender com](https://github.com/user-attachments/assets/d4488a55-c91b-434f-b610-36f3430aa1b4)
![Screenshot_30-6-2025_213115_option-greeks-calculator-using-black-nbhm onrender com](https://github.com/user-attachments/assets/e2d62640-7f08-4e95-b2b1-86abd9494268)

## Formula Used

> ![call_formula](https://github.com/user-attachments/assets/ab771fda-cd90-4a14-9a4f-72c098f4ab33)
> ![put_formula](https://github.com/user-attachments/assets/7ea0656b-79ff-47f5-8bac-770e888b66d1)
> ![d1_d2_formula](https://github.com/user-attachments/assets/f126ed18-9c62-411e-8ba9-960eddb40e14)
> ![greeks_formula](https://github.com/user-attachments/assets/f57b9b9b-5a6a-4c77-8400-abfe191405ac)

---

## 🔹 Features

* ✅ **Call and Put Option Pricing** using the Black-Scholes formula
* ✅ **Delta, Gamma, Theta, Vega, Rho** calculators
* ✅ **Interactive input sliders and number boxes** via Streamlit UI
* ✅ **Line plots** to visualize how Greeks vary with spot price
* ✅ Designed for **real-time educational & analytical use**

---

## 📊 What Are Option Greeks?

* **Delta**: Measures sensitivity to changes in the underlying price
* **Gamma**: Measures the rate of change of Delta
* **Theta**: Measures sensitivity to time decay
* **Vega**: Measures sensitivity to volatility
* **Rho**: Measures sensitivity to interest rate changes

Each Greek is critical in managing the risk and reward profile of an options portfolio.

---

## 🚀 Technologies Used

| Feature            | Library/Framework         |
| ------------------ | ------------------------- |
| App Framework      | Streamlit                 |
| Math & Computation | NumPy, SciPy              |
| Visualization      | Matplotlib, Seaborn       |
| Deployment Ready   | Streamlit Sharing / Cloud |

---

## 📅 How to Run Locally

### 🖊️ Clone the Repository

```bash
git clone https://github.com/utkarshsonpipre/Option-Greeks-calculator-Using-Black-Scholes-Model.git
```

### 🚀 Setup Environment

```bash
pip install -r requirements.txt
```

### 🔊 Launch the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🌐 Use Cases

* Educational tools for financial engineering
* Risk analysis for option traders
* Visual learning for portfolio managers

---

## ⚠️ Disclaimer

This calculator is for **educational and informational purposes only**. It does not constitute financial advice or a recommendation to trade. Please consult with a licensed financial advisor before making investment decisions.

---

