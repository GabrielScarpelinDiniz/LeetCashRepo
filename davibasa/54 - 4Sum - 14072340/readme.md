## 4Sum

O método `FourSum` encontra todos os quadrupletos únicos em um array que somam um valor alvo específico.

### Funcionamento:

1. **Ordenação**: Ordena o array para facilitar a busca e evitar duplicatas.
2. **Dois loops externos**: Fixa os dois primeiros números do quadrupleto.
3. **Dois ponteiros**: Usa técnica de dois ponteiros para encontrar os outros dois números.
4. **Evita duplicatas**: Pula números repetidos em todas as posições.
5. **Overflow protection**: Usa `long` para evitar overflow na soma.

### Exemplos:

- Entrada: `nums = [1,0,-1,0,-2,2], target = 0`
  Saída: `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`
- Entrada: `nums = [2,2,2,2,2], target = 8`
  Saída: `[[2,2,2,2]]`

### Complexidade:

- **Tempo:** O(n³), onde `n` é o tamanho do array.
- **Espaço:** O(1) adicional, desconsiderando o espaço para a saída.

### Nota:

Esta é uma extensão natural do problema 3Sum, usando a mesma técnica de dois ponteiros.
