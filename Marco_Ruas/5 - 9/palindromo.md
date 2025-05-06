# Que dia triste, mas faz parte

## desafio 05/200 (sim, agora estou atrasado, mas vou voltar ao meu streak)

Hoje serei curto e grosso, perdi o dia de ontem então é isso.

Palindromo é coisa que se repete lido de trás pra frente ou de frente pra trás.

Pra resolver exercício assim, é só pegar a palavra/número inverter e comparar com o orginal, no meu caso eu fui pelo caminho mais fácil

Usei o parInt para converter para inteiro, o x.toString para converter para string, o . split divide a string e coloca em um array, o reverse inverte tudo e o join junta em uma string de novo.

Eu tinha visto uma solução dessa parecido em python, então sabia que dava para fazer de forma simples sem a matemática, claro que demorou mais porque tive que pesquisar cada função, mas valei a pena.

```javascript
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let invertido = parseInt(x.toString().split('').reverse().join(''));

    if (invertido === x){
        return true
    }
    else{
        return false
    }
};
```


[Código da tristeza](https://leetcode.com/problems/palindrome-number/submissions/1624057139)