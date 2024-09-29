# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

import math

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        self.nums=nums
        self.target=target
        self.sums=0
        self.diff=math.inf
        self.nums.sort()
        for i in range(0,len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if target>sum:
                    left+=1
                elif target<sum:
                    right-=1
                else:
                    self.sums=sum
                    return self.sums
                if abs(sum-target)<self.diff:
                    self.sums=sum
                    self.diff=abs(target-sum)
        return self.sums
    
nums=eval(input())
tar=input()
sum=Solution().threeSumClosest(nums,tar)
print(sum)