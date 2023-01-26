class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        size = len(heights)-1
        for i in range(size):
            if heights[i] >= heights[i+1]:
                continue        
            else: 
                heapq.heappush(heap, heights [i+1]-heights[i])
                if ladders<len(heap):
                    bricks -= heapq.heappop(heap)
                    if bricks < 0:
                        return i
                
        return  size
