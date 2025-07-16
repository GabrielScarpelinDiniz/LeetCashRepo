## Exercício: 48. Rotate Image
**Objetivo**: Dado uma matriz de inteiros que representa uma imagem, gire a imagem 90° em sentido horário. A rotação deve ser _in-place_.

## Descrição geral da estratégia
Para resolver primeiro faço a transposta da matriz ( elemento na linha $i$ e coluna $j$ é trocado pelo elemento da linha $j$ e coluna $i$). Em seguida, inverto os elementos da matriz no eixo x (primeiro elemento da linha é trocado pelo último).  

## Análise de complexidade
Para uma matriz $n \times n$, tem-se:
- **Time complexity**: $O(n^2)$ ( $\Theta(2n n^2)$ )
- **Space complexity**: $O(1)$ 