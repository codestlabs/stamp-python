"""
Stamp PatternAI Module

Pattern recognition and anomaly detection utilities.

Usage:
    >>> from stamp.oaiftrs.ptr import PatternAI
    >>> pattern_ai = PatternAI()
    >>> patterns = pattern_ai.detectPatterns(log_text)
"""

import re
from typing import List, Dict, Any, Tuple
from enum import Enum
from collections import Counter

# Module-level constants
DEFAULT_PATTERN_WINDOW = 5
DEFAULT_ANOMALY_THRESHOLD = 2.0
DEFAULT_PATTERN_MIN_OCCURRENCES = 3

class PatternType(Enum):
	"""Types of patterns detectable."""
	SEQUENTIAL = "sequential"
	CYCLICAL = "cyclical"
	BURST = "burst"
	GRADUAL = "gradual"
	RANDOM = "random"

class PatternAI:
	"""Pattern recognition and anomaly detection."""
	
	def __init__(self):
		"""Initialize PatternAI analyzer."""
		pass
	
	def detectPatterns(self, text: str, patterns: List[str] = None) -> Dict[str, Any]:
		"""Detect patterns in text using regex patterns.
		
		Args:
		    text: Input text to analyze
		    patterns: Optional list of regex patterns to search
		
		Returns:
		    Dict with detected patterns and counts
		"""
		if patterns is None:
			patterns = [
				r"error\s+\w+",
				r"warning\s+\w+",
				r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
				r"[A-Z]{2,}_\w+",
				r"\d{4}-\d{2}-\d{2}"
			]
		
		if not text or not isinstance(text, str):
			return {"patterns_found": [], "counts": {}}
		
		results = {"patterns_found": [], "counts": {}}
		
		for pattern in patterns:
			try:
				matches = re.findall(pattern, text, re.IGNORECASE)
				if matches and len(matches) >= DEFAULT_PATTERN_MIN_OCCURRENCES:
					results["patterns_found"].append(pattern)
					results["counts"][pattern] = len(matches)
			except re.error:
				continue
		
		return results
	
	def findAnomalies(self, data: List[float], threshold: float = None) -> List[int]:
		"""Find anomalies in numerical data using z-score.
		
		Args:
		    data: List of numerical data points
		    threshold: Standard deviation threshold for anomaly detection
		
		Returns:
		    List of indices where anomalies occur
		"""
		if threshold is None:
			threshold = DEFAULT_ANOMALY_THRESHOLD
		
		if not data or len(data) < 3:
			return []
		
		avg = sum(data) / len(data)
		variance = sum((x - avg) ** 2 for x in data) / len(data)
		
		if variance == 0:
			return []
		
		std_dev = variance ** 0.5
		anomalies = []
		
		for i, value in enumerate(data):
			z_score = abs(value - avg) / std_dev
			if z_score > threshold:
				anomalies.append(i)
		
		return anomalies
	
	def predictNext(self, sequence: List[Any]) -> Any:
		"""Predict next value in sequence (simple moving average).
		
		Args:
		    sequence: List of sequence values
		
		Returns:
		    Predicted next value or None if insufficient data
		"""
		if not sequence or len(sequence) < 2:
			return None
		
		recent = sequence[-5:] if len(sequence) >= 5 else sequence
		
		if all(isinstance(x, (int, float)) for x in recent):
			return sum(recent) / len(recent)
		
		most_common = Counter(recent).most_common(1)
		return most_common[0][0] if most_common else None
	
	def classifyBehavior(self, data_points: List[float]) -> str:
		"""Classify behavior pattern from data points.
		
		Args:
		    data_points: List of numerical data points
		
		Returns:
		    String description of behavior
		"""
		if not data_points or len(data_points) < 2:
			return "insufficient_data"
		
		first = data_points[0]
		last = data_points[-1]
		trend = last - first
		
		if abs(trend) < 0.01 * abs(first):
			return "stable"
		elif trend > 0:
			return "increasing"
		else:
			return "decreasing"
	
	def detectCycles(self, data: List[float]) -> Dict[str, Any]:
		"""Detect cyclical patterns in data.
		
		Args:
		    data: List of numerical data points
		
		Returns:
		    Dict with cycle detection results
		"""
		if not data or len(data) < 6:
			return {"has_cycles": False, "period": None}
		
		correlations = []
		max_period = len(data) // 2
		
		for period in range(2, min(max_period, 10)):
			correlated = 0
			for i in range(len(data) - period):
				if (data[i] > data[i + period] and data[i + 1] > data[i + period + 1]) or \
				   (data[i] < data[i + period] and data[i + 1] < data[i + period + 1]):
					correlated += 1
			
			if correlated > len(data) * 0.5:
				correlations.append((period, correlated))
		
		if correlations:
			best = max(correlations, key=lambda x: x[1])
			return {"has_cycles": True, "period": best[0], "confidence": best[1] / len(data)}
		
		return {"has_cycles": False, "period": None}
	
	def findBursts(self, data: List[float]) -> List[Tuple[int, int]]:
		"""Find burst patterns (sudden increases) in data.
		
		Args:
		    data: List of numerical data points
		
		Returns:
		    List of tuples (start_index, end_index) for each burst
		"""
		if not data or len(data) < 3:
			return []
		
		avg = sum(data) / len(data)
		bursts = []
		in_burst = False
		start = 0
		
		for i, value in enumerate(data):
			if value > avg * 2.0:
				if not in_burst:
					start = i
					in_burst = True
			else:
				if in_burst:
					bursts.append((start, i - 1))
					in_burst = False
		
		if in_burst:
			bursts.append((start, len(data) - 1))
		
		return bursts

# Main exports
__all__ = ["PatternAI", "PatternType"]

if __name__ == "__main__":
	from rich import print as rp
	from rich.panel import Panel
	
	rp(Panel.fit(
		"[bold cyan]Stamp PatternAI[/]\n"
		"[bold]Pattern Recognition & Anomaly Detection[/]",
		title="[bold]PatternAI[/bold]"
	))
