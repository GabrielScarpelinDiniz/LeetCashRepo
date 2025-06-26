class Solution(object):
    def buildArray(self, nums):
        resposta = []
        for i in range(len(nums)):
            resposta.append(nums[nums[i]])
        return resposta
        
        