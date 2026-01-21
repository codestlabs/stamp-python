"""
Stamp Other AI Features Module

Collection of AI-powered utilities for NLP, semantic search,
and performance optimization.

Usage:
    >>> from stamp.oaiftrs import NLPText, SmartSearch
    >>> nlp = NLPText()
    >>> sentiment = nlp.sentiment(text)
"""

import os
import re
from collections import Counter
from typing import List, Dict, Any, Tuple
from enum import Enum

# Module-level constants
DEFAULT_N_TOP_KEYWORDS = 10
DEFAULT_SENTIMENT_THRESHOLD = 0.1
DEFAULT_SIMILARITY_THRESHOLD = 0.7
DEFAULT_SEARCH_LIMIT = 10

class Sentiment(Enum):
	"""Sentiment classifications."""
	POSITIVE = "positive"
	NEGATIVE = "negative"
	NEUTRAL = "neutral"

# ============================================================================
# NLP TEXT - Natural Language Processing
# ============================================================================

class NLPText:
	"""Text intelligence utilities for sentiment, keywords, language."""
	
	def __init__(self):
		"""Initialize NLPText analyzer."""
		self.positive_words = {"good", "great", "excellent", "positive", "success", "passed"}
		self.negative_words = {"bad", "error", "fail", "negative", "critical", "failed"}
	
	def sentiment(self, text: str) -> Dict[str, Any]:
		"""Analyze sentiment of text.
		
		Args:
		    text: Input text to analyze
		
		Returns:
		    Dict with sentiment classification and confidence
		"""
		if not text or not isinstance(text, str):
			return {"sentiment": "neutral", "confidence": 0.0}
		
		words = text.lower().split()
		pos_count = sum(1 for w in words if w in self.positive_words)
		neg_count = sum(1 for w in words if w in self.negative_words)
		
		total = pos_count + neg_count
		if total == 0:
			return {"sentiment": "neutral", "confidence": 0.0}
		
		pos_ratio = pos_count / total
		
		if pos_ratio > 0.6:
			return {"sentiment": "positive", "confidence": pos_ratio}
		elif pos_ratio < 0.4:
			return {"sentiment": "negative", "confidence": 1.0 - pos_ratio}
		else:
			return {"sentiment": "neutral", "confidence": 0.5}
	
	def extractKeywords(self, text: str, top_n: int = None) -> List[str]:
		"""Extract top keywords from text.
		
		Args:
		    text: Input text
		    top_n: Number of keywords to return
		
		Returns:
		    List of top keywords
		"""
		if top_n is None:
			top_n = DEFAULT_N_TOP_KEYWORDS
		
		if not text or not isinstance(text, str):
			return []
		
		words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
		stop_words = {"the", "and", "for", "are", "but", "not", "you", "all"}
		
		filtered = [w for w in words if w not in stop_words]
		counter = Counter(filtered)
		
		return [word for word, _ in counter.most_common(top_n)]
	
	def detectLanguage(self, text: str) -> str:
		"""Detect language of text (basic implementation).
		
		Args:
		    text: Input text
		
		Returns:
		    Language code (en, unknown)
		"""
		if not text or not isinstance(text, str):
			return "unknown"
		
		common_en_words = {"the", "be", "to", "of", "and", "a", "in", "that", "have", "i"}
		words = set(text.lower().split())
		
		if len(words & common_en_words) >= 2:
			return "en"
		
		return "unknown"
	
	def summarizeSimple(self, text: str, max_len: int = 200) -> str:
		"""Simple text summarization (first sentences).
		
		Args:
		    text: Input text
		    max_len: Maximum length of summary
		
		Returns:
		    Summary text
		"""
		if not text or not isinstance(text, str):
			return ""
		
		sentences = re.split(r'[.!?]+', text)
		summary = ""
		
		for sent in sentences:
			if len(summary) + len(sent) > max_len:
				break
			if sent.strip():
				summary += sent.strip() + ". "
		
		return summary.strip()
	
	def extractEntities(self, text: str) -> List[Dict[str, str]]:
		"""Extract named entities (basic pattern matching).
		
		Args:
		    text: Input text
		
		Returns:
		    List of entities with type and value
		"""
		if not text or not isinstance(text, str):
			return []
		
		entities = []
		
		# IPs
		for ip in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text):
			entities.append({"type": "ip", "value": ip})
		
		# Dates
		for date in re.findall(r'\d{4}-\d{2}-\d{2}', text):
			entities.append({"type": "date", "value": date})
		
		# Timestamps
		for ts in re.findall(r'\d{2}:\d{2}:\d{2}', text):
			entities.append({"type": "time", "value": ts})
		
		return entities
	
	def classifyCategory(self, text: str, categories: List[str]) -> str:
		"""Classify text into one of given categories.
		
		Args:
		    text: Input text
		    categories: List of category names to match against
		
		Returns:
		    Best matching category or "unknown"
		"""
		if not text or not isinstance(text, str) or not categories:
			return "unknown"
		
		text_lower = text.lower()
		
		for category in categories:
			if category.lower() in text_lower:
				return category.lower()
		
		return "unknown"

# ============================================================================
# SMART SEARCH - Semantic File Search
# ============================================================================

class SmartSearch:
	"""Semantic search utilities for finding files by meaning."""
	
	def __init__(self):
		"""Initialize SmartSearch engine."""
		self._index = {}
	
	def searchByMeaning(self, query: str, files: List[str]) -> List[str]:
		"""Search files by semantic meaning (keyword-based).
		
		Args:
		    query: Search query
		    files: List of file paths to search
		
		Returns:
		    List of matching file paths
		"""
		if not query or not files:
			return []
		
		query_words = set(query.lower().split())
		results = []
		
		for file_path in files:
			try:
				if not os.path.exists(file_path):
					continue
				
				with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
					content = f.read()
				
				content_words = set(content.lower().split())
				match_count = len(query_words & content_words)
				
				if match_count > 0:
					results.append((file_path, match_count))
			except Exception:
				continue
		
		results.sort(key=lambda x: x[1], reverse=True)
		return [r[0] for r in results]
	
	def findSimilar(self, content: str, files: List[str]) -> List[Tuple[str, float]]:
		"""Find files with similar content.
		
		Args:
		    content: Reference content
		    files: List of file paths to compare
		
		Returns:
		    List of tuples (file_path, similarity_score)
		"""
		if not content or not files:
			return []
		
		ref_words = set(content.lower().split())
		results = []
		
		for file_path in files:
			try:
				if not os.path.exists(file_path):
					continue
				
				with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
					file_content = f.read()
				
				file_words = set(file_content.lower().split())
				
				if not ref_words or not file_words:
					continue
				
				intersection = len(ref_words & file_words)
				union = len(ref_words | file_words)
				
				similarity = intersection / union if union > 0 else 0.0
				
				if similarity > 0:
					results.append((file_path, similarity))
			except Exception:
				continue
		
		results.sort(key=lambda x: x[1], reverse=True)
		return results[:DEFAULT_SEARCH_LIMIT]
	
	def contextAwareSearch(self, query: str, context: str, files: List[str]) -> List[str]:
		"""Search files using query with additional context.
		
		Args:
		    query: Main search query
		    context: Additional context for refinement
		    files: List of file paths to search
		
		Returns:
		    List of matching file paths
		"""
		combined_query = f"{query} {context}"
		return self.searchByMeaning(combined_query, files)
	
	def clusterSimilar(self, docs: List[str]) -> List[List[str]]:
		"""Cluster documents by similarity.
		
		Args:
		    docs: List of document contents
		
		Returns:
			List of clusters (each cluster is a list of indices)
		"""
		if not docs:
			return []
		
		clusters = []
		assigned = set()
		
		for i, doc1 in enumerate(docs):
			if i in assigned:
				continue
			
			cluster = [i]
			words1 = set(doc1.lower().split())
			
			for j, doc2 in enumerate(docs):
				if j <= i or j in assigned:
					continue
				
				words2 = set(doc2.lower().split())
				
				if not words1 or not words2:
					continue
				
				intersection = len(words1 & words2)
				union = len(words1 | words2)
				similarity = intersection / union if union > 0 else 0.0
				
				if similarity >= DEFAULT_SIMILARITY_THRESHOLD:
					cluster.append(j)
					assigned.add(j)
			
			clusters.append(cluster)
		
		return clusters

