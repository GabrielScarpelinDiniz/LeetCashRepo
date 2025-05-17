class Solution:
    def sortColors(self, nums: List[int]) -> None:
        vermelho = []
        branco = []
        azul = []

        for i in range(len(nums)):
            if nums[i] == 0:
                vermelho.append(nums[i])
            elif nums[i] == 1:
                branco.append(nums[i])
            elif nums[i] == 2:
                azul.append(nums[i])
        
        nums[:] = vermelho + branco + azul