# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2666, que pede para criar uma função `once` em JavaScript, que só permite que outra função seja chamada uma vez. Para isso eu segui os seguintes passos:

1. Criei a função `once` que recebe uma função `fn`.

2. Dentro dela, defini uma variável `chamado` para controlar se a função já foi chamada, e uma `resultado` para guardar o retorno.

3. Retornei uma nova função que aceita qualquer argumento.

    3.1. Se ainda não foi chamada, executa `fn`, salva o resultado e marca como chamada.

    3.2. Se já foi chamada, retorna `undefined`.

4. Assim, a função só pode ser executada uma vez, mesmo que tente chamar de novo.

E pronto! Mais um exercício resolvido!!!