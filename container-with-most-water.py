class Solution:
    def maxArea(self, height: list[int]) -> int:
        lst =[]
        start = 0
        end = len(height)-1

        while start < end:
            width = end - start
            height1 = min(height[start], height[end])
            area = width * height1
            lst.append(area)
            
            if height1 == height[start]:
                start += 1
            elif height1 == height [end]:
                end-=1
        return max(lst)
