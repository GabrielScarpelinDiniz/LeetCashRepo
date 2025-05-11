# Outro dia de LeetCash

Oi Gente! Acharam que eu não iria aparecer por aqui hoje?? Pois é, ainda estou na competição sim!!!

Como a ponderada de CC veio para acabar com vidas, cá estou eu resolvendo mais um exercício usando memoização e programação dinâmica, sendo assim o exercício que eu resolvi é o 1137, em que ao invés de fazer o fibonacci eu fiz o Tribonacci. O objetivo é o mesmo, mas ao invés de somar os dois últimos valores, é somado os três últimos, logo os passos de execução são os seguintes:

1. Define o dicionário `memo` no construtor `__init__`, para criar a memória dos cálculos efetuados.

2. Se a entrada ``n`` está no dicionário, retorna o valor contido no dicionário.

3. Se ``n`` igual 1, atribui à posição 1 o valor 1 no dicionário.

4. Se ``n`` igual 0, atribui à posição 0 o valor 0 no dicionário.

5. Se ``n`` igual 2, atribui à posição 2 o valor 1 no dicionário.

6. Se não é nenhum desses casos, é aplicada a recursão para calcular o valor de Tribonacci, por meio do seguinte código: ``self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)``

7. Retorna o valor de ``memo[n]``.

E é isso, mais um exercício resolvido! Obrigada pela atenção gente!!!
