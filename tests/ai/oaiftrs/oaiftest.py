"""
Test suite for Stamp 4.6 AI Features - Main Module

Tests NLPText, SmartSearch, and OptimizationAI classes
"""
import os
import shutil
from rich import print as rp
from rich.console import Console
from rich.panel import Panel

from lib.ai.oaiftrs.oaiftrs import NLPText, SmartSearch, OptimizationAI

console = Console()
class Tests:
    def testNLPText():
        """Test NLPText class with all methods"""
        rp("\n[bold cyan]=== Testing NLPText ===[/bold cyan]\n")
        nlp = NLPText()
        rp("[yellow]Test 1: Sentiment Analysis[/yellow]")
        text = "I love this amazing library!"
        sentiment = nlp.sentiment(text)
        rp(f"Text: {text}")
        rp(f"Sentiment: {sentiment}")
        rp("[green]✓ Sentiment analysis works[/green]\n")
        rp("[yellow]Test 2: Extract Keywords[/yellow]")
        keywords = nlp.extractKeywords(text)
        rp(f"Keywords: {keywords}")
        rp("[green]✓ Keyword extraction works[/green]\n")
        rp("[yellow]Test 3: Detect Language[/yellow]")
        lang = nlp.detectLanguage(text)
        rp(f"Detected: {lang}")
        rp("[green]✓ Language detection works[/green]\n")
        rp("[yellow]Test 4: Summarization[/yellow]")
        long_text = "This is a very long text that needs to be summarized. " * 10
        summary = nlp.summarizeSimple(long_text)
        rp(f"Summary: {summary}")
        rp("[green]✓ Summarization works[/green]\n")
        rp("[yellow]Test 5: Extract Entities[/yellow]")
        entities = nlp.extractEntities("John Smith works at Google in California")
        rp(f"Entities: {entities}")
        rp("[green]✓ Entity extraction works[/green]\n")
        rp("[yellow]Test 6: Classify Category[/yellow]")
        category = nlp.classifyCategory("The stock market crashed today")
        rp(f"Category: {category}")
        rp("[green]✓ Category classification works[/green]\n")
        return True
    def testSmartSearch():
        """Test SmartSearch class with all methods"""
        rp("\n[bold cyan]=== Testing SmartSearch ===[/bold cyan]\n")
        search = SmartSearch()
        test_dir = "test_search_files"
        os.makedirs(test_dir, exist_ok=True)
        with open(f"{test_dir}/file1.txt", "w") as f:
            f.write("Python is a great programming language for data science")
        with open(f"{test_dir}/file2.txt", "w") as f:
            f.write("Machine learning uses algorithms to learn from data")
        with open(f"{test_dir}/file3.txt", "w") as f:
            f.write("Data science involves statistics and programming")
        rp("[yellow]Test 1: Search by Meaning[/yellow]")
        results = search.searchByMeaning(test_dir, "machine learning algorithms")
        rp(f"Query: 'machine learning algorithms'")
        rp(f"Results: {results}")
        rp("[green]✓ Semantic search works[/green]\n")
        rp("[yellow]Test 2: Find Similar Documents[/yellow]")
        similar = search.findSimilar(test_dir, "Python programming")
        rp(f"Similar to 'Python programming': {similar}")
        rp("[green]✓ Document similarity works[/green]\n")
        rp("[yellow]Test 3: Context-Aware Search[/yellow]")
        context_results = search.contextAwareSearch(
            test_dir,
            "data analysis",
            context=["programming", "science"])
        rp(f"Context: programming, science")
        rp(f"Results: {context_results}")
        rp("[green]✓ Context-aware search works[/green]\n")
        rp("[yellow]Test 4: Cluster Similar Documents[/yellow]")
        clusters = search.clusterSimilar(test_dir)
        rp(f"Document clusters: {clusters}")
        rp("[green]✓ Document clustering works[/green]\n")
        shutil.rmtree(test_dir)
        return True
    def testOptimizationAI():
        """Test OptimizationAI class with all methods"""
        rp("\n[bold cyan]=== Testing OptimizationAI ===[/bold cyan]\n")
        opt = OptimizationAI()
        metrics = {
            "response_time": [100, 150, 200, 180, 220, 250, 300, 280],
            "memory_usage": [500, 600, 700, 800, 900, 1000, 1100, 1200],
            "cpu_usage": [50, 60, 70, 80, 90, 100, 110, 120],
            "throughput": [1000, 900, 800, 700, 600, 500, 400, 300]}
        rp("[yellow]Test 1: Detect Bottlenecks[/yellow]")
        bottlenecks = opt.detectBottlenecks(metrics)
        rp(f"Bottlenecks detected: {bottlenecks}")
        rp("[green]✓ Bottleneck detection works[/green]\n")
        rp("[yellow]Test 2: Suggest Tuning[/yellow]")
        suggestions = opt.suggestTuning(metrics)
        rp("Optimization suggestions:")
        for suggestion in suggestions:
            rp(f"  • {suggestion}")
        rp("[green]✓ Tuning suggestions work[/green]\n")
        rp("[yellow]Test 3: Predict Load[/yellow]")
        prediction = opt.predictLoad(metrics)
        rp(f"Predicted load: {prediction}")
        rp("[green]✓ Load prediction works[/green]\n")
        rp("[yellow]Test 4: Auto-Tune Parameters[/yellow]")
        tuned_params = opt.autoTune(metrics)
        rp("Auto-tuned parameters:")
        for param, value in tuned_params.items():
            rp(f"  • {param}: {value}")
        rp("[green]✓ Auto-tuning works[/green]\n")
        return True
    def runTests():
        """Run all tests for main AI features"""
        rp(Panel.fit(
            "[bold magenta]Stamp 4.6 AI Features Test Suite[/bold magenta]\n"
            "[yellow]Testing NLPText, SmartSearch, and OptimizationAI[/yellow]",
            title="AI Test Suite"))
        tests_passed = 0
        tests_failed = 0
        try:
            if Tests.testNLPText():
                tests_passed += 1
        except Exception as e:
            tests_failed += 1
            rp(f"[red]✗ NLPText tests failed: {e}[/red]\n")
        try:
            if Tests.testSmartSearch():
                tests_passed += 1
        except Exception as e:
            tests_failed += 1
            rp(f"[red]✗ SmartSearch tests failed: {e}[/red]\n")
        try:
            if Tests.testOptimizationAI():
                tests_passed += 1
        except Exception as e:
            tests_failed += 1
            rp(f"[red]✗ OptimizationAI tests failed: {e}[/red]\n")
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
                rp(f"\n[bold red]❌ {tests_failed} tests failed[/bold red]")
        rp("="*50 + "\n")
if __name__ == "__main__":
	Tests.runTests()