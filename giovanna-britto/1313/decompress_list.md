# Quadragésimo Segundo Dia de LeetCash

Hoje resolvi o exercício 1313, que pede para descompactar uma lista codificada em RLE (run-length encoding). O array de entrada tem pares de valores: o primeiro é a frequência e o segundo é o valor a ser repetido. Preciso devolver a lista descompactada. Para isso eu segui os seguintes passos:

1. Criei três variáveis: `freq` para a frequência, `val` para o valor e `arr` para guardar o resultado.
2. Usei um for que vai de 2 em 2 no array `nums`:

    2.1. Pego a frequência em `nums[i]`.

    2.2. Pego o valor em `nums[i+1]`.

    2.3. Adiciono o valor repetido pela frequência na lista `arr`.

3. No final, retorno `arr` com a lista descompactada.

E pronto! Mais um exercício resolvido!