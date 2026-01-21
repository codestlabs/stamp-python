"""
KnowledgeGraphAI - Knowledge graph module for Stamp 4.7

Provides graph building, querying, path finding,
connection recommendations, and community detection.
"""

import json
import hashlib

class KnowledgeGraphAI:
	"""
	Knowledge graph class.
	
	Provides methods for building knowledge graphs, querying,
	finding paths, recommending connections, and detecting communities.
	"""
	
	def buildGraph(entities, relationships):
		"""
		Build knowledge graph from entities and relationships.
		
		Parameters:
			entities: List of entities
			relationships: List of relationships between entities
		
		Returns:
			dict: Graph structure
		
		Example:
			>>> kg = KnowledgeGraphAI()
			>>> kg.buildGraph(["A", "B"], [("A", "knows", "B")])
			{"nodes": ["A", "B"], "edges": [...]}
		"""
		if not entities:
			return {"error": "no entities provided"}
		
		# Build graph structure
		graph = {
			"nodes": list(entities) if isinstance(entities, list) else [str(entities)],
			"edges": [],
			"node_count": len(entities) if isinstance(entities, list) else 1,
			"edge_count": 0
		}
		
		# Add relationships
		if relationships:
			if isinstance(relationships, list):
				for rel in relationships:
					if len(rel) >= 3:
						graph["edges"].append({
							"source": str(rel[0]),
							"target": str(rel[1]),
							"relation": str(rel[2]),
							"weight": float(rel[3]) if len(rel) > 3 else 1.0
						})
			else:
				graph["edges"].append({
					"source": str(relationships[0]) if len(relationships) > 0 else "unknown",
					"target": str(relationships[1]) if len(relationships) > 1 else "unknown",
					"relation": str(relationships[2]) if len(relationships) > 2 else "related"
				})
			
			graph["edge_count"] = len(graph["edges"])
		
		# Generate graph ID
		graph_str = json.dumps(graph, sort_keys=True)
		graph_hash = hashlib.md5(graph_str.encode()).hexdigest()[:8]
		graph["graph_id"] = f"graph_{graph_hash}"
		
		return graph
	
	def queryGraph(graph, query):
		"""
		Query knowledge graph.
		
		Parameters:
			graph: Graph structure
			query: Query string or pattern
		
		Returns:
			list: Query results
		
		Example:
			>>> kg = KnowledgeGraphAI()
			>>> kg.queryGraph(graph, "find all people")
			["Alice", "Bob"]
		"""
		if not graph or not query:
			return []
		
		# Check if graph has nodes
		if "nodes" not in graph:
			return []
		
		query_lower = query.lower()
		results = []
		
		# Simple pattern matching
		for node in graph["nodes"]:
			node_str = str(node).lower()
			
			# Check for various query patterns
			if "all" in query_lower or "find" in query_lower:
				results.append(node)
			elif node_str in query_lower:
				results.append(node)
		
		# Also check edges
		if "edges" in graph:
			for edge in graph["edges"]:
				edge_str = f"{edge.get('source', '')} {edge.get('relation', '')} {edge.get('target', '')}".lower()
				if any(word in edge_str for word in query_lower.split()):
					results.append(f"{edge['source']} -> {edge['target']}")
		
		return list(set(results))  # Remove duplicates
	
	def findShortestPath(graph, start, end):
		"""
		Find shortest path between two entities.
		
		Parameters:
			graph: Graph structure
			start: Starting entity
			end: Ending entity
		
		Returns:
			list: Path from start to end
		
		Example:
			>>> kg = KnowledgeGraphAI()
			>>> kg.findShortestPath(graph, "A", "C")
			["A", "B", "C"]
		"""
		if not graph or not start or not end:
			return []
		
		if "nodes" not in graph or "edges" not in graph:
			return []
		
		start = str(start)
		end = str(end)
		
		# Build adjacency list
		adj = {node: [] for node in graph["nodes"]}
		for edge in graph["edges"]:
			source = edge.get("source")
			target = edge.get("target")
			if source in adj and target in adj:
				adj[source].append(target)
				adj[target].append(source)  # Undirected
		
		# BFS to find shortest path
		from collections import deque
		queue = deque([[start]])
		visited = set([start])
		
		while queue:
			path = queue.popleft()
			node = path[-1]
			
			if node == end:
				return path
			
			for neighbor in adj.get(node, []):
				if neighbor not in visited:
					visited.add(neighbor)
					new_path = list(path)
					new_path.append(neighbor)
					queue.append(new_path)
		
		return []  # No path found
	
	def recommendConnections(graph, entity):
		"""
		Recommend connections for an entity.
		
		Parameters:
			graph: Graph structure
			entity: Entity to get recommendations for
		
		Returns:
			list: Recommended connections
		
		Example:
			>>> kg = KnowledgeGraphAI()
			>>> kg.recommendConnections(graph, "Alice")
			["Bob", "Charlie", "David"]
		"""
		if not graph or not entity:
			return []
		
		if "nodes" not in graph or "edges" not in graph:
			return []
		
		entity = str(entity)
		
		# Find existing connections
		connections = set()
		for edge in graph["edges"]:
			if edge.get("source") == entity:
				connections.add(edge.get("target"))
			elif edge.get("target") == entity:
				connections.add(edge.get("source"))
		
		# Find friends of friends
		recommendations = {}
		for edge in graph["edges"]:
			source = edge.get("source")
			target = edge.get("target")
			
			if source in connections and target != entity and target not in connections:
				recommendations[target] = recommendations.get(target, 0) + 1
			if target in connections and source != entity and source not in connections:
				recommendations[source] = recommendations.get(source, 0) + 1
		
		# Sort by score
		sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
		
		return [rec[0] for rec in sorted_recs[:5]]  # Top 5
	
	def detectCommunities(graph):
		"""
		Detect communities in graph.
		
		Parameters:
			graph: Graph structure
		
		Returns:
			dict: Communities detected
		
		Example:
			>>> kg = KnowledgeGraphAI()
			>>> kg.detectCommunities(graph)
			{"community1": ["A", "B"], "community2": ["C", "D"]}
		"""
		if not graph or "nodes" not in graph:
			return {}
		
		# Simple community detection based on connectivity
		if "edges" not in graph or not graph["edges"]:
			# No edges, each node is its own community
			communities = {}
			for i, node in enumerate(graph["nodes"]):
				communities[f"community_{i+1}"] = [node]
			return communities
		
		# Build adjacency list
		adj = {node: [] for node in graph["nodes"]}
		for edge in graph["edges"]:
			source = edge.get("source")
			target = edge.get("target")
			if source in adj and target in adj:
				adj[source].append(target)
				adj[target].append(source)
		
		# Find connected components (communities)
		visited = set()
		communities = {}
		community_id = 1
		
		for node in graph["nodes"]:
			if node not in visited:
				# BFS to find all connected nodes
				component = []
				queue = [node]
				visited.add(node)
				
				while queue:
					current = queue.pop(0)
					component.append(current)
					
					for neighbor in adj.get(current, []):
						if neighbor not in visited:
							visited.add(neighbor)
							queue.append(neighbor)
				
				communities[f"community_{community_id}"] = component
				community_id += 1
		
		return communities
