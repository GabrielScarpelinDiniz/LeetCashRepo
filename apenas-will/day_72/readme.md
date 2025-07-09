## Exercício: 108. Convert Sorted Array to Binary Search Tree
**Objetivo**: Dado um array de inteiros ordenados, organize-os em uma BST (árvore binária de busca é uma árvore binária na qual o filho da esquerda é sempre menor que o pai, enquanto o da direita é sempre maior);

## Descrição geral da estratégia
Para resolver primeiro crio a raiz da árvore binária (que será retornada ao final do algoritmo). Para criar a raiz, escolho o elemento central do array. Em seguida, aplico uma função de DFS que toma como argumento um nó raiz e dois arrays, o primeiro contendo os elementos à sua esquerda e o segundo contendo elementos à direita. Agora, de maneira recursiva, a função vai construindo as subárvores da direita e esquerda, usando o nó do meio como raiz dessas subárvores. Por exemplo: considera-se a raiz $r$, e as listas $L$ e $R$, sendo, respectivamente, os elementos à esquerda e direita de $r$. Recursivamente, a função vai tornar o elemento central de $L$ como filho esquerdo de $r$ e o elemento central de $R$ como filho direito de $r$. Sendo assim, a função constrói a árvore das folhas para a raiz de forma recursiva. Ao final, retorna-se a raiz da árvore (salva no início do algoritmo);

## Análise de complexidade
Para um array com $n$ inteiros, tem-se:
- **Time complexity**: $O(n \log(n))$
- **Space complexity**: $O(n)$