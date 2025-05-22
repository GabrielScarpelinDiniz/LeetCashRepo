# Maximum Depth of Binary Tree

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Maximum Depth of Binary Tree é receber a raiz de uma árvore e retornar sua profundidade.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Cria pilha contendo nó e profundidade
        stack = [[root, 1]]
        # resultado da profundidade
        res = 0

        # Itera enquanto a pilha não estiver vazia
        while stack:
            # Atribui os valores root a node e o valor 1 a depth e remove eles da pilha
            node, depth = stack.pop()

            # Caso o nó não esteja vazio
            if node:
                # Atualiza profundidade 
                res = max(res, depth)
                # Adiciona na pilha os filhos dos nós junto com sua profundidade
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        # Retorna profundidade final
        return res
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n$), onde n é o tamanho da pilha.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é o tamanho da pilha.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata24.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
