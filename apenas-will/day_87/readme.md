## Exercício: 208. Implement Trie (Prefix Tree)
**Objetivo**: Implementar uma classe Trie (pronúncia-se "Try"). Tries (ou árvores de prefixo) são estruturas de dados baseadas em árvores que armazenam strings. Nessa estrutura, cada caracter é um nó da árvore e um caminho da raiz até um determino nó formam palavras. Para uma palavra ser válida, é necessário que o elemento final esteja marcado como "válido", indicando que o caminho até aquele ponto forma uma palavra. São estruturas de dados úteis quando se lida com cadeias de caracteres, principalmente quando se quer conferir **diversas vezes** se uma palavra existe em algum contexto ou se ela inicia de uma dada maneira (por isso também é chamada de árvore de prefixo).

## Descrição geral da estratégia
Para resolver, implemento uma classe `TrieNode` que tem como atributo `validWord`, uma variável booleana que indica se aquele nó é o último caracter de uma palavra, e `children`, um HashMap que relaciona caracteres aos nós filhos daquele _node_ da árvore. Após isso, implemento os métodos de inserção, busca e conferência de prefixo. A inserção de palavras consiste em percorrer uma string adicionando um nó para cada caracter ainda não adicionado e marcar o `validWord` do nó do último caracter como `true`. A busca se resume a percorrer uma string, conferindo se cada caracter está presente na árvore e se o último o nó do último caracter tem o valor `true` em `validWord`, retornando `false` caso alguma das condições anteriores não seja atendida. E a busca de prefixo é similar a busca, exceto que não há a necessidade de conferir se o último caracter tem `validWord` igual a `true`.

## Análise de complexidade

### Inserção
Para uma string com $c$ caracteres e uma Trie com $n$ nós, tem-se:
- **Time complexity**: $O(c)$ 
- **Space complexity**: $O(n)$ (quanto mais palavras são adicionadas, a estrutura começa a ter comportamento $O(\log(n))$ ) 

### Busca
Para uma string com $c$ caracteres e uma Trie com $n$ nós, tem-se:
- **Time complexity**: $O(c)$ ou $O(\log(n))$ 
- **Space complexity**: $O(1)$

### Busca de prefixo
Para um prefixo com $c$ caracteres e uma Trie com $n$ nós, tem-se:
- **Time complexity**: $O(c)$ ou $O(\log(n))$
- **Space complexity**: $O(1)$ 