class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        lista = Counter(nums)
        furtivos = [num for num, freq in lista.items() if freq == 2]
        return furtivos