
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        size = len(citations)
        citations.sort()

        if len(citations) == 1 and citations[0] != 0:
            return 1
        else:
            while size>0:
                temp = len(citations)-size
                if citations[temp]>=size:
                    return size
                size-=1
        return 0
