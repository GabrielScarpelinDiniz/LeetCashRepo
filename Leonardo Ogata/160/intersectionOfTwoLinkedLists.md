# Intersection of Two Linked Lists

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Intersection of Two Linked Lists é encontrar o nó em que duas listas ligadas se encontram

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    # Define o nó atual de A e o contador para verificar tamanho da lista
    currentA = headA 
    counterA = 0

    # Percorre a lista e mede seu tamanho
    while currentA.next != None:
        currentA = currentA.next
        counterA += 1
    # Volta o a lista para seu valor inicial 
    currentA = headA 

    # Define o nó atual de B e o contador para verificar tamanho da lista
    currentB = headB 
    counterB = 0

    # Percorre a lista e mede seu tamanho
    while currentB.next != None:
        currentB = currentB.next
        counterB += 1
    # Volta o a lista para seu valor inicial 
    currentB = headB 

    # Mede a diferença de tamanho entre as listas
    skip = abs(counterA - counterB)

    # Atribui cada lista a variável menor ou maior dependendo do seu tamanho
    if counterA > counterB:
        smallest = currentB
        biggest = currentA
    else: 
        smallest = currentA
        biggest = currentB

    # Avança a diferença de tamanho entre as listas na lista maior para que as listas comecem da mesma posição
    for x in range(skip):
        biggest = biggest.next

    # Itera sobre ambas as listas ao mesmo tempo
    while biggest and smallest:
        # Caso o nó atual de ambas as listas sejam iguais retorne o nó    
        if biggest == smallest:
            return biggest
        # Avança para o próximo nó de cada lista    
        biggest = biggest.next
        smallest = smallest.next
    # Retorna nulo caso as listas não se encontrem    
    return 
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n + m), onde n e m são o tamanho das listas.

- Espaço: O uso de espaço adicional é O(1), pois o algoritmo usa apenas variáveis auxiliares.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata30.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
