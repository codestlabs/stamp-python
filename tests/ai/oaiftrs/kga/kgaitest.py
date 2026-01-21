print("""
Tests for KnowledgeGraphAI module (Stamp 4.7)

Required test files:
- No external files needed (uses synthetic graph data)
""")

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../..'))

from lib.ai.oaiftrs.kga.kgai import KnowledgeGraphAI

def test_buildGraph():
	"""Test graph building"""
	print("Running test_buildGraph")
	entities = ["A", "B", "C"]
	relationships = [("A", "knows", "B"), ("B", "knows", "C")]
	result = KnowledgeGraphAI.buildGraph(entities, relationships)
	print(f"Result: {result}")
	assert isinstance(result, dict)

def test_queryGraph():
	"""Test graph querying"""
	print("Running test_queryGraph")
	graph = {"nodes": ["A", "B"], "edges": []}
	result = KnowledgeGraphAI.queryGraph(graph, "find all")
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_findShortestPath():
	"""Test shortest path finding"""
	print("Running test_findShortestPath")
	graph = {"nodes": ["A", "B", "C"], "edges": [{"source": "A", "target": "B"}, {"source": "B", "target": "C"}]}
	result = KnowledgeGraphAI.findShortestPath(graph, "A", "C")
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_recommendConnections():
	"""Test connection recommendations"""
	print("Running test_recommendConnections")
	graph = {"nodes": ["A", "B", "C", "D"], "edges": [{"source": "A", "target": "B"}]}
	result = KnowledgeGraphAI.recommendConnections(graph, "A")
	print(f"Result: {result}")
	assert isinstance(result, list)

def test_detectCommunities():
	"""Test community detection"""
	print("Running test_detectCommunities")
	graph = {"nodes": ["A", "B", "C", "D"], "edges": [{"source": "A", "target": "B"}, {"source": "C", "target": "D"}]}
	result = KnowledgeGraphAI.detectCommunities(graph)
	print(f"Result: {result}")
	assert isinstance(result, dict)

if __name__ == "__main__":
	print("\n=== Testing KnowledgeGraphAI module ===")
	print("No external files needed\n")
	
	try:
		test_buildGraph()
		test_queryGraph()
		test_findShortestPath()
		test_recommendConnections()
		test_detectCommunities()
		print("\n✓ All KnowledgeGraphAI tests passed!")
	except AssertionError as e:
		print(f"\n✗ Test failed: {e}")
	except Exception as e:
		print(f"\n✗ Error: {e}")
