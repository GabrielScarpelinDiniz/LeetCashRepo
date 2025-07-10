## Exercício: 988. Smallest String Starting From Leaf
**Objetivo**: Dado uma árvore binária de inteiros no intervalo de $[0, 25]$, representando as letras do alfabeto ( $0: a, 1: b, \cdots, 25:z$ ), retorne a menor string em ordem lexicográfica (ordem alfabética) formada pelo caminho das folhas à raiz.

## Descrição geral da estratégia
Para resolver uso uma abordagem que combina DFS com backtracking. Primeiramente, crio um array de strings com 1 elemento (faço isso pois strings são objetos imutáveis no java e, exceto quando são globais, não podem ser alterados por funções) com valor inicial "{" que armazenará a resposta [1]. A função de DFS, de forma recursiva, adiciona os filhos deo nó analisado à uma lista `currVal`. Quando encontra-se um nó folha, a lista de inteiros `currVal` é então convertida para string e comparada com a string presente em `res[0]`. Se a string analisada for menor, `res[0]` a recebe, permanecendo inalterado caso contrário. Na volta da chamada recursiva, o elemento que foi anteriormente adicionado em `currVal` é removido (backtracking). Ao final de todo o processo, é retornado o valor presente em `res[0]`.

<sub>1. A escolha pelo caracter se deve ao fato que, na tabela ASCII, as chaves são os primeiros caracteres posteriores ao alfabeto minúsculo. Isso implica que não haverá nenhuma string com valor maior que este. Uma analogia é pensar que "{" é para os caracteres o mesmo que `Integer.MAX_VALUE` é para os inteiros.</sub>

## Análise de complexidade
Para uma árvore com $n$ nós, tem-se:
- **Time complexity**: $O(n)$ (mais precisamente, $O(l \cdot h)$ , sendo $l$ a quantidade de folhas da árvore e $h$ a altura da árvore. Por vezes, pode-se converter para $(l \log(n))$ caso seja utilizada uma árvore balanceada)
- **Space complexity**: $O(n)$ ( $O(\log{n})$ caso a árvore seja balanceada)