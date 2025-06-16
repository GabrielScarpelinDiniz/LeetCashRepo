# Dia 50 de LeetCash

Hoje chegamos ao quinquagésimo dia, ou seja, temos 1/4 da competição até esse momento, e as perdas foram baixas, por isso ainda seguimos firmes e fortes em nosso propósito.

Hoje eu resolvi o exercício 1672, no qual, dado uma lista de contas com o dinheiro de um cliente, deveríamos dizer qual o cliente mais rico baseado em quantos cada um tem na conta. Para isso, eu segui os seguintes passos:

1. Criação de uma lista `Soma`, para armazenar o valor total em cada conta
2. Variável `total` para ir somando os valores
3. For que itera sobre a entrada `accounts` e começa zerando o valor do ``total``
4. Segundo for que itera sobre `accounts[i]` e adiciona o valor de `accounts[i][j]` em `total`.
5. Quando o segundo for para de iterar eu adiciono o valor do total em `soma`
6. Por fim, retorno o maior valor de soma

E Pronto! Mais um exercício resolvido!!