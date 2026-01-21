print("""
Tests for QuantizerAI module (Stamp 4.7)

Required test files:
- No external files needed (uses synthetic model data)
""")

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))

from lib.ai.oaiftrs.qzr.quzr import QuantizerAI

def test_quantizeModel():
	"""Test model quantization"""
	print("Running test_quantizeModel")
	model = {"weights": [1, 2, 3, 4, 5]}
	result = QuantizerAI.quantizeModel(model, 8)
	print(f"Result: {result}")
	assert isinstance(result, dict)
	assert "model_id" in result

def test_dequantizeModel():
	"""Test model dequantization"""
	print("Running test_dequantizeModel")
	quantized = {"model_id": "quant_123", "bits": 8}
	result = QuantizerAI.dequantizeModel(quantized)
	print(f"Result: {result}")
	assert isinstance(result, dict)
	assert "model_id" in result

def test_compareModels():
	"""Test model comparison"""
	print("Running test_compareModels")
	original = {"weights": [1, 2, 3, 4, 5]}
	quantized = {"weights": [1, 2, 3, 4, 5]}
	test_data = [1, 2, 3]
	result = QuantizerAI.compareModels(original, quantized, test_data)
	print(f"Result: {result}")
	assert isinstance(result, dict)

def test_optimizeForDeployment():
	"""Test deployment optimization"""
	print("Running test_optimizeForDeployment")
	model = {"weights": [1, 2, 3, 4, 5]}
	result = QuantizerAI.optimizeForDeployment(model, "mobile")
	print(f"Result: {result}")
	assert isinstance(result, dict)
	assert "deployment_ready" in result

def test_estimateSizeReduction():
	"""Test size reduction estimation"""
	print("Running test_estimateSizeReduction")
	model = {"weights": [1, 2, 3, 4, 5]}
	result = QuantizerAI.estimateSizeReduction(model, 8)
	print(f"Result: {result}")
	assert isinstance(result, dict)
	assert "savings_percent" in result

def test_validateAccuracy():
	"""Test accuracy validation"""
	print("Running test_validateAccuracy")
	original = {"weights": [1, 2, 3, 4, 5]}
	quantized = {"weights": [1, 2, 3, 4, 5]}
	test_data = [1, 2, 3]
	result = QuantizerAI.validateAccuracy(original, quantized, test_data)
	print(f"Result: {result}")
	assert isinstance(result, dict)
	assert "pass" in result

if __name__ == "__main__":
	print("\n=== Testing QuantizerAI module ===")
	print("No external files needed\n")
	
	try:
		test_quantizeModel()
		test_dequantizeModel()
		test_compareModels()
		test_optimizeForDeployment()
		test_estimateSizeReduction()
		test_validateAccuracy()
		print("\n✓ All QuantizerAI tests passed!")
	except AssertionError as e:
		print(f"\n✗ Test failed: {e}")
	except Exception as e:
		print(f"\n✗ Error: {e}")
