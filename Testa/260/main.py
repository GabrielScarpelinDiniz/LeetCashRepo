class Solution:
    def singleNumber(self, nums) -> int:
        val = []
        nums.sort()
        i = 0
        while i < len(nums):
          if (len(nums)-1) < i+1 or nums[i] != nums[i+1]:
            val.append(nums[i])
            i += 1
          else:
            i += 2
        return val

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 3, 4, 4, 1, 1, 5]))