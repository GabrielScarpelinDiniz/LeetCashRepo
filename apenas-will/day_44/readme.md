## Exercício: 657. Robot Return to Origin
**Objetivo**: Dada uma string contendo os movimentos de um robô (para cima, para baixo etc.) determine se, após todos os movimentos, ele retorna à posição inicial;

## Descrição geral da estratégia
Para resolver itero pela string, armazenando a quantidade de movimentos para cada direção em um array. Ao final, retorno se a diferença na quantidade de movimentos no eixo x (direita e esquerda) e no eixo y (para cima e para baixo) é igual a 0, retornando esse resultado.

## Análise de complexidade
Para um array com $n$ movimentos, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$