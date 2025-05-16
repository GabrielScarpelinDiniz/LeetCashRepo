# Sabe o que é engraçado, sou o único de eng soft e não desisto

## Desafio 17/200

Pouco tempo novamente, se eu continuar assim vou parar de fazer documentação e só entregar o código.

Então nesse exercicio é basicamente para saber se existe numero duplicado ou não

Código: Objeto existir pra guardar se o valor repetiu ou não, faz a iteração e verifica se já existe ou não.

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  let repetir = {};

  for(let i = 0; i < nums.length; i++){
    if(repetir[nums[i]] === true){
        return true;
    }
    repetir[nums[i]] = true;
  }
  return false;
};
```
[Gateway](https://leetcode.com/problems/contains-duplicate/submissions/1635150517)