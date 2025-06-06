# Mais um dia de LeetCash

Hoje resolvi o exercício 1021, que pede para remover os parênteses mais externos de cada grupo válido em uma string só de parênteses. Para isso, eu segui os seguintes passos:

1. Criei uma string vazia chamada ``resposta`` para guardar o resultado.
2. Usei uma variável ``cont`` para contar o nível de profundidade dos parênteses.
3. Passei por cada caractere da string s usando um for.
4. Se o caractere for '(': 
    4.1. Se já estou dentro de pelo menos um parêntese (ou seja, cont >= 1), adiciono o '(' em resposta. 
    4.2. Aumento o contador cont.
5. Se o caractere for ')': 
    5.1. Diminui o contador cont. 
    5.2. Se ainda estou dentro de pelo menos um parêntese (ou seja, cont >= 1), adiciono o ')' em resposta.
6.No final, retorno a string resposta sem os parênteses mais externos de cada grupo.
E pronto! Mais um resolvido no LeetCash!