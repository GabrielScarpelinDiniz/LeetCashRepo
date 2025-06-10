# Missing Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Missing Number é dado um array encontrar qual número falta na faixa entre o e o tamanho do aray

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```javascript
var missingNumber = function(nums) {
    // Calcula a soma da PA para o tamanho do array
    let paSum = (nums.length / 2) * (2 * 1 + (nums.length - 1) * 1)
    // Cria variável para armazenar a soma do array
    let arrSum = 0

    // Itera sobre o array para calcular a soma de todos os itens
    for(let i = 0; i < nums.length; i++){
        arrSum += nums[i]
    }

    // Retorna a diferença entre a soma da PA e a soma do array
    return paSum - arrSuma
};
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho do array.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata35.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
