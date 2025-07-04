class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        res=0
        for num in nums:
            if num+diff in nums and num+2*diff in nums:
                res+=1
        return res
        