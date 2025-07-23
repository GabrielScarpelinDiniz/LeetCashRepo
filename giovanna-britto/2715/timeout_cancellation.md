# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2715, que pede para criar uma função que executa outra função com atraso, mas que pode ser cancelada antes de rodar. Para isso eu segui os seguintes passos:

1. Criei a função `cancellable` que recebe uma função `fn`, um array de argumentos `args` e o tempo de espera `t`.

2. Usei `setTimeout` para agendar a execução de `fn` com os argumentos depois de `t` milissegundos.

3. Criei uma função `cancelaFuncao` que chama `clearTimeout` para cancelar o timer antes da função ser executada.

4. Retornei `cancelaFuncao` para permitir o cancelamento externo.

E pronto! Mais um exercício resolvido!!!