``` python
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        answer = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            answer.append(count)

        return answer
```

Esse código usa dois laços for aninhados pra comparar cada número da lista com todos os outros. O primeiro for percorre cada posição da lista (i), e o segundo compara esse número com todos os outros (j). Dentro do segundo for, ele verifica se o índice é diferente (i != j) e se o número nums[j] é menor que nums[i]. Se for, aumenta um contador. No final de cada volta do laço de fora, ele adiciona esse contador numa lista chamada answer. Essa lista guarda, para cada número original, quantos números menores que ele existem no array, e é o que a função retorna no fim. Tudo feito com lógica básica e sem precisar de funções externas.