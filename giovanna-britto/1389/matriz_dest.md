# Dia tantos de LeetCash

Boa noite Pessoal! Acabei de voltar do hospital com o Marco Ruas, sim o bichinho estava dodói, então segue minha resolução nível easy. Então eu resolvi o exercício 1389, no qual dado um array de nums e index, eu devo anexar em uma nova lista o valor de nums[i] no indíce index[i]. Para isso eu segui os seguintes passos:

1. Crio uma variável `dest`
2. For para iterar sobre o array de nums:
    2.1. Insiro na posição ``index[i]`` o valor ``nums[i]``
3. Retorno a lista `dest`