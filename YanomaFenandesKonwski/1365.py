class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        resp = sorted(nums)
        resposta = []
        for i in range(len(nums)):
            for j in range(len(resp)):
                if nums[i]==resp[j]:
                    resposta.append(j)
                    break
        return resposta
        