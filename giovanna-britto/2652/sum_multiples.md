# Mais um dia de LeetCash

Maior sacanagem que poderíamos ter feito era não termos dados férias do LeetCash para a gente, então cá estamos nós fazendo isso! Hoje eu resolvi o exercício 2652, em que dado o intervalo de um número de 1 até `n`, eu devo retornar a soma de todos os números que são múltiplos de 3,5 e 7. Para resolver isso eu segui os seguintes passos:

1. Declaro a variável `total` que armazena o valor dos itens que serão somados
2. For que itera até `n+1`

    2.1. Se `i % 3 == 0 or i % 5 == 0 or i % 7 == 0` então eu somo o valor de i à `total`

3. Retorno o valor de total

E pronto!! Mais um exercício resolvido!!!