import numpy as np
import itertools

class Solution:
  def countSubarrays(self, nums, k) -> int:
    n = len(nums)
    l = 0
    subSum = 0
    total = 0
    
    for r in range(n):
      subSum += nums[r]
      while l <= r and subSum * (r - l + 1) >= k:
        subSum -= nums[l]
        l += 1
      total += (r - l + 1)
    
    return total
      
if __name__ == "__main__":
  nums = [2,1,4,3,5]
  k = 10
  solution = Solution()
  result = solution.countSubarrays(nums, k)
  print(result)  # Expected output: 2