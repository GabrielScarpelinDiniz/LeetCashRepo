# Quase 50 dias de LeetCash

Hoje resolvi o exercício 938, que pede para somar todos os valores de um intervalo low, high em uma árvore binária de busca (BST). Para isso, eu segui os seguintes passos:

1. Criei a função `rangeSumBST` que recebe a raiz da árvore, o valor mínimo `low` e o máximo `high`.

2. Se o nó atual for None, retorno 0.

3. Se o valor do nó estiver dentro do intervalo, somo o valor do nó com o resultado da função para a subárvore da esquerda e da direita.

4. Se o valor do nó for menor que `low`, só preciso olhar para a subárvore da direita.

5. Se o valor do nó for maior que `high`, só olho para a subárvore da esquerda.

6. Assim, a função só percorre os ramos necessários, aproveitando que a árvore é de busca.

E pronto! Mais um exercício resolvido!