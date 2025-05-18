# Same Tree

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Same Tree é receber duas raízes e retornar se suas árvores são iguais ou não. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
# Função para listar as árvores em préordem
def preOrder(node, arr):
    if node is None:
        arr.append(None)
        return
    arr.append(node.val)
    preOrder(node.left, arr)
    preOrder(node.right, arr)


    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Armazena as árvores
        arrp = []
        arrq = []

        # Aplica a preordem nas duas árvores
        preOrder(p, arrp)
        preOrder(q, arrq)

        # Retorna caso as árvores sejam iguais
        return arrp == arrq


```

## Lógica do Algoritmo
- Dois arrays são criados, um para cada árvore
- Os arrays são preenchidos com cada árvore utilizando pré ordem
- Os arrays são comparados para verificar se são iguais

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n$), onde n é o tamanho das árvores.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é o tamanho das árvores.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata20.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
