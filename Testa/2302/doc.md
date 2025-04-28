Esse exercício não se mostrou nada trivial, visto que ele não executa caso o algoritmo tenha uma complexidade maior ou igual a O(n²).
Logo meus amigos, O(n) ou inferior é necessário.
Consegui finalizar com a graça de Deus e muita pesquisa na web, pois depois de fazer em O(n³) e O(n²) tive que utilizar uma técnica de duplo ponteiro para resolver.

Básicamente o algoritmo cria dois ponteiros, o ponteiro da direita vai caminhando pela lista e somando os valores dos subarrays. Quando um subarray estoura o valor quer dizer que ele é o limite e então nós vamos caminhando com o ponteiro da esquerda até que o subarray volte a ser menor ou igual ao valor limite.
Depois repetimos o processo anterior até que chegue ao final da lista.

![Menos foco, mais ansiedade](./imagem.jpg)

Assinado
**Testinha do Fatorial**