class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 0
        for k, g in groupby(chars):
            chars[i] = k
            i += 1
            len_g = len(list(g))
            if len_g > 1:
                for num in str(len_g):
                    chars[i] = num
                    i += 1
        return i
