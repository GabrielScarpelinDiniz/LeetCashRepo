# Move Zeroes

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Move Zeroes é mover todos os 0s de um array para o final

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```javascript
var moveZeroes = function(nums) {
    // variável para contar 0s
    let counter = 0;

    // Conta a quantidade de 0s
    for(let i = 0; i < nums.length; i++){
        if(nums[i] == 0){
            counter += 1;
        }
    }

    // Remove os 0s e adiciona eles nos final
    for(let i = 0; i < counter; i++){
        nums.splice(nums.indexOf(0), 1)
        nums.push(0)
    }
    
};
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n^2$), onde n é o tamanho do array.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata46.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
