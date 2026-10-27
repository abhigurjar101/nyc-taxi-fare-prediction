import math
import unittest
from predict_fare import predict_taxi_fare

class FareTests(unittest.TestCase):
    def test_invalid_inputs(self):
        for distance in [0, -1, math.nan, math.inf, "3", True]:
            self.assertIn("error", predict_taxi_fare(distance))
        for hour in [-1, 24, 1.5, True]:
            self.assertIn("error", predict_taxi_fare(3, pickup_hour=hour))
        self.assertIn("error", predict_taxi_fare(3, is_jfk_airport=True, is_laguardia=True))
        self.assertIn("error", predict_taxi_fare(3, passenger_count=0))

    def test_breakdown_and_rush_hour_boundaries(self):
        midday = predict_taxi_fare(3, pickup_hour=14)
        rush = predict_taxi_fare(3, pickup_hour=16)
        weekend = predict_taxi_fare(3, pickup_hour=16, is_weekday=False)
        self.assertGreater(rush["estimated_total_fare"], midday["estimated_total_fare"])
        self.assertEqual(weekend["total_surcharges"], midday["total_surcharges"])
        self.assertEqual(predict_taxi_fare(3, pickup_hour=20)["total_surcharges"], 3.5)
        self.assertEqual(predict_taxi_fare(3, pickup_hour=6)["total_surcharges"], 2.5)
        self.assertEqual(midday["estimated_total_fare"], round(midday["subtotal_fare"] + midday["recommended_tip"], 2))
