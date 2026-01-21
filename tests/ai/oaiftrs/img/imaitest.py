print("""
Tests for ImageAI module (Stamp 4.7)

Required test files:
- test.jpg: A test image file for classification, object detection, feature extraction, face detection, and quality analysis
- img1.jpg: First image for comparison test
- img2.jpg: Second image for comparison test
"""
)
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../..'))

from lib.ai.oaiftrs.img.imai import ImageAI

def test_classifyImage():
	"""Test image classification - needs: test.jpg"""
	print("Running test_classifyImage - needs: test.jpg")
	result = ImageAI.classifyImage("test.jpg")
	print(f"Result: {result}")
	assert result is not None

def test_detectObjects():
	"""Test object detection - needs: test.jpg"""
	print("Running test_detectObjects - needs: test.jpg")
	result = ImageAI.detectObjects("test.jpg")
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_extractFeatures():
	"""Test feature extraction - needs: test.jpg"""
	print("Running test_extractFeatures - needs: test.jpg")
	result = ImageAI.extractFeatures("test.jpg")
	print(f"Result: {result}")
	assert isinstance(result, dict)

def test_compareImages():
	"""Test image comparison - needs: img1.jpg, img2.jpg"""
	print("Running test_compareImages - needs: img1.jpg, img2.jpg")
	result = ImageAI.compareImages("img1.jpg", "img2.jpg")
	print(f"Result: {result}")
	assert isinstance(result, float)

def test_detectFaces():
	"""Test face detection - needs: test.jpg"""
	print("Running test_detectFaces - needs: test.jpg")
	result = ImageAI.detectFaces("test.jpg")
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_analyzeQuality():
	"""Test quality analysis - needs: test.jpg"""
	print("Running test_analyzeQuality - needs: test.jpg")
	result = ImageAI.analyzeQuality("test.jpg")
	print(f"Result: {result}")
	assert isinstance(result, dict)

if __name__ == "__main__":
	print("\n=== Testing ImageAI module ===")
	print("Required test files: test.jpg, img1.jpg, img2.jpg\n")
	
	try:
		test_classifyImage()
		test_detectObjects()
		test_extractFeatures()
		test_compareImages()
		test_detectFaces()
		test_analyzeQuality()
		print("\n✓ All ImageAI tests passed!")
	except AssertionError as e:
		print(f"\n✗ Test failed: {e}")
	except Exception as e:
		print(f"\n✗ Error: {e}")
		print("Make sure required test files exist in the test directory")
