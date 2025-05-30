## Exercício: 461. Hamming Distance
**Objetivo**: Dados dois inteiros, determine a distância Hamming (número de bits distintos) entre eles;

## Descrição geral da estratégia
Para resolver primeiro apliquei a operação `XOR` (ou exclusivo) nos dois inteiros e depois transformei o valor resultante em uma string. Em seguida, percorri a string contando os caracteres iguais a "1" (o `XOR` é uma operação de valores binários que retorna 1 caso os dois bits sejam distintos, retornando 0 caso contrário).

## Análise de complexidade
Para uma inteiro com $n$ bits, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$ 