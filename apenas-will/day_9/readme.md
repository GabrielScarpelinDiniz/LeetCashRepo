## Exercício: 844. Backspace String Compare
**Objetivo**: Dadas duas strings $s$ e $t$, determine se ambas são iguais após a exclusão de determinados caracteres. Um "#" indica um backspace (caracter deletado), sendo assim, o objetivo é pré-computar as strings e determinar se elas são iguais ou não;

## Descrição geral da estratégia
Para resolver, utilizei de duas stacks, removendo um caracter da stack caso encontre um "#", adicionando-o caso contrário. Por fim, bastou remover todos os elementos de ambas as stacks, conferindo se eles eram iguais. Caso não fossem, retornava um `false`. Caso nenhum fosse diferente, retornava `true` ao final do loop.

## Análise de complexidade
Para uma string $s$ com $n$ caracteres e uma string $t$ com $m$ caracteres, tem-se:
- **Time complexity**: $O(n + m)$
- **Space complexity**: $O(n + m)$

## OBS.
Há um jeito de fazer esse exercício usando duplo ponteiro do tipo _reset_, entretanto, não tive tempo hábil entre pensar nessa abordagem e aplicá-la para trazer essa versão. Caso ela fosse efetuada, sua complexidade de tempo seria $O(n + m)$ e a complexidade de espaço seria $O(1)$.
