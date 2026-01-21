# AI Features - API Reference

Stamp 4.6 includes powerful AI capabilities organized into 8 classes with 38 methods.

## Overview

The AI module (`stamp.lib.ai.oaiftrs`) provides:
- **Natural Language Processing** - Text analysis and understanding
- **Smart Search** - Semantic document search and clustering
- **Optimization AI** - Performance monitoring and tuning
- **Pattern Recognition** - Detect patterns, anomalies, and trends
- **Code Intelligence** - Code analysis and refactoring suggestions
- **Data Analysis** - Statistical analysis and visualization suggestions
- **ML Predictions** - Machine learning classification and regression
- **Security Intelligence** - Threat detection and security analysis

## Installation

The AI features are included with Stamp 4.6. No additional dependencies required.

```python
from stamp.lib.ai.oaiftrs.oaiftrs import NLPText, SmartSearch, OptimizationAI
from stamp.lib.ai.oaiftrs.ptr.ptai import PatternAI
from stamp.lib.ai.oaiftrs.cdi.coai import CodeAI
from stamp.lib.ai.oaiftrs.daz.daai import DataAnalyzer
from stamp.lib.ai.oaiftrs.prd.prai import PredictSystem, ModelType
from stamp.lib.ai.oaiftrs.sec.sai import SecurityAI
```

## NLPText

Natural language processing for text analysis.

### sentiment(text: str) -> str
Analyzes the sentiment of text.
- **Parameters**: `text` - The text to analyze
- **Returns**: Sentiment (e.g., "positive", "negative", "neutral")

### extractKeywords(text: str) -> list
Extracts keywords from text.
- **Parameters**: `text` - The text to analyze
- **Returns**: List of keywords

### detectLanguage(text: str) -> str
Detects the language of text.
- **Parameters**: `text` - The text to analyze
- **Returns**: Language code (e.g., "en", "es", "fr")

### summarizeSimple(text: str) -> str
Summarizes text content.
- **Parameters**: `text` - The text to summarize
- **Returns**: Summary text

### extractEntities(text: str) -> list
Extracts named entities from text.
- **Parameters**: `text` - The text to analyze
- **Returns**: List of entities (people, places, organizations)

### classifyCategory(text: str) -> str
Classifies text into categories.
- **Parameters**: `text` - The text to classify
- **Returns**: Category (e.g., "tech", "finance", "health")

## SmartSearch

Semantic search and document analysis.

### searchByMeaning(directory: str, query: str) -> list
Searches files by meaning (semantic search).
- **Parameters**: 
  - `directory` - Directory to search
  - `query` - Search query
- **Returns**: List of matching files

### findSimilar(directory: str, query: str) -> list
Finds documents similar to query.
- **Parameters**:
  - `directory` - Directory to search
  - `query` - Query text
- **Returns**: List of similar documents

### contextAwareSearch(directory: str, query: str, context: list) -> list
Performs context-aware search.
- **Parameters**:
  - `directory` - Directory to search
  - `query` - Search query
  - `context` - List of context terms
- **Returns**: List of matching files

### clusterSimilar(directory: str) -> dict
Clusters similar documents together.
- **Parameters**: `directory` - Directory to analyze
- **Returns**: Dictionary of document clusters

## OptimizationAI

Performance monitoring and optimization.

### detectBottlenecks(metrics: dict) -> list
Detects performance bottlenecks.
- **Parameters**: `metrics` - Dictionary of performance metrics
- **Returns**: List of detected bottlenecks

### suggestTuning(metrics: dict) -> list
Suggests performance tuning options.
- **Parameters**: `metrics` - Dictionary of performance metrics
- **Returns**: List of tuning suggestions

### predictLoad(metrics: dict) -> dict
Predicts future load.
- **Parameters**: `metrics` - Dictionary of historical metrics
- **Returns**: Dictionary of load predictions

### autoTune(metrics: dict) -> dict
Automatically tunes parameters.
- **Parameters**: `metrics` - Dictionary of performance metrics
- **Returns**: Dictionary of tuned parameters

## PatternAI

Pattern recognition and time series analysis.

### detectPatterns(sequence: list) -> list
Detects patterns in data sequences.
- **Parameters**: `sequence` - List of values
- **Returns**: List of detected patterns

### findAnomalies(sequence: list) -> list
Finds anomalies in data.
- **Parameters**: `sequence` - List of values
- **Returns**: List of anomalies found

### predictNext(sequence: list) -> float
Predicts the next value in a sequence.
- **Parameters**: `sequence` - List of values
- **Returns**: Predicted next value

### classifyBehavior(sequence: list) -> str
Classifies the behavior of a sequence.
- **Parameters**: `sequence` - List of values
- **Returns**: Behavior type (e.g., "increasing", "cyclical")

### detectCycles(sequence: list) -> list
Detects cycles in data.
- **Parameters**: `sequence` - List of values
- **Returns**: List of detected cycles

