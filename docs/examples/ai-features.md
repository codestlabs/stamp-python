# AI Features - Usage Examples

This guide provides practical examples for using Stamp 4.6's AI features.

## Table of Contents

- [Natural Language Processing](#natural-language-processing)
- [Smart Search](#smart-search)
- [Optimization AI](#optimization-ai)
- [Pattern Recognition](#pattern-recognition)
- [Code Intelligence](#code-intelligence)
- [Data Analysis](#data-analysis)
- [Machine Learning Predictions](#machine-learning-predictions)
- [Security Intelligence](#security-intelligence)

## Natural Language Processing

### Analyze Text Sentiment

```python
from stamp.lib.ai.oaiftrs.oaiftrs import NLPText

nlp = NLPText()

# Analyze sentiment
text = "I absolutely love this amazing library! It works perfectly."
sentiment = nlp.sentiment(text)
print(f"Sentiment: {sentiment}")  # Output: "positive"
```

### Extract Keywords

```python
# Extract keywords from article
article = """
Machine learning is transforming how we analyze data. 
Algorithms can now detect patterns in large datasets.
"""

keywords = nlp.extractKeywords(article)
print(f"Keywords: {keywords}")
# Output: ["machine learning", "algorithms", "data", "patterns"]
```

### Detect Language

```python
# Detect language of text
spanish_text = "Hola, ¿cómo estás?"
language = nlp.detectLanguage(spanish_text)
print(f"Language: {language}")  # Output: "es"
```

### Summarize Text

```python
# Summarize long text
long_text = """This is a very long article about artificial intelligence..."""

summary = nlp.summarizeSimple(long_text)
print(f"Summary: {summary}")
```

### Extract Named Entities

```python
# Extract entities from text
text = "Elon Musk founded SpaceX in 2002 in Hawthorne, California."
entities = nlp.extractEntities(text)
print(f"Entities: {entities}")
# Output: [{"name": "Elon Musk", "type": "person"}, 
#          {"name": "SpaceX", "type": "organization"}, ...]
```

### Classify Text Category

```python
# Classify text into categories
news_article = "The stock market reached new highs today..."
category = nlp.classifyCategory(news_article)
print(f"Category: {category}")  # Output: "finance"
```

## Smart Search

### Semantic Document Search

```python
from stamp.lib.ai.oaiftrs.oaiftrs import SmartSearch

search = SmartSearch()

# Search documents by meaning, not just keywords
results = search.searchByMeaning("documents/", "machine learning algorithms")
for file in results:
    print(f"Found: {file}")
```

### Find Similar Documents

```python
# Find documents similar to a reference
similar_docs = search.findSimilar("docs/", "Python programming tutorial")
print(f"Similar documents: {similar_docs}")
```

### Context-Aware Search

```python
# Search with context awareness
context_results = search.contextAwareSearch(
    "articles/",
    "data analysis",
    context=["programming", "science", "statistics"]
)
```

### Cluster Similar Documents

```python
# Group similar documents together
clusters = search.clusterSimilar("documents/")
for cluster_id, files in clusters.items():
    print(f"Cluster {cluster_id}: {files}")
```

## Optimization AI

### Detect Performance Bottlenecks

```python
from stamp.lib.ai.oaiftrs.oaiftrs import OptimizationAI

opt = OptimizationAI()

# Monitor application performance
metrics = {
    "response_time": [100, 150, 200, 250, 300, 500, 1000],
    "memory_usage": [500, 600, 700, 800, 900, 1500, 3000],
    "cpu_usage": [50, 60, 70, 80, 90, 100, 100]
}

bottlenecks = opt.detectBottlenecks(metrics)
print(f"Bottlenecks: {bottlenecks}")
```

### Get Optimization Suggestions

```python
# Get tuning suggestions
suggestions = opt.suggestTuning(metrics)
for suggestion in suggestions:
    print(f"• {suggestion}")
```

### Predict Future Load

```python
# Predict resource needs
prediction = opt.predictLoad(metrics)
print(f"Predicted load: {prediction}")
```

### Auto-Tune Parameters

```python
# Automatically optimize parameters
tuned_params = opt.autoTune(metrics)
for param, value in tuned_params.items():
    print(f"{param}: {value}")
```

## Pattern Recognition

### Detect Patterns in Data

```python
from stamp.lib.ai.oaiftrs.ptr.ptai import PatternAI

pattern = PatternAI()

# Find patterns in sequence data
sequence = [1, 2, 3, 1, 2, 3, 1, 2, 3]
detected = pattern.detectPatterns(sequence)
print(f"Patterns: {detected}")
```

### Find Anomalies

```python
# Detect anomalies in data
data = [10, 12, 11, 10, 100, 12, 11, 10]
anomalies = pattern.findAnomalies(data)
print(f"Anomalies: {anomalies}")
# Output: Indices of anomalous values
```

### Predict Next Value

```python
# Predict next value in sequence
history = [1, 2, 3, 4, 5]
next_val = pattern.predictNext(history)
print(f"Next value: {next_val}")
```

### Classify Behavior

```python
# Classify time series behavior
series = [1, 2, 3, 4, 5, 6, 7]
behavior = pattern.classifyBehavior(series)
print(f"Behavior: {behavior}")  # Output: "increasing"
```

### Detect Cycles

```python
# Find cyclical patterns
cyclic_data = [10, 20, 15, 10, 20, 15, 10, 20, 15]
cycles = pattern.detectCycles(cyclic_data)
print(f"Cycles: {cycles}")
```

### Find Bursts in Time Series

```python
# Detect bursts of activity
time_series = [5, 5, 50, 50, 50, 5, 5, 5]
bursts = pattern.findBursts(time_series)
print(f"Bursts: {bursts}")
```

## Code Intelligence

### Detect Duplicate Code

```python
from stamp.lib.ai.oaiftrs.cdi.coai import CodeAI

code = CodeAI()

# Find duplicate functions
code_samples = [
    """def calculate_sum(numbers):
        total = 0
        for num in numbers:
            total += num
        return total""",
    """def calc_sum(nums):
        s = 0
        for n in nums:
            s += n
        return s"""
]

duplicates = code.detectDuplicates(code_samples)
print(f"Duplicates found: {len(duplicates)}")
```

### Find Code Smells

```python
# Analyze code for issues
function_code = """
def get_data():
    data = []
    for i in range(100):
        item = fetch_item(i)
        data.append(item)
    return data
"""

smells = code.findSmells(function_code)
for smell in smells:
    print(f"• {smell}")
```

### Analyze Code Complexity

```python
# Calculate complexity metrics
complexity = code.analyzeComplexity(function_code)
print(f"Complexity: {complexity}")
```

### Get Refactoring Suggestions

```python
# Suggest improvements
suggestions = code.suggestRefactoring(function_code)
for suggestion in suggestions:
    print(f"• {suggestion}")
```

### Check Code Similarity

```python
# Compare two code blocks
similarity_score = code.codeSimilarity(
    code_samples[0], 
    code_samples[1]
)
print(f"Similarity: {similarity_score:.2f}")
```

### Check Line Length

```python
# Find lines exceeding limit
long_code = """very_long_line_that_exceeds_standard_limits(...)"""
long_lines = code.checkLineLength(long_code, max_length=80)
for line in long_lines:
    print(f"Line {line['line_number']}: {line['length']} chars")
```

## Data Analysis

### Detect Trends

```python
from stamp.lib.ai.oaiftrs.daz.daai import DataAnalyzer

analyzer = DataAnalyzer()

# Find trend in data
sales_data = [100, 110, 120, 130, 140, 150]
trend = analyzer.detectTrends(sales_data)
print(f"Trend: {trend}")
```

### Find Outliers

```python
# Detect anomalous values
data = [10, 12, 11, 10, 100, 12, 11]
outliers = analyzer.findOutliers(data)
print(f"Outliers: {outliers}")
```

### Statistical Summary

```python
# Get comprehensive statistics
stats = analyzer.statisticalSummary(data)
for key, value in stats.items():
    print(f"{key}: {value}")
# Output: mean, median, std, min, max, etc.
```

### Visualization Suggestions

```python
# Get visualization recommendations
time_series = [50, 52, 55, 53, 58, 60, 62, 65]
suggestions = analyzer.visualizeSuggestions(time_series)
for suggestion in suggestions:
    print(f"• {suggestion}")
```

### Correlate Features

```python
# Calculate correlation between datasets
feature1 = [1, 2, 3, 4, 5]
feature2 = [2, 4, 6, 8, 10]
correlation = analyzer.correlateFeatures(feature1, feature2)
print(f"Correlation: {correlation:.2f}")
```

### Detect Seasonality

```python
# Find seasonal patterns
seasonal_data = [10, 20, 15, 25, 10, 20, 15, 25, 10, 20, 15, 25]
seasonality = analyzer.detectSeasonality(seasonal_data)
print(f"Seasonality: {seasonality}")
```

## Machine Learning Predictions

### Train Classification Model

```python
from stamp.lib.ai.oaiftrs.prd.prai import PredictSystem, ModelType

predictor = PredictSystem()

# Prepare training data
training_data = [
    {"features": [5.1, 3.5, 1.4], "label": "setosa"},
    {"features": [4.9, 3.0, 1.4], "label": "setosa"},
    {"features": [7.0, 3.2, 4.7], "label": "versicolor"},
    {"features": [6.4, 3.2, 4.5], "label": "versicolor"}
]

# Train model
model_id = predictor.train(training_data, ModelType.CLASSIFIER)
print(f"Model trained: {model_id}")
```

### Make Predictions

```python
# Predict with trained model
test_features = [
    [5.0, 3.4, 1.5],
    [6.5, 3.0, 5.5]
]

predictions = predictor.predict(model_id, test_features)
print(f"Predictions: {predictions}")
```

### Classify Data

```python
# Classify new data
classifications = predictor.classify(model_id, test_features)
for i, classification in enumerate(classifications):
    print(f"Sample {i}: {classification}")
```

### Evaluate Model Performance

```python
# Evaluate model accuracy
test_labels = ["setosa", "versicolor"]
metrics = predictor.evaluate(model_id, test_features, test_labels)
print(f"Metrics: {metrics}")
```

### Train Regression Model

```python
# Train regression model
regression_data = [
    {"features": [1, 2], "label": 3},
    {"features": [2, 3], "label": 5},
    {"features": [3, 4], "label": 7}
]

reg_model_id = predictor.train(regression_data, ModelType.REGRESSOR)
predictions = predictor.predict(reg_model_id, [[4, 5]])
print(f"Regression prediction: {predictions}")
```

## Security Intelligence

### Detect Malicious Patterns

```python
from stamp.lib.ai.oaiftrs.sec.sai import SecurityAI

security = SecurityAI()

# Analyze logs for threats
log_entries = [
    "Normal user login: john_doe",
    "SELECT * FROM users WHERE '1'='1'",
    "User uploaded: document.pdf",
    "rm -rf /var/www/html"
]

threats = security.detectMalicious(log_entries)
for threat in threats:
    print(f"⚠️ Threat detected: {threat}")
```

### Analyze Anomaly Score

```python
# Calculate anomaly score
current = {"requests_per_minute": 1000, "avg_response": 500}
baseline = {"requests_per_minute": 50, "avg_response": 200}

score = security.analyzeAnomalyScore(current, baseline)
print(f"Anomaly score: {score}")
```

### Identify Threat Type

```python
# Classify threat type
threat_input = "rm -rf /var/www/html"
threat_type = security.identifyThreatType(threat_input)
print(f"Threat type: {threat_type}")
```

### Predict Attack Probability

```python
# Predict likelihood of attack
pattern = {
    "login_attempts": 15,
    "failed_logins": 12,
    "location": "unknown"
}

probability = security.predictAttackProbability(pattern)
print(f"Attack probability: {probability:.2%}")
```

### Get Mitigation Suggestions

```python
# Get security recommendations
attack = {"type": "brute_force", "source_ip": "192.168.1.100"}
mitigations = security.suggestMitigation(attack)
for mitigation in mitigations:
    print(f"• {mitigation}")
```

### Score Threat Severity

```python
# Assess threat severity
threat = {"type": "sql_injection", "attempts": 5}
severity = security.scoreThreatSeverity(threat)
print(f"Severity: {severity}/10")
```

## Advanced Examples

### Complete Analysis Pipeline

```python
from stamp.lib.ai.oaiftrs.oaiftrs import NLPText
from stamp.lib.ai.oaiftrs.daz.daai import DataAnalyzer

# Analyze customer reviews
reviews = [
    "This product is amazing! Love it!",
    "Terrible quality, disappointed.",
    "Average product, nothing special."
]

# Sentiment analysis
nlp = NLPText()
sentiments = [nlp.sentiment(review) for review in reviews]

# Convert to numeric for analysis
sentiment_scores = [1 if s == "positive" else -1 if s == "negative" else 0 
                    for s in sentiments]

# Analyze distribution
analyzer = DataAnalyzer()
stats = analyzer.statisticalSummary(sentiment_scores)
print(f"Review analysis: {stats}")
```

### Code Quality Pipeline

```python
from stamp.lib.ai.oaiftrs.cdi.coai import CodeAI
import os

# Analyze all Python files
code = CodeAI()
total_issues = 0

for root, _, files in os.walk("src"):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file)) as f:
                content = f.read()
            
            # Check for issues
            smells = code.findSmells(content)
            long_lines = code.checkLineLength(content, max_length=100)
            
            if smells or long_lines:
                print(f"\n{file}:")
                for smell in smells:
                    print(f"  • {smell}")
                for line in long_lines:
                    print(f"  • Line {line['line_number']} too long")
                total_issues += len(smells) + len(long_lines)

print(f"\nTotal issues: {total_issues}")
```

## Testing

Run the test suite to verify AI features:

```bash
python tests/ai/oaiftrs/oaiftest.py      # Main AI features
python tests/ai/oaiftrs/ptr/ptaitest.py  # Pattern recognition
python tests/ai/oaiftrs/cdi/coaitest.py  # Code intelligence
python tests/ai/oaiftrs/daz/daaitest.py  # Data analysis
python tests/ai/oaiftrs/prd/praitest.py  # ML predictions
python tests/ai/oaiftrs/sec/saitest.py  # Security intelligence
```

## See Also

- [AI API Reference](../api/ai.md)
- [Testing Guide](../../tests/ai/oaiftrs/)
