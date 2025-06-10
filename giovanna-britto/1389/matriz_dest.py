class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        dest = []

        for i in range(len(nums)):
            dest.insert(index[i], nums[i])

        return dest