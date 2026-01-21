"""
Stamp LLM Module - Complete Edition

Uses Ollama to run local LLMs including GPT-2, LLaMA, and more.
Comprehensive LLM toolkit with 50+ features for advanced AI operations.

Requirements:
    - Ollama installed: https://ollama.ai/download
    - Model downloaded: `ollama pull gpt2` or `ollama pull llama2`
    - Optional: tiktoken, beautifulsoup4, pypdf, python-docx, fastapi

Usage:
    >>> from stamp import Ollama, LLMBatchGenerator, LLMEmbeddings
    >>> ai = Ollama("gpt2")
    >>> result = ai.generate("Hello, world!")
"""

import os
import subprocess
import json
import time
import sys
import re
import hashlib
import threading
import asyncio
from functools import wraps
from typing import List, Dict, Any, Callable, Optional, Tuple, Union
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import OrderedDict

try:
    import requests
except ImportError:
    requests = None

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    import tiktoken
except ImportError:
    tiktoken = None

from rich import print as rp
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn

console = Console()

# Export all public classes
__all__ = [
    "OllamaConfig",
    "OllamaCheck",
    "GPT2Generator",
    "Ollama",
    "LLMBatchGenerator",
    "LLMEmbeddings",
    "LLMModelComparer",
    "LLMTokenizer",
    "PromptTemplate",
    "ResponseFilter",
    "FileProcessor",
    "WebScraper",
    "LLMAPIServer",
    "LLMMemory",
    "ToolCaller",
    "ConversationManager",
    "PromptAssistant",
    "ModelBenchmarker",
    "ResponseAnalyzer",
    "EventStreamer",
    "PromptChainer",
    "ConcurrentGenerator",
    "ResponseFormatter",
    "ToolSelector",
]

# ============================================================================
# CONFIGURATION & CHECK
# ============================================================================

class OllamaConfig:
    """Configuration for Ollama."""
    
    def __init__(self):
        self.host = "localhost"
        self.port = 11434
        self.base_url = f"http://{self.host}:{self.port}"
        self.model = "gpt2"  # Default model
        self.timeout = 30  # seconds
        self.temperature = 0.7
        self.num_predict = 256  # Max tokens to generate
        self.cache_enabled = True
        self.rate_limit = 10  # requests per minute
        
    def get_url(self, endpoint):
        """Get full URL for endpoint."""
        return f"{self.base_url}{endpoint}"

