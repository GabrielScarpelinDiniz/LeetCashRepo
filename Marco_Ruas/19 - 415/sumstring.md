# Não dá tempo

## Desafio 19/200

Hoje eu tô com raiva.

Basicamente somar duas strings e retornar em string.

```javascript
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let soma = BigInt(num1) + BigInt(num2)

    return String(soma)
};
```

[Bolo](https://leetcode.com/problems/add-strings/submissions/1636872328)