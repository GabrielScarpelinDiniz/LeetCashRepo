## 3Sum

O método `ThreeSum` encontra todos os tripletos únicos em um array que somam zero.

### Funcionamento:

1. Ordena o array para facilitar a busca de combinações.
2. Usa um loop para fixar o primeiro número e dois ponteiros (esquerdo e direito) para encontrar os outros dois números.
3. Evita duplicatas ao pular números repetidos.
4. Adiciona os tripletos que somam zero à lista de resultados.

### Exemplos:

- Entrada: `nums = [-1,0,1,2,-1,-4]` → Saída: `[[-1,-1,2],[-1,0,1]]`
- Entrada: `nums = [0,1,1]` → Saída: `[]`
- Entrada: `nums = [0,0,0]` → Saída: `[[0,0,0]]`

### Complexidade:

- **Tempo:** O(n²), onde `n` é o tamanho do array, devido ao loop e busca com dois ponteiros.
- **Espaço:** O(1) adicional, desconsiderando o espaço para a saída.

Se precisar de ajustes ou novos exemplos, é só avisar! 🚀
