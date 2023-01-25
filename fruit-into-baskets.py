class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        j = 0
        ans = 0
        dictionary = {}

        for idx,fruit in enumerate(fruits):
            dictionary[fruit] = idx
            if len(dictionary) > 2:
                old= min(dictionary.values())
                del dictionary[fruits[old]]
                j = old+ 1
            ans = max(ans, idx - j + 1)

        return ans
