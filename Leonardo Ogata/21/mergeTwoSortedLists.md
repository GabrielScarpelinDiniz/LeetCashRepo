# Merge Two Sorted Lists

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Merge Two Sorted Lists é mergear duas linked lists de forma que mantenha a linked list final em ordem crescente

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

    // Cria um nó temporário 
    ListNode temp = new ListNode(0);
    // Cria ponteiro para construir a nova lista
    ListNode currentNode = temp;

    // Loop até que alguma das duas listas estejam vazias
    while (list1 != null && list2 != null) {
        
        // Compara os valores das duas listas
        if (list1.val < list2.val) {
            // Se o valor de list1 for menor, adiciona list1 à lista resultante
            currentNode.next = list1;
            // Pula list1 para o próximo nó
            list1 = list1.next;
        } else {
            // Caso contrário, adiciona list2 à lista resultante
            currentNode.next = list2;
            // Pula list2 para o próximo nó
            list2 = list2.next;
        }

        // Pula o ponteiro da lista resultante para o próximo nó
        currentNode = currentNode.next;
    }

    // Se ainda sobrar algum elemento na list1 conecta o com o fim da lista resultante
    if (list1 != null) {
        currentNode.next = list1;
    }

    // Se ainda restarem elementos em list2, conecta-os diretamente à lista resultante
    if (list2 != null) {
        currentNode.next = list2;
    }

    // Retorna a nova lista pulando o primeiro nó utilizado como temporário
    return temp.next;
}

```

## Lógica do Algoritmo
- Após a criação das variáveis auxiliares o código entra num loop até que alguma das listas termine
    - O valor da lista 1 é comparado com o valor atual da lista 2
        - Caso o valor da lista 1 seja menor ele é adicionado a nova linked list e pulamos para o próximo nó na lista 1
        - Caso o contrário o valor da lista 2 é adicionado a nova linked list e pulamos para o próximo nó na lista 2
    - Após alguma dessas duas decisões serem tomadas pulamos para o próximo nó na nova linked list
- Caso ao final do nó alguma das listas não esteja vazia esse resto é todo adicioando ao fim da nova linkes list
- Ao final é retornado a nova linked list pulando o primeiro nó que foi utilizado apenas como auxiliar

## Complexidade
- Tempo: O algoritmo possui complexidade O(${n + m}$), onde n é a quantidade de nós da lista 1 e m é quantidade de nós da lista 2.
- Espaço: O uso de espaço adicional é O(${1}$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata6.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
