"""
ForecastAI - Time series forecasting module for Stamp 4.7

Provides ARIMA forecasting, seasonality detection,
anomaly detection, trend decomposition, and multivariate forecasting.
"""

import json
import hashlib
from collections import deque

class ForecastAI:
	"""
	Time series forecasting class.
	
	Provides methods for ARIMA forecasting, seasonality detection,
	anomaly detection, trend decomposition, and multivariate forecasting.
	"""
	
	def forecastARIMA(data, periods):
		"""
		ARIMA forecasting.
		
		Parameters:
			data: Time series data
			periods: Number of periods to forecast
		
		Returns:
			list: Forecasted values
		
		Example:
			>>> forecast = ForecastAI()
			>>> forecast.forecastARIMA(data, 5)
			[100, 102, 105, 108, 110]
		"""
		if not data:
			return []
		
		# Convert data to list of numbers
		if isinstance(data, (list, tuple)):
			values = [float(x) for x in data]
		else:
			values = [float(data)]
		
		# Simple ARIMA-like forecasting using moving average
		if len(values) < 3:
			return values[:periods] if len(values) >= periods else values
		
		# Calculate moving average and trend
		window = min(5, len(values))
		ma = sum(values[-window:]) / window
		
		# Calculate trend
		if len(values) >= 2:
			trend = (values[-1] - values[0]) / len(values)
		else:
			trend = 0
		
		# Generate forecast
		forecast = []
		for i in range(periods):
			# Add trend and some noise
			prediction = ma + trend * (i + 1)
			noise = (hash(str(i)) % 100) / 1000.0 * ma * 0.05
			forecast.append(round(prediction + noise, 2))
		
		return forecast
	
	def detectSeasonality(data):
		"""
		Detect seasonal patterns.
		
		Parameters:
			data: Time series data
		
		Returns:
			dict: Seasonality information
		
		Example:
			>>> forecast = ForecastAI()
			>>> forecast.detectSeasonality(data)
			{"has_seasonality": True, "period": 12}
		"""
		if not data:
			return {"has_seasonality": False, "period": None}
		
		# Convert to list
		if isinstance(data, (list, tuple)):
			values = [float(x) for x in data]
		else:
			values = [float(data)]
		
		if len(values) < 12:
			return {"has_seasonality": False, "period": None, "reason": "insufficient data"}
		
		# Simple seasonality detection using autocorrelation
		periods_to_test = [7, 12, 30, 365]
		
		best_period = None
		best_correlation = 0
		
		# Calculate mean
		mean = sum(values) / len(values)
		
		for period in periods_to_test:
			if period >= len(values):
				continue
			
			# Calculate correlation with lagged series
			original = values[:len(values) - period]
			lagged = values[period:]
			
			if len(original) < 2:
				continue
			
			# Calculate correlation
			cov = sum((o - mean) * (l - mean) for o, l in zip(original, lagged))
			var = sum((x - mean) ** 2 for x in values)
			
			if var > 0:
				correlation = abs(cov / var)
				
				if correlation > best_correlation and correlation > 0.3:
					best_correlation = correlation
					best_period = period
		
		return {
			"has_seasonality": best_period is not None,
			"period": best_period,
			"confidence": round(best_correlation, 3) if best_correlation else 0.0
		}
	
	def anomalyDetection(data):
		"""
		Detect anomalies in time series.
		
		Parameters:
			data: Time series data
		
		Returns:
			list: Indices of anomalies found
		
		Example:
			>>> forecast = ForecastAI()
			>>> forecast.anomalyDetection(data)
			[5, 12, 20]
		"""
		if not data:
			return []
		
		# Convert to list
		if isinstance(data, (list, tuple)):
			values = [float(x) for x in data]
		else:
			values = [float(data)]
		
		if len(values) < 5:
			return []
		
		# Calculate statistics
		mean = sum(values) / len(values)
		variance = sum((x - mean) ** 2 for x in values) / len(values)
		stddev = variance ** 0.5
		
		# Detect anomalies using z-score
		anomalies = []
		threshold = 2.5  # Standard deviations
		
		for i, value in enumerate(values):
			if stddev > 0:
				z_score = abs(value - mean) / stddev
				if z_score > threshold:
					anomalies.append({
						"index": i,
						"value": value,
						"z_score": round(z_score, 3),
						"severity": "high" if z_score > 3.0 else "medium"
					})
		
		return anomalies
	
	def trendDecomposition(data):
		"""
		Decompose into trend, seasonal, and residual.
		
		Parameters:
			data: Time series data
		
		Returns:
			dict: Decomposed components
		
		Example:
			>>> forecast = ForecastAI()
			>>> forecast.trendDecomposition(data)
			{"trend": [...], "seasonal": [...], "residual": [...]}
		"""
		if not data:
			return {"trend": [], "seasonal": [], "residual": []}
		
		# Convert to list
		if isinstance(data, (list, tuple)):
			values = [float(x) for x in data]
		else:
			values = [float(data)]
		
		if len(values) < 3:
			return {
				"trend": values,
				"seasonal": [0] * len(values),
				"residual": [0] * len(values)
			}
		
		# Simple trend using moving average
		window = min(7, len(values) // 3)
		trend = []
		
		for i in range(len(values)):
			start = max(0, i - window // 2)
			end = min(len(values), i + window // 2 + 1)
			trend.append(round(sum(values[start:end]) / (end - start), 2))
		
		# Residual (data - trend)
		residual = [round(v - t, 2) for v, t in zip(values, trend)]
		
		# Seasonal component (simplified)
		seasonal = [round(r - (sum(residual) / len(residual)), 2) for r in residual]
		
		return {
			"trend": trend,
			"seasonal": seasonal,
			"residual": residual,
			"original": values
		}
	
	def multiVariateForecast(data, target):
		"""
		Multivariate forecasting.
		
		Parameters:
			data: Multivariate time series data
			target: Target variable name or index
		
		Returns:
			list: Forecasted values for target
		
		Example:
			>>> forecast = ForecastAI()
			>>> forecast.multiVariateForecast(data, "price")
			[100, 102, 105, 108, 110]
		"""
		if not data:
			return []
		
		# Parse data
		if isinstance(data, dict):
			# Dictionary with multiple variables
			if target in data:
				target_data = data[target]
			else:
				# Use first key
				target_data = list(data.values())[0]
		elif isinstance(data, list):
			# List of dictionaries or list of lists
			if all(isinstance(d, dict) for d in data):
				# Extract target column
				if isinstance(target, str) and target in data[0]:
					target_data = [d[target] for d in data]
				else:
					# Use first key
					first_key = list(data[0].keys())[0]
					target_data = [d[first_key] for d in data]
			elif all(isinstance(row, (list, tuple)) for row in data):
				# Use specified column index
				target_idx = int(target) if str(target).isdigit() else 0
				target_data = [row[target_idx] for row in data]
			else:
				target_data = data
		else:
			target_data = [float(data)]
		
		# Forecast using ARIMA method
		return self.forecastARIMA(target_data, min(5, len(target_data)))
