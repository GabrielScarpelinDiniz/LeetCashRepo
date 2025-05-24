# Balanced Binary Tree

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Balanced Binary Tree é dado a raiz de uma árvore retorne se ele a é balanceada ou não

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # Caso base em que é uma árvore vazia
            if not root:
                return [True, 0]

            # Busca a profundidade da árvore da esquerda e da direita
            left, right = dfs(root.left), dfs(root.right)

            # Retorna se a árvore é balanceada olhando tanto o resultado de suas sub árvores quando o seu próprio resultado
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Retorna se a árvore é balanceada e sua profundidade
            return[balance, 1 + max(left[1], right[1])]

        # Retorna se a árvore inteira é balanceada
        return(dfs(root)[0])
```


## Complexidade
- Tempo: O algoritmo possui complexidade O($n$), onde n é tamanho da arvore.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata27.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
