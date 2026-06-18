class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [height[0]]
        postfix_max = [0] * len(height)
        postfix_max[len(height)-1] = height[len(height)-1]

        for i in range(1, len(height)):
            prefix_max.append(max(prefix_max[len(prefix_max) - 1], height[i]))
        
        for i in range(len(height) - 2, -1, -1):
            postfix_max[i] = (max(postfix_max[i+1], height[i]))
        
        answer = 0

        for i in range(0, len(height)):
            if height[i] < prefix_max[i] and height[i] < postfix_max[i]:
                answer += min(prefix_max[i], postfix_max[i]) - height[i]

        return answer
