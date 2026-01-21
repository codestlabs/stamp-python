"""
Stamp PredictSystem Module

Machine learning prediction utilities.

Usage:
    >>> from stamp.oaiftrs.prd import PredictSystem
    >>> predictor = PredictSystem()
    >>> model = predictor.train(data, target)
"""

from typing import List, Dict, Any, Tuple
from collections import Counter
import statistics

# Module-level constants
DEFAULT_TEST_SPLIT = 0.2
MIN_TRAINING_SAMPLES = 10

class ModelType(Enum):
	"""Types of prediction models supported."""
	REGRESSION = "regression"
	CLASSIFICATION = "classification"
	SEQUENTIAL = "sequential"

class PredictSystem:
	"""Simple ML prediction system."""
	
	def __init__(self):
		"""Initialize PredictSystem."""
		self._models = {}
	
	def train(self, data: List[Dict], target: str, model_type: str = "regression") -> Dict[str, Any]:
		"""Train a prediction model from data.
		
		Args:
		    data: List of dicts with features and target
		    target: Name of target column
		    model_type: Type of model ('regression' or 'classification')
		
		Returns:
		    Dict with trained model info and metrics
		"""
		if not data or len(data) < MIN_TRAINING_SAMPLES:
			return {"model": None, "error": "insufficient_data"}
		
		if not isinstance(data[0], dict) or target not in data[0]:
			return {"model": None, "error": "invalid_target"}
		
		if model_type not in ["regression", "classification"]:
			return {"model": None, "error": "invalid_model_type"}
		
		# Split features and target
		features = []
		targets = []
		
		for item in data:
			if isinstance(item, dict) and target in item:
				feature_dict = {k: v for k, v in item.items() if k != target}
				features.append(feature_dict)
				targets.append(item[target])
		
		if len(features) < MIN_TRAINING_SAMPLES:
			return {"model": None, "error": "insufficient_training_samples"}
		
		# Train based on model type
		if model_type == "regression":
			model = self._trainRegression(features, targets)
		else:
			model = self._trainClassification(features, targets)
		
		# Calculate training accuracy
		predictions = [self._predictWithModel(f, model) for f in features]
		metrics = self._calculateMetrics(targets, predictions, model_type)
		
		return {
			"model": model,
			"model_type": model_type,
			"features": list(features[0].keys()) if features else [],
			"target": target,
			"training_samples": len(features),
			"metrics": metrics
		}
	
	def predict(self, model: Dict, new_data: Dict) -> Any:
		"""Make prediction using trained model.
		
		Args:
		    model: Trained model dict
		    new_data: New data point as dict
		
		Returns:
		    Prediction value or None
		"""
		if not model or not new_data:
			return None
		
		if "model" not in model or model["model"] is None:
			return None
		
		return self._predictWithModel(new_data, model["model"])
	
	def classify(self, model: Dict, new_data: Dict) -> str:
		"""Classify new data point.
		
		Args:
		    model: Trained classification model
		    new_data: New data point as dict
		
		Returns:
		    Predicted class or "unknown"
		"""
		if not model or not new_data:
			return "unknown"
		
		if model.get("model_type") != "classification":
			return "unknown"
		
		prediction = self.predict(model, new_data)
		return str(prediction) if prediction is not None else "unknown"
	
	def evaluate(self, model: Dict, test_data: List[Dict]) -> Dict[str, Any]:
		"""Evaluate model performance on test data.
		
		Args:
		    model: Trained model
		    test_data: Test data points
		
		Returns:
		    Dict with evaluation metrics
		"""
		if not model or not test_data:
			return {"error": "invalid_input"}
		
		if "model" not in model or model["model"] is None:
			return {"error": "invalid_model"}
		
		target = model.get("target")
		model_type = model.get("model_type", "regression")
		
		if not target:
			return {"error": "no_target_in_model"}
		
		# Extract features and targets
		features = []
		actual_targets = []
		
		for item in test_data:
			if isinstance(item, dict) and target in item:
				feature_dict = {k: v for k, v in item.items() if k != target}
				features.append(feature_dict)
				actual_targets.append(item[target])
		
		if not features:
			return {"error": "no_valid_test_data"}
		
		# Make predictions
		predictions = [self.predict(model, f) for f in features]
		
		# Calculate metrics
		metrics = self._calculateMetrics(actual_targets, predictions, model_type)
		metrics["test_samples"] = len(features)
		
		return metrics
	
	def _trainRegression(self, features: List[Dict], targets: List[Any]) -> Dict:
		"""Train simple regression model (weighted average)."""
		model = {"type": "regression", "weights": {}}
		
		# Calculate average target
		avg_target = statistics.mean([t for t in targets if isinstance(t, (int, float))])
		
		# Calculate feature correlations
		for key in features[0].keys():
			feature_values = []
			corresponding_targets = []
			
			for i, f in enumerate(features):
				if key in f and isinstance(f[key], (int, float)):
					feature_values.append(f[key])
					corresponding_targets.append(targets[i] if isinstance(targets[i], (int, float)) else avg_target)
			
			if len(feature_values) >= 2:
				corr = self._calculateCorrelation(feature_values, corresponding_targets)
				model["weights"][key] = corr
			else:
				model["weights"][key] = 0.0
		
		model["base_value"] = avg_target
		return model
	
	def _trainClassification(self, features: List[Dict], targets: List[Any]) -> Dict:
		"""Train simple classification model (k-nearest neighbors)."""
		model = {"type": "classification", "training_data": []}
		
		for i, feature in enumerate(features):
			model["training_data"].append({
				"features": feature,
				"target": targets[i]
			})
		
		return model
	
	def _predictWithModel(self, new_data: Dict, model: Dict) -> Any:
		"""Make prediction using internal model structure."""
		if model.get("type") == "regression":
			prediction = model.get("base_value", 0)
			
			for key, weight in model.get("weights", {}).items():
				if key in new_data and isinstance(new_data[key], (int, float)):
					prediction += weight * new_data[key]
			
			return prediction
		
		elif model.get("type") == "classification":
			training_data = model.get("training_data", [])
			
			if not training_data:
				return None
			
			# Simple 1-nearest neighbor
			min_distance = float('inf')
			best_target = None
			
			for train_point in training_data:
				distance = self._calculateDistance(new_data, train_point["features"])
				
				if distance < min_distance:
					min_distance = distance
					best_target = train_point["target"]
			
			return best_target
		
		return None
	
	def _calculateDistance(self, data1: Dict, data2: Dict) -> float:
		"""Calculate Euclidean distance between two data points."""
		distance = 0.0
		
		for key in set(data1.keys()) & set(data2.keys()):
			if isinstance(data1[key], (int, float)) and isinstance(data2[key], (int, float)):
				distance += (data1[key] - data2[key]) ** 2
		
		return distance ** 0.5
	
	def _calculateCorrelation(self, x: List[float], y: List[float]) -> float:
		"""Calculate correlation coefficient."""
		if len(x) != len(y) or len(x) < 2:
			return 0.0
		
		mean_x = statistics.mean(x)
		mean_y = statistics.mean(y)
		
		numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
		
		denom_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
		denom_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5
		
		if denom_x == 0 or denom_y == 0:
			return 0.0
		
		return numerator / (denom_x * denom_y)
	
	def _calculateMetrics(self, actual: List[Any], predicted: List[Any], model_type: str) -> Dict[str, Any]:
		"""Calculate evaluation metrics."""
		metrics = {}
		
		if model_type == "regression":
			numeric_actual = [a for a, p in zip(actual, predicted) if isinstance(a, (int, float)) and isinstance(p, (int, float))]
			
			if numeric_actual:
				numeric_predicted = [p for a, p in zip(actual, predicted) if isinstance(a, (int, float)) and isinstance(p, (int, float))]
				
				errors = [a - p for a, p in zip(numeric_actual, numeric_predicted)]
				metrics["mae"] = statistics.mean([abs(e) for e in errors])
				metrics["mse"] = statistics.mean([e ** 2 for e in errors])
				metrics["rmse"] = metrics["mse"] ** 0.5
		
		elif model_type == "classification":
			correct = sum(1 for a, p in zip(actual, predicted) if a == p)
			total = len(actual)
			
			if total > 0:
				metrics["accuracy"] = correct / total
				metrics["correct_predictions"] = correct
				metrics["total_predictions"] = total
		
		return metrics

# Main exports
__all__ = ["PredictSystem", "ModelType"]

if __name__ == "__main__":
	from rich import print as rp
	from rich.panel import Panel
	
	rp(Panel.fit(
		"[bold cyan]Stamp PredictSystem[/]\n"
		"[bold]Machine Learning Prediction System[/]",
		title="[bold]PredictSystem[/bold]"
	))
