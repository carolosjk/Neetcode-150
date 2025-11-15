class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights) - 1
        max_vol = 0

        while i < j:
            height = min(heights[i],heights[j])
            width = j-i
            vol = height * width
            max_vol = max(max_vol,vol)

            if heights[i] < heights[j]:
                i +=1
            else:
                j -= 1
        
        return max_vol
        