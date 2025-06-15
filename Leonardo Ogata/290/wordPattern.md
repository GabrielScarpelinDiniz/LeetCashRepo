# Word Pattern

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Word Pattern é verificar se a string ``pattern`` e `s` seguem o mesmo padrão

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```javascript
var wordPattern = function(pattern, s) {
    // Cria dicionario para armazenar indices
    let dicPattern = {}
    // Cria array para armazenar o padrão
    let arrPattern = []

    // Itera sobre a string pattern
    for(let i = 0; i < pattern.length; i++){
        // Se a letra já tiver sido adicionada o seu indice é adicionado no array
        if (pattern[i] in dicPattern){
            arrPattern.push(dicPattern[pattern[i]]);
        // Caso ela não tenha sido adicionada ela é adicionada no array e no dicionário com um novo indice
        }else{
            dicPattern[pattern[i]] = i;
            arrPattern.push(i);
        }
    }

    // Cria array com palavras separadas 
    wordsArray = s.split(" ")

    // Cria dicionario para armazenar indices
    let dicS = Object.create(null);
    // Cria array para armazenar o padrão
    let arrS = []

    for(let i = 0; i < wordsArray.length; i++){
        // Se a letra já tiver sido adicionada o seu indice é adicionado no array
        if (wordsArray[i] in dicS){
            arrS.push(dicS[wordsArray[i]]);
            // Caso ela não tenha sido adicionada ela é adicionada no array e no dicionário com um novo indice
        }else{
            dicS[wordsArray[i]] = i;
            arrS.push(i);
        }
    }

    // Retorna se os arrays são iguais
    return JSON.stringify(arrS) == JSON.stringify(arrPattern)
};
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n + m), onde n e m são o tamanho dos arrays.

- Espaço: O uso de espaço adicional é O(n + m).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata48.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
