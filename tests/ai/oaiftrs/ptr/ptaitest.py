"""
Test suite for Stamp 4.6 AI Features - Pattern Recognition Module

Tests PatternAI class
"""
import json
from rich import print as rp
from rich.console import Console
from rich.panel import Panel
from lib.ai.oaiftrs.ptr.ptai import PatternAI
console = Console()
class Tests:
	def testPatternAI():
		"""Test PatternAI class with all methods"""
		rp("\n[bold cyan]=== Testing PatternAI ===[/bold cyan]\n")
		pattern = PatternAI()
		sequence1 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
		sequence2 = [100, 150, 200, 250, 300]
		sequence3 = [10, 20, 15, 30, 25, 40]
		sequence4 = [5, 10, 5, 10, 5, 10, 5, 10]
		rp("[yellow]Test 1: Detect Patterns[/yellow]")
		detected = pattern.detectPatterns(sequence1)
		rp(f"Sequence: {sequence1}")
		rp(f"Detected patterns: {detected}")
		rp("[green]✓ Pattern detection works[/green]\n")
		rp("[yellow]Test 2: Find Anomalies[/yellow]")
		anomalies = pattern.findAnomalies(sequence3)
		rp(f"Sequence: {sequence3}")
		rp(f"Anomalies: {anomalies}")
		rp("[green]✓ Anomaly detection works[/green]\n")
		rp("[yellow]Test 3: Predict Next Value[/yellow]")
		predicted = pattern.predictNext(sequence2)
		rp(f"Sequence: {sequence2}")
		rp(f"Predicted next: {predicted}")
		rp("[green]✓ Prediction works[/green]\n")
		rp("[yellow]Test 4: Classify Behavior[/yellow]")
		behavior = pattern.classifyBehavior(sequence4)
		rp(f"Sequence: {sequence4}")
		rp(f"Behavior type: {behavior}")
		rp("[green]✓ Behavior classification works[/green]\n")
		rp("[yellow]Test 5: Detect Cycles[/yellow]")
		cycles = pattern.detectCycles(sequence1)
		rp(f"Sequence: {sequence1}")
		rp(f"Detected cycles: {cycles}")
		rp("[green]✓ Cycle detection works[/green]\n")
		rp("[yellow]Test 6: Find Bursts[/yellow]")
		time_series = [1, 1, 1, 5, 5, 5, 5, 2, 2, 2]
		bursts = pattern.findBursts(time_series)
		rp(f"Time series: {time_series}")
		rp(f"Bursts: {bursts}")
		rp("[green]✓ Burst detection works[/green]\n")
		return True
	def runTests():
		"""Run all tests for pattern recognition AI"""
		rp(Panel.fit(
			"[bold magenta]Stamp 4.6 AI Test Suite - Pattern Recognition[/bold magenta]\n"
			"[yellow]Testing PatternAI class[/yellow]",
			title="PatternAI Test Suite"
		))
		tests_passed = 0
		tests_failed = 0
		try:
			if Tests.testPatternAI():
				tests_passed += 1
		except Exception as e:
			tests_failed += 1
			rp(f"[red]✗ PatternAI tests failed: {e}[/red]\n")
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