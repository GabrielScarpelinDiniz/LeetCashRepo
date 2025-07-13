## Jump Game II

O método `Jump` calcula o número mínimo de saltos para chegar ao último índice do array.

### Funcionamento:

1. Percorre o array mantendo o alcance máximo (`farthest`) que pode ser atingido.
2. Quando chega ao final do alcance atual (`currentEnd`), incrementa o número de saltos e atualiza o alcance.
3. Repete até alcançar o final do array.

### Exemplos:

- Entrada: `nums = [2,3,1,1,4]` → Saída: `2`
- Entrada: `nums = [2,3,0,1,4]` → Saída: `2`

### Complexidade:

- **Tempo:** O(n), onde `n` é o tamanho do array.
- **Espaço:** O(1), pois utiliza apenas variáveis auxiliares.

Se precisar de mais alguma coisa, é só avisar! 🚀
