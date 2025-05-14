# Mesmo cansado estou aqui

## Desafio 14/200


A ideia é simples: começo do índice 1 e vou percorrendo o array. Se o número atual for diferente do anterior único (nums[k - 1]), então é um novo valor, e eu jogo ele pra posição k. Depois é só incrementar k.

No fim, o array original tem os primeiros k elementos como os únicos, em ordem, e o resto? O juiz do LeetCode mandou ignorar. 

```javascript
var removeDuplicates = function(nums) {
    if (nums.length === 0) return 0;

    let k = 1; 

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[k - 1]) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
};
```


[Vitaminada de banana](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1632406237)