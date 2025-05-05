# Sétimo dia de Leet Cash???

É isso mesmo, estamos chegando ao final da primeira semana que esse desafio começou e eu já me arrependo de ter entrado nele. Mas como não podemos perder essa ofensiva, segue mais um desafio...

Hoje, dia 04 de maio, o desagio que eu resolvi se chama Longest Common Prefix, e dado uma string de entrada eu tenho que encontrar o maior prefixo e o com maior recorrência dentro de um array, para resolver isso eu segui as seguintes etapas:

1. Verifico se o array strs está vazio. Se estiver, retorno uma string vazia "", pois não há prefixo comum possível.

2. Crio a variável ``prefixo`` e atribuo a ela o valor da primeira string do array, assumindo que o prefixo comum será inicialmente igual a ela.

3. Faço um laço for para percorrer todas as outras strings do array, começando da segunda:

    - Dentro do for, uso um while para verificar se a string atual começa com o valor de prefixo.
    - Enquanto não começar com o prefixo, reduzo o prefixo retirando o último caractere usando slice(0, -1).
    - Se o prefixo se tornar uma string vazia, significa que não há nenhum prefixo comum, então retorno "".

4. Após o laço, retorno o valor da variável prefixo, que agora contém o maior prefixo comum entre todas as strings do array (ou uma string vazia, caso não exista nenhum).

Então assim temos o exercício resolvido. É isso, obrigada pela atenção!!!