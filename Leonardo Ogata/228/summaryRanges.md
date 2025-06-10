# Summary Ranges

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Summary Ranges é identificar onde as sequências estão quebradas.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```javascript
var summaryRanges = function(nums) {
    // Ponteiro que marca início da sequência
    var start = 0
    // Ponteiro que marca fim da sequência
    var end = 0
    // array que armazena resposta
    arr = []

    // Itera sobre o array
    for(let i = 0; i < nums.length; i++){
        // Caso a sequência continue no próximo o ponteiro do fim é avançado  
        if(nums[i] + 1 == nums[i + 1]){
            end ++;
        }else{
            if(start == end){
                arr.push("" +  nums[start] + "")
                start = end + 1;
                end ++;
            }else{
                // Caso fim e começo sejam diferentes a sequência é adicionada
                arr.push(nums[start] + "->" + nums[end])
                // Atualiza começo
                start = end + 1;
                // Atualiza Fim
                end ++;
            }
        }
    }

    // Retorna array da resposta
    return arr

}; 
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho do array.

- Espaço: O uso de espaço adicional é O(n), onde n é o tamanho do array.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata43.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
