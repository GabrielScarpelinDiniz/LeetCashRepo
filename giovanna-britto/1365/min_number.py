class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lista = []

        for i in range(len(nums)):
            cont = 0
            for j in range(len(nums)):
                if (nums[j] < nums[i] and i != j):
                    cont += 1
            lista.append(cont)

        return lista