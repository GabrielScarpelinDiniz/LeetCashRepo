# Dia w de LeetCash

Boa noite galerinha, hoje é dia 16 de maio de 2025, e eu ainda continuo firme na competição. Temos um novo competidor no jogo, veremos como será os próximos meses, eu continuo não acreditando em mim, mas cá estou eu, fazendo um desafio nível médio (nem eu acreditei que isso um dia poderia acontecer).

Sendo assim, vamos para o código. Eu resolvi o exercício 75, de ordenação de arrays. Basicamente, esse exercício dava uma lista de arrays com números entre 0, 1 e 2, que representam vermelho, branco, azul, respectivamente. E o problema pedia que os números fossem ordenados considerando a seguinte ordem: primeiro os vermelhos (0), depois os brancos (1) e os azuis (2). Para resolver isso, eu segui os seguintes passos:

1. Crio um array `vermelho` para armazenar os valores correspondentes a 0;
2. Crio um array `branco` para armazenar os valores correspondentes a 1;
4. Crio um array `azul` para armazenar os valores correspondentes a 2;
5. Uso um for para iterar sobre o array nums e completar os arrays anteriores por meio de um if, que compara:
    - Se `nums[i] == 0` adiciona o valor ao array vermelho;
    - Se `nums[i] == 1` adiciona o valor ao array branco;
    - Se `nums[i] == 2` adiciona o valor ao array azul;
6. Adiciona os arrays em ordem ao array original.

Dessa forma temos o exercício resolvido! Por hoje é isso, obrigada gente!!!