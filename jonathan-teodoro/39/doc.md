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
                
Na preparação para a prova, optei por treinar backtracking via leetcode. Então nada melhor que aproveitar o exercicio para o leetcash. Cara, a logica do backtracking não é trivial, mas tá longe de ser difícil. Gero uma função auxiliar de backtrack. Começo com a condição de chegada, que nesse caso é a soma ser igual ao target. Se for eu adiciono no array de resposta e sigo minha vida. Depois gero um loop de possibilidades - seguindo a logica do backtrack que é, por natureza, recursivo. Tomando o cuidado de adicionar antes da recursividadde e subtrair após. Bala! 