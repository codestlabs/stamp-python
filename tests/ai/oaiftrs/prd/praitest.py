"""
Test suite for Stamp 4.6 AI Features - ML Predictions Module

Tests PredictSystem class
"""
from rich import print as rp
from rich.console import Console
from rich.panel import Panel

from lib.ai.oaiftrs.prd.prai import PredictSystem, ModelType
console = Console()
class Tests:
	def testPredictSystem():
		"""Test PredictSystem class with all methods"""
		rp("\n[bold cyan]=== Testing PredictSystem ===[/bold cyan]\n")
		predictor = PredictSystem()
		training_data = [
			{"features": [5.1, 3.5, 1.4, 0.2], "label": "setosa"},
			{"features": [4.9, 3.0, 1.4, 0.2], "label": "setosa"},
			{"features": [7.0, 3.2, 4.7, 1.4], "label": "versicolor"},
			{"features": [6.4, 3.2, 4.5, 1.5], "label": "versicolor"},
			{"features": [6.3, 3.3, 6.0, 2.5], "label": "virginica"},
			{"features": [5.8, 2.7, 5.1, 1.9], "label": "virginica"}
		]
		test_features = [
			[5.0, 3.4, 1.5, 0.2],
			[6.5, 3.0, 5.5, 1.8]
		]
		rp("[yellow]Test 1: Train Model[/yellow]")
		model_id = predictor.train(training_data, model_type=ModelType.CLASSIFIER)
		rp(f"Trained model with {len(training_data)} samples")
		rp(f"Model ID: {model_id}")
		rp("[green]✓ Model training works[/green]\n")
		rp("[yellow]Test 2: Make Predictions[/yellow]")
		predictions = predictor.predict(model_id, test_features)
		rp(f"Test features: {test_features}")
		rp(f"Predictions: {predictions}")
		rp("[green]✓ Prediction works[/green]\n")
		rp("[yellow]Test 3: Classify Data[/yellow]")
		classifications = predictor.classify(model_id, test_features)
		rp(f"Classifications: {classifications}")
		rp("[green]✓ Classification works[/green]\n")
		rp("[yellow]Test 4: Evaluate Model[/yellow]")
		test_labels = ["setosa", "versicolor"]
		metrics = predictor.evaluate(model_id, test_features, test_labels)
		rp(f"Model evaluation metrics:")
		for metric, value in metrics.items():
			rp(f"  • {metric}: {value}")
		rp("[green]✓ Model evaluation works[/green]\n")
		rp("[yellow]Test 5: Train Regression Model[/yellow]")
		regression_data = [
			{"features": [1, 2, 3], "label": 6},
			{"features": [2, 3, 4], "label": 9},
			{"features": [3, 4, 5], "label": 12},
			{"features": [4, 5, 6], "label": 15}
		]
		reg_model_id = predictor.train(regression_data, model_type=ModelType.REGRESSOR)
		rp(f"Trained regression model: {reg_model_id}")
		reg_test = [[2, 3, 4], [3, 4, 5]]
		reg_predictions = predictor.predict(reg_model_id, reg_test)
		rp(f"Regression predictions: {reg_predictions}")
		rp("[green]✓ Regression model works[/green]\n")
		return True
	def runTests():
		"""Run all tests for ML predictions AI"""
		rp(Panel.fit(
			"[bold magenta]Stamp 4.6 AI Test Suite - ML Predictions[/bold magenta]\n"
			"[yellow]Testing PredictSystem class[/yellow]",
			title="PredictSystem Test Suite"
		))
		tests_passed = 0
		tests_failed = 0
		try:
			if Tests.testPredictSystem():
				tests_passed += 1
		except Exception as e:
			tests_failed += 1
			rp(f"[red]✗ PredictSystem tests failed: {e}[/red]\n")
		rp("\n" + "="*50)
		rp(f"[bold]Test Summary[/bold]")
		rp(f"[green]Passed: {tests_passed}[/green]")
		rp(f"[red]Failed: {tests_failed}[/red]")
		rp(f"[cyan]Total: {tests_passed + tests_failed}[/cyan]")
		if tests_failed == 0:
			rp("\n[bold green]🎉 All tests passed![/bold green]")
		else:
			if tests_failed > 1:
				rp(f"\n[bold red]❌ {tests_failed} tests failed[/bold red]")
			else:
				rp(f"\n[bold red]❌ {tests_failed} test failed[/bold red]")
		rp("="*50 + "\n")
if __name__ == "__main__":
	Tests.runTests()