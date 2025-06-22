# Mais um dia de LeetCash

Hoje eu resolvi o exercício 1684, que pede para contar quantas palavras de uma lista só têm letras permitidas por uma string `allowed`. Para isso segui os seguintes passos:

1. Transformei a string `allowed` em um set chamado `selecionadas` para facilitar a checagem das letras.

2. Criei uma variável `cont` para contar quantas palavras NÃO são consistentes.

3. Para cada palavra em `words`:

    3.1. Para cada letra da palavra, verifiquei se ela não está em `selecionadas`.

    3.2. Se encontrar uma letra não permitida, aumento `cont` e paro de checar essa palavra.

4. No final, retorno o total de palavras menos `cont`, que é o número de palavras consistentes.

E é isso, mais um exercício resolvido!!