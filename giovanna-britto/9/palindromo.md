# Terceiro dia de Sofrimento

Quem diria que eu chegaria até aqui!? Até eu mesma duvidei que faria isso... Mas cá estou! 

Sabe as desvantagens de deixar para fazer os exercícios no final do dia? Você pensa muito em desistir, você começa a refletir sobre as suas decisões de vida, mas é sempre bom pensar que não importa as circunstâncias, você tem que continuar firme, forte e constante (Se é que me entendem).

Partindo para a resolução do problema... O ruim de deixar para última hora, é que você acaba fazendo as coisas mal feitas, logo segue uma resolução não ótima do exercício Palindrome Number. 

Confessor que foi um exercício fácil de fazer, pensando de forma não ótima. O problema basicamente solicitava que dado uma entrada `int` você deveria dizer se ela era um palindromo ou não. Um palindromo é quando ao inverter o número ou a string, eles continuam iguais ou não, logo para resolver isso, seguiu-se as seguintes etapas:

1. Verifica se o número não é negativo, se for retorna `false`.
2. Converte a entrada para string, e cria uma variável `newWord`, para armazenar o numero invertido.
3. Executa um for do tamanho de `x.length`, para inverter o número.
4. Após a inversão, é comparado se `x` é igual a `newWord` (`x == newWord`), caso sim retorna `true`, caso não retorna `false`.

Assim, chegamos na resposta correta do exercício, mas não de forma ótima. Para verificar a minha submissão (descobri ontem como submeter no LeetCode - hahaha), basta acessar:

[Sim, Eu duvido de Você Giovanna!](https://docs.google.com/document/d/1yg95tsyo0keXi2wp5q__NHhtKiTTOGZ4MhzTV1Rzr6E/edit?usp=sharing)