# Ollama/GPT-2 API

The `stamp.gpt2` module provides a Pythonic interface to [Ollama](https://ollama.ai), a local LLM runner that allows you to run models like GPT-2, LLaMA, and many others directly on your machine.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Classes](#classes)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)

## Installation

### 1. Download Ollama

Go to **https://ollama.ai/download** and download Ollama for your platform:
- Windows: Download the `.exe` installer
- macOS: Download the DMG file
- Linux: Download the script or package

Install it on your system.

### 2. Pull a Model

Open your terminal/command prompt and run:

```bash
ollama pull gpt2
```

That's it! You can now use GPT-2.

**Want other models?**
```bash
ollama pull llama2
ollama pull mistral
ollama pull codellama
```

### 3. Start Ollama

Ollama should start automatically. If not:

```bash
ollama serve
```

## Quick Start

```python
from stamp import Ollama, GPT2Generator

# Method 1: Using the Ollama class
ollama = Ollama(model="gpt2")
result = ollama.generate("Hello, world!")
print(result)

# Method 2: Using GPT2Generator directly
generator = GPT2Generator(model="gpt2")
result = generator.generate("Write a short poem about Python")
print(result)
```

## Classes

### OllamaConfig

Configuration for the Ollama connection and generation parameters.

```python
config = OllamaConfig()

# Properties:
config.host = "localhost"        # Ollama server host
config.port = 11434               # Ollama server port
config.base_url                  # Full API URL (auto-generated)
config.model = "gpt2"            # Default model to use
config.timeout = 30               # Request timeout in seconds
config.temperature = 0.7           # Generation temperature (0-1)
config.num_predict = 256          # Maximum tokens to generate
```

### OllamaCheck

Utility class to check Ollama status and manage models.

```python
from stamp import OllamaCheck

# Check if Ollama is installed
if OllamaCheck.is_installed():
    print("Ollama is installed!")

# Check if server is running
if OllamaCheck.is_running():
    print("Ollama server is running!")

# List available models
models = OllamaCheck.list_models()
print(f"Available models: {models}")

# Check if a specific model is available
if OllamaCheck.is_model_available("gpt2"):
    print("GPT-2 model is available!")

# Download/pull a new model
OllamaCheck.pull_model("llama2")
```

### GPT2Generator

High-level text generator with Ollama integration.

```python
from stamp import GPT2Generator

generator = GPT2Generator(model="gpt2")

# Generate text
result = generator.generate(
    prompt="Explain quantum computing",
    temperature=0.7,
    num_predict=256
)
print(result)

# Generate with streaming
generator.generate_stream("Tell me a story")

# Code completion
code = generator.complete_code(
    prefix="def fibonacci(n):",
    temperature=0.3
)

# Chat-style generation
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language..."},
    {"role": "user", "content": "What are its main features?"}
]
response = generator.chat(messages)

# Summarize text
summary = generator.summarize(long_text)

# Translate text
translation = generator.translate(
    text="Hello, how are you?",
    target_language="Spanish"
)

# Manage history
history = generator.get_history()
generator.clear_history()
generator.export_history("chat_history.json")
```

### Ollama

Main Ollama interface providing easy access to generation functions.

```python
from stamp import Ollama

ollama = Ollama(model="gpt2")

# Generate text
result = ollama.generate("Write code to sort a list")

# Generate with streaming
ollama.generate_stream("Tell me about AI")

# Chat
messages = [
    {"role": "user", "content": "Hello!"},
]
response = ollama.chat(messages)

# Code completion
code = ollama.complete_code("def bubble_sort(")

# Switch models
ollama.set_model("llama2")

# List available models
models = ollama.list_models()

# Pull new model
ollama.pull_model("mistral")
```

## Usage Examples

### Text Generation

```python
from stamp import Ollama

# Create generator
ollama = Ollama(model="gpt2")

# Simple generation
result = ollama.generate("The future of AI is")

# With custom parameters
result = ollama.generate(
    prompt="Write a haiku about programming",
    temperature=0.8,      # Higher = more creative
    num_predict=50         # Limit length
)
print(result)
```

### Code Completion

```python
from stamp import GPT2Generator

generator = GPT2Generator(model="codellama")

# Complete a function
code = generator.complete_code("""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
""", temperature=0.3)

print(code)
```

### Chat Application

```python
from stamp import GPT2Generator

generator = GPT2Generator(model="llama2")

conversation = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        break
    
    conversation.append({"role": "user", "content": user_input})
    
    response = generator.chat(conversation)
    print(f"AI: {response}")
    
    conversation.append({"role": "assistant", "content": response})
```

### Streaming Output

```python
from stamp import Ollama

ollama = Ollama(model="gpt2")

# Stream text as it's generated
ollama.generate_stream("Write a short story about a robot")
```

### Multiple Models

```python
from stamp import Ollama

# Use GPT-2 for creative writing
gpt2 = Ollama(model="gpt2")
creative = gpt2.generate("Write a creative story")

# Use LLaMA for factual questions
llama2 = Ollama(model="llama2")
factual = llama2.generate("What is the capital of France?")

# Use CodeLlama for programming
codellama = Ollama(model="codellama")
code = codellama.generate("Write a Python function to reverse a string")
```

## API Reference

### OllamaConfig

| Property | Type | Default | Description |
|----------|------|----------|-------------|
| `host` | str | `"localhost"` | Ollama server hostname |
| `port` | int | `11434` | Ollama server port |
| `base_url` | str | Auto | Full API URL (read-only) |
| `model` | str | `"gpt2"` | Default model to use |
| `timeout` | int | `30` | Request timeout in seconds |
| `temperature` | float | `0.7` | Generation temperature (0.0-1.0) |
| `num_predict` | int | `256` | Maximum tokens to generate |

### GPT2Generator Methods

| Method | Description |
|--------|-------------|
| `generate(prompt, temperature, num_predict, show_progress)` | Generate text from prompt |
| `generate_stream(prompt, temperature, num_predict)` | Generate with streaming output |
| `complete_code(prefix, temperature)` | Complete code from prefix |
| `chat(messages, temperature)` | Chat-style generation |
| `summarize(text, temperature)` | Summarize text |
| `translate(text, target_language, temperature)` | Translate text |
| `get_history()` | Get generation history |
| `clear_history()` | Clear generation history |
| `export_history(filename)` | Export history to JSON file |

### Ollama Methods

| Method | Description |
|--------|-------------|
| `generate(prompt, **kwargs)` | Generate text |
| `generate_stream(prompt, **kwargs)` | Generate with streaming |
| `chat(messages, **kwargs)` | Chat interaction |
| `complete_code(prefix, **kwargs)` | Complete code |
| `set_model(model)` | Change the model |
| `list_models()` | List available models |
| `pull_model(model)` | Download a new model |

### OllamaCheck Methods

| Method | Description |
|--------|-------------|
| `is_installed()` | Check if Ollama is installed |
| `is_running(config)` | Check if Ollama server is running |
| `list_models(config)` | List available models |
| `is_model_available(model, config)` | Check if a model is available |
| `pull_model(model, config)` | Download a new model |

## Recommended Models

| Model | Size | Best For |
|-------|------|----------|
| `gpt2` | ~500MB | General text, code |
| `llama2` | ~3.8GB | General purpose, chat |
| `mistral` | ~4.1GB | High quality generation |
| `codellama` | ~3.8GB | Code completion, programming |
| `tinyllama` | ~1.1GB | Lightweight, fast generation |

## Tips

1. **Temperature**:
   - Lower (0.1-0.3): More deterministic, good for code
   - Medium (0.5-0.7): Balanced, good for general use
   - Higher (0.8-1.0): More creative, good for stories

2. **Model Selection**:
   - Use smaller models for faster generation
   - Use larger models for higher quality
   - Use code-specific models for programming tasks

3. **Performance**:
   - Ollama runs locally, so performance depends on your hardware
   - GPU acceleration significantly speeds up generation
   - Streaming provides immediate feedback

4. **Storage**:
   - Models are downloaded to `~/.ollama/models/`
   - Each model typically takes 1-5GB of disk space

## Troubleshooting

### Ollama not installed
```
Error: Ollama not installed
```
**Solution**: Download and install Ollama from [ollama.ai](https://ollama.ai/download)

### Server not running
```
Error: Ollama server is not running!
```
**Solution**: Run `ollama serve` in a terminal

### Model not found
```
Error: Model 'gpt2' is not available!
```
**Solution**: Run `ollama pull gpt2` to download the model

### Connection timeout
```
Error: Error communicating with Ollama
```
**Solution**: 
- Check that Ollama server is running
- Verify port 11434 is not blocked by firewall
- Increase timeout in OllamaConfig

## See Also

- [Ollama Documentation](https://ollama.ai/docs)
- [Main Stamp Documentation](../all/index.md)
- [Quick Start Guide](../guides/quickstart.md)
