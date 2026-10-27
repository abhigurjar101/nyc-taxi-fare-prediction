# NYC taxi trip exploration and fare calculator

A notebook exploring sampled NYC yellow-taxi trips, alongside a standalone, rule-based fare calculator. The calculator uses hand-written distance, time, airport, and tip rules; it does not load a trained regression model.

## Quick demo and tests

```bash
git clone https://github.com/abhigurjar101/nyc-taxi-fare-prediction.git
cd nyc-taxi-fare-prediction
python3 predict_fare.py
python3 -m unittest discover -s tests -v
```

These two commands require only Python's standard library. The examples print a fare breakdown. They are demonstrations; the test suite contains assertions.

## Reproduce the notebook

1. Create a virtual environment and install `requirements.txt`.
2. Obtain yellow-taxi trip Parquet files and taxi-zone shapefiles from the [NYC TLC trip-record data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
3. Set `NYC_TAXI_DATA_DIR` to the Parquet directory and `NYC_TAXI_ZONES_PATH` to the `.shp` file, including its supporting shapefile files.
4. Launch `jupyter lab` and run `notebooks/EDA_Optimising_NYC_Taxis_Abhi_Gurjar.ipynb` from top to bottom.

The notebook samples 5% from each available Parquet file with seed 42, concatenates the sample, maps pickup density, and explores demand, fare revenue, and tips. Original data are not bundled. Row count depends on the input files; cached notebook output is not a fresh benchmark. Loading each whole monthly file before sampling can require substantial memory.

## Scope

The fare calculator is illustrative. Its constants and traffic multipliers are assumptions, it applies congestion fees unconditionally, and it omits parts of the official tariff and route eligibility rules. It is not a current taxi quote. Passenger count is validated and reported but does not change price. No holdout MAE, RMSE, or R² result is claimed. The next modeling step is a reproducible train/test workflow with leakage checks, a baseline, and held-out metrics.

## Structure

- `notebooks/`: exploratory analysis
- `predict_fare.py`: illustrative calculator
- `tests/`: invalid inputs, surcharge boundaries and arithmetic consistency
- `.github/workflows/tests.yml`: regression checks

[Abhi Kumar Gurjar](https://www.linkedin.com/in/abhigurjar) · Data Scientist & GenAI Engineer
