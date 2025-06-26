# Mais um dia de LeetCash

Hoje eu resolvi o exercício 2000, que pede para inverter o prefixo de uma string até o primeiro caractere igual a `ch`. Para isso eu segui os seguintes passos:

1. Verifico se o caractere `ch` está presente em `word`.

2. Se estiver, pego o prefixo da palavra até o primeiro `ch`, transformo em lista e inverto.

3. Pego o restante da palavra (depois do `ch`), também como lista.

4. Junto o prefixo invertido com o restante e retorno como string.

5. Se `ch` não estiver em `word`, retorno a palavra original.

E pronto! Mais um exercício resolvido!!