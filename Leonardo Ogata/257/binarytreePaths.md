# Add Digits

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema addDigits é somar os digitos de um número até que o número possua apenas um caractere. Sim eu sei que parece muito fácil e na verdade é mesmo, porém eu tive que passar uma meia hora pesquisando pra descobrir como faz isso com a complexidade O(1)

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        # Armazena resultados
        result = []
        
        # Função do backtracking
        def backtrack(node, path):
            # Caso não tenha nenhum nó é retornada uma solução vaiza
            if not node:
                return

            # Adiciona valor ao caminho
            path.append(str(node.val))

            # Caso o nó seja uma folha o caminho é adicionado ao array de resultados
            if not node.left and not node.right:
                result.append("->".join(path))
            # Caso o nó tenha filhos eles são explorados
            else:
                backtrack(node.left, path)
                backtrack(node.right, path)

            # Remove último item do caminho para explorar novas soluções
            path.pop()

        # Chama a função com raiz e array vazio para os caminhos
        backtrack(root, [])

        # Retorna array de resultado
        return result
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n^2$).

- Espaço: O uso de espaço adicional é O($n^2$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata50.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
