"""
Test suite for Stamp 4.6 AI Features - Code Intelligence Module

Tests CodeAI class
"""
from rich import print as rp
from rich.console import Console
from rich.panel import Panel
from lib.ai.oaiftrs.cdi.coai import CodeAI
console = Console()
class Tests:
	def testCodeAI():
		"""Test CodeAI class with all methods"""
		rp("\n[bold cyan]=== Testing CodeAI ===[/bold cyan]\n")
		code = CodeAI()
		code1 = """def calculate_sum(numbers):
		total = 0
		for num in numbers:
			total += num
		return total
		"""
		code2 = """def calculate_sum(nums):
		s = 0
		for n in nums:
			s += n
		return s
		"""
		code3 = """def get_data():
			data = []
			for i in range(100):
				item = fetch_item(i)
				data.append(item)
			return data
		"""
		rp("[yellow]Test 1: Detect Duplicates[/yellow]")
		duplicates = code.detectDuplicates([code1, code2])
		rp(f"Found {len(duplicates)} duplicate functions")
		for dup in duplicates:
			rp(f"  • {dup}")
		rp("[green]✓ Duplicate detection works[/green]\n")
		rp("[yellow]Test 2: Find Code Smells[/yellow]")
		smells = code.findSmells(code3)
		rp("Code smells detected:")
		for smell in smells:
			rp(f"  • {smell}")
		rp("[green]✓ Code smell detection works[/green]\n")
		rp("[yellow]Test 3: Analyze Complexity[/yellow]")
		complexity = code.analyzeComplexity(code1)
		rp(f"Code complexity: {complexity}")
		rp("[green]✓ Complexity analysis works[/green]\n")
		rp("[yellow]Test 4: Suggest Refactoring[/yellow]")
		suggestions = code.suggestRefactoring(code3)
		rp("Refactoring suggestions:")
		for suggestion in suggestions:
			rp(f"  • {suggestion}")
		rp("[green]✓ Refactoring suggestions work[/green]\n")
		rp("[yellow]Test 5: Code Similarity[/yellow]")
		similar = code.codeSimilarity(code1, code2)
		rp(f"Similarity score: {similar}")
		rp("[green]✓ Code similarity works[/green]\n")
		rp("[yellow]Test 6: Check Line Length[/yellow]")
		long_code = """result = very_long_function_name_that_exceeds_standard_line_length_limits_and_should_be_refactored_into_smaller_pieces(parameter1, parameter2, parameter3, parameter4)"""
		long_lines = code.checkLineLength(long_code, max_length=100)
		rp(f"Found {len(long_lines)} lines exceeding max length")
		for line in long_lines:
			rp(f"  • Line {line['line_number']}: {line['length']} chars")
		rp("[green]✓ Line length checking works[/green]\n")
		return True
	def runTests():
		"""Run all tests for code intelligence AI"""
		rp(Panel.fit(
			"[bold magenta]Stamp 4.6 AI Test Suite - Code Intelligence[/bold magenta]\n"
			"[yellow]Testing CodeAI class[/yellow]",
			title="CodeAI Test Suite"
		))
		tests_passed = 0
		tests_failed = 0
		try:
			if Tests.testCodeAI():
				tests_passed += 1
		except Exception as e:
			tests_failed += 1
			rp(f"[red]✗ CodeAI tests failed: {e}[/red]\n")
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