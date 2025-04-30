## Execício romain (Não liguem pros erros de portugues, nao tive tempo pra pensar)

Então, esse exercício é bem simples, basicamente é saber qual número é a partir do número romano,então se o input do `S` for `III` o resultado vai ser 3.

Para fazer isso, eu pensei em fazer igual o mano Yanomã, criar um switch case, atribuir os valores em cada caso e depois verificar a condição, porém depois de quase terminar, me toquei que era só fazer um hashmap, colocar as chaves valores lá e depois fazer a condição, então primeiro é feito uma iteração em cada caracter, atribui o valor na váriavel atual e depois na váriavel próximo é atribuído o valor do caractere mais 1. 

E faz a seguinte condição: se o proximo for maior que o atual subtrai da váriavel numero, dessa forma vai atribuindo na váriavel número até o for acabar.
``` javascript
if (proximo > atual) {
            numero -= atual;
        } else {
            numero += atual;
        }
```