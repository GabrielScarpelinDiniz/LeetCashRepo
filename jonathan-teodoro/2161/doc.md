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

O código separa os números em três listas: os menores que o pivot, os iguais ao pivot e os maiores que o pivot, preservando a ordem original dentro de cada grupo. No final, junta tudo nessa ordem (menores + iguais + maiores) e retorna o novo array reorganizado.