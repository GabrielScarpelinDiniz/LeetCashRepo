# Mais um dia de LeetCash

Hoje resolvi o exercício 2695, que pede para criar uma classe `ArrayWrapper` em JavaScript, capaz de somar arrays e converter para string de forma personalizada. Para isso eu segui os seguintes passos:

1. Criei a função construtora `ArrayWrapper` que recebe um array de números e salva em `this.nums`.
2. Implementei o método `valueOf`, que retorna a soma dos elementos do array usando `reduce`. Assim, quando faço `obj1 + obj2`, ele soma os valores dos dois arrays.
3. Implementei o método `toString`, que retorna o array como string no formato `[1,2,3]` usando `join`.

E pronto! Mais um exercício resolvido!!!