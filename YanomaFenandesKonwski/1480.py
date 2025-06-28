class Solution(object):
    def runningSum(self, nums):
        soma=0
        resposta = []
        for i in range(len(nums)):
            soma+= nums[i]
            resposta.append(soma)
        return resposta