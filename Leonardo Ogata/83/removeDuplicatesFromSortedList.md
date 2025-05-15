# Remove Duplicates from Sorted List

&nbsp;&nbsp;&nbsp;&nbsp; Gente queria dizer que estou muito feliz com esse código, talvez eu finalmente tenha entendido como listas ligadas funcionam!😁

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Remove Duplicates from Sorted List é receber uma lista ligada e remover os valores duplicados dessa lista.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public ListNode deleteDuplicates(ListNode head) {
        // Define primeiro item como item atual
        ListNode current = head;

        // Loop enquanto valor atual e próximo não forem nulos
        while(current != null && current.next != null){
            if(current.val == current.next.val){
                // Se o valor de um item for igual o valor do próximo conecto o primeiro item com o valor do item depois do próximo
                current.next = current.next.next;
            }else{
                // Caso o contrário avanço para o próximo item
                current = current.next;
            }
        }   

        // Retorna o primeiro item da lista
        return head;
    }
```

## Lógica do Algoritmo
- Cria variável para definir o primeiro item como item atual
- Loop enquanto o valor atual e o próximo forem diferentes de nulo 
    - Caso o valor de `current` for igual ao valor de `current.next`, `current.next` é transformado em `current.next.next`, assim desconectando o item da lista
    - Caso o valor seja diferente `current` é atualizado para `current.next`
- Retorna o primeiro item da lista
    

## Complexidade
- Tempo: O algoritmo possui complexidade de O($n$), onde n é o tamanho da lista.
- Espaço: O uso de espaço adicional é O($1$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata18.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos e feliz dia das mães, vejo vocês amanhã!</p>
    </div>
</div>
