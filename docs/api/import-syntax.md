# Stamp Import Syntax

## Basic Import

Import Stamp to access all core functionality:

```python
from stamp import Stamp, lstamp, __cstring__, call
```

Usage:

```python
# Core functions
Stamp.stamp_()
lstamp._lstamp()
```

## Importing Specific Modules

### From Main Module

```python
from stamp.main import ErrorSystem, globalsys, ListDirectory, call
```

```python
ErrorSystem.CustomError("MyError", "Error message")
globalsys
ListDirectory.listdir(fromRoot=True)
call("echo hello")
```

### AI Features (Stamp 4.5)

```python
from stamp.llm import Ollama, GPT2Generator, LLMMemory
```

```python
# LLM
Ollama.generate("Tell me a joke")
GPT2Generator.generate("Once upon a time")
LLMMemory.add_message("user", "Hi")
```

### AI Features (Stamp 4.6)

```python
from stamp.lib.ai.oaiftrs.oaiftrs import NLPText, SmartSearch, OptimizationAI
from stamp.lib.ai.oaiftrs.ptr.ptai import PatternAI
from stamp.lib.ai.oaiftrs.cdi.coai import CodeAI
from stamp.lib.ai.oaiftrs.daz.daai import DataAnalyzer
from stamp.lib.ai.oaiftrs.prd.prai import PredictSystem
from stamp.lib.ai.oaiftrs.sec.scai import SecurityAI
```

```python
# NLP
NLPText.sentiment("I love Stamp!")
NLPText.summarizeSimple("Long text here")
NLPText.extractEntities("John works at Microsoft")

# Pattern Detection
PatternAI.detectPatterns([1, 2, 3, 4, 5])
PatternAI.findAnomalies([1, 2, 3, 4, 5])
PatternAI.predictNext([1, 2, 3])

# Code Analysis
CodeAI.detectDuplicates(code)
CodeAI.findSmells(code)
CodeAI.analyzeComplexity(code)

# Data Analysis
DataAnalyzer.detectTrends([1, 2, 3, 4, 5, 6])
DataAnalyzer.findOutliers([1, 2, 3, 4, 5])
DataAnalyzer.statisticalSummary(data)

# Security
SecurityAI.detectMalicious(code)
SecurityAI.predictAttackProbability(data)
SecurityAI.scoreThreatSeverity(threat_data)
```

### AI Features (Stamp 4.7)

```python
from stamp.lib.ai.oaiftrs.img.imai import ImageAI
from stamp.lib.ai.oaiftrs.aud.adai import AudioAI
from stamp.lib.ai.oaiftrs.dpl.dlai import DeepLearningAI
from stamp.lib.ai.oaiftrs.fct.fcai import ForecastAI
from stamp.lib.ai.oaiftrs.kga.kgai import KnowledgeGraphAI
from stamp.lib.ai.oaiftrs.rec.rcai import RecommendationAI
from stamp.lib.ai.oaiftrs.vis.viai import VisionAI
from stamp.lib.ai.qzr.quzr import QuantizerAI
```

```python
# Image AI
ImageAI.classifyImage("photo.jpg")
ImageAI.detectObjects("image.png")
ImageAI.extractFeatures("img.jpg")

# Audio AI
AudioAI.transcribeAudio("speech.wav")
AudioAI.detectLanguage("audio.mp3")
AudioAI.analyzeSentiment("sound.wav")

# Deep Learning
DeepLearningAI.trainDeepModel(data, "cnn")
DeepLearningAI.predictDeep(model_id, input_data)
DeepLearningAI.exportModel(model_id, "model.pt")

# Forecasting
ForecastAI.forecastARIMA(time_series, 5)
ForecastAI.detectSeasonality(data)
ForecastAI.anomalyDetection(data)

# Knowledge Graph
KnowledgeGraphAI.buildGraph(entities, relationships)
KnowledgeGraphAI.queryGraph(graph, query)
KnowledgeGraphAI.findShortestPath(graph, node_a, node_b)

# Recommendations
RecommendationAI.trainRecommender(user_data)
RecommendationAI.recommendItems(user_id, 10)
RecommendationAI.getSimilarItems(item_id, 5)

# Vision AI
VisionAI.detectObjects("video.mp4")
VisionAI.trackObjects("video.mp4")
VisionAI.analyzeMotion("video.mp4")

# Quantizer
QuantizerAI.quantizeModel(model, 8)
QuantizerAI.optimizeForDeployment(model, "mobile")
```

## Utility Functions

### String Operations

```python
from stamp import __cstring__, edit, __cmp__, pdec
```

```python
__cstring__("Hello World")
edit.join(["Hello", "World"])
edit.replace("old", "new", "old text")
__cmp__.compare(N1=10, N2=20, operator="lt")
pdec.pdec(3, 14, returnOutput=True)
```

### File Operations

```python
from stamp import _export, _import, _mkdir, _mkfile, ListDirectory
```

```python
_export(data="content", file="test.txt", end="\n")
_import("test.txt")
_mkdir("new_folder")
_mkfile("new.txt", "Hello", wmode=True)
ListDirectory.listdir(fromRoot=False, openInSeperateCMD=True)
```

### Debugging

```python
from stamp import Debug, adverr, advout, advin
```

```python
Debug.debug("Debug message")
Debug.info("Info message")
Debug.warning("Warning")
Debug.error("Error")

adverr.e0()  # KeyboardInterrupt
adverr.e1()  # NotADirectoryError
adverr.e2()  # FileNotFoundError
advout.advout("command", "directory")
```

