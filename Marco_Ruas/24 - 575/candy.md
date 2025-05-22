# Como prometido, eu mudei

## Desafio 24/200

Então, aproveitei o momento e decidi fazer logo agora, infelizmente não vou ser o primeiro, já que a Gi roubou ele, mas o segundo lugar não é nada mal também.

O problema pede pra menina comer menos doce se não ela engorda, mas ela gosta muito de doce, então o medico disse que ela pode comer n / 2 doces por semena, só que tem vários tipos de doces e ela quer comer o máximo de tipos de doce seguindo a ordem do doctor, então para isso segue o código abaixo:

Crio o objeto pra guardar os tipos de doce que existe e faço a verificação se o doce já existe, se ele não existe, crio ele no objeto e depois crio o tipos que armazena sem repetir os números que existe no array, então 1,2,3 existem 3 tipos, agora 1,1,2 existem dois. Depois disso calculo qual o máximo de doces que ela pode comer. Se o maximo de doces for maior que o tipo, ela só vai comer os tipos, agora se tipos de doces for maior, ela come o maximo.


```javascript

/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    let objeto = {}

    for(let i = 0; i < candyType.length; i++){
        if(!objeto[candyType[i]]){
            objeto[candyType[i]] = true
        }
        
    }

    let tipos = Object.keys(objeto).length
    let maximo = candyType.length / 2

    if(tipos < maximo){
        return tipos
    }
    else{
        return maximo
    }

};

```

[First time](https://leetcode.com/problems/distribute-candies/submissions/1640875686)