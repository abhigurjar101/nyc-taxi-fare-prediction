"""
NYC Taxi Fare Predictor & Operations Optimization
Calculates dynamic metered taxi fare based on trip distance, pickup/dropoff borough,
time of day, passenger count, airport surcharges, and congestion fees.
"""

import math
from typing import Dict, Any


# Illustrative demo constants; not a complete or current official tariff.
BASE_FARE = 3.00
PER_MILE_RATE = 2.80
CONGESTION_SURCHARGE = 2.50
NIGHT_SURCHARGE = 1.00       # 8:00 PM to 6:00 AM
RUSH_HOUR_SURCHARGE = 2.50   # 4:00 PM to 8:00 PM weekdays
JFK_FLAT_RATE = 70.00
AIRPORT_ACCESS_FEE = 1.75


def predict_taxi_fare(
    trip_distance_miles: float,
    pickup_hour: int = 14,
    is_weekday: bool = True,
    is_jfk_airport: bool = False,
    is_laguardia: bool = False,
    passenger_count: int = 1
) -> Dict[str, Any]:
    """
    Predicts NYC Yellow Taxi fare breakdown and estimated tip.
    """
    if (isinstance(trip_distance_miles, bool) or not isinstance(trip_distance_miles, (int, float))
            or not math.isfinite(trip_distance_miles) or trip_distance_miles <= 0):
        return {"error": "Trip distance must be a finite number greater than 0"}
    if isinstance(pickup_hour, bool) or not isinstance(pickup_hour, int) or not 0 <= pickup_hour <= 23:
        return {"error": "Pickup hour must be an integer from 0 to 23"}
    if isinstance(passenger_count, bool) or not isinstance(passenger_count, int) or not 1 <= passenger_count <= 6:
        return {"error": "Passenger count must be an integer from 1 to 6"}
    if not all(isinstance(flag, bool) for flag in (is_weekday, is_jfk_airport, is_laguardia)):
        return {"error": "Weekday and airport flags must be booleans"}
    if is_jfk_airport and is_laguardia:
        return {"error": "Select at most one airport mode"}

    if is_jfk_airport:
        meter_fare = JFK_FLAT_RATE
        rate_type = "JFK Flat Rate"
    else:
        # Distance-based fare calculation with standard non-linear traffic slowdown factor
        traffic_multiplier = 1.25 if (16 <= pickup_hour <= 19 and is_weekday) else 1.05
        meter_fare = BASE_FARE + (trip_distance_miles * PER_MILE_RATE * traffic_multiplier)
        rate_type = "Standard Meter Rate"

    # Surcharges
    surcharges = CONGESTION_SURCHARGE
    if 20 <= pickup_hour or pickup_hour < 6:
        surcharges += NIGHT_SURCHARGE
    elif 16 <= pickup_hour <= 19 and is_weekday:
        surcharges += RUSH_HOUR_SURCHARGE

    if is_jfk_airport or is_laguardia:
        surcharges += AIRPORT_ACCESS_FEE

    subtotal = round(meter_fare + surcharges, 2)
    suggested_tip_18 = round(subtotal * 0.18, 2)
    total_fare = round(subtotal + suggested_tip_18, 2)

    return {
        "rate_type": rate_type,
        "trip_distance_miles": trip_distance_miles,
        "pickup_hour": f"{pickup_hour:02d}:00",
        "passenger_count": passenger_count,
        "base_meter_fare": round(meter_fare, 2),
        "total_surcharges": round(surcharges, 2),
        "subtotal_fare": subtotal,
        "recommended_tip": suggested_tip_18,
        "estimated_total_fare": total_fare
    }


def main():
    print("=" * 80)
    print("🚖 NYC TAXI FARE PREDICTION ENGINE")
    print("   Exploratory Analysis & Predictive Modeling by Abhi Gurjar")
    print("=" * 80)

    scenarios = [
        {"name": "Midday Midtown to Lower Manhattan", "dist": 3.4, "hour": 14, "weekday": True, "jfk": False, "lga": False},
        {"name": "Weekday Evening Rush Hour (Midtown to Brooklyn)", "dist": 5.8, "hour": 17, "weekday": True, "jfk": False, "lga": False},
        {"name": "Late Night Trip to JFK International Airport", "dist": 16.5, "hour": 23, "weekday": True, "jfk": True, "lga": False},
    ]

    for s in scenarios:
        res = predict_taxi_fare(
            trip_distance_miles=s["dist"],
            pickup_hour=s["hour"],
            is_weekday=s["weekday"],
            is_jfk_airport=s["jfk"],
            is_laguardia=s["lga"]
        )
        print(f"\n📍 Scenario: {s['name']}")
        print(f"   • Distance:         {res['trip_distance_miles']} miles")
        print(f"   • Pickup Hour:      {res['pickup_hour']}")
        print(f"   • Meter Fare:       ${res['base_meter_fare']}")
        print(f"   • NYC Surcharges:   ${res['total_surcharges']}")
        print(f"   • Subtotal:         ${res['subtotal_fare']}")
        print(f"   • 18% Tip Estimate: ${res['recommended_tip']}")
        print(f"   • Total Estimated:  ${res['estimated_total_fare']}")

    print("\n" + "=" * 80)
    print("Demo complete. Run the test suite for assertions.")
    print("=" * 80)


if __name__ == "__main__":
    main()
