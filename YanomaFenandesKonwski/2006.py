class Solution(object):
    def countKDifference(self, nums, k):
        resposta = 0
        j=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                numero = max(nums[i],nums[j])
                numero_min = min(nums[i],nums[j])
                if (numero-numero_min==k):
                    resposta+=1
        return resposta