## Exercício: 129. Sum Root to Leaf Numbers
**Objetivo**: Dado uma árvore binária de inteiros retorne a soma de todos os inteiros formados pelo caminho entre a raiz e as folhas. Exemplo abaixo:

**Input:**

```
  1
 / \
2   3
```

**Output:** 25

**Explicação:**
- primeiro caminho $1 \rightarrow 2$ forma o número $12$.
- segundo caminho $1 \rightarrow 3$ forma o número $13$.
- $12 + 13 = 25$

## Descrição geral da estratégia
Para resolver aplico um DFS que vai compondo o número a ser somado a cada nível da árvore, somando o valor ao chegar nas folhas. Para isso, defino uma função que toma de parâmetros um array `res`, onde será armazenado o resultado, a raiz de uma subárvore e `currVal`, que indica o valor atual do número que estamos analisando. A ideia é que, a cada chamada da função recursiva, iremos descer um nível, isto é, adicionaremos um digito ao número que estamos analisando. Isso acontece ao multiplicar o `currVal` por 10 e somar o valor do nó atual. Esse processo continua até chegarmos num nó folha, quando o valor $\text{currVal} \cdot 10 + \text{root.val}$ é somado ao valor presente em resultado. Ao final, retorno o valor presente no primeiro elemento de `res` (o uso desse array se deve ao fato de que o Java não permite modificação de tipos primitivos que não sejam variáveis globais dentro de funções).

## Análise de complexidade
Para uma árvore com $n$ inteiros, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$ ( $O(\log{n})$ caso a árvore seja balanceada)