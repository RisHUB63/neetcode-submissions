class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        diff = len(heights) - 1

        max_water = 0

        while start < end:
            to_be = heights[start] if heights[end] >= heights[start] else heights[end]
            max_water = max(max_water, (to_be * diff))

            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
            diff -= 1
        
        return max_water
            