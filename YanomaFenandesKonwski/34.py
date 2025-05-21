class Solution(object):
    def searchRange(self, nums, target):
        def acho_primeiro(nums, target):
            esquerda = 0
            direita = len(nums) - 1
            primeiro = -1
            while esquerda <= direita:
                meio = (esquerda + direita) // 2
                if nums[meio] < target:
                    esquerda = meio + 1
                else:
                    if nums[meio] == target:
                        primeiro = meio
                    direita = meio - 1
            return primeiro

        def acho_ultimo(nums, target):
            esquerda = 0
            direita = len(nums) - 1
            ultimo = -1
            while esquerda <= direita:
                meio = (esquerda + direita) // 2
                if nums[meio] > target:
                    direita = meio - 1
                else:
                    if nums[meio] == target:
                        ultimo = meio
                    esquerda = meio + 1
            return ultimo

        return [acho_primeiro(nums, target), acho_ultimo(nums, target)]