# ============================================================================
# OPTIMIZATION AI - Performance Optimization
# ============================================================================

class OptimizationAI:
	"""Performance optimization and tuning utilities."""
	
	def __init__(self):
		"""Initialize OptimizationAI engine."""
		pass
	
	def detectBottlenecks(self, data: List[Dict]) -> List[Dict]:
		"""Detect performance bottlenecks from timing data.
		
		Args:
		    data: List of dicts with 'operation' and 'duration' keys
		
		Returns:
		    List of bottleneck descriptions
		"""
		if not data:
			return []
		
		bottlenecks = []
		durations = [d.get('duration', 0) for d in data if isinstance(d, dict)]
		
		if not durations:
			return []
		
		avg_duration = sum(durations) / len(durations)
		threshold = avg_duration * 2.0
		
		for item in data:
			if not isinstance(item, dict):
				continue
			
			duration = item.get('duration', 0)
			operation = item.get('operation', 'unknown')
			
			if duration > threshold:
				bottlenecks.append({
					"operation": operation,
					"duration": duration,
					"threshold": threshold,
					"severity": duration / avg_duration
				})
		
		return sorted(bottlenecks, key=lambda x: x['duration'], reverse=True)
	
	def suggestTuning(self, performance_data: Dict) -> List[str]:
		"""Suggest system tuning based on performance data.
		
		Args:
		    performance_data: Dict with performance metrics
		
		Returns:
		    List of tuning suggestions
		"""
		suggestions = []
		
		memory_usage = performance_data.get('memory_usage', 0)
		cpu_usage = performance_data.get('cpu_usage', 0)
		disk_io = performance_data.get('disk_io', {})
		
		if cpu_usage > 80:
			suggestions.append("Reduce CPU load: optimize algorithms or add parallel processing")
		
		if memory_usage > 90:
			suggestions.append("High memory usage: implement caching or data streaming")
		
		if disk_io.get('read_rate', 0) > 1000:
			suggestions.append("High disk reads: consider in-memory caching")
		
		if disk_io.get('write_rate', 0) > 1000:
			suggestions.append("High disk writes: implement batching")
		
		return suggestions
	
	def predictLoad(self, historical_data: List[float]) -> Dict:
		"""Predict future load from historical data.
		
		Args:
		    historical_data: List of historical load values
		
		Returns:
		    Dict with predicted load and trend
		"""
		if len(historical_data) < 2:
			return {"prediction": None, "trend": "insufficient_data"}
		
		recent = historical_data[-5:] if len(historical_data) >= 5 else historical_data
		avg_recent = sum(recent) / len(recent)
		
		trend = historical_data[-1] - historical_data[0]
		
		if trend > 0:
			direction = "increasing"
		elif trend < 0:
			direction = "decreasing"
		else:
			direction = "stable"
		
		return {
			"prediction": avg_recent,
			"trend": direction,
			"rate": trend / len(historical_data)
		}
	
	def autoTune(self, parameters: Dict, target_metric: str) -> Dict:
		"""Automatically tune parameters for target metric.
		
		Args:
		    parameters: Dict of parameter names and values
		    target_metric: Name of metric to optimize
		
		Returns:
		    Dict with tuned parameters
		"""
		tuned = parameters.copy()
		
		for param, value in tuned.items():
			if isinstance(value, (int, float)):
				if target_metric == "memory":
					tuned[param] = int(value * 0.8)  # Reduce memory usage
				elif target_metric == "speed":
					tuned[param] = int(value * 1.2)  # Increase for speed
				elif target_metric == "balanced":
					tuned[param] = int(value)
		
		return tuned

# ============================================================================
# MAIN EXPORTS
# ============================================================================

__all__ = [
	"NLPText",
	"SmartSearch",
	"OptimizationAI",
	"Sentiment",
]

if __name__ == "__main__":
	from rich import print as rp
	from rich.panel import Panel
	
	rp(Panel.fit(
		"[bold cyan]Stamp Other AI Features[/]\n"
		"[bold]3 AI-Powered Utilities:[/]\n"
		"- NLPText: Text intelligence\n"
		"- SmartSearch: Semantic file search\n"
		"- OptimizationAI: Performance tuning",
		title="[bold]Other AI Features[/bold]"
	))
