class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        nums.sort()
        return nums  

Tirei o dia para fazer o desafio mais facil da historia do leetcode. Sequencia de passos simples - percorro o array pelo indice, primeiro, se for par vira 0, se for impar vira, depois so ordenar e sair pro abraco. É nós!!!