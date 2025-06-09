``` python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]

        sum = 0
        for i in gain:
            sum += i
            answer.append(sum)
        print(answer)

        max = float('-inf') 
        for i in answer:
            if i > max:
                max = i
        return max
```

Exercicio legal da minha lista de 75 exercicios que estou resolvendo. Esse é bem simplesinho, nada demais. Percorro o array vou adicionando as somas a um array auxiliar, em sequencia o percorro o array auxiliar, buscando o maior valor que há nele. Bem trivial e simples. BORAAA!!!!