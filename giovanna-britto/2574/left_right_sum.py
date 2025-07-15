class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        somaTotal = sum(nums)
        somaEsq = 0 

        for i in range(len(nums)):
            somaDir = somaTotal - somaEsq - nums[i]
            answer[i] = abs(somaEsq - somaDir)
            somaEsq += nums[i]

        return answer