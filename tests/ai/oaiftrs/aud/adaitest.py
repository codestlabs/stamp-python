print("""
Tests for AudioAI module (Stamp 4.7)

Required test files:
- test.wav: A test audio file for transcription, language detection, sentiment analysis, and feature extraction
- speech.wav: Speech file for speaker identification
- noise.wav: Audio file with noise for noise detection
""")

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../..'))

from lib.ai.oaiftrs.aud.adai import AudioAI

def test_transcribeAudio():
	"""Test speech transcription - needs: test.wav"""
	print("Running test_transcribeAudio - needs: test.wav")
	result = AudioAI.transcribeAudio("test.wav")
	print(f"Result: {result}")
	assert isinstance(result, str)

def test_detectLanguage():
	"""Test language detection - needs: test.wav"""
	print("Running test_detectLanguage - needs: test.wav")
	result = AudioAI.detectLanguage("test.wav")
	print(f"Result: {result}")
	assert isinstance(result, str)

def test_analyzeSentiment():
	"""Test sentiment analysis - needs: test.wav"""
	print("Running test_analyzeSentiment - needs: test.wav")
	result = AudioAI.analyzeSentiment("test.wav")
	print(f"Result: {result}")
	assert result in ["positive", "negative", "neutral"]

def test_extractFeatures():
	"""Test feature extraction - needs: test.wav"""
	print("Running test_extractFeatures - needs: test.wav")
	result = AudioAI.extractFeatures("test.wav")
	print(f"Result: {result}")
	assert isinstance(result, dict)

def test_identifySpeakers():
	"""Test speaker identification - needs: speech.wav"""
	print("Running test_identifySpeakers - needs: speech.wav")
	result = AudioAI.identifySpeakers("speech.wav")
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_detectNoise():
	"""Test noise detection - needs: noise.wav"""
	print("Running test_detectNoise - needs: noise.wav")
	result = AudioAI.detectNoise("noise.wav")
	print(f"Result: {result}")
	assert isinstance(result, dict)

if __name__ == "__main__":
	print("\n=== Testing AudioAI module ===")
	print("Required test files: test.wav, speech.wav, noise.wav\n")
	
	try:
		test_transcribeAudio()
		test_detectLanguage()
		test_analyzeSentiment()
		test_extractFeatures()
		test_identifySpeakers()
		test_detectNoise()
		print("\n✓ All AudioAI tests passed!")
	except AssertionError as e:
		print(f"\n✗ Test failed: {e}")
	except Exception as e:
		print(f"\n✗ Error: {e}")
		print("Make sure required test files exist in test directory")
