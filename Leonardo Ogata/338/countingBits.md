# Counting Bits

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Counting Bits é contar a quantidade de vezes que o número 1 aparece no binário dos números de 1 à n+1

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```javascript
var countBits = function(n) {
    // Armazena resultados
    arr = []

    // Itera sobre os números
    for(let i = 0; i < n + 1; i++){
        // Recebe o valor decimal
        dec = i
        // Armazena valor binário
        binary = 0

        // Soma os valores de 1
        while (dec > 0) {
            binary = (dec % 2) + binary;
            dec = Math.floor(dec / 2);
        }

        // Adiciona o valor ao array
        arr.push(binary)
    }

    return arr

};
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n\log{n}$), onde n é o tamanho de n.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata47.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
