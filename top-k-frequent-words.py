class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = collections.defaultdict(int)
        for word in words:
            d[str(word)] += 1

        return [i[0] for i in sorted(d.items(), key = lambda x : (-x[1], x[0]))[:k]] 
