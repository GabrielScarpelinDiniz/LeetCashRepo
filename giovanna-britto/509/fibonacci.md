# Dia 10 de Leet Cash

Hoje é o décimo dia que a competição começou, está sendo uma experiência divertida, acho que o clima de competição está fazendo bem para os ânimos de todos os competidores. Sempre quando lembramos da competição tentamos advinhar se alguém irá perder algum dia, ou então duvidamos da nossa própria capacidade de manter a constância por 200 dias... Pelo menos eu duvido, só que hoje não será esse dia!

Eu resolvi o exercício 509 que é o da sequência de Fibonacci, mas antes que pensem "Nossa, é esse que ela resolveu?", saibam que isso é para ajudar a fixar os conteúdos da aula, já que para aprender programação dinâmica é preciso aprender memoização, sendo assim, peguem a minha solução do problema de Fibonacci. 

O algoritmo segue os seguintes passos:

1. Define o dicionário `memo`, para criar a memória dos cálculos efetuados.
2. Se a entrada `n` está no dicionário retorna o valor contido no dicionário.
3. Se `n` igual 1, atribui a posição 1 o valor 1 no dicionário. 
3. Se `n` igual 0, atribui a posição 0 o valor 0 no dicionário. 
4. Se não é nenhum desses casos, é aplicado a recursão para calcular o valor de fibonacci, por meio do seguinte código: `self.memo[n] = self.fib(n-1) + self.fib(n-2)`
5. Retorna o valor de `memo[n]`

Sendo assim, um código que tinha potencial de ser exponencial, tem uma complexidade $O(n)$. Logo, o problema foi resolvido e com uma boa complexidade, sendo assim, obrigada pela atenção!!!