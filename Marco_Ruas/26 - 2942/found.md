# Found o número chama

## Desafio 26/200

Então estou muito muito muito chateado, anteontem eu esqueci de dar push e perdi minha ofensiva, tô com dois dias atrasados, então vocês vão ver minha raiva nos próximos dias.

Uma lista para armazenar o caractere e dois for, um para percorrer cada palavra e outro pro caracter e ai adiciona no indice e retorna

```javascript

/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function(words, x) {
    let indices = [];
    for(let i = 0; i < words.length; i++){
        for(let j = 0; j < words[i].length; j++){
            if(words[i][j] === x){
                indices.push(i);
                break;
            }
        }
    }
    return indices;
};


```

[batata frita](https://leetcode.com/problems/find-words-containing-character/submissions/1644560135)