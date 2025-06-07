
# Mais um dia de LeetCash

Hoje resolvi o exercício 202, que pede para descobrir se um número é "feliz". Um número é feliz se, ao substituir ele pela soma dos quadrados dos seus dígitos várias vezes, ele chega no 1. Se cair num ciclo que não chega no 1, não é feliz. Para isso eu segui os seguintes passos:

1. Criei uma função ``get_next`` que recebe um número, transforma em string, pega cada dígito, eleva ao quadrado e soma tudo.

2. No método ``isHappy``, criei um set chamado ``aux`` para guardar os números já vistos e evitar loop infinito.

3. Enquanto o número não for 1 e não tiver repetido: 

    3.1. Adiciono o número atual no set ``aux``. 

    3.2. Troco o número pelo resultado da função ``get_next``.

4. Se sair do loop com o número igual a 1, retorno True (é feliz). Se não, retorno False (não é feliz).

E é isso! Mais um exercício resolvido!