## Pascal's Triangle II

O método constrói iterativamente o Triângulo de Pascal até a linha `rowIndex`. Cada linha é gerada com base na anterior, onde cada número é a soma dos dois números diretamente acima dele, e as bordas são sempre 1. Todas as linhas geradas até `rowIndex` são armazenadas internamente antes de retornar a linha solicitada.

**Complexidade de Tempo:** O(rowIndex²)

**Complexidade de Espaço:** O(rowIndex²)
