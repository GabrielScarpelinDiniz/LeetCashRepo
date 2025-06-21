class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)

        return answer

Queria resolver esse exercício com binary search, mas não o fiz. Ele é muito simplesinho, ordena o array e pega os indices dos valores que sao iguais ao target, depois adicionamos isso em um array auxiliar "answer" e o retornamos, bem tranquilinho.