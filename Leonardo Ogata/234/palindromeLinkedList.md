# Palindrome Linked List

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Palindrome Linked List é identificar se a lista ligada é um palíndromo ou não.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```javascript
var isPalindrome = function(head) {
    // Atribui o valor da cabeça da lista a current
    var current = head;
    // Cria array para receber valores da lista
    const arr = [];

    // Loop para adicionar valores da lista ao array
    while(current != null){
        arr.push(current.val);
        current = current.next;
    }

    // Cria Array invertido com base no array original
    const reverseArr = [...arr].reverse();
    
    // Compara se os itens do array são iguais
    return arr.every((val, i) => val === reverseArr[i]);
};
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(N), onde n é o número de itens da lista.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata39.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
