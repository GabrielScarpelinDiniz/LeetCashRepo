# Mais um dia de LeetCash

Hoje eu resolvi o exercício 3545, que pede para encontrar a soma da maior frequência de uma vogal e da maior frequência de uma consoante em uma string. Para isso eu seui os seguintes passos:

1. Defini uma string `vogais` com todas as vogais.

2. Criei um dicionário `d` para contar a frequência de cada caractere da string.

3. Passei por cada caractere de `s` e aumentei sua contagem em `d`.

4. Calculei `maxVogal` pegando a maior frequência entre as vogais.

5. Zerei a contagem das vogais no dicionário para não interferir no cálculo das consoantes.

6. Calculei `maxConso` pegando o maior valor restante no dicionário, que agora só tem consoantes.

7. Retornei a soma de `maxVogal` e `maxConso` como resposta.

E pronto! Mais um exercício resolvido!!