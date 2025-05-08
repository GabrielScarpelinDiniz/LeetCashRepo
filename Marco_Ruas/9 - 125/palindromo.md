# Quase esqueci de novo, mas aqui estamos

## Desafio 09/200

Hoje fiquei caçando algum exercício fácil (mas um bem fácil mesmo), pois não tenho tempo pra nada.

Dessa forma, fiz assim:

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {    
    s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let invertido = s.split('').reverse().join('');
    return s === invertido;
};