# Inimigo da otimizaçã

## Desafio 13/200

Hoje vou aplicar o famoso 5 sprints em 5 horas, deixei acumular tudo no fim do dia e ainda vou ter que comer o bolo do Yanomã ;)

Desafio clean de hoje é encontrar a interseção dos números nos dois array, bem simples e eu ainda apliquei o On².

Código:
Crio um array e um objeto, e coloco dois for pra iterar a cada array. Depois, verifico se o número atual de `nums1` é igual ao de `nums2` e, pra evitar duplicados, uso um objeto (`existe`) pra marcar os números que já foram adicionados na interseção. Se ainda não foi adicionado, coloco no array `intersecao` e marco no objeto como `true`.

O resultado final é um array com os números que aparecem nos dois arrays de entrada, sem repetição. Bem direto, mas com complexidade **O(n²)** por causa dos dois loops aninhados.


```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let intersecao = []
    let existe = {}

    for(let i = 0; i < nums1.length; i++){
        for(let j = 0; j < nums2.length; j++){
            if(nums1[i] === nums2[j] && existe[nums1[i]] !== true){
                intersecao.push(nums1[i]);
                existe[nums1[i]] = true;
                break;
            }
        }
    }
};
```


[Bolo de milho](https://leetcode.com/problems/intersection-of-two-arrays/submissions/1631377583)