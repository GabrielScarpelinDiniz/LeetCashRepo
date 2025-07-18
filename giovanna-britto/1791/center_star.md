# Mais um dia de LeetCash

Hoje eu resolvi o exercício 1791, que pede para encontrar o centro de uma estrela em um grafo dado apenas as arestas em uma lista de listas. Para isso eu segui os seguintes passos:

1. Peguei os dois primeiros pares de vértices das arestas: `a, b` e `c, d`.

2. O centro da estrela é o vértice que aparece nos dois pares.

3. Verifiquei se `a` é igual a `c` ou `d`. Se for, retorno `a`.

4. Senão, retorno `b`, que é o outro vértice que aparece nos dois pares.

E pronto! Mais um exercício resolvido!!