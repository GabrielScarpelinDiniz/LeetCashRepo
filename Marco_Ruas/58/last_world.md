# Exercício mais fácil da minha vida

## Desafio dia 06/200

Agora eu corro contra o tempo para voltar um dia na liderança, prometo a vocês que estão lendo isso que vou me reerguer novamente, o erro de ontem ficou no passado, não é?

Eu posso tá me aproveitando das funções do javascript? Talvez! Mas nas entrevistas de emprego o entrevistador não vai pedir pra fazer do 0 e lá lá lá (eu espero).

Bom esse exercício realmente foi fácil, do tipo de fazer em duas linhas KKKKKKK Acho que tá na hora de me aventurar mais.

Mas enfim, basicamente vai ti dar uma lista e quer saber o comprimento da última palavra da lista, para isso eu usei o trim() para remover os espaços em brancos do início e fim da lista, aí o split(" "), para separar a string em um array de substrings, aí foi moleza, tenho uma lista com cada palavra separada, é só dar um remover[remover.length], né? Calma que isso vai dar erro, pois não existe nada nesse índice, temos que dar -1 para retornar a última palavra, ficando remover[remover.length - 1], agora temos a última palavra e nessa altura do campeonato vocês já devem saber que o length retorna o tamanho de algo e nesse caso retornando o tamanho da substring. E pronto, aí o exercício que fiz em 15 segundos. (Mas também né?)

Código:
``` javascript
var lengthOfLastWord = function(s) {
    let remover = s.trim().split(' '); 
    return remover[remover.length - 1].length
}
```

[Resolução hiper master blaster](https://leetcode.com/problems/length-of-last-word/submissions/1624927964)