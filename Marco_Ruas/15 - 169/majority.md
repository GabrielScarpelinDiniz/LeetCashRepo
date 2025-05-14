# No meio do evento de blockchain

## Desafio 15/200

Cada dia que passa eu percebo o quão persistente eu sou, mesmo perdendo e sendo desacreditado, aqui estou, dia após dia, brick by brick, mas não posso desistir, a esperança é a última que morre.

Basicamente é saber sobre qual é o número majoritário de um array, n/2 = ?


Tenho um objeto para armazenar os valores e quantas vezes ele se repete no array. Após isso, faça o cálculo para saber quantas vezes o número tem que apareceer para ser majoritário. Faço a iteração no array e adiciono os valores no objeto e quantas vezes ele se repete, e faço a condição se o número do objeto for maior que o limite, retorna ele.

```javascript
var majorityElement = function(nums) {
    let valor = {};
    let limite = Math.floor(nums.length / 2);

    for(let i = 0; i < nums.length; i++){
        valor[nums[i]] = (valor[nums[i]] || 0) + 1;

        if (valor[nums[i]] > limite) {
            return nums[i];
        }
    }
};
```


[Blockchain é tudo](https://leetcode.com/problems/majority-element/submissions/1633289726)