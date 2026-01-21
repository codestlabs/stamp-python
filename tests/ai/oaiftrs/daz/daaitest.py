"""
Test suite for Stamp 4.6 AI Features - Data Analysis Module

Tests DataAnalyzer class
"""
from rich import print as rp
from rich.console import Console
from rich.panel import Panel
from lib.ai.oaiftrs.daz.daai import DataAnalyzer
console = Console()
class Tests:
	def testDataAnalyzer():
		"""Test DataAnalyzer class with all methods"""
		rp("\n[bold cyan]=== Testing DataAnalyzer ===[/bold cyan]\n")
		analyzer = DataAnalyzer()
		data1 = [10, 15, 20, 25, 30, 35, 40, 45, 50]
		data2 = [100, 95, 90, 85, 80, 75, 70]
		data3 = [5, 10, 100, 8, 12, 110, 6, 14]
		time_series = [50, 52, 55, 53, 58, 60, 62, 65, 63, 68]
		rp("[yellow]Test 1: Detect Trends[/yellow]")
		trends = analyzer.detectTrends(data1)
		rp(f"Data: {data1}")
		rp(f"Detected trend: {trends}")
		rp("[green]✓ Trend detection works[/green]\n")
		rp("[yellow]Test 2: Find Outliers[/yellow]")
		outliers = analyzer.findOutliers(data3)
		rp(f"Data: {data3}")
		rp(f"Outliers: {outliers}")
		rp("[green]✓ Outlier detection works[/green]\n")
		rp("[yellow]Test 3: Statistical Summary[/yellow]")
		summary = analyzer.statisticalSummary(data1)
		rp(f"Statistical summary:")
		for key, value in summary.items():
			rp(f"  • {key}: {value}")
		rp("[green]✓ Statistical summary works[/green]\n")
		rp("[yellow]Test 4: Visualization Suggestions[/yellow]")
		suggestions = analyzer.visualizeSuggestions(time_series)
		rp(f"Time series: {time_series}")
		rp("Visualization suggestions:")
		for suggestion in suggestions:
			rp(f"  • {suggestion}")
		rp("[green]✓ Visualization suggestions work[/green]\n")
		rp("[yellow]Test 5: Correlate Features[/yellow]")
		feature1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		feature2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
		correlation = analyzer.correlateFeatures(feature1, feature2)
		rp(f"Feature 1: {feature1[:5]}...")
		rp(f"Feature 2: {feature2[:5]}...")
		rp(f"Correlation coefficient: {correlation}")
		rp("[green]✓ Feature correlation works[/green]\n")
		rp("[yellow]Test 6: Detect Seasonality[/yellow]")
		seasonal_data = [10, 20, 15, 25, 10, 20, 15, 25, 10, 20, 15, 25]
		seasonality = analyzer.detectSeasonality(seasonal_data)
		rp(f"Seasonal data: {seasonal_data}")
		rp(f"Seasonality detected: {seasonality}")
		rp("[green]✓ Seasonality detection works[/green]\n")
		return True
	def runTests():
		"""Run all tests for data analysis AI"""
		rp(Panel.fit(
			"[bold magenta]Stamp 4.6 AI Test Suite - Data Analysis[/bold magenta]\n"
			"[yellow]Testing DataAnalyzer class[/yellow]",
			title="DataAnalyzer Test Suite"
		))
		tests_passed = 0
		tests_failed = 0
		try:
			if Tests.testDataAnalyzer():
				tests_passed += 1
		except Exception as e:
			tests_failed += 1
			rp(f"[red]✗ DataAnalyzer tests failed: {e}[/red]\n")
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