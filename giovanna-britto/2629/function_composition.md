# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2629, que pede para implementar uma função `compose` em JavaScript, que faz a composição de várias funções (ou seja, encadeia elas da direita para a esquerda). Para isso eu segui os seguintes passos:

1. Criei a função `compose` que recebe um array de funções `functions`.

2. Se o array estiver vazio, retorno uma função que só devolve o próprio argumento (função identidade).

3. Se não estiver vazio, usei `reduceRight` para encadear as funções, criando uma nova função que aplica todas em sequência, da última para a primeira.

4. Assim, quando chamo o resultado passando um valor, ele executa todas as funções na ordem correta.

E pronto! Mais um exercício resolvido!!!