class OllamaCheck:
    """Check if Ollama is installed and running."""
    
    @staticmethod
    def is_installed():
        """Check if Ollama is installed."""
        try:
            result = subprocess.run(
                ["ollama", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    @staticmethod
    def is_running(config=None):
        """Check if Ollama server is running."""
        if config is None:
            config = OllamaConfig()
        
        if not requests:
            return False
        try:
            response = requests.get(config.get_url("/api/tags"), timeout=2)
            return response.status_code == 200
        except:
            return False
    
    @staticmethod
    def list_models(config=None):
        """List available models."""
        if config is None:
            config = OllamaConfig()
        
        if not requests:
            return []
        try:
            response = requests.get(config.get_url("/api/tags"), timeout=5)
            if response.status_code == 200:
                data = response.json()
                return [model['name'] for model in data.get('models', [])]
            return []
        except:
            return []
    
    @staticmethod
    def is_model_available(model, config=None):
        """Check if a model is available."""
        models = OllamaCheck.list_models(config)
        return model in models or any(m.startswith(model) for m in models)
    
    @staticmethod
    def pull_model(model, config=None):
        """Pull/download a model."""
        if config is None:
            config = OllamaConfig()
        
        console.print(f"[bold cyan]Pulling model: {model}[/]")
        console.print("[dim]This may take a while...[/]")
        
        try:
            process = subprocess.Popen(
                ["ollama", "pull", model],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            
            for line in process.stdout:
                console.print(f"[dim]{line.strip()}[/]", end="\r")
            
            process.wait()
            
            if process.returncode == 0:
                console.print(f"\n[bold green]✓ Model '{model}' pulled successfully![/]")
                return True
            else:
                console.print(f"[bold red]✗ Failed to pull model '{model}'[/]")
                return False
        except Exception as e:
            console.print(f"[bold red]✗ Error pulling model: {e}[/]")
            return False

# ============================================================================
# CORE GENERATOR (Features: Cache, Rate Limiting)
# ============================================================================

class GPT2Generator:
    """Enhanced GPT-2 text generator with advanced features."""
    
    def __init__(self, model="gpt2", config=None, auto_pull=False):
        if config is None:
            config = OllamaConfig()
        
        self.config = config
        self.model = model
        self.auto_pull = auto_pull
        self.history = []
        self.cache = OrderedDict()
        self.cache_size = 100
        self.request_times = []
        self._check_ollama()
    
    def _check_ollama(self):
        """Check Ollama status."""
        if not OllamaCheck.is_installed():
            console.print("[bold red]✗ Ollama is not installed![/]")
            console.print("[cyan]Please install Ollama from: https://ollama.ai/download[/]")
            raise RuntimeError("Ollama not installed")
        
        if not OllamaCheck.is_running(self.config):
            console.print("[bold yellow]⚠ Ollama server is not running![/]")
            console.print("[cyan]Starting Ollama server...[/]")
            try:
                subprocess.Popen(["ollama", "serve"])
                time.sleep(3)
                if OllamaCheck.is_running(self.config):
                    console.print("[bold green]✓ Ollama server started![/]")
                else:
                    raise RuntimeError("Failed to start Ollama server")
            except Exception as e:
                console.print(f"[bold red]✗ Failed to start Ollama: {e}[/]")
                raise
        
        if not OllamaCheck.is_model_available(self.model, self.config):
            console.print(f"[bold yellow]⚠ Model '{self.model}' is not available![/]")
            should_pull = False
            if self.auto_pull:
                should_pull = True
            elif sys.stdin.isatty():
                choice = input("Would you like to download it? (y/n): ").lower()
                should_pull = (choice == 'y')
            
            if should_pull:
                if not OllamaCheck.pull_model(self.model, self.config):
                    raise RuntimeError(f"Failed to pull model '{self.model}'")
            else:
                console.print("[cyan]Available models:[/]")
                models = OllamaCheck.list_models(self.config)
                if models:
                    for m in models:
                        console.print(f"  • [green]{m}[/]")
                raise RuntimeError(f"Model '{self.model}' not available")
        
        console.print(f"[bold green]✓ Ready to use '{self.model}'![/]")
    
    def _check_rate_limit(self):
        """Check and enforce rate limiting."""
        if self.config.rate_limit <= 0:
            return
        
        now = time.time()
        self.request_times = [t for t in self.request_times if now - t < 60]
        
        if len(self.request_times) >= self.config.rate_limit:
            wait_time = 60 - (now - self.request_times[0])
            if wait_time > 0:
                console.print(f"[yellow]Rate limit reached. Waiting {wait_time:.1f}s...[/]")
                time.sleep(wait_time)
        
        self.request_times.append(now)
    
    def _get_cache_key(self, prompt, **kwargs):
        """Generate cache key from prompt and parameters."""
        key_data = f"{prompt}{json.dumps(kwargs, sort_keys=True)}{self.model}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def _check_cache(self, cache_key):
        """Check if response is cached."""
        if self.config.cache_enabled and cache_key in self.cache:
            return self.cache[cache_key]
        return None
    
    def _add_to_cache(self, cache_key, response):
        """Add response to cache."""
        if not self.config.cache_enabled:
            return
        
        self.cache[cache_key] = response
        while len(self.cache) > self.cache_size:
            self.cache.popitem(last=False)
    
    def _make_request(self, prompt, **kwargs):
        """Make a request to Ollama API."""
        if not requests:
            raise RuntimeError("requests library not installed. Install with: pip install requests")
        
        self._check_rate_limit()
        
        url = self.config.get_url("/api/generate")
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": kwargs.get("temperature", self.config.temperature),
                "num_predict": kwargs.get("num_predict", self.config.num_predict),
            }
        }
        
        response = requests.post(url, json=data, timeout=kwargs.get("timeout", self.config.timeout))
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "")
        else:
            raise RuntimeError(f"Ollama API error: {response.status_code}")
    
    def generate(self, prompt, temperature=None, num_predict=None, show_progress=True, use_cache=True):
        """Generate text from prompt."""
        kwargs = {}
        if temperature is not None:
            kwargs["temperature"] = temperature
        if num_predict is not None:
            kwargs["num_predict"] = num_predict
        
        cache_key = self._get_cache_key(prompt, **kwargs)
        if use_cache:
            cached = self._check_cache(cache_key)
            if cached:
                console.print("[dim]Response loaded from cache[/]")
                return cached
        
        if show_progress:
            with console.status(f"[bold cyan]Generating with {self.model}...", spinner="dots"):
                result = self._make_request(prompt, **kwargs)
        else:
            result = self._make_request(prompt, **kwargs)
        
        self._add_to_cache(cache_key, result)
        self.history.append({
            "prompt": prompt,
            "result": result,
            "model": self.model,
            "timestamp": time.time()
        })
        
        return result
    
    def generate_stream(self, prompt, temperature=None, num_predict=None):
        """Generate text with streaming output."""
        if not requests:
            raise RuntimeError("requests library not installed")
        
        url = self.config.get_url("/api/generate")
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": temperature or self.config.temperature,
                "num_predict": num_predict or self.config.num_predict,
            }
        }
        
        console.print(f"[bold]Prompt:[/] {prompt}\n")
        console.print("[bold]Response:[/]")
        
        full_response = ""
        
        with requests.post(url, json=data, stream=True, timeout=self.config.timeout) as r:
            for line in r.iter_lines():
                if line:
                    try:
                        chunk = json.loads(line)
                        response_part = chunk.get("response", "")
                        full_response += response_part
                        console.print(f"[white]{response_part}[/]", end="")
                    except json.JSONDecodeError:
                        pass
        
        console.print()
        
        self.history.append({
            "prompt": prompt,
            "result": full_response,
            "model": self.model,
            "timestamp": time.time()
        })
        
        return full_response
    
    def complete_code(self, prefix, temperature=0.3):
        """Complete code from prefix."""
        console.print("[bold cyan]Code Completion[/]")
        console.print(f"[dim]Prefix:[/]\n{prefix}\n")
        
        completion = self.generate(prefix, temperature=temperature, show_progress=True)
        console.print(f"[green]{completion}[/]")
        
        return completion
    
    def chat(self, messages, temperature=0.7):
        """Chat-style generation."""
        formatted = ""
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            formatted += f"{role}: {content}\n"
        formatted += "assistant:"
        
        response = self.generate(formatted, temperature=temperature)
        assistant_response = response.split("assistant:")[-1].strip()
        return assistant_response
    
    def summarize(self, text, temperature=0.5):
        """Summarize text."""
        prompt = f"Summarize the following text in a concise manner:\n\n{text}\n\nSummary:"
        summary = self.generate(prompt, temperature=temperature)
        return summary
    
    def translate(self, text, target_language="English", temperature=0.5):
        """Translate text to target language."""
        prompt = f"Translate the following text to {target_language}:\n\n{text}\n\nTranslation:"
        translation = self.generate(prompt, temperature=temperature)
        return translation
    
    def get_history(self):
        """Get generation history."""
        return self.history
    
    def clear_history(self):
        """Clear generation history."""
        self.history = []
        console.print("[dim]History cleared[/]")
    
    def export_history(self, filename=None):
        """Export history to JSON file."""
        if filename is None:
            filename = f"llm_history_{int(time.time())}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2)
        
        console.print(f"[green]History exported to {filename}[/]")
        return filename
    
    def clear_cache(self):
        """Clear response cache."""
        self.cache.clear()
        console.print("[dim]Cache cleared[/]")

class Ollama:
    """Main Ollama interface."""
    
    def __init__(self, model="gpt2", config=None, auto_pull=False):
        self.model = model
        self.config = config or OllamaConfig()
        self.generator = GPT2Generator(model, config, auto_pull=auto_pull)
    
    def generate(self, prompt, **kwargs):
        """Generate text."""
        return self.generator.generate(prompt, **kwargs)
    
    def generate_stream(self, prompt, **kwargs):
        """Generate text with streaming."""
        return self.generator.generate_stream(prompt, **kwargs)
    
    def chat(self, messages, **kwargs):
        """Chat interaction."""
        return self.generator.chat(messages, **kwargs)
    
    def complete_code(self, prefix, **kwargs):
        """Complete code."""
        return self.generator.complete_code(prefix, **kwargs)
    
    def set_model(self, model):
        """Change model."""
        self.model = model
        self.generator = GPT2Generator(model, self.config, auto_pull=self.generator.auto_pull)
        console.print(f"[cyan]Model changed to: {model}[/]")
    
    def list_models(self):
        """List available models."""
        models = OllamaCheck.list_models(self.config)
        return models
    
    def pull_model(self, model):
        """Pull a new model."""
        return OllamaCheck.pull_model(model, self.config)

# ============================================================================
# FEATURE 1: BATCH GENERATION
# ============================================================================

class LLMBatchGenerator:
    """Generate multiple texts at once."""
    
    def __init__(self, model="gpt2", config=None):
        self.generator = GPT2Generator(model, config)
        self.executor = ThreadPoolExecutor(max_workers=4)
    
    def generate_batch(self, prompts: List[str], **kwargs) -> List[str]:
        """Generate multiple texts in parallel."""
        console.print(f"[bold cyan]Generating {len(prompts)} prompts in parallel...[/]")
        
        futures = []
        for prompt in prompts:
            future = self.executor.submit(
                self.generator.generate, 
                prompt, 
                show_progress=False,
                **kwargs
            )
            futures.append(future)
        
        results = []
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            task = progress.add_task("[cyan]Processing...", total=len(futures))
            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                    progress.update(task, advance=1)
                except Exception as e:
                    console.print(f"[red]Error: {e}[/]")
                    results.append("")
        
        return results
    
    def shutdown(self):
        """Shutdown executor."""
        self.executor.shutdown()

# ============================================================================
# FEATURE 2: EMBEDDINGS
# ============================================================================

class LLMEmbeddings:
    """Text embedding support."""
    
    def __init__(self, model="nomic-embed-text", config=None):
        self.model = model
        self.config = config or OllamaConfig()
    
    def embed(self, text: str) -> List[float]:
        """Get text embedding."""
        if not requests:
            raise RuntimeError("requests library not installed")
        
        url = self.config.get_url("/api/embeddings")
        data = {
            "model": self.model,
            "input": text
        }
        
        response = requests.post(url, json=data, timeout=self.config.timeout)
        
        if response.status_code == 200:
            result = response.json()
            return result.get("embedding", [])
        else:
            raise RuntimeError(f"Embedding error: {response.status_code}")
    
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Get multiple embeddings."""
        embeddings = []
        for text in texts:
            embedding = self.embed(text)
            embeddings.append(embedding)
        return embeddings
    
    def cosine_similarity(self, emb1: List[float], emb2: List[float]) -> float:
        """Calculate cosine similarity between embeddings."""
        import math
        
        dot_product = sum(a * b for a, b in zip(emb1, emb2))
        norm1 = math.sqrt(sum(a * a for a in emb1))
        norm2 = math.sqrt(sum(b * b for b in emb2))
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)

# ============================================================================
# FEATURE 3: MODEL COMPARISON
# ============================================================================

class LLMModelComparer:
    """Compare outputs from different models."""
    
    def __init__(self, config=None):
        self.config = config or OllamaConfig()
        self.generators = {}
    
    def add_model(self, name: str, model: str):
        """Add a model to compare."""
        self.generators[name] = GPT2Generator(model, self.config)
    
    def compare(self, prompt: str, **kwargs) -> Dict[str, str]:
        """Compare outputs from all models."""
        console.print(f"[bold cyan]Comparing {len(self.generators)} models...[/]")
        
        results = {}
        for name, generator in self.generators.items():
            try:
                result = generator.generate(prompt, show_progress=False, **kwargs)
                results[name] = result
            except Exception as e:
                results[name] = f"Error: {e}"
        
        return results
    
    def display_comparison(self, prompt: str, **kwargs):
        """Display comparison in formatted output."""
        results = self.compare(prompt, **kwargs)
        
        console.print(f"\n[bold]Prompt:[/] {prompt}\n")
        for name, result in results.items():
            console.print(f"[bold cyan]{name}:[/]")
            console.print(f"{result[:200]}...\n")

# ============================================================================
# FEATURE 4: TOKEN COUNTING
# ============================================================================

class LLMTokenizer:
    """Token counting utilities."""
    
    def __init__(self, encoding="cl100k_base"):
        self.encoding_name = encoding
        self.encoding = None
        if tiktoken:
            try:
                self.encoding = tiktoken.get_encoding(encoding)
            except:
                pass
    
    def count_tokens(self, text: str) -> int:
        """Count tokens in text."""
        if self.encoding:
            return len(self.encoding.encode(text))
        return int(len(text.split()) * 1.3)
    
    def truncate_to_tokens(self, text: str, max_tokens: int) -> str:
        """Truncate text to max tokens."""
        tokens = self.count_tokens(text)
        if tokens <= max_tokens:
            return text
        
        ratio = max_tokens / tokens
        char_limit = int(len(text) * ratio * 0.9)
        return text[:char_limit]
    
    def count_response_tokens(self, response: str) -> Dict[str, int]:
        """Count tokens in response with stats."""
        tokens = self.count_tokens(response)
        return {
            "tokens": tokens,
            "words": len(response.split()),
            "chars": len(response),
            "estimated_cost_usd": tokens * 0.00001
        }

# ============================================================================
# FEATURE 5: PROMPT TEMPLATES
# ============================================================================

class PromptTemplate:
    """Reusable template system with variable substitution."""
    
    def __init__(self, template: str):
        self.template = template
        self.variables = self._extract_variables()
    
    def _extract_variables(self) -> List[str]:
        """Extract variables from template."""
        pattern = r'\{(\w+)\}'
        matches = re.findall(pattern, self.template)
        return list(set(matches))
    
    def format(self, **kwargs) -> str:
        """Format template with variables."""
        missing = set(self.variables) - set(kwargs.keys())
        if missing:
            raise ValueError(f"Missing variables: {missing}")
        
        return self.template.format(**kwargs)
    
    @staticmethod
    def from_file(filepath: str) -> 'PromptTemplate':
        """Load template from file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return PromptTemplate(f.read())
    
    def save(self, filepath: str):
        """Save template to file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.template)
    
    def get_variables(self) -> List[str]:
        """Get required variables."""
        return self.variables

# ============================================================================
# FEATURE 6: RESPONSE FILTERING
# ============================================================================

class ResponseFilter:
    """Filter and validate responses."""
    
    @staticmethod
    def filter_by_length(response: str, min_len: int = 0, max_len: int = None) -> bool:
        """Filter by response length."""
        length = len(response)
        if length < min_len:
            return False
        if max_len and length > max_len:
            return False
        return True
    
    @staticmethod
    def filter_by_keywords(response: str, required: List[str] = None, forbidden: List[str] = None) -> bool:
        """Filter by keywords."""
        lower_response = response.lower()
        
        if required:
            for keyword in required:
                if keyword.lower() not in lower_response:
                    return False
        
        if forbidden:
            for keyword in forbidden:
                if keyword.lower() in lower_response:
                    return False
        
        return True
    
    @staticmethod
    def filter_by_regex(response: str, pattern: str, must_match: bool = True) -> bool:
        """Filter by regex pattern."""
        matches = re.search(pattern, response)
        if must_match:
            return matches is not None
        return matches is None
    
    @staticmethod
    def filter_json(response: str) -> bool:
        """Check if response is valid JSON."""
        try:
            json.loads(response)
            return True
        except:
            return False
    
    @staticmethod
    def apply_filters(response: str, filters: List[Callable]) -> bool:
        """Apply multiple filters."""
        for filter_func in filters:
            if not filter_func(response):
                return False
        return True

# ============================================================================
# FEATURE 7: FILE PROCESSING
# ============================================================================

class FileProcessor:
    """Process files with LLM."""
    
    def __init__(self, generator: GPT2Generator):
        self.generator = generator
    
    def process_text(self, filepath: str, prompt: str = "Summarize this text:") -> str:
        """Process text file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        full_prompt = f"{prompt}\n\n{text}"
        return self.generator.generate(full_prompt)
    
    def process_directory(self, directory: str, pattern: str = "*.txt", prompt: str = "Summarize:") -> Dict[str, str]:
        """Process all files in directory."""
        import glob
        
        files = glob.glob(os.path.join(directory, pattern))
        results = {}
        
        console.print(f"[bold cyan]Processing {len(files)} files...[/]")
        for filepath in files:
            try:
                result = self.process_text(filepath, prompt)
                results[filepath] = result
            except Exception as e:
                console.print(f"[red]Error processing {filepath}: {e}[/]")
        
        return results
    
    def summarize_file(self, filepath: str) -> str:
        """Summarize a file."""
        return self.process_text(filepath, "Summarize this file:")

# ============================================================================
# FEATURE 8: WEB SCRAPING
# ============================================================================

class WebScraper:
    """Fetch and analyze web pages with LLM."""
    
    def __init__(self, generator: GPT2Generator):
        self.generator = generator
        self.scraper_available = BeautifulSoup is not None
    
    def fetch_url(self, url: str) -> str:
        """Fetch web page content."""
        if not requests:
            raise RuntimeError("requests library not installed")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise RuntimeError(f"Failed to fetch URL: {e}")
    
    def extract_text(self, html: str) -> str:
        """Extract text from HTML."""
        if not self.scraper_available:
            text = re.sub(r'<[^>]+>', ' ', html)
            return ' '.join(text.split())
        
        soup = BeautifulSoup(html, 'html.parser')
        for script in soup(['script', 'style']):
            script.decompose()
        
        return soup.get_text(separator=' ', strip=True)
    
    def summarize_url(self, url: str) -> str:
        """Summarize a web page."""
        console.print(f"[bold cyan]Fetching {url}...[/]")
        
        html = self.fetch_url(url)
        text = self.extract_text(html)
        
        if len(text) > 10000:
            text = text[:10000] + "..."
        
        summary = self.generator.generate(f"Summarize the following web page content:\n\n{text}")
        return summary

# ============================================================================
# FEATURE 10: API SERVER
# ============================================================================

