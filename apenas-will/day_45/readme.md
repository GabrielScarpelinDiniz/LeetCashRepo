## Exercício: 1929. Concatenation of Array
**Objetivo**: Dada um array de inteiros, retorne a concatenação desse array com ele mesmo;

## Descrição geral da estratégia
Para resolver crio um array com o dobro de comprimento do array original. Em seguida, itero pelo array original, adicionando na posição `j + i * nums.length` o elemento `nums[j]`, sendo que `i` indica se estamos na primeira ou segunda iteração (assumindo o valor de 0 ou 1), `j` indica a posição do array original em que estamos e `nums.length` é o comprimento do array original.

## Análise de complexidade
Para um array com $n$ elementos, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(n)$ ( $O(1)$ se considerar apenas espaço auxiliar)