# Remove Linked List Elements

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Remove Linked List Elements é remover um valor de uma lista ligada

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Define head como nó atual
        current = head

        # Array para recebr os valores da lista
        arr = []
        
        # Adiciona valores no array
        while current:
            arr.append(current.val)
            current = current.next
        
        # Remove itens do valor no array
        for i in range(len(arr) -1, -1, -1):
            if arr[i] == val:
                arr.pop(i)
        
        # Lista para receber os nós
        arrNodes = []

        # Itera sobre os valores criando nós e adicionando no array
        for x in range(len(arr)):
            arrNodes.append(ListNode(arr[x]))

        # Conecta os nós
        for i in range(len(arrNodes) - 1):
            arrNodes[i].next = arrNodes[i + 1]

        # Retorna o nó inicial caso ele seja existente
        return arrNodes[0] if arrNodes else None
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n^2$), onde n é o tamanho do número.

- Espaço: O uso de espaço adicional é O($n$), onde n é o tamanho da lista.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata38.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
