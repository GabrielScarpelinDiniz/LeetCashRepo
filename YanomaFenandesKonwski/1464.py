class Solution(object):
    def maxProduct(self, nums):
        rep = sorted(nums)
        resposta = rep[-1]*rep[-2]
        return (rep[-1]-1)*(rep[-2]-1)
        