class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counts = Counter(arr)
        result, constant = 0, (10 ** 9 + 7)
        for i in range(101):
            if counts[i] == 0:
                continue 
            j, k = i, 100
            while j <= k:
                if j + k > target - i:
                    k -= 1
                    
                elif j + k < target - i:
                    j += 1
                    
                else:
                    if i == j == k:
                        result += counts[i] * (counts[i] - 1) * (counts[i] - 2) // 6
                        
                    elif i == j:
                        result += counts[i] * (counts[i] - 1) * counts[k] // 2
                        
                    elif j == k:
                        result += counts[i] * counts[j] * (counts[j] - 1) // 2
                        
                    else:
                        result += counts[i] * counts[j] * counts[k]
                    j += 1
                    k -= 1
                    
        return result % constant
