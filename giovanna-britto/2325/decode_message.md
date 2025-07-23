# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2325, que pede para decodificar uma mensagem usando uma chave que define uma cifra por substituição. Para isso eu segui os seguintes passos:

1. Criei um dicionário `cifras` para guardar o mapeamento de cada letra da chave para o alfabeto.

2. Defini uma string `alfabeto` com todas as letras minúsculas.

3. Passei pela chave `key` e, para cada caractere diferente de espaço e ainda não mapeado, associei à próxima letra do alfabeto.

4. Criei uma string `resultado` para montar a mensagem decodificada.

5. Para cada caractere da mensagem, se for espaço, adiciono espaço; senão, substituo pela letra correspondente no dicionário `cifras`.

6. No final, retorno `resultado` com a mensagem decodificada.

E pronto! Mais um exercício resolvido!!