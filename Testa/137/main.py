class Solution:
    def singleNumber(self, nums) -> int:
        val = 0
        nums.sort()
        i = 0
        while i < len(nums):
            if len(nums) < i+2 or nums[i] != nums[i+2]:
                val = nums[i]
                break
            i += 3 
        return val;

if __name__ == "__main__":
    s = Solution()
    s.singleNumber([2, 3, 4, 2, 1, 2, 1, 3, 1, 3])