"""
Stamp CodeAI Module

Code intelligence utilities for quality analysis and refactoring.

Usage:
    >>> from stamp.oaiftrs.cdi import CodeAI
    >>> code_ai = CodeAI()
    >>> duplicates = code_ai.detectDuplicates(code_text)
"""

import re
import os
from typing import List, Dict, Any, Tuple
from enum import Enum
from collections import Counter

# Module-level constants
DEFAULT_SIMILARITY_THRESHOLD = 0.8
DEFAULT_MAX_FUNCTION_LINES = 50
DEFAULT_MAX_NESTING = 3
MAX_LINE_LENGTH = 126

class CodeSmell(Enum):
	"""Common code smell types."""
	DUPLICATE = "duplicate_code"
	LONG_FUNCTION = "long_function"
	COMPLEX_LOGIC = "complex_logic"
	MAGIC_NUMBER = "magic_number"
	HARDCODED_PATH = "hardcoded_path"
	DEEP_NESTING = "deep_nesting"

class CodeAI:
	"""Code intelligence and quality analysis."""
	
	def __init__(self):
		"""Initialize CodeAI analyzer."""
		self.magic_numbers = {0, 1, -1}
	
	def detectDuplicates(self, code: str, similarity_threshold: float = None) -> List[Tuple[int, int, float]]:
		"""Detect duplicate code blocks.
		
		Args:
		    code: Source code to analyze
		    similarity_threshold: Minimum similarity for duplicate detection
		
		Returns:
		    List of tuples (line1, line2, similarity) for duplicates
		"""
		if similarity_threshold is None:
			similarity_threshold = DEFAULT_SIMILARITY_THRESHOLD
		
		if not code or not isinstance(code, str):
			return []
		
		lines = code.split('\n')
		duplicates = []
		
		for i, line1 in enumerate(lines):
			for j, line2 in enumerate(lines):
				if j <= i:
					continue
				
				if not line1.strip() or not line2.strip():
					continue
				
				sim = self._calculateSimilarity(line1, line2)
				if sim >= similarity_threshold:
					duplicates.append((i + 1, j + 1, sim))
		
		return duplicates
	
	def findSmells(self, code: str) -> List[Dict[str, Any]]:
		"""Find code smells in source code.
		
		Args:
		    code: Source code to analyze
		
		Returns:
		    List of code smell descriptions
		"""
		if not code or not isinstance(code, str):
			return []
		
		smells = []
		lines = code.split('\n')
		
		for i, line in enumerate(lines, 1):
			# Magic numbers
			numbers = re.findall(r'\b\d+\b', line)
			for num in numbers:
				if int(num) not in self.magic_numbers:
					smells.append({
						"type": CodeSmell.MAGIC_NUMBER.value,
						"line": i,
						"code": line.strip(),
						"value": num
					})
			
			# Hardcoded paths
			if re.search(r'["\']([A-Z]:|/)[^"\']*["\']', line):
				smells.append({
					"type": CodeSmell.HARDCODED_PATH.value,
					"line": i,
					"code": line.strip()
				})
		
		# Deep nesting
		for i, line in enumerate(lines, 1):
			indent = len(line) - len(line.lstrip())
			if indent > DEFAULT_MAX_NESTING * 4:
				smells.append({
					"type": CodeSmell.DEEP_NESTING.value,
					"line": i,
					"code": line.strip(),
					"indent_level": indent // 4
				})
		
		return smells
	
	def analyzeComplexity(self, code: str) -> Dict[str, Any]:
		"""Analyze code complexity metrics.
		
		Args:
		    code: Source code to analyze
		
		Returns:
		    Dict with complexity metrics
		"""
		if not code or not isinstance(code, str):
			return {}
		
		lines = code.split('\n')
		functions = self._extractFunctions(code)
		
		metrics = {
			"total_lines": len(lines),
			"code_lines": len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
			"blank_lines": len([l for l in lines if not l.strip()]),
			"comment_lines": len([l for l in lines if l.strip().startswith('#')]),
			"function_count": len(functions),
			"avg_function_length": 0,
			"long_functions": []
		}
		
		if functions:
			total_len = sum(f['end'] - f['start'] for f in functions)
			metrics['avg_function_length'] = total_len / len(functions)
			
			for func in functions:
				func_len = func['end'] - func['start']
				if func_len > DEFAULT_MAX_FUNCTION_LINES:
					metrics['long_functions'].append({
						"name": func['name'],
						"length": func_len,
						"line": func['start'] + 1
					})
		
		return metrics
	
	def suggestRefactoring(self, code: str) -> List[str]:
		"""Suggest refactoring improvements.
		
		Args:
		    code: Source code to analyze
		
		Returns:
		    List of refactoring suggestions
		"""
		suggestions = []
		
		if not code or not isinstance(code, str):
			return suggestions
		
		smells = self.findSmells(code)
		complexity = self.analyzeComplexity(code)
		
		for smell in smells:
			if smell["type"] == "magic_number":
				suggestions.append(f"Line {smell['line']}: Replace magic number {smell['value']} with constant")
			elif smell["type"] == "hardcoded_path":
				suggestions.append(f"Line {smell['line']}: Use os.path.join() instead of hardcoded path")
			elif smell["type"] == "deep_nesting":
				suggestions.append(f"Line {smell['line']}: Reduce nesting level (currently {smell['indent_level']})")
		
		for func in complexity.get('long_functions', []):
			suggestions.append(f"Function '{func['name']}' at line {func['line']} is too long ({func['length']} lines)")
		
		if complexity.get('avg_function_length', 0) > DEFAULT_MAX_FUNCTION_LINES:
			suggestions.append(f"Average function length is high ({complexity['avg_function_length']:.1f} lines)")
		
		return suggestions
	
	def codeSimilarity(self, code1: str, code2: str) -> float:
		"""Calculate similarity between two code snippets.
		
		Args:
		    code1: First code snippet
		    code2: Second code snippet
		
		Returns:
		    Similarity score (0.0 to 1.0)
		"""
		if not code1 or not code2:
			return 0.0
		
		lines1 = set(code1.lower().split())
		lines2 = set(code2.lower().split())
		
		if not lines1 or not lines2:
			return 0.0
		
		intersection = len(lines1 & lines2)
		union = len(lines1 | lines2)
		
		return intersection / union if union > 0 else 0.0
	
	def checkLineLength(self, code: str) -> List[int]:
		"""Check for lines exceeding max length.
		
		Args:
		    code: Source code to check
		
		Returns:
		    List of line numbers that exceed max length
		"""
		if not code:
			return []
		
		lines = code.split('\n')
		long_lines = []
		
		for i, line in enumerate(lines, 1):
			if len(line) > MAX_LINE_LENGTH:
				long_lines.append(i)
		
		return long_lines
	
	def _calculateSimilarity(self, str1: str, str2: str) -> float:
		"""Calculate string similarity (Jaccard index)."""
		set1 = set(str1.lower().split())
		set2 = set(str2.lower().split())
		
		if not set1 or not set2:
			return 0.0
		
		intersection = len(set1 & set2)
		union = len(set1 | set2)
		
		return intersection / union if union > 0 else 0.0
	
	def _extractFunctions(self, code: str) -> List[Dict[str, Any]]:
		"""Extract function definitions from code."""
		functions = []
		lines = code.split('\n')
		
		for i, line in enumerate(lines):
			if re.match(r'\s*def\s+\w+\s*\(', line):
				name = re.search(r'def\s+(\w+)', line)
				if name:
					func_start = i
					indent = len(line) - len(line.lstrip())
					
					for j in range(i + 1, len(lines)):
						if lines[j].strip() and not lines[j].strip().startswith('#'):
							current_indent = len(lines[j]) - len(lines[j].lstrip())
							if current_indent <= indent and j > i:
								functions.append({
									"name": name.group(1),
									"start": func_start,
									"end": j
								})
								break
					else:
						functions.append({
							"name": name.group(1),
							"start": func_start,
							"end": len(lines)
						})
		
		return functions

# Main exports
__all__ = ["CodeAI", "CodeSmell"]

if __name__ == "__main__":
	from rich import print as rp
	from rich.panel import Panel
	
	rp(Panel.fit(
		"[bold cyan]Stamp CodeAI[/]\n"
		"[bold]Code Intelligence & Quality Analysis[/]",
		title="[bold]CodeAI[/bold]"
	))
