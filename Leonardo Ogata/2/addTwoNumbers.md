# Reverse Integer

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Reverse Integer é inverter um inteiro e caso o inteiro ocupe mais que 32 bits retorne 0 .

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python        
    def addTwoNumbers(self, l1, l2):
    """
    :type x: int
    :rtype: int
    """
    # Cria nó primeiro nó
    dummy = ListNode(0)
    # Variável de nó atual
    current = dummy
    # Número carregado para próximo nó
    carry = 0

    # loop enquanto lista 1 ou lista 2 ou carry tiverem itens
    while l1 or l2 or carry:
        # valor 1 caso l1 tenha itens, caso o contráro l1 recebe 0
        val1 = l1.val if l1 else 0
        # valor 2 caso l2 tenha itens, caso o contráro l2 recebe 0
        val2 = l2.val if l2 else 0

        # valor total da soma
        total = val1 + val2 + carry
        # carry recebe o valor que não pode ser adicionado no nó
        carry = total // 10
        # Cria nova nó com o valor restante
        new_node = ListNode(total % 10)
        # Conecta o novo nó com a lista
        current.next = new_node
        # Atualiza valor atual
        current = current.next

        # Atualiza valor da lista
        if l1:
            l1 = l1.next
        # Atualiza valor da lista
        if l2:
            l2 = l2.next

    return dummy.next
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho do inteiros.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata25.png" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
