# Mais um dia de LeetCash

Boa noite, pessoal!!! Estou com preguiça de escrever meus sentimentos hoje, então vamos direto ao ponto: eu resolvi o exercício 1365, no qual dado um array de números, retornar para cada elemento quantos números no array são menores que ele. Para resolver, fiz assim:

1. Criei uma lista vazia chamada ``lista`` para guardar as respostas.
2. Usei um for para passar por cada elemento do array ``nums``.
3. Para cada elemento, criei uma variável ``cont`` para contar quantos números são menores.
4. Fiz outro for para comparar o elemento atual com todos os outros do array.   
    4.1. Se o número na posição j for menor que o da posição i (e não for o mesmo índice), aumento o contador cont.
    4.2. Depois de contar, adiciono o valor de cont na lista de respostas.
5. Retorno a lista com as respostas.

E é isso! Mais um exercício resolvido!!!