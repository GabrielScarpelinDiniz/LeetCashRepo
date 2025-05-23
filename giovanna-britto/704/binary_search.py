class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = nums[int(len(nums)/2)]
        esq = 0
        dire = len(nums) -1

        for i in range(len(nums)):
            if (nums[i] == target):
                return i
            elif(nums[i] < mid):
                dire = mid -1
            else:
                esq = mid + 1
        
        return -1
        