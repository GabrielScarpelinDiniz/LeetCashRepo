class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(aux, res, nums):
            if len(aux) == len(nums):
                res.append(aux[:])
                return
                 
            for i in range(len(nums)):
                if nums[i] not in aux:
                    aux.append(nums[i])
                    backtracking(aux,res,nums)
                    aux.pop()
            print(res)
            return res
            
        return backtracking([],res,nums)