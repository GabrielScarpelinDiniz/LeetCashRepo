# O Joe foi preso e descobrímos que o verdadeiro monstro, é você!

## Desafio 08/200

Esse exercício teoricamente é fácil, só retornar o número que não se repete, aí já pensei na hora em comparar os pares, porém o enunciado fala, que tem que ter tempo e espaço constante, aí quebrou minhas pernas, fiquei olhando o código, o código olhou pra mim e no fim tive que correr pro hint, mas fazer o quê? Aí o hint me disse pra usar o operador XOR, aí vi isso e pensei, "Isso eu sei pô, vi no técnico, ele muda inverte os valores", tá, como aplica isso? Aí tive que pesquisar e entender como usava em [js](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR), e voala.

Basicamente cria a váriavel que vou atribuir o valor do XOR, com isso faça a interação por todo o array, o a operação vai ser a seguinte, o primeiro valor vai ficar salvo, pois vai ficar assim:

exemplo = [4, 1, 2, 1, 2]
exemplo = exemplo ^ 0
print(exemplo) = 4

O operador XOR basicamente muda os bits, aí como foi comparado com 0, e o 0 não muda nada, o resultado vai ser o primeiro número. Aí depois é só passar por cada valor da lista, e vai ficar só os bits do valor que não se repete.

```javascript
var singleNumber = function(nums) {
    let repetido = 0;
    for(let i = 0; i < nums.length; i++){
        repetido = repetido ^ nums[i]
    }
    return repetido
};
```

[Tenho café com os doadores, e eu tô aqui!](https://leetcode.com/problems/single-number/submissions/1626721012)
