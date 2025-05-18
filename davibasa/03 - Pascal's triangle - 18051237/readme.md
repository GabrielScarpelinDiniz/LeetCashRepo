## Pascal's Triangle

Dado um inteiro `numRows`, o algoritmo gera e retorna as primeiras `numRows` do Triângulo de Pascal. No Triângulo de Pascal, cada número é a soma dos dois números diretamente acima dele, com as bordas externas da linha (o primeiro e o último elemento) sempre sendo 1. O algoritmo utiliza uma abordagem iterativa para construir o triângulo linha por linha, de cima para baixo. Esta é uma forma de programação dinâmica, onde cada nova linha é eficientemente calculada com base na linha anterior já computada.

**Complexidade de Tempo:** O(numRows²)

**Complexidade de Espaço:** O(numRows²)