### findBursts(sequence: list) -> list
Finds bursts in time series data.
- **Parameters**: `sequence` - List of values
- **Returns**: List of bursts detected

## CodeAI

Code analysis and refactoring assistance.

### detectDuplicates(code_blocks: list) -> list
Detects duplicate code blocks.
- **Parameters**: `code_blocks` - List of code strings
- **Returns**: List of duplicate code

### findSmells(code: str) -> list
Finds code smells.
- **Parameters**: `code` - Code string to analyze
- **Returns**: List of code smells

### analyzeComplexity(code: str) -> dict
Analyzes code complexity.
- **Parameters**: `code` - Code string to analyze
- **Returns**: Complexity metrics dictionary

### suggestRefactoring(code: str) -> list
Suggests refactoring options.
- **Parameters**: `code` - Code string to analyze
- **Returns**: List of refactoring suggestions

### codeSimilarity(code1: str, code2: str) -> float
Calculates similarity between code blocks.
- **Parameters**:
  - `code1` - First code string
  - `code2` - Second code string
- **Returns**: Similarity score (0.0 to 1.0)

### checkLineLength(code: str, max_length: int) -> list
Checks for lines exceeding max length.
- **Parameters**:
  - `code` - Code string to check
  - `max_length` - Maximum line length
- **Returns**: List of long lines with line numbers

## DataAnalyzer

Statistical analysis and data insights.

### detectTrends(data: list) -> str
Detects trends in data.
- **Parameters**: `data` - List of values
- **Returns**: Trend description

### findOutliers(data: list) -> list
Finds outliers in data.
- **Parameters**: `data` - List of values
- **Returns**: List of outliers

### statisticalSummary(data: list) -> dict
Calculates statistical summary.
- **Parameters**: `data` - List of values
- **Returns**: Dictionary of statistics (mean, median, std, etc.)

### visualizeSuggestions(data: list) -> list
Suggests visualizations for data.
- **Parameters**: `data` - List of values
- **Returns**: List of visualization suggestions

### correlateFeatures(feature1: list, feature2: list) -> float
Calculates correlation between features.
- **Parameters**:
  - `feature1` - First feature list
  - `feature2` - Second feature list
- **Returns**: Correlation coefficient

### detectSeasonality(data: list) -> dict
Detects seasonality in data.
- **Parameters**: `data` - List of values
- **Returns**: Seasonality information

## PredictSystem

Machine learning predictions.

### train(training_data: list, model_type: ModelType) -> str
Trains a machine learning model.
- **Parameters**:
  - `training_data` - List of training samples with features and labels
  - `model_type` - Type of model (CLASSIFIER or REGRESSOR)
- **Returns**: Model ID

### predict(model_id: str, features: list) -> list
Makes predictions using a trained model.
- **Parameters**:
  - `model_id` - ID of trained model
  - `features` - List of feature vectors to predict
- **Returns**: List of predictions

### classify(model_id: str, features: list) -> list
Classifies data using trained model.
- **Parameters**:
  - `model_id` - ID of trained model
  - `features` - List of feature vectors to classify
- **Returns**: List of classifications

### evaluate(model_id: str, test_features: list, test_labels: list) -> dict
Evaluates model performance.
- **Parameters**:
  - `model_id` - ID of trained model
  - `test_features` - Test feature vectors
  - `test_labels` - Test labels
- **Returns**: Evaluation metrics dictionary

## SecurityAI

Security threat detection and analysis.

### detectMalicious(log_entries: list) -> list
Detects malicious patterns in logs.
- **Parameters**: `log_entries` - List of log entries
- **Returns**: List of detected threats

### analyzeAnomalyScore(current_metrics: dict, baseline: dict) -> float
Analyzes anomaly score.
- **Parameters**:
  - `current_metrics` - Current metrics
  - `baseline` - Baseline metrics
- **Returns**: Anomaly score

### identifyThreatType(threat: str) -> str
Identifies type of threat.
- **Parameters**: `threat` - Threat string
- **Returns**: Threat type

### predictAttackProbability(pattern: dict) -> float
Predicts attack probability.
- **Parameters**: `pattern` - Pattern dictionary
- **Returns**: Probability (0.0 to 1.0)

### suggestMitigation(threat: dict) -> list
Suggests mitigation strategies.
- **Parameters**: `threat` - Threat dictionary
- **Returns**: List of mitigation suggestions

### scoreThreatSeverity(threat: dict) -> int
Scores threat severity.
- **Parameters**: `threat` - Threat dictionary
- **Returns**: Severity score (1-10)

## ModelType Enum

Types of machine learning models.

- `ModelType.CLASSIFIER` - Classification model
- `ModelType.REGRESSOR` - Regression model

## See Also

- [AI Examples](../examples/ai-features.md)
- [Testing AI Features](../../tests/ai/oaiftrs/)
