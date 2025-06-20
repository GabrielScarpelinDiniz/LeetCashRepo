## Task Scheduler

O método `LeastInterval` calcula o número mínimo de intervalos de CPU necessários para executar todas as tarefas, considerando um intervalo de resfriamento `n` entre tarefas iguais.

**Funcionamento:**

1. Conta a frequência de cada tarefa.
2. Encontra a frequência máxima (`maxFreq`) e quantas tarefas possuem essa frequência (`maxCount`).
3. Usa a fórmula: `(maxFreq - 1) * (n + 1) + maxCount` para calcular o número mínimo de intervalos necessários.
4. O resultado final é o maior entre o número de tarefas e o cálculo acima, pois pode haver tarefas suficientes para preencher todos os intervalos sem ociosidade.

**Exemplos:**

- Entrada: tasks = ["A","A","A","B","B","B"], n = 2 → Saída: 8
- Entrada: tasks = ["A","C","A","B","D","B"], n = 1 → Saída: 6
- Entrada: tasks = ["A","A","A", "B","B","B"], n = 3 → Saída: 10

**Complexidade de Tempo:** O(t), onde t é o número de tarefas.

**Complexidade de Espaço:** O(1), pois o array de frequência tem tamanho fixo (26 letras).
