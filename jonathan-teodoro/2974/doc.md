class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []

        nums.sort(reverse=True)

        while len(nums)>0:
            first = nums.pop()
            second = nums.pop()
            arr.append(second)
            arr.append(first)

        return arr

Bem facil - ordeno na ordem reversa e sigo os passos do enunciado, removo dois itens, adicioo primeiro o segundo depois o primero, tudo isso enquanto o tamanho de nums for maior que 0. Facil.