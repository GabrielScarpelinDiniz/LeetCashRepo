# Cansado, capenga e sem energia

## Desafio 12/200

Eu tô cheio de coisa pra fazer e perdi a ponderada, então hoje é dia das trevas.

Desafio simples e capenga, dado um array é pra retornar verdadeiro se tem uma sequência de 3 números ímpares nele, se não falso.

Código:
Intera no array e faz a verificação se existir o resto em uma sequência de três números, retorna true, se não falso.

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {

    for(let i = 0; i < arr.length; i++){
        if(arr[i] % 2 && arr[i+1] % 2 && arr[i+2] % 2){
            return true
        }
    }
    return false

};
```

[Godó ruim da peste](https://leetcode.com/problems/three-consecutive-odds/submissions/1630568326)