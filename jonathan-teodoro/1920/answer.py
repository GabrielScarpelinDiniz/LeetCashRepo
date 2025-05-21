class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        index = 0
        answer = []
        for i in nums:
            answer.append(nums[nums[index]])
            index += 1
        
        return answer