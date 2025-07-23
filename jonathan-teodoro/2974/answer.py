class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []

        nums.sort(reverse=True)

        while len(nums)>0:
            first = nums.pop()
            second = nums.pop()
            arr.append(second)
            arr.append(first)

        return arr