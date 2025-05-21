# Primeiro desafio de academia também 

## Desafio 21/200

Então estou passando aqui que vou parar de fazer leetcode tarde porque pelo andar da carroagem, não vai dar mais pra ficar brincando desse jeito, dito isso vou documentar rápido.

É só saber o tipo de triângulo kkkkkk

Cria 3 váriaveis e faz as verificações

se todas as váriaveis forem iguais é equilatero, se só dois lados forem é isoceles e tudo diferente é escaleno. Aí é só if elif e else.


```python
from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
            
        if a == b == c:
            return "equilateral"
        elif a == b or a == c or b == c:
            return "isoceles"
        else:
            return "scalene"

```


[Odeio pimenta](https://leetcode.com/problems/type-of-triangle/submissions/1638848928)


# Desafio 1/100

Agora também vou postar um pouco sobre academia, projetinho que tô fazendo com o Yanomã
## Dia de peito
![alt text](../academia/acad1.jpeg)