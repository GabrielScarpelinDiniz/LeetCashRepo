# Dia W de LeetCash

Hoje eu resolvi esse exercício do LeetCash porque o Scarpelin me desafiou a fazer. Ele foi bem simples e segue as seguintes etapas:

1. Cria a lista `answer`, que será usada para armazenar os valores da saída final.
2. Percorre os números de `1` até `n` (inclusive), usando um laço `for`.
3. Para cada número `i`, verifica se ele é múltiplo de 3 **e** 5 ao mesmo tempo. Se for, adiciona a string `"FizzBuzz"` à lista `answer`.
4. Caso contrário, se `i` for apenas múltiplo de 3, adiciona `"Fizz"` à lista `answer`.
5. Caso contrário, se `i` for apenas múltiplo de 5, adiciona `"Buzz"` à lista `answer`.
6. Se `i` não for múltiplo de 3 nem de 5, adiciona o próprio número `i`, convertido para string, à lista `answer`.
7. Após o laço, retorna a lista `answer` com todos os valores gerados segundo as regras do problema.

Pronto! Mais um exercício resolvido!!!