## Detectar Uso de Maiúsculas (Detect Capital Use)

O método `DetectCapitalUse` verifica se o uso de letras maiúsculas em uma palavra está correto segundo as seguintes regras:

1. Todas as letras da palavra são maiúsculas (ex: "USA")
2. Todas as letras da palavra são minúsculas (ex: "leetcode")
3. Apenas a primeira letra da palavra é maiúscula (ex: "Google")

O algoritmo funciona da seguinte forma:

1. Se a palavra tiver menos de 2 caracteres, o uso é sempre considerado correto
2. Se os dois primeiros caracteres forem maiúsculos, todas as letras restantes também devem ser maiúsculas
3. Se o primeiro caractere for maiúsculo e o segundo for minúsculo, todas as letras restantes devem ser minúsculas
4. Se o primeiro caractere for minúsculo, todas as letras restantes também devem ser minúsculas

**Complexidade de Tempo:** O(n), onde n é o comprimento da palavra.

**Complexidade de Espaço:** O(1), pois utiliza apenas variáveis simples independente do tamanho da entrada.
