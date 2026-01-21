print("""
Tests for ForecastAI module (Stamp 4.7)

Required test files:
- No external files needed (uses synthetic time series data)
""")

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../..'))

from lib.ai.oaiftrs.fct.fcai import ForecastAI

def test_forecastARIMA():
	"""Test ARIMA forecasting"""
	print("Running test_forecastARIMA")
	data = [10, 12, 14, 16, 18, 20]
	result = ForecastAI.forecastARIMA(data, 3)
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_detectSeasonality():
	"""Test seasonality detection"""
	print("Running test_detectSeasonality")
	data = list(range(50))
	result = ForecastAI.detectSeasonality(data)
	print(f"Result: {result}")
	assert isinstance(result, dict)

def test_anomalyDetection():
	"""Test anomaly detection"""
	print("Running test_anomalyDetection")
	data = [10, 12, 14, 100, 16, 18]
	result = ForecastAI.anomalyDetection(data)
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_trendDecomposition():
	"""Test trend decomposition"""
	print("Running test_trendDecomposition")
	data = list(range(20))
	result = ForecastAI.trendDecomposition(data)
	print(f"Result: {result}")
	assert isinstance(result, dict)

def test_multiVariateForecast():
	"""Test multivariate forecasting"""
	print("Running test_multiVariateForecast")
	data = {"price": [10, 12, 14], "volume": [100, 120, 140]}
	result = ForecastAI.multiVariateForecast(data, "price")
	print(f"Result: {result}")
	assert isinstance(result, list)

if __name__ == "__main__":
	print("\n=== Testing ForecastAI module ===")
	print("No external files needed\n")
	
	try:
		test_forecastARIMA()
		test_detectSeasonality()
		test_anomalyDetection()
		test_trendDecomposition()
		test_multiVariateForecast()
		print("\n✓ All ForecastAI tests passed!")
	except AssertionError as e:
		print(f"\n✗ Test failed: {e}")
	except Exception as e:
		print(f"\n✗ Error: {e}")