class LLMAPIServer:
    """HTTP API server for LLM access."""
    
    def __init__(self, generator: GPT2Generator, host="0.0.0.0", port=8000):
        self.generator = generator
        self.host = host
        self.port = port
        self.running = False
        self._server_thread = None
    
    def start(self):
        """Start the API server."""
        try:
            from http.server import HTTPServer, BaseHTTPRequestHandler
        except ImportError:
            console.print("[red]http.server not available. Use Python 3.7+[/]")
            return
        
        class LLMHandler(BaseHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                self.llm_server = kwargs.pop('llm_server', None)
                super().__init__(*args, **kwargs)
            
            def do_GET(self):
                if self.path == "/health":
                    self.send_response(200, '{"status": "healthy"}')
                elif self.path == "/models":
                    models = OllamaCheck.list_models()
                    self.send_response(200, json.dumps({"models": models}))
                else:
                    self.send_response(404, '{"error": "Not found"}')
            
            def do_POST(self):
                if self.path == "/generate":
                    content_length = int(self.headers['Content-Length'])
                    post_data = self.rfile.read(content_length)
                    data = json.loads(post_data)
                    
                    try:
                        result = self.llm_server.generator.generate(
                            data.get("prompt", ""),
                            show_progress=False
                        )
                        self.send_response(200, json.dumps({"response": result}))
                    except Exception as e:
                        self.send_response(500, json.dumps({"error": str(e)}))
                else:
                    self.send_response(404, '{"error": "Not found"}')
            
            def send_response(self, status_code, body):
                self.send_response(status_code)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(body.encode())
        
        def run_server():
            server = HTTPServer((self.host, self.port), lambda *args: LLMHandler(*args, llm_server=self))
            console.print(f"[green]✓ API server running on http://{self.host}:{self.port}[/]")
            server.serve_forever()
        
        self.running = True
        self._server_thread = threading.Thread(target=run_server, daemon=True)
        self._server_thread.start()
    
    def stop(self):
        """Stop the server."""
        self.running = False
        if self._server_thread:
            self._server_thread.join(timeout=5)

# ============================================================================
# FEATURE 11: MEMORY SYSTEM
# ============================================================================

class LLMMemory:
    """Long-term conversation memory with vector similarity."""
    
    def __init__(self, max_memories=100):
        self.memories = []
        self.max_memories = max_memories
        self.embedder = None
    
    def add_memory(self, text: str, metadata: Dict = None):
        """Add a memory entry."""
        memory = {
            "text": text,
            "metadata": metadata or {},
            "timestamp": time.time(),
            "embedding": None
        }
        
        # Get embedding if embedder available
        if self.embedder:
            try:
                memory["embedding"] = self.embedder.embed(text)
            except:
                pass
        
        self.memories.append(memory)
        
        # Maintain memory limit
        while len(self.memories) > self.max_memories:
            self.memories.pop(0)
    
    def set_embedder(self, embedder: LLMEmbeddings):
        """Set embedding model for similarity search."""
        self.embedder = embedder
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search memories by similarity."""
        if not self.embedder:
            # Fallback: keyword search
            query_lower = query.lower()
            results = []
            for memory in self.memories:
                if query_lower in memory["text"].lower():
                    results.append(memory)
            return results[:top_k]
        
        # Vector similarity search
        try:
            query_emb = self.embedder.embed(query)
            scored_memories = []
            
            for memory in self.memories:
                if memory["embedding"]:
                    similarity = self.embedder.cosine_similarity(
                        query_emb, 
                        memory["embedding"]
                    )
                    scored_memories.append((similarity, memory))
            
            # Sort by similarity (descending)
            scored_memories.sort(key=lambda x: x[0], reverse=True)
            return [mem for score, mem in scored_memories[:top_k]]
        except:
            return []
    
    def get_memories(self) -> List[Dict]:
        """Get all memories."""
        return self.memories
    
    def clear(self):
        """Clear all memories."""
        self.memories = []

# ============================================================================
# FEATURE 12: TOOL CALLING
# ============================================================================

class ToolCaller:
    """LLM can call Stamp functions."""
    
    def __init__(self, generator: GPT2Generator):
        self.generator = generator
        self.tools = {}
    
    def register_tool(self, name: str, func: Callable, description: str):
        """Register a tool."""
        self.tools[name] = {
            "func": func,
            "description": description
        }
    
    def parse_tool_call(self, response: str) -> Dict:
        """Parse tool call from response."""
        # Look for patterns like: TOOL_CALL: tool_name(args)
        pattern = r'TOOL_CALL:\s*(\w+)\s*\(([^)]*)\)'
        match = re.search(pattern, response)
        
        if match:
            tool_name = match.group(1)
            args_str = match.group(2)
            
            try:
                args = json.loads(args_str)
            except:
                args = {}
            
            return {"tool": tool_name, "args": args}
        
        return None
    
    def execute_tool_call(self, tool_name: str, args: Dict) -> Any:
        """Execute a registered tool."""
        if tool_name not in self.tools:
            return f"Error: Tool '{tool_name}' not found"
        
        try:
            result = self.tools[tool_name]["func"](**args)
            return result
        except Exception as e:
            return f"Error executing tool: {e}"
    
    def generate_with_tools(self, prompt: str, tools_desc: str = "") -> str:
        """Generate with tool awareness."""
        tool_list = "\n".join([
            f"- {name}: {info['description']}" 
            for name, info in self.tools.items()
        ])
        
        full_prompt = f"""Available tools:
{tool_list}

User request: {prompt}

Respond with your answer, or use TOOL_CALL: tool_name(args) if you need to use a tool."""
        
        response = self.generator.generate(full_prompt)
        
        # Check for tool call
        tool_call = self.parse_tool_call(response)
        if tool_call:
            tool_result = self.execute_tool_call(
                tool_call["tool"], 
                tool_call["args"]
            )
            
            # Generate final response with tool result
            followup = f"""Tool '{tool_call['tool']}' returned: {tool_result}

Now provide your answer based on this result."""
            return self.generator.generate(followup)
        
        return response
    
    def list_tools(self) -> List[Dict]:
        """List registered tools."""
        return [
            {"name": name, "description": info["description"]}
            for name, info in self.tools.items()
        ]

# ============================================================================
# FEATURE 13: MULTI-TURN CONVERSATIONS
# ============================================================================

class ConversationManager:
    """Advanced conversation management."""
    
    def __init__(self, generator: GPT2Generator, max_context=10):
        self.generator = generator
        self.conversations = {}
        self.max_context = max_context
    
    def create_conversation(self, conv_id: str):
        """Create a new conversation."""
        self.conversations[conv_id] = {
            "messages": [],
            "created": time.time(),
            "metadata": {}
        }
    
    def add_message(self, conv_id: str, role: str, content: str, metadata: Dict = None):
        """Add message to conversation."""
        if conv_id not in self.conversations:
            self.create_conversation(conv_id)
        
        self.conversations[conv_id]["messages"].append({
            "role": role,
            "content": content,
            "timestamp": time.time(),
            "metadata": metadata or {}
        })
    
    def get_context(self, conv_id: str) -> str:
        """Get formatted context for LLM."""
        if conv_id not in self.conversations:
            return ""
        
        messages = self.conversations[conv_id]["messages"]
        
        # Truncate to max_context
        recent_messages = messages[-self.max_context:]
        
        # Format messages
        context = ""
        for msg in recent_messages:
            context += f"{msg['role']}: {msg['content']}\n"
        
        return context
    
    def get_conversation(self, conv_id: str) -> List[Dict]:
        """Get all messages."""
        if conv_id not in self.conversations:
            return []
        return self.conversations[conv_id]["messages"]
    
    def list_conversations(self) -> List[str]:
        """List all conversation IDs."""
        return list(self.conversations.keys())
    
    def delete_conversation(self, conv_id: str):
        """Delete a conversation."""
        if conv_id in self.conversations:
            del self.conversations[conv_id]

# ============================================================================
# FEATURE 16: PROMPT ENGINEERING ASSISTANT
# ============================================================================

class PromptAssistant:
    """AI helper to craft better prompts."""
    
    def __init__(self, generator: GPT2Generator):
        self.generator = generator
    
    def improve_prompt(self, original_prompt: str, task_type: str = "general") -> str:
        """Improve a prompt."""
        improvement_instruction = f"""You are a prompt engineering expert. Improve the following prompt for {task_type} tasks.

Original prompt:
{original_prompt}

Provide only the improved prompt, no explanations."""
        
        improved = self.generator.generate(
            improvement_instruction,
            temperature=0.3
        )
        return improved.strip()
    
    def generate_system_prompt(self, task: str, constraints: List[str] = None) -> str:
        """Generate a system prompt."""
        constraints_text = "\n".join(f"- {c}" for c in constraints) if constraints else ""
        
        instruction = f"""Generate a detailed system prompt for the following task:
Task: {task}
{f'Constraints:\n{constraints_text}' if constraints else ''}

The system prompt should:
1. Define the AI's role and expertise
2. Set clear boundaries and guidelines
3. Include relevant constraints
4. Be concise but comprehensive

Provide only the system prompt text."""
        
        system_prompt = self.generator.generate(instruction, temperature=0.5)
        return system_prompt.strip()
    
    def suggest_examples(self, prompt: str, num_examples: int = 3) -> List[str]:
        """Suggest few-shot examples."""
        instruction = f"""Generate {num_examples} diverse example prompts and responses for this task:

Task/Context: {prompt}

Provide examples in format:
Example 1:
Input: ...
Output: ...

Do not include explanations."""
        
        examples_text = self.generator.generate(instruction, temperature=0.7)
        
        # Parse examples
        examples = []
        parts = re.split(r'Example \d+:', examples_text)
        for part in parts[1:]:
            if "Input:" in part and "Output:" in part:
                examples.append(part.strip())
        
        return examples

# ============================================================================
# FEATURE 17: MODEL BENCHMARKING
# ============================================================================

class ModelBenchmarker:
    """Test and compare model performance."""
    
    def __init__(self, config=None):
        self.config = config or OllamaConfig()
        self.results = {}
    
    def benchmark_generation(self, model: str, prompts: List[str]) -> Dict:
        """Benchmark text generation."""
        generator = GPT2Generator(model, self.config)
        
        times = []
        for prompt in prompts:
            start = time.time()
            try:
                generator.generate(prompt, show_progress=False)
                elapsed = time.time() - start
                times.append(elapsed)
            except Exception:
                times.append(None)
        
        valid_times = [t for t in times if t is not None]
        
        return {
            "model": model,
            "avg_time": sum(valid_times) / len(valid_times) if valid_times else 0,
            "min_time": min(valid_times) if valid_times else 0,
            "max_time": max(valid_times) if valid_times else 0,
            "success_rate": len(valid_times) / len(times),
            "total_prompts": len(prompts)
        }
    
    def benchmark_accuracy(self, model: str, test_cases: List[Dict]) -> Dict:
        """Benchmark on labeled test cases."""
        tokenizer = LLMTokenizer()
        generator = GPT2Generator(model, self.config)
        
        correct = 0
        total = len(test_cases)
        
        for case in test_cases:
            response = generator.generate(case["prompt"], show_progress=False)
            
            # Simple accuracy check: exact match or contains
            if "expected" in case:
                if response.lower().strip() == case["expected"].lower().strip():
                    correct += 1
            elif "contains" in case:
                if case["contains"].lower() in response.lower():
                    correct += 1
        
        return {
            "model": model,
            "accuracy": correct / total if total > 0 else 0,
            "correct": correct,
            "total": total
        }
    
    def compare_models(self, models: List[str], prompts: List[str]) -> List[Dict]:
        """Compare multiple models."""
        results = []
        
        for model in models:
            bench = self.benchmark_generation(model, prompts)
            results.append(bench)
        
        # Sort by average time
        results.sort(key=lambda x: x["avg_time"])
        return results
    
    def get_results(self) -> List[Dict]:
        """Get all benchmark results."""
        return list(self.results.values())

# ============================================================================
# FEATURE 18: RESPONSE ANALYSIS
# ============================================================================

class ResponseAnalyzer:
    """Quality scoring and metrics."""
    
    @staticmethod
    def calculate_perplexity(text: str, model_vocab: int = 50257) -> float:
        """Estimate perplexity (simplified)."""
        words = text.split()
        if not words:
            return 0.0
        
        # Simplified: based on word frequency
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
        total_words = len(words)
        unique_words = len(word_counts)
        
        # Lower perplexity = more predictable
        perplexity = total_words / unique_words
        return perplexity
    
    @staticmethod
    def analyze_diversity(responses: List[str]) -> Dict:
        """Analyze diversity of responses."""
        if not responses:
            return {"diversity_score": 0.0, "unique_ratio": 0.0}
        
        # Count unique responses
        unique_responses = len(set(responses))
        total_responses = len(responses)
        
        return {
            "diversity_score": unique_responses / total_responses,
            "unique_ratio": unique_responses / total_responses,
            "total_unique": unique_responses
        }
    
    @staticmethod
    def calculate_coherence(response: str, reference: str = None) -> Dict:
        """Calculate coherence metrics."""
        sentences = re.split(r'[.!?]+', response)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        
        metrics = {
            "avg_sentence_length": avg_sentence_length,
            "sentence_count": len(sentences),
            "word_count": len(response.split())
        }
        
        if reference:
            # Simple BLEU-like metric (word overlap)
            ref_words = set(reference.lower().split())
            resp_words = set(response.lower().split())
            overlap = ref_words & resp_words
            metrics["word_overlap"] = len(overlap)
            metrics["overlap_ratio"] = len(overlap) / len(ref_words) if ref_words else 0
        
        return metrics
    
    @staticmethod
    def full_analysis(response: str, reference: str = None, time_taken: float = None) -> Dict:
        """Complete response analysis."""
        tokenizer = LLMTokenizer()
        token_stats = tokenizer.count_response_tokens(response)
        perplexity = ResponseAnalyzer.calculate_perplexity(response)
        coherence = ResponseAnalyzer.calculate_coherence(response, reference)
        
        return {
            "tokens": token_stats,
            "perplexity": perplexity,
            "coherence": coherence,
            "time_taken_seconds": time_taken,
            "tokens_per_second": token_stats["tokens"] / time_taken if time_taken else 0
        }

# ============================================================================
# FEATURE 19: STREAMING WITH EVENTS
# ============================================================================

class EventStreamer:
    """Event-driven streaming with callbacks."""
    
    def __init__(self, generator: GPT2Generator):
        self.generator = generator
        self.on_chunk = None
        self.on_complete = None
        self.on_error = None
    
    def set_event_handlers(self, on_chunk=None, on_complete=None, on_error=None):
        """Set event callbacks."""
        self.on_chunk = on_chunk
        self.on_complete = on_complete
        self.on_error = on_error
    
    def stream_with_events(self, prompt: str, **kwargs):
        """Stream with event callbacks."""
        try:
            import requests
        except ImportError:
            raise RuntimeError("requests library not installed")
        
        full_response = ""
        
        url = self.generator.config.get_url("/api/generate")
        data = {
            "model": self.generator.model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": kwargs.get("temperature", self.generator.config.temperature),
                "num_predict": kwargs.get("num_predict", self.generator.config.num_predict),
            }
        }
        
        try:
            with requests.post(url, json=data, stream=True, timeout=self.generator.config.timeout) as r:
                for line in r.iter_lines():
                    if line:
                        try:
                            chunk = json.loads(line)
                            response_part = chunk.get("response", "")
                            full_response += response_part
                            
                            # Fire on_chunk event
                            if self.on_chunk:
                                self.on_chunk(response_part, full_response)
                        except json.JSONDecodeError:
                            pass
            
            # Fire on_complete event
            if self.on_complete:
                self.on_complete(full_response)
        
        except Exception as e:
            # Fire on_error event
            if self.on_error:
                self.on_error(e)
            raise

# ============================================================================
# FEATURE 20: PROMPT CHAINING
# ============================================================================

class PromptChainer:
    """Chain multiple prompts with output→input flow."""
    
    def __init__(self, generator: GPT2Generator):
        self.generator = generator
        self.chain_history = []
    
    def add_link(self, name: str, input_prompt: str, output_extractor: Callable = None):
        """Add a link to the chain."""
        self.chain_history.append({
            "name": name,
            "input_prompt": input_prompt,
            "output_extractor": output_extractor,
            "last_output": None
        })
    
    def run_chain(self, initial_input: str) -> List[Dict]:
        """Execute entire chain."""
        results = []
        current_input = initial_input
        
        for link in self.chain_history:
            # Generate with current input
            output = self.generator.generate(
                link["input_prompt"].replace("{input}", current_input),
                show_progress=False
            )
            
            # Extract next input if extractor provided
            next_input = current_input
            if link["output_extractor"]:
                next_input = link["output_extractor"](output)
            
            # Store result
            result = {
                "link_name": link["name"],
                "input": current_input,
                "output": output,
                "next_input": next_input
            }
            results.append(result)
            
            # Update link state
            link["last_output"] = output
            current_input = next_input
        
        return results
    
    def get_chain_history(self) -> List[Dict]:
        """Get chain configuration."""
        return self.chain_history
    
    def clear_chain(self):
        """Clear the chain."""
        self.chain_history = []

# ============================================================================
# FEATURE 22: CONCURRENT GENERATION
# ============================================================================

class ConcurrentGenerator:
    """Generate multiple requests in parallel (async)."""
    
    def __init__(self, generator: GPT2Generator, max_workers=4):
        self.base_generator = generator
        self.max_workers = max_workers
    
    async def generate_async(self, prompt: str, **kwargs) -> str:
        """Async generation wrapper."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: self.base_generator.generate(prompt, show_progress=False, **kwargs))
    
    async def generate_batch_async(self, prompts: List[str], **kwargs) -> List[str]:
        """Generate multiple prompts concurrently."""
        tasks = [self.generate_async(p, **kwargs) for p in prompts]
        return await asyncio.gather(*tasks)
    
    def generate_concurrent(self, prompts: List[str], **kwargs) -> List[str]:
        """Concurrent generation interface."""
        try:
            return asyncio.run(self.generate_batch_async(prompts, **kwargs))
        except RuntimeError:
            # Fallback to ThreadPoolExecutor if asyncio fails
            return self._generate_concurrent_threadpool(prompts, **kwargs)
    
    def _generate_concurrent_threadpool(self, prompts: List[str], **kwargs) -> List[str]:
        """Thread pool fallback."""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for prompt in prompts:
                future = executor.submit(
                    self.base_generator.generate,
                    prompt,
                    show_progress=False,
                    **kwargs
                )
                futures.append(future)
            
            results = []
            for future in as_completed(futures):
                try:
                    results.append(future.result())
                except Exception:
                    results.append("")
            
            return results

# ============================================================================
# FEATURE 23: RESPONSE FORMATTING
# ============================================================================

class ResponseFormatter:
    """Force specific output formats."""
    
    def __init__(self, generator: GPT2Generator):
        self.generator = generator
    
    def format_as_json(self, prompt: str, schema: Dict = None) -> Dict:
        """Generate and format as JSON."""
        schema_desc = json.dumps(schema, indent=2) if schema else "any valid JSON"
        
        format_prompt = f"""Generate a JSON response for this request:
{prompt}

Expected format: JSON
{f'Schema/structure:\n{schema_desc}' if schema else ''}

Respond ONLY with valid JSON, no other text."""
        
        response = self.generator.generate(format_prompt, temperature=0.3)
        
        # Clean and parse
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:-3]
        elif response.startswith("```"):
            response = response[3:-3]
        
        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            return {"error": f"Invalid JSON: {str(e)}", "raw": response}
    
    def format_as_xml(self, prompt: str, root_tag: str = "response") -> str:
        """Generate and format as XML."""
        format_prompt = f"""Generate an XML response for this request:
{prompt}

Response format: XML
Root tag: <{root_tag}>

Respond ONLY with valid XML, no other text."""
        
        response = self.generator.generate(format_prompt, temperature=0.3)
        
        # Clean code blocks
        response = response.strip()
        if response.startswith("```xml"):
            response = response[6:-3]
        elif response.startswith("```"):
            response = response[3:-3]
        
        return response
    
    def format_as_code(self, prompt: str, language: str = "python") -> str:
        """Generate code in specific language."""
        format_prompt = f"""Generate {language} code for this request:
{prompt}

Provide ONLY code, no explanations or markdown formatting.
Do not wrap in code blocks, just raw code."""
        
        response = self.generator.generate(format_prompt, temperature=0.2)
        
        # Clean markdown code blocks
        response = response.strip()
        if response.startswith(f"```{language}"):
            response = response[3+len(language)+1:-3]
        elif response.startswith("```"):
            response = response[3:-3]
        
        return response
    
    def format_as_csv(self, prompt: str, columns: List[str]) -> str:
        """Generate and format as CSV."""
        columns_str = ",".join(columns)
        format_prompt = f"""Generate a CSV response for this request:
{prompt}

Response format: CSV
Columns: {columns_str}

Respond ONLY with valid CSV, no other text.
No headers, just data rows."""
        
        response = self.generator.generate(format_prompt, temperature=0.3)
        
        # Clean code blocks
        response = response.strip()
        if response.startswith("```csv"):
            response = response[6:-3]
        elif response.startswith("```"):
            response = response[3:-3]
        
        return response

