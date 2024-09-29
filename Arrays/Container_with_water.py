# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


#brute-force
# class Solution:
#     def maxArea(self, height:list[int]) -> int:
#         self.height=height
#         area_max=0
#         for index in range(len(height)-1):
#             for i in range(1,len(height)):
#                 if height[index] > height[i]:
#                     area=height[i]*(i-index)
#                 else:
#                     area=height[index]*(i-index)
#                 if area_max<area:
#                     area_max=area
#         return area_max
    
# heights=eval(input())
# area=Solution().maxArea(heights)
# print(area)

#Two-pointer technique
class Solution:
    def maxArea(self, height:list[int]) -> int:
        self.height=height
        area_max=0
        lt_ptr=0
        rt_ptr=len(height)-1
        while lt_ptr<rt_ptr:
            area=min(height[lt_ptr],height[rt_ptr])*(rt_ptr-lt_ptr)
            area_max=max(area_max,area)
            if height[lt_ptr]<height[rt_ptr]:
                lt_ptr+=1
            else:
                rt_ptr-=1
        return area_max
    
heights=eval(input())
area=Solution().maxArea(heights)
print(area)