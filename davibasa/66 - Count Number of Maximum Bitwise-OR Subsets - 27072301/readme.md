## Count Number of Maximum Bitwise-OR Subsets

O método `CountMaxOrSubsets` retorna o número de subconjuntos não vazios cujo OR bit a bit é igual ao maior OR possível de qualquer subconjunto.

### Funcionamento:

1. **Cálculo do OR máximo**: Faz o OR de todos os elementos para obter o valor alvo.
2. **Busca por subconjuntos**: Usa backtracking para testar todos os subconjuntos possíveis.
3. **Contagem**: Soma todos os subconjuntos cujo OR é igual ao máximo.

### Exemplos:

- Entrada: `nums = [3,1]` → Saída: `2`
- Entrada: `nums = [2,2,2]` → Saída: `7`
- Entrada: `nums = [3,2,1,5]` → Saída: `6`

### Complexidade:

- **Tempo:** O(2^n), onde n é o tamanho do array (até 16).
- **Espaço:** O(n) para a pilha de recursão.

### Nota:

Como n ≤ 16, é viável testar todos os subconjuntos usando backtracking.
