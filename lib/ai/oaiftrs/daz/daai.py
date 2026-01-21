"""
Stamp DataAnalyzer Module

Data intelligence utilities for analysis and statistics.

Usage:
    >>> from stamp.oaiftrs.daz import DataAnalyzer
    >>> analyzer = DataAnalyzer()
    >>> trends = analyzer.detectTrends(data)
"""

from typing import List, Dict, Any, Tuple
from collections import Counter
import statistics

# Module-level constants
DEFAULT_WINDOW_SIZE = 5
DEFAULT_OUTLIER_THRESHOLD = 2.0
DEFAULT_TOP_N = 10

class DataAnalyzer:
	"""Data intelligence and statistical analysis."""
	
	def __init__(self):
		"""Initialize DataAnalyzer."""
		pass
	
	def detectTrends(self, data: List[float], window_size: int = None) -> List[Dict[str, Any]]:
		"""Detect trends in time series data.
		
		Args:
		    data: List of numerical data points
		    window_size: Size of sliding window for trend detection
		
		Returns:
		    List of trend descriptions with start/end indices
		"""
		if window_size is None:
			window_size = DEFAULT_WINDOW_SIZE
		
		if not data or len(data) < window_size * 2:
			return []
		
		trends = []
		
		for i in range(0, len(data) - window_size + 1):
			window = data[i:i + window_size]
			
			if len(window) < 2:
				continue
			
			start_val = window[0]
			end_val = window[-1]
			change = end_val - start_val
			change_pct = (change / start_val * 100) if start_val != 0 else 0
			
			if abs(change_pct) > 5.0:
				direction = "increasing" if change > 0 else "decreasing"
				trends.append({
					"start_index": i,
					"end_index": i + window_size - 1,
					"direction": direction,
					"change": change,
					"change_percent": change_pct
				})
		
		return trends
	
	def findOutliers(self, data: List[float], method: str = "iqr") -> List[int]:
		"""Find outliers in data using specified method.
		
		Args:
		    data: List of numerical data points
		    method: Method to use ('iqr' or 'zscore')
		
		Returns:
		    List of indices where outliers occur
		"""
		if not data or len(data) < 4:
			return []
		
		outliers = []
		
		if method == "iqr":
			sorted_data = sorted(data)
			q1 = statistics.median(sorted_data[:len(sorted_data) // 2])
			q3 = statistics.median(sorted_data[len(sorted_data) // 2:])
			iqr = q3 - q1
			
			lower_bound = q1 - 1.5 * iqr
			upper_bound = q3 + 1.5 * iqr
			
			for i, value in enumerate(data):
				if value < lower_bound or value > upper_bound:
					outliers.append(i)
		
		elif method == "zscore":
			mean = statistics.mean(data)
			stdev = statistics.stdev(data) if len(data) > 1 else 0
			
			if stdev == 0:
				return []
			
			for i, value in enumerate(data):
				z_score = abs(value - mean) / stdev
				if z_score > DEFAULT_OUTLIER_THRESHOLD:
					outliers.append(i)
		
		return outliers
	
	def statisticalSummary(self, data: List[Any]) -> Dict[str, Any]:
		"""Generate statistical summary of data.
		
		Args:
		    data: List of data points (can be numeric or categorical)
		
		Returns:
		    Dict with statistical metrics
		"""
		if not data:
			return {}
		
		summary = {"count": len(data), "type": "mixed"}
		
		numeric_data = [x for x in data if isinstance(x, (int, float))]
		
		if numeric_data:
			summary["type"] = "numeric"
			summary["min"] = min(numeric_data)
			summary["max"] = max(numeric_data)
			summary["mean"] = statistics.mean(numeric_data)
			summary["median"] = statistics.median(numeric_data)
			
			if len(numeric_data) > 1:
				summary["std_dev"] = statistics.stdev(numeric_data)
				summary["variance"] = statistics.variance(numeric_data)
			
			summary["sum"] = sum(numeric_data)
		else:
			summary["type"] = "categorical"
			counter = Counter(data)
			summary["unique"] = len(counter)
			summary["most_common"] = counter.most_common(DEFAULT_TOP_N)
		
		return summary
	
	def visualizeSuggestions(self, data: List[Any]) -> List[str]:
		"""Suggest visualization types for data.
		
		Args:
		    data: List of data points
		
		Returns:
		    List of suggested visualization types
		"""
		if not data:
			return []
		
		suggestions = []
		numeric_data = [x for x in data if isinstance(x, (int, float))]
		
		if numeric_data:
			if len(numeric_data) > 1:
				suggestions.append("line_chart: Time series trends")
				suggestions.append("histogram: Distribution")
			
			if len(set(numeric_data)) > 5:
				suggestions.append("box_plot: Outliers and quartiles")
			
			if len(numeric_data) > 2:
				suggestions.append("scatter_plot: Correlation analysis")
		else:
			if len(set(data)) <= 10:
				suggestions.append("bar_chart: Category comparison")
				suggestions.append("pie_chart: Proportion")
			else:
				suggestions.append("bar_chart: Top categories")
		
		return suggestions
	
	def correlateFeatures(self, data1: List[float], data2: List[float]) -> Dict[str, Any]:
		"""Calculate correlation between two features.
		
		Args:
		    data1: First feature data
		    data2: Second feature data
		
		Returns:
		    Dict with correlation coefficient and strength
		"""
		if not data1 or not data2 or len(data1) != len(data2):
			return {"correlation": None, "strength": "insufficient_data"}
		
		if len(data1) < 2:
			return {"correlation": None, "strength": "insufficient_data"}
		
		mean1 = statistics.mean(data1)
		mean2 = statistics.mean(data2)
		
		numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
		
		sum1 = sum((x - mean1) ** 2 for x in data1)
		sum2 = sum((y - mean2) ** 2 for y in data2)
		
		denominator = (sum1 ** 0.5) * (sum2 ** 0.5)
		
		if denominator == 0:
			return {"correlation": None, "strength": "no_variance"}
		
		correlation = numerator / denominator
		
		if abs(correlation) >= 0.8:
			strength = "very_strong"
		elif abs(correlation) >= 0.6:
			strength = "strong"
		elif abs(correlation) >= 0.4:
			strength = "moderate"
		elif abs(correlation) >= 0.2:
			strength = "weak"
		else:
			strength = "very_weak"
		
		return {"correlation": correlation, "strength": strength}
	
	def detectSeasonality(self, data: List[float], period: int) -> Dict[str, Any]:
		"""Detect seasonal patterns in time series data.
		
		Args:
		    data: List of numerical data points
		    period: Expected period length
		
		Returns:
		    Dict with seasonality detection results
		"""
		if not data or len(data) < period * 3:
			return {"has_seasonality": False, "confidence": 0.0}
		
		# Decompose into periods
		periods = []
		for i in range(0, len(data) - period + 1, period):
			if i + period <= len(data):
				periods.append(data[i:i + period])
		
		if len(periods) < 2:
			return {"has_seasonality": False, "confidence": 0.0}
		
		# Calculate correlation between periods
		correlations = []
		for i in range(len(periods) - 1):
			corr = self.correlateFeatures(periods[i], periods[i + 1])
			if corr["correlation"] is not None:
				correlations.append(abs(corr["correlation"]))
		
		if not correlations:
			return {"has_seasonality": False, "confidence": 0.0}
		
		avg_correlation = sum(correlations) / len(correlations)
		
		return {
			"has_seasonality": avg_correlation > 0.7,
			"confidence": avg_correlation,
			"avg_period_correlation": avg_correlation
		}

# Main exports
__all__ = ["DataAnalyzer"]

if __name__ == "__main__":
	from rich import print as rp
	from rich.panel import Panel
	
	rp(Panel.fit(
		"[bold cyan]Stamp DataAnalyzer[/]\n"
		"[bold]Data Intelligence & Statistical Analysis[/]",
		title="[bold]DataAnalyzer[/bold]"
	))
