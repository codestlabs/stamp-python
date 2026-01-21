"""
Stamp SecurityAI Module

Security intelligence and threat detection utilities.

Usage:
    >>> from stamp.oaiftrs.sec import SecurityAI
    >>> security = SecurityAI()
    >>> anomalies = security.detectAnomalies(log_lines)
"""

import re
from typing import List, Dict, Any
from collections import Counter

# Module-level constants
DEFAULT_THREAT_THRESHOLD = 0.7
DEFAULT_SUSPICIOUS_PATTERNS = [
	r"failed\s+password",
	r"brute\s+force",
	r"sql\s+injection",
	r"unauthorized\s+access",
	r"malware\s+detected",
	r"suspicious\s+activity"
]

class ThreatLevel(Enum):
	"""Security threat levels."""
	CRITICAL = "critical"
	HIGH = "high"
	MEDIUM = "medium"
	LOW = "low"
	INFO = "info"

class SecurityAI:
	"""Security intelligence and threat detection."""
	
	def __init__(self):
		"""Initialize SecurityAI."""
		self.suspicious_patterns = DEFAULT_SUSPICIOUS_PATTERNS
		self.threat_keywords = {
			"critical": {"critical", "emergency", "severe", "fatal"},
			"high": {"danger", "attack", "breach", "intrusion"},
			"medium": {"warning", "alert", "suspicious", "unusual"},
			"low": {"info", "notice", "minor", "trivial"}
		}
	
	def detectAnomalies(self, logs: List[str]) -> List[Dict[str, Any]]:
		"""Detect anomalies in log data.
		
		Args:
		    logs: List of log lines to analyze
		
		Returns:
		    List of anomaly descriptions with indices
		"""
		if not logs:
			return []
		
		anomalies = []
		
		for i, log in enumerate(logs):
			if not isinstance(log, str):
				continue
			
			for pattern in self.suspicious_patterns:
				if re.search(pattern, log, re.IGNORECASE):
					anomalies.append({
						"line_index": i,
						"line": log.strip(),
						"pattern": pattern,
						"severity": self._classifySeverity(log)
					})
					break
		
		return anomalies
	
	def classifyThreat(self, pattern: str) -> str:
		"""Classify threat level from pattern.
		
		Args:
		    pattern: Threat pattern string
		
		Returns:
		    Threat level string
		"""
		if not pattern:
			return "unknown"
		
		pattern_lower = pattern.lower()
		
		for level, keywords in self.threat_keywords.items():
			if any(kw in pattern_lower for kw in keywords):
				return level
		
		return "low"
	
	def predictRisk(self, data_points: List[float]) -> Dict[str, Any]:
		"""Predict security risk from data points.
		
		Args:
		    data_points: List of numerical risk indicators
		
		Returns:
		    Dict with risk prediction and level
		"""
		if not data_points:
			return {"risk": None, "level": "insufficient_data"}
		
		avg_risk = sum(data_points) / len(data_points)
		
		if avg_risk >= 0.8:
			level = "critical"
		elif avg_risk >= 0.6:
			level = "high"
		elif avg_risk >= 0.4:
			level = "medium"
		elif avg_risk >= 0.2:
			level = "low"
		else:
			level = "info"
		
		return {
			"risk": avg_risk,
			"level": level,
			"data_points": len(data_points)
		}
	
	def scanVulnerabilities(self, code: str) -> List[Dict[str, Any]]:
		"""Scan code for security vulnerabilities.
		
		Args:
		    code: Source code to scan
		
		Returns:
		    List of vulnerability descriptions
		"""
		if not code or not isinstance(code, str):
			return []
		
		vulnerabilities = []
		lines = code.split('\n')
		
		vulnerability_patterns = {
			"sql_injection": [
				r'execute\s*\(\s*[\'"][\w\s]*\+',
				r'format\s*\(\s*[\'"][\w\s]*%',
				r'select.*\s+from.*\s+where.*\s*=',
			],
			"hardcoded_secrets": [
				r'(password|api[_-]?key|secret)\s*=\s*["\'][^"\']+["\']',
				r'token\s*=\s*["\'][^"\']{20,}["\']',
			],
			"weak_encryption": [
				r'md5\s*\(',
				r'sha1\s*\(',
				r'base64\.encode\s*\(',
			],
			"insecure_random": [
				r'random\.random\s*\(',
				r'math\.random\s*\(',
			]
		}
		
		for i, line in enumerate(lines, 1):
			for vuln_type, patterns in vulnerability_patterns.items():
				for pattern in patterns:
					if re.search(pattern, line, re.IGNORECASE):
						vulnerabilities.append({
							"type": vuln_type,
							"line": i,
							"code": line.strip(),
							"severity": "high" if vuln_type == "hardcoded_secrets" else "medium"
						})
						break
		
		return vulnerabilities
	
	def analyzeLogPatterns(self, logs: List[str]) -> Dict[str, Any]:
		"""Analyze log patterns for security insights.
		
		Args:
		    logs: List of log lines
		
		Returns:
		    Dict with pattern analysis results
		"""
		if not logs:
			return {}
		
		# Count error types
		error_keywords = ["error", "fail", "exception", "critical"]
		warning_keywords = ["warning", "warn", "alert"]
		
		error_count = sum(1 for log in logs if any(kw in log.lower() for kw in error_keywords))
		warning_count = sum(1 for log in logs if any(kw in log.lower() for kw in warning_keywords))
		
		# Extract IP addresses
		ips = []
		for log in logs:
			found_ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)
			ips.extend(found_ips)
		
		ip_frequency = Counter(ips)
		suspicious_ips = [ip for ip, count in ip_frequency.items() if count > 10]
		
		# Time-based analysis
		timestamps = re.findall(r'\d{2}:\d{2}:\d{2}', ' '.join(logs))
		hour_distribution = Counter()
		
		for ts in timestamps:
			hour = ts.split(':')[0]
			hour_distribution[hour] += 1
		
		return {
			"total_logs": len(logs),
			"error_count": error_count,
			"warning_count": warning_count,
			"suspicious_ips": suspicious_ips,
			"unique_ips": len(ip_frequency),
			"peak_hours": [h for h, c in hour_distribution.most_common(3)] if hour_distribution else [],
			"risk_score": self._calculateLogRisk(error_count, warning_count, len(logs))
		}
	
	def detectBruteForce(self, logs: List[str], threshold: int = 5) -> List[Dict[str, Any]]:
		"""Detect brute force attack patterns.
		
		Args:
		    logs: List of log lines
		    threshold: Number of failed attempts before flagging
		
		Returns:
		    List of detected brute force attempts
		"""
		if not logs:
			return []
		
		failed_attempts = {}
		
		for log in logs:
			# Extract IP and failure indicator
			ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)
			if ip_match:
				ip = ip_match.group()
				
				if re.search(r'failed|denied|incorrect', log, re.IGNORECASE):
					if ip not in failed_attempts:
						failed_attempts[ip] = 0
					failed_attempts[ip] += 1
		
		# Flag IPs exceeding threshold
		brute_force_attempts = []
		
		for ip, count in failed_attempts.items():
			if count >= threshold:
				brute_force_attempts.append({
					"ip": ip,
					"failed_attempts": count,
					"severity": "critical" if count >= threshold * 3 else "high"
				})
		
		return sorted(brute_force_attempts, key=lambda x: x['failed_attempts'], reverse=True)
	
	def _classifySeverity(self, text: str) -> str:
		"""Classify severity of a security event."""
		text_lower = text.lower()
		
		if any(kw in text_lower for kw in self.threat_keywords["critical"]):
			return "critical"
		elif any(kw in text_lower for kw in self.threat_keywords["high"]):
			return "high"
		elif any(kw in text_lower for kw in self.threat_keywords["medium"]):
			return "medium"
		elif any(kw in text_lower for kw in self.threat_keywords["low"]):
			return "low"
		
		return "info"
	
	def _calculateLogRisk(self, error_count: int, warning_count: int, total_logs: int) -> float:
		"""Calculate risk score from log statistics."""
		if total_logs == 0:
			return 0.0
		
		error_ratio = error_count / total_logs
		warning_ratio = warning_count / total_logs
		
		return (error_ratio * 0.7 + warning_ratio * 0.3) * 10

# Main exports
__all__ = ["SecurityAI", "ThreatLevel"]

if __name__ == "__main__":
	from rich import print as rp
	from rich.panel import Panel
	
	rp(Panel.fit(
		"[bold cyan]Stamp SecurityAI[/]\n"
		"[bold]Security Intelligence & Threat Detection[/]",
		title="[bold]SecurityAI[/bold]"
	))