# ============================================================================
# FEATURE 25: TOOL SELECTION
# ============================================================================

class ToolSelector:
    """Intelligently pick model based on task type."""
    
    def __init__(self, config=None):
        self.config = config or OllamaConfig()
        self.available_models = OllamaCheck.list_models(config)
        self.task_rules = {
            "code": ["codellama", "deepseek-coder", "gpt2"],
            "creative": ["llama2", "mistral", "gpt2"],
            "factual": ["llama2", "mistral"],
            "chat": ["llama2", "mistral", "phi"],
            "summary": ["llama2", "gpt2"],
            "translation": ["llama2", "mistral"]
        }
    
    def detect_task_type(self, prompt: str) -> str:
        """Detect task type from prompt."""
        prompt_lower = prompt.lower()
        
        # Keywords for each task type
        keywords = {
            "code": ["code", "function", "class", "program", "debug", "fix bug"],
            "creative": ["story", "poem", "write", "creative", "fiction"],
            "factual": ["what is", "explain", "define", "facts", "history"],
            "chat": ["hello", "hi", "hey", "conversation"],
            "summary": ["summarize", "summary", "brief", "overview"],
            "translation": ["translate", "translation", "in spanish", "in french"]
        }
        
        # Score each task type
        scores = {}
        for task_type, task_keywords in keywords.items():
            score = sum(1 for kw in task_keywords if kw in prompt_lower)
            scores[task_type] = score
        
        # Return highest scoring type
        if scores:
            return max(scores, key=scores.get)
        return "general"  # Default
    
    def select_model(self, prompt: str, preferred_model: str = None) -> str:
        """Select best model for task."""
        # If user specifies model, use it
        if preferred_model and preferred_model in self.available_models:
            return preferred_model
        
        # Detect task type
        task_type = self.detect_task_type(prompt)
        
        # Get models for task type
        task_models = self.task_rules.get(task_type, self.available_models)
        
        # Find first available model
        for model in task_models:
            if model in self.available_models:
                return model
        
        # Fallback to first available
        if self.available_models:
            return self.available_models[0]
        
        # Last resort
        return "gpt2"
    
    def get_task_recommendation(self, prompt: str) -> Dict:
        """Get model recommendation with reasoning."""
        task_type = self.detect_task_type(prompt)
        recommended = self.select_model(prompt)
        
        return {
            "task_type": task_type,
            "recommended_model": recommended,
            "reasoning": f"Detected task as '{task_type}', selecting best available model",
            "available_models": self.available_models
        }

# ============================================================================
# MAIN EXPORTS & DEMO
# ============================================================================

if __name__ == "__main__":
    console.print(Panel.fit(
        "[bold cyan]Stamp LLM Module[/]\n"
        "[bold]Complete Edition - 22 New Features[/]",
        title="[bold]LLM Demo[/bold]"
    ))
    
    # Basic demo
    console.print(f"\n[bold]Basic Usage:[/]")
    console.print(f"  Installed: {'[green]✓[/]' if OllamaCheck.is_installed() else '[red]✗[/]'}")
    console.print(f"  Running: {'[green]✓[/]' if OllamaCheck.is_running() else '[red]✗[/]'}")
    
    models = OllamaCheck.list_models()
    if models:
        console.print(f"  Models: [green]{', '.join(models[:3])}[/]" + (f" ...and {len(models)-3} more" if len(models) > 3 else ""))
    else:
        console.print(f"  Models: [dim]None[/]")