### Type Conversion

```python
from stamp import Type, tconstant, tlist, superobj
```

```python
Type.constant("NAME")
Type.list(["a", "b", "c"])
Type.type("variable")
tconstant.typeToConstant("constant")
tlist.typeToList(["item1", "item2"])
superobj.superobj("123")
```

## Multiple Imports

```python
from stamp.main import Stamp, lstamp, call, __cstring__
from stamp.lib.ai.oaiftrs.oaiftrs import NLPText, SmartSearch
from stamp.lib.ai.oaiftrs.img.imai import ImageAI
from stamp.lib.ai.qzr.quzr import QuantizerAI
```

## Import Patterns

### Pattern 1: Import Everything
```python
from stamp.main import *
```

### Pattern 2: Selective Import
```python
from stamp.main import Stamp, call, Debug
```

### Pattern 3: AI Module Import
```python
from stamp.lib.ai.oaiftrs.oaiftrs import NLPText, PatternAI
from stamp.lib.ai.oaiftrs.img.imai import ImageAI
```

### Pattern 4: Utility Import
```python
from stamp.main import edit, _export, Debug
```

## Available Modules

### Core (main.py)
- **Stamp, lstamp, PCStamp**
- **ErrorSystem, globalsys, ListDirectory**
- **CallError, call, \_\_cstring\_\_, \_\_cmd\_\_**
- **_py_classlvl_consts, superobj, \_\_jsonconf\_\_**
- **_history, _kvstore, _note, _notes, _cl, _lock**
- **S1, S2, C1, C2, K1, K2, T1, T2, L1, L2, R1, R2**
- **temp, taskmgr, edit, Unite, Kit, Abomination, Angle, Alias**
- **\_\_isin\_\_, \_\_log\_\_, Royal, _count_ds, _count_subds, _calc**
- **Frozen, _seed, _dynvar, _link, TimeError, ixpd, _uname**
- **\_\_version\_\_, exit, License**
- **adverr, advout, advin, \_\_cmp\_\_, \_\_helpcmd\_\_, pdec, \_\_exf\_\_, \_\_cd\_\_
- **tconstant, tlist, Type, UnknownAdverrIntError, Control, Debug**
- **DirectoryExistsError, ArgumentError, _export, _import, _mkdir, _mkfile**
- **HTML, join3, rj3, _ShortType**
- **PyInstaller, Error501, Error502, Error503, Error504, Error505, Error506, Error507, Error508**
### LLM (llm.py)
- **OllamaConfig, OllamaCheck**
- **GPT2Generator**
- **Ollama**
- **LLMBatchGenerator, LLMEmbeddings**
- **LLMModelComparer, LLMTokenizer, PromptTemplate**
- **ResponseFilter, FileProcessor, WebScraper**
- **LLMAPIServer, LLMMemory, ToolCaller**
- **ConversationManager, PromptAssistant, ModelBenchmarker**
- **ResponseAnalyzer, EventStreamer, PromptChainer**
- **ConcurrentGenerator, ResponseFormatter, ToolSelector**

### AI Features (lib/ai/oaiftrs/)
- **4.6**: **NLPText, SmartSearch, OptimizationAI, PatternAI, CodeAI, DataAnalyzer, PredictSystem, SecurityAI**
- **4.7**: **ImageAI, AudioAI, DeepLearningAI, ForecastAI, KnowledgeGraphAI, RecommendationAI, VisionAI**
- **Quantizer**: **QuantizerAI (lib/ai/qzr/)**

### Java Emulation (main.py)
- **java.System, java.out, java.util.Calendar**
- **java.util.Properties, java.util.Base64, java.net.URL**
- **java.io.Streams, java.util.Date, java.text.SimpleDateFormat**
- **java.lang.String, java.lang.StringBuilder, java.util.UUID**
- **java.io.File, java.util.Arrays, java.lang.Math**
- **java.util.Random, java.util.ArrayList, java.util.HashMap**
- **java.util.LinkedList, java.util.HashSet, java.util.Stack, java.util.Queue**

### Scratch Emulation (main.py)
- **Scratch.motion**, **Scratch.looks**, **Scratch.sound**

## Important Notes

### Import Path Structure

Stamp uses sibling module imports:

```
Use: from stamp.sibling import thing
Don't: from stamp import thing
```

### Module Locations

- Core: `stamp.`**`main`**
- LLM: `stamp.llm`
- AI 4.6: `stamp.lib.ai.oaiftrs.*`
- AI 4.7: `stamp.lib.ai.oaiftrs.*`
- Quantizer: `stamp.lib.ai.qzr`

### Version Tracking

Check module version in VERSIONS.txt:
- Stamp 4.x: Core features
- Stamp 4.5: LLM features
- Stamp 4.6: AI features (NLP, Pattern, Code, etc.)
- Stamp 4.7: AI features (Image, Audio, Vision, etc.)

## Best Practices

### For General Use
```python
from stamp.main import Stamp, lstamp, call, Debug
```

### For AI Projects
```python
from stamp.lib.ai.oaiftrs.oaiftrs import NLPText, PatternAI
from stamp.lib.ai.oaiftrs.img.imai import ImageAI
```

### For LLM Projects
```python
from stamp.llm import Ollama, LLMMemory, GPT2Generator
```

### For Utilities
```python
from stamp import edit, _export, Debug, Type
```