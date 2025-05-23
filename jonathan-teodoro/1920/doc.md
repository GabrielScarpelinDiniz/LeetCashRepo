class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        index = 0
        answer = []
        for i in nums:
            answer.append(nums[nums[index]])
            index += 1
        
        return answer

exercicio trivial, pra cada indice do array ey adiciono o valor do numero que tem o indicie igual. Para isso, percorro o array com um for e vou appendando em um array answer o resultado esperado. Bem imples. Aqui ta facil.