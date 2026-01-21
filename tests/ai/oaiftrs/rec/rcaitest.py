print("""
Tests for RecommendationAI module (Stamp 4.7)

Required test files:
- No external files needed (uses synthetic user-item data)
""")

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../..'))

from lib.ai.oaiftrs.rec.rcai import RecommendationAI

def test_trainRecommender():
	"""Test recommender training"""
	print("Running test_trainRecommender")
	data = {"user1": ["item1", "item2"], "user2": ["item2", "item3"]}
	result = RecommendationAI.trainRecommender(data)
	print(f"Result: {result}")
	assert isinstance(result, str)

def test_recommendItems():
	"""Test item recommendations"""
	print("Running test_recommendItems")
	result = RecommendationAI.recommendItems("user123", 5)
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_getSimilarItems():
	"""Test similar items"""
	print("Running test_getSimilarItems")
	result = RecommendationAI.getSimilarItems("item1", 3)
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_coldStart():
	"""Test cold start handling"""
	print("Running test_coldStart")
	features = {"age": 25, "location": "NYC"}
	result = RecommendationAI.coldStart(features)
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_explainRecommendation():
	"""Test recommendation explanation"""
	print("Running test_explainRecommendation")
	result = RecommendationAI.explainRecommendation("user123", "item1")
	print(f"Result: {result}")
	assert isinstance(result, dict)

if __name__ == "__main__":
	print("\n=== Testing RecommendationAI module ===")
	print("No external files needed\n")
	
	try:
		test_trainRecommender()
		test_recommendItems()
		test_getSimilarItems()
		test_coldStart()
		test_explainRecommendation()
		print("\n✓ All RecommendationAI tests passed!")
	except AssertionError as e:
		print(f"\n✗ Test failed: {e}")
	except Exception as e:
		print(f"\n✗ Error: {e}")
