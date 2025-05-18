# Symmetric Tree

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Symmetric Tree é receber a raiz de uma árvore e identificar se ela é simétrica ou não. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
 def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Cria arrays para armazenar o lado direito e o esquerda da árvore
        rightArray = []
        leftArray = []

        # Utiliza método para calcular a árvore da direita espelhada
        self.preOrderMirror(root.right, rightArray)
        # Utiliza método para calcular a árvore da esquerda
        self.preOrder(root.left, leftArray)

        #Retorna se elas são iguais ou não
        return rightArray == leftArray

    # Método pré ordem
    def preOrder(self, node, arr):
        if(node == None):
            arr.append(None)
            return
        
        arr.append(node.val)
        self.preOrder(node.left, arr)
        self.preOrder(node.right, arr)

    # Método pré ordem espelhado
    def preOrderMirror(self, node, arr):
        if(node == None):
            arr.append(None)
            return
        
        arr.append(node.val)
        self.preOrderMirror(node.right, arr)
        self.preOrderMirror(node.left, arr)
```

## Lógica do Algoritmo
- Dois arrays são criados, um para cada lado da árvore
- Os arrays são preenchidos porém um deles de forma espelhada
- Caso eles sejam iguais é retornado true, caso o contrário false

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n$), onde n é o tamanho da árvore.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é o tamanho da árvore.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata21.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
