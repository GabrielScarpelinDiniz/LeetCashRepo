## Next Permutation

O método `NextPermutation` encontra a próxima permutação lexicograficamente maior de um array de inteiros.

### Funcionamento:

1. **Encontrar pivot**: Procura da direita para esquerda o primeiro elemento que é menor que seu sucessor.
2. **Encontrar sucessor**: Se o pivot existe, encontra o menor elemento à direita que é maior que o pivot.
3. **Trocar**: Troca o pivot com seu sucessor.
4. **Reverter**: Reverte a parte à direita do pivot para obter a menor permutação possível.

### Algoritmo paso a paso:

- Se não há pivot (array em ordem decrescente), reverte todo o array
- Caso contrário, executa os 4 passos acima

### Exemplos:

- Entrada: `nums = [1,2,3]` → Saída: `[1,3,2]`
- Entrada: `nums = [3,2,1]` → Saída: `[1,2,3]`
- Entrada: `nums = [1,1,5]` → Saída: `[1,5,1]`

### Complexidade:

- **Tempo:** O(n), onde `n` é o comprimento do array.
- **Espaço:** O(1), usa apenas espaço constante adicional.

### Nota:

Este é o algoritmo clássico para gerar permutações em ordem lexicográfica.
