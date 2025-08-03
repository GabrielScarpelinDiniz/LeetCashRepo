## Exercício: 14. Longest Common Prefix
**Objetivo**: Dado um array de strings, retorne o maior prefixo comum à todas as palavras, retornando uma string vazia caso não haja prefixo comum à todas.

## Descrição geral da estratégia
Para resolver crio uma variável que irá armazenar o maior prefixo comum. Em seguida, itero pelos caracteres da primeira palavra, comparando-o aos caracteres de todas as demais palavras. Caso seja encontrado um caracter diferente, retorno o maior prefixo atual. Caso não hajam mais caracteres em determinada string (a primeira string é maior que alguma outra), retorno o maior prefixo atual. Caso seja encontrada uma string vazia, retorno também uma string vazia (se há uma string vazia, automaticamente não há prefixo comum à todas as strings). Se nenhuma das condições anteriores for satisfeita, então adiciono o caracter analisado como parte do prefixo e averiguo o caracter seguinte, repetindo esse processo até que alguma condição seja atingida ou que eu tenha iterado por toda a string inicial (ela é o próprio prefixo), situação na qual eu retorno o prefixo ao final de tudo. Cabe citar que adicionei uma validação inicial que verifica se o array de strings possui apenas 1 elemento, situação na qual retorno esse único elemento (uma palavra é prefixo dela própria). 

## Análise de complexidade
Para um array com $n$ strings e um prefixo de tamanho máximo $k$, tem-se:
- **Time complexity**: $O(nk)$ 
- **Space complexity**: $O(k)$
