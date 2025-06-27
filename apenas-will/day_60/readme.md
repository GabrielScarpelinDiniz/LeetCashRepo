## Exercício: 3110. Score of a String
**Objetivo**: Dada uma string, retorne seu score. O score de uma string é calculado como a diferença absoluta entre os valores da tabela ASCII dos seus caracteres consecutivos ( $\sum_{i=0}^{s-1} |\text{ascii}(c_i) - \text{ascii}(c_{i + 1})|$, com $s$ sendo o comprimento da string e $c_i$ o caracter na posição $i$);

## Descrição geral da estratégia
Para resolver implemento o comportamento descrito acima usando um loop que itera pelos caracteres da string, calculando a diferença absoluta entre o valor da tabela ASCII desse elemento com o seu sucessor e somando essa diferença à uma variável. Por fim, retorno esse total.

## Análise de complexidade
Para um string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$