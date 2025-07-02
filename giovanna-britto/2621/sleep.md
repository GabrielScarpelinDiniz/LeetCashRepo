# Mais um dia de LeetCash

Hoje resolvi o exercício 2621, que pede para criar uma função `sleep` em JavaScript, que espera um certo número de milissegundos antes de continuar. Para isso eu segui os seguintes passos:

1. Criei uma função assíncrona chamada `sleep` que recebe um número  `millis` de milissegundos.

2. Dentro da função, usei `await` em uma nova Promise que só resolve depois de  `millis` milissegundos usando `setTimeout`.

3. Assim, quando chamo `sleep(100)`, o código espera 100ms antes de continuar.

E pronto! Mais um exercício resolvido!!!