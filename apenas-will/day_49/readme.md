## Exercício: 832. Flipping an Image
**Objetivo**: Dado uma matriz de bits que representa uma imagem, inverta-a horizontalmente e coloque-a em negativo (troque `0` por `1` e vice versa);

## Descrição geral da estratégia
Para resolver implementei uma abordagem _naive_ que percorre a matrix invertendo suas linhas e os seus bits.

## Análise de complexidade
Para uma matriz $n \times n$, tem-se:
- **Time complexity**: $O(2^n)$
- **Space complexity**: $O(1)$ (fiz a alteração in-place) 