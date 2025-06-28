class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        menor = []
        igual = []
        maior = []

        for num in nums:
            if num < pivot:
                menor.append(num)
            elif num == pivot:
                igual.append(num)
            else:
                maior.append(num)

        return menor + igual + maior