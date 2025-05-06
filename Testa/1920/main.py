import itertools

class Solution:
    def buildArray(self, nums):
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + (nums[nums[i]] % n) * n
        for i in range(n):
            nums[i] = nums[i] // n
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.buildArray([0, 2, 1, 5, 3, 4]))
