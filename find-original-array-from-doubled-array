class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        data = Counter(changed)
        result = []
        for k in sorted(data):
            if data[k] < 0:
                return []
            elif k == 0:
                x, y = divmod(data[k], 2)
                if y == 1:
                    return []
                result += [0] * x
            elif data[k] > 0:
                value = k * 2
                if data[value] == 0:
                    return []
                min_value = min(value, data[k])
                result += [k] * min_value
                data[k] -= min_value
                data[value] -= min_value
        return result
