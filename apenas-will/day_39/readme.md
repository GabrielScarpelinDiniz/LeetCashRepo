## Exercício: 242. Valid Anagram
**Objetivo**: Dadas duas strings, determine se elas são anagramas (palavras formadas pelos mesmos caracteres mas em ordens distintas);

## Descrição geral da estratégia
Para resolver itero pelas strings adicionando seus elementos em um hashmap no qual as chaves são os caracteres e os valores são as quantidades que esses caracteres aparecem. Após isso, apenas itero pelas chaves conferindo as quantidades, retornando `false` se eu encontrar algum caracter em que a quantidade é diferente nos dois hashmaps.

## Análise de complexidade
Para strings com $s$ e $t$ caracteres, tem-se:
- **Time complexity**: $O(s + t)$ 
- **Space complexity**: $O(s + t)$ 