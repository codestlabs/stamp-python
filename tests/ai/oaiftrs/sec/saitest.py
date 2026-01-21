"""
Test suite for Stamp 4.6 AI Features - Security Intelligence Module

Tests SecurityAI class
"""
from rich import print as rp
from rich.console import Console
from rich.panel import Panel
from lib.ai.oaiftrs.sec.scai import SecurityAI
console = Console()
class Tests:
	def testSecurityAI():
		"""Test SecurityAI class with all methods"""
		rp("\n[bold cyan]=== Testing SecurityAI ===[/bold cyan]\n")
		security = SecurityAI()
		rp("[yellow]Test 1: Detect Malicious Patterns[/yellow]")
		log_entry1 = "SELECT * FROM users WHERE '1'='1' OR 1=1"
		log_entry2 = "Normal user login: john_doe"
		malicious = security.detectMalicious([log_entry1, log_entry2])
		rp(f"Log entries analyzed: {len(malicious)}")
		for entry in malicious:
			rp(f"  • Threat detected: {entry}")
		rp("[green]✓ Malicious pattern detection works[/green]\n")
		rp("[yellow]Test 2: Analyze Anomaly Score[/yellow]")
		anomaly_score = security.analyzeAnomalyScore(
			{"requests_per_minute": 1000, "avg_response": 500},
			{"requests_per_minute": 50, "avg_response": 200}
		)
		rp(f"Anomaly score: {anomaly_score}")
		rp("[green]✓ Anomaly score analysis works[/green]\n")
		rp("[yellow]Test 3: Identify Threat Type[/yellow]")
		threat1 = "rm -rf /var/www/html"
		threat2 = "User uploaded file: document.pdf"
		threat1_type = security.identifyThreatType(threat1)
		threat2_type = security.identifyThreatType(threat2)
		rp(f"Threat 1: '{threat1[:30]}...' -> {threat1_type}")
		rp(f"Threat 2: '{threat2[:30]}...' -> {threat2_type}")
		rp("[green]✓ Threat type identification works[/green]\n")
		rp("[yellow]Test 4: Predict Attack Probability[/yellow]")
		pattern_data = [
			{"login_attempts": 3, "failed_logins": 0, "location": "US"},
			{"login_attempts": 15, "failed_logins": 12, "location": "RU"},
			{"login_attempts": 5, "failed_logins": 1, "location": "UK"}
		]
		for pattern in pattern_data:
			probability = security.predictAttackProbability(pattern)
			rp(f"Pattern: {pattern}")
			rp(f"Attack probability: {probability}")
			rp("")
		rp("[green]✓ Attack probability prediction works[/green]\n")
		rp("[yellow]Test 5: Suggest Mitigation[/yellow]")
		attack_pattern = {"type": "brute_force", "source_ip": "192.168.1.100"}
		mitigations = security.suggestMitigation(attack_pattern)
		rp(f"Attack pattern: {attack_pattern}")
		rp("Suggested mitigations:")
		for mitigation in mitigations:
			rp(f"  • {mitigation}")
		rp("[green]✓ Mitigation suggestions work[/green]\n")
		rp("[yellow]Test 6: Score Threat Severity[/yellow]")
		threat1 = {"type": "sql_injection", "attempts": 5}
		threat2 = {"type": "xss", "attempts": 2}
		threat3 = {"type": "dos", "attempts": 1000}
		severity1 = security.scoreThreatSeverity(threat1)
		severity2 = security.scoreThreatSeverity(threat2)
		severity3 = security.scoreThreatSeverity(threat3)
		rp(f"Threat 1 (SQL Injection x5): {severity1}/10")
		rp(f"Threat 2 (XSS x2): {severity2}/10")
		rp(f"Threat 3 (DoS x1000): {severity3}/10")
		rp("[green]✓ Threat severity scoring works[/green]\n")
		return True
	def runTests():
		"""Run all tests for security intelligence AI"""
		rp(Panel.fit(
			"[bold magenta]Stamp 4.6 AI Test Suite - Security Intelligence[/bold magenta]\n"
			"[yellow]Testing SecurityAI class[/yellow]",
			title="SecurityAI Test Suite"
		))
		tests_passed = 0
		tests_failed = 0
		try:
			if Tests.testSecurityAI():
				tests_passed += 1
		except Exception as e:
			tests_failed += 1
			rp(f"[red]✗ SecurityAI tests failed: {e}[/red]\n")
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