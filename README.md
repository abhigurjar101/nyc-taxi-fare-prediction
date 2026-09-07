# NYC Taxi Fare Prediction & Operations Optimization 🚖🏙️

> **An end-to-end Big Data Exploratory Data Analysis (EDA) and predictive regression pipeline analyzing 1.89 Million NYC Yellow Taxi trips across 12 monthly Parquet files by Abhi Gurjar.**

---

## 💡 What Is This Project? (Explained Like a Human)

New York City is one of the busiest metropolitan transit hubs on Earth. Every day, tens of thousands of yellow cabs take passengers through Manhattan gridlock, airport corridors (JFK & LaGuardia), and outer boroughs.

For riders, getting hit with an unexpected \$60 fare due to traffic or confusing peak-hour surcharges causes frustration. For fleet dispatchers, failing to predict demand means hundreds of cabs idle in Queens while thousands of passengers are stranded in Midtown during rainstorms.

**This project performs a comprehensive Big Data investigation on 1.89 Million real NYC taxi trips.** It models the pricing dynamics—including distance multipliers, rush hour bottlenecks, congestion zone fees, airport flat rates, and tip distributions—and provides an instant fare estimation engine.

---

## 📊 Big Data Analytics Highlights

- **Dataset Scale**: Analyzed 1.89 Million taxi trip records across 12 monthly Parquet files from the NYC Taxi & Limousine Commission (TLC).
- **Temporal Patterns**: Evaluated hourly demand spikes (8:00 AM morning commute and 5:00 PM – 7:00 PM evening peak).
- **Spatial Analysis**: Mapped pickup and dropoff zone density, calculating average speeds and congestion drag across Manhattan zones.
- **Tipping Behavior**: Discovered that credit card transactions cluster sharply at standard 18%, 20%, and 25% tip brackets, while cash trips record zero recorded tips in official TLC ledgers.

---

## 🚀 How to Run in 5 Seconds

Zero external setup needed to test the pricing model:

```bash
# 1. Clone the repository
git clone https://github.com/abhigurjar101/nyc-taxi-fare-prediction.git
cd nyc-taxi-fare-prediction

# 2. Run the fare calculation engine
python3 predict_fare.py
```

### What You Will See:
- Dynamic meter calculation comparing standard Midtown trips vs. Evening Rush Hour vs. JFK Airport flat-rate trips.
- Itemized surcharges (NYC Congestion Fee, Night Surcharge, Airport Access Fee).
- Estimated tip recommendation and final predicted total.

---

## 📁 Repository Structure

```
nyc-taxi-fare-prediction/
├── notebooks/
│   └── EDA_Optimising_NYC_Taxis_Abhi_Gurjar.ipynb  # Comprehensive 1.89M trip EDA
├── predict_fare.py                                  # Standalone fare estimator
├── requirements.txt                                 # Pandas, PyArrow, Scikit-Learn
└── README.md                                        # You are here! Simple human documentation
```

---

## 👤 Author

**Abhi Gurjar**  
- Portfolio: [abhigurjar.vercel.app](https://abhigurjar.vercel.app)  
- GitHub: [@abhigurjar101](https://github.com/abhigurjar101)  
- LinkedIn: [Abhi Gurjar](https://in.linkedin.com/in/abhi-gurjar-b13067203)
