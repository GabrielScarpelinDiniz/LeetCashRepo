class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(res, candidates, target, soma, aux):
            if (soma == target):
                res.append(aux[:])
                print(res)
                return

            for i in range(len(candidates)):
                if soma <= target:
                    aux.append(candidates[i])
                    soma += candidates[i]
                    backtracking(res,candidates, target, soma, aux)
                    soma -= candidates[i]
                    aux.pop()
            
            return res

        print(backtracking([],candidates,target,0,[], 0))
                