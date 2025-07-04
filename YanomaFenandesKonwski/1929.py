class Solution(object):
    def getConcatenation(self, nums):
        count = 0
        resposta = []
        while count<2:
            for i in range(len(nums)):
                resposta.append(nums[i])
            count+=1
        return resposta