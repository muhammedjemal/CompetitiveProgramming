class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:

		frequency = {}

		for num in nums:

			if num not in frequency:

				frequency[num] = 1

			else:

				frequency[num] = frequency[num] + 1

		frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

		result = list(frequency.keys())[:k]

		return result
