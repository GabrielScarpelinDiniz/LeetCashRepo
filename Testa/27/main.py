class Solution:
    def searchInsert(self, nums, target) -> int:
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
              k = i   
              break
            if nums[i] > target:
              k = i
              break 
        return k

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 4, 5], 2))