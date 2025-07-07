# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2520, no qual eu deveria dizer por quantos dígitos de `num` ele poderia ser divido, para resolver isso eu segui os seguintes passos:

1. Converti `num` para string
2. Transformei a string em uma lista `arr`
3. Criei a variável `cont` para armazenar a quantida de números válido
4. Fiz um for que itera sobre `arr` e verifica:
    Se `num % int(arr[i]) == 0` o `cont` recebe +1
5. Ao final da execução, retorno `cont`

E pronto!! Mais um exercício resolvido!!