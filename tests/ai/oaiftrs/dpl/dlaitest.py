print("""
Tests for DeepLearningAI module (Stamp 4.7)

Required test files:
- No external files needed (uses synthetic data)
""")

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../..'))

from lib.ai.oaiftrs.dpl.dlai import DeepLearningAI

def test_trainDeepModel():
	"""Test model training"""
	print("Running test_trainDeepModel")
	data = [{"x": 1, "y": 2}, {"x": 2, "y": 4}]
	result = DeepLearningAI.trainDeepModel(data, "cnn")
	print(f"Result: {result}")
	assert isinstance(result, str)

def test_predictDeep():
	"""Test prediction"""
	print("Running test_predictDeep")
	result = DeepLearningAI.predictDeep("model_123", [1, 2, 3])
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_exportModel():
	"""Test model export"""
	print("Running test_exportModel")
	result = DeepLearningAI.exportModel("model_123", "test_model.pkl")
	print(f"Result: {result}")
	assert isinstance(result, bool)

def test_importModel():
	"""Test model import"""
	print("Running test_importModel")
	result = DeepLearningAI.importModel("test_model.pkl")
	print(f"Result: {result}")
	assert isinstance(result, str)

def test_hyperparameterTune():
	"""Test hyperparameter tuning"""
	print("Running test_hyperparameterTune")
	data = [1, 2, 3, 4, 5]
	result = DeepLearningAI.hyperparameterTune(data)
	print(f"Result: {result}")
	assert isinstance(result, dict)

def test_transferLearn():
	"""Test transfer learning"""
	print("Running test_transferLearn")
	result = DeepLearningAI.transferLearn("base_model", [1, 2, 3])
	print(f"Result: {result}")
	assert isinstance(result, str)

if __name__ == "__main__":
	print("\n=== Testing DeepLearningAI module ===")
	print("No external files needed\n")
	
	try:
		test_trainDeepModel()
		test_predictDeep()
		test_exportModel()
		test_importModel()
		test_hyperparameterTune()
		test_transferLearn()
		print("\n✓ All DeepLearningAI tests passed!")
	except AssertionError as e:
		print(f"\n✗ Test failed: {e}")
	except Exception as e:
		print(f"\n✗ Error: {e}")
