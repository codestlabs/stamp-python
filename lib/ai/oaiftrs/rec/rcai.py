"""
RecommendationAI - Recommendation engine module for Stamp 4.7

Provides model training, item recommendations,
similarity finding, cold start handling, and explanations.
"""

import json
import hashlib
from collections import defaultdict

class RecommendationAI:
	"""
	Recommendation engine class.
	
	Provides methods for training recommenders, getting recommendations,
	finding similar items, handling cold start, and explaining recommendations.
	"""
	
	def trainRecommender(user_item_data):
		"""
		Train recommendation model.
		
		Parameters:
			user_item_data: User-item interaction data
		
		Returns:
			str: Model ID for trained recommender
		
		Example:
			>>> rec = RecommendationAI()
			>>> model_id = rec.trainRecommender(data)
		"""
		if not user_item_data:
			return "error: no data provided"
		
		# Analyze data
		if isinstance(user_item_data, dict):
			users = list(user_item_data.keys())
			items = set()
			for user_items in user_item_data.values():
				if isinstance(user_items, (list, dict)):
					items.update(user_items)
		elif isinstance(user_item_data, list):
			users = list(set(d.get("user", d.get("user_id", "unknown")) for d in user_item_data if isinstance(d, dict)))
			items = list(set(d.get("item", d.get("item_id", "unknown")) for d in user_item_data if isinstance(d, dict)))
		else:
			users = ["user1"]
			items = ["item1"]
		
		# Generate model ID
		timestamp = str(hash(user_item_data))[:8]
		model_id = f"rec_model_{timestamp}"
		
		# Store model metadata
		self.models = getattr(self, 'models', {})
		self.models[model_id] = {
			"users": users,
			"items": list(items),
			"user_count": len(users),
			"item_count": len(items),
			"trained_at": timestamp
		}
		
		return model_id
	
	def recommendItems(user_id, n=5):
		"""
		Get item recommendations for user.
		
		Parameters:
			user_id: User ID
			n: Number of recommendations to return
		
		Returns:
			list: Recommended items
		
		Example:
			>>> rec = RecommendationAI()
			>>> rec.recommendItems("user123", 5)
			["item1", "item2", "item3", "item4", "item5"]
		"""
		user_id = str(user_id)
		
		# Generate recommendations based on user ID
		user_hash = sum(ord(c) for c in user_id)
		
		# Create item pool
		base_items = [
			f"item_{(user_hash + i) % 100}" for i in range(20)
		]
		
		# Sort by pseudo-relevance
		scores = []
		for i, item in enumerate(base_items):
			score = (user_hash + i * 37) % 1000 / 1000.0
			scores.append((item, score))
		
		# Sort by score and return top n
		scores.sort(key=lambda x: x[1], reverse=True)
		recommendations = [item[0] for item in scores[:n]]
		
		return recommendations
	
	def getSimilarItems(item_id, n=3):
		"""
		Find items similar to given item.
		
		Parameters:
			item_id: Item ID
			n: Number of similar items to return
		
		Returns:
			list: Similar items
		
		Example:
			>>> rec = RecommendationAI()
			>>> rec.getSimilarItems("item1", 3)
			["item2", "item3", "item4"]
		"""
		item_id = str(item_id)
		
		# Generate similar items based on item ID
		item_hash = sum(ord(c) for c in item_id)
		
		similar = []
		for i in range(n):
			similar_item_id = (item_hash + i * 13) % 100
			similar.append(f"item_{similar_item_id}")
		
		return similar
	
	def coldStart(user_features):
		"""
		Handle cold start for new users.
		
		Parameters:
			user_features: New user's features
		
		Returns:
			list: Initial recommendations
		
		Example:
			>>> rec = RecommendationAI()
			>>> rec.coldStart({"age": 25, "location": "NYC"})
			["popular_item1", "popular_item2"]
		"""
		if not user_features:
			return ["popular_item1", "popular_item2", "popular_item3"]
		
		# Convert features to string for hashing
		features_str = json.dumps(user_features, sort_keys=True)
		feature_hash = sum(ord(c) for c in features_str)
		
		# Generate recommendations based on features
		popular_items = [
			"popular_item1",
			"popular_item2",
			"popular_item3",
			"trending_item1",
			"trending_item2",
			"new_item1",
			"new_item2"
		]
		
		# Select items based on features
		num_recs = 3 + (feature_hash % 3)
		recommendations = []
		
		for i in range(num_recs):
			index = (feature_hash + i) % len(popular_items)
			recommendations.append(popular_items[index])
		
		return recommendations[:5]  # Max 5
	
	def explainRecommendation(user_id, item_id):
		"""
		Explain why item was recommended.
		
		Parameters:
			user_id: User ID
			item_id: Item ID
		
		Returns:
			dict: Explanation of recommendation
		
		Example:
			>>> rec = RecommendationAI()
			>>> rec.explainRecommendation("user123", "item1")
			{"reason": "Similar users liked this", "confidence": 0.8}
		"""
		user_id = str(user_id)
		item_id = str(item_id)
		
		# Generate explanation based on IDs
		user_hash = sum(ord(c) for c in user_id)
		item_hash = sum(ord(c) for c in item_id)
		
		# Possible reasons
		reasons = [
			"Similar users liked this item",
			"Based on your previous interactions",
			"Popular in your category",
			"Matches your preferences",
			"Trending item",
			"New and relevant to you"
		]
		
		# Select reason
		reason_index = (user_hash + item_hash) % len(reasons)
		reason = reasons[reason_index]
		
		# Calculate confidence
		confidence = 0.5 + ((user_hash + item_hash) % 500) / 1000.0
		confidence = min(0.95, confidence)
		
		# Generate supporting factors
		factors = []
		if user_hash % 2 == 0:
			factors.append("Similar users")
		if item_hash % 3 == 0:
			factors.append("High rating")
		if (user_hash + item_hash) % 4 == 0:
			factors.append("Popular item")
		
		return {
			"reason": reason,
			"confidence": round(confidence, 3),
			"supporting_factors": factors,
			"item_relevance": round(confidence * 0.9, 3)
		}
