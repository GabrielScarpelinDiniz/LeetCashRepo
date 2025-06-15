# Isomorphic Strings

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Isomorphic Strings é identificar se as strings s e t são isomorficas, ou seja, podem ser mapeadas da mesma forma.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```javascript
var isIsomorphic = function(s, t) {
    // Dicionário para guardar letras da string S
    dicS = {}
    // Array para armazenar mapeamento da string S
    arrS = []   

    // Itera sobre string S
    for(let i = 0; i < s.length; i++){
        // Se i já estiver no dicionário seu indice é adicionado no array
        if(s[i] in dicS){
            arrS.push(dicS[s[i]])
        }else{
            dicS[s[i]] = i
            arrS.push(i)
        }
    }

    // Dicionário para guardar letras da string T
    dicT = {}
    // Array para armazenar mapeamento da string T
    arrT = []

    // Itera sobre string T
    for(let i = 0; i < t.length; i++){
        // Se i já estiver no dicionário seu indice é adicionado no array
        if(t[i] in dicT){
            arrT.push(dicT[t[i]])
        // Se i não estiver no dicionário seu indice é adicionado no dicionário e no array
        }else{
            dicT[t[i]] = i
            arrT.push(i)
        }
    }

    // Compara se os arrays de mapeamento são iguais
    return JSON.stringify(arrT) == JSON.stringify(arrS)
};
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n + m), onde n e m são os tamanhos das strings.

- Espaço: O uso de espaço adicional é O(n + m).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata49.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
