class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = []
        non_divisible = []

        for i in range(1, n + 1):
            if i % m == 0:
                divisible.append(i)
            else:
                non_divisible.append(i)
        
        num1 = sum(non_divisible)
        num2 = sum(divisible)
        
        return num1 - num2


Exercicio facil. Percorro o array pegando o que é divisivel (divisao resto zero) e o que nao é difvisivel e adicionando em arrays auxiliares, depois somo esses valores de cada array e subtraio a soma de um pelo do outro. Trivial pq to de ferias. 