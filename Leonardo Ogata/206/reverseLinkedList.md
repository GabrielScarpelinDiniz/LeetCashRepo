# Reverse Linked List

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Reverse Linked List é receber uma lista ligada e retornar sua versão invertida

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Atribui o valor de head como valor atual 
        current = head
        # Criar array para armazenar valores da lista
        arrVal = []

        # Adiciona os valores da lista no array
        while current:
            arrVal.append(current.val)
            current = current.next
        
        # Inverte a lista de valores
        arrVal.reverse()

        # Cria lista para receber nós
        arrNodes = []

        # Adiciona nós com valores no array nós
        for x in range(len(arrVal)):
            arrNodes.append(ListNode(arrVal[x]))
        
        # Conecta os nós do array
        for i in range(len(arrNodes) - 1):
            arrNodes[i].next = arrNodes[i + 1]
        
        # Retorna nó inicial, caso head seja vazio retorna head
        return arrNodes[0] if head else head
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho da lista ligada.

- Espaço: O uso de espaço adicional é O(n), onde n é o tamanho da lista ligada.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata36.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
