# Dutch Flag doido

## Desafio 18/200

Hoje o desafio era organizar um array que só tem 0, 1 e 2, tudo no lugar certo, sem usar função pronta de sort.

Código:  
Crio três ponteiros: `low`, `mid` e `high`. O `low` marca onde os zeros vão ficar, o `high` onde os dois vão parar, e o `mid` vai percorrendo o array.  
- Se achar 0, troca com o início (`low`), avança os dois.
- Se achar 1, só segue o baile.
- Se achar 2, troca com o final (`high`) e só o `high` volta, porque pode ter vindo um 0 ou 1 pra posição do `mid`.


```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let low = 0, mid = 0, high = nums.length - 1;

    while (mid <= high) {
        if (nums[mid] === 0) {
            [nums[low], nums[mid]] = [nums[mid], nums[low]];
            low++;
            mid++;
        } else if (nums[mid] === 1) {
            mid++;
        } else {
            [nums[mid], nums[high]] = [nums[high], nums[mid]];
            high--;
        }
    }  
};
```

[Hoje eu sofri](https://leetcode.com/problems/sort-colors/submissions/1636002897)