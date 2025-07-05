class Solution(object):
    def shuffle(self, nums, n):
        resp=[]
        for i in range(n):
            resp.append(nums[i])
            resp.append(nums[n+i])
        return resp

        