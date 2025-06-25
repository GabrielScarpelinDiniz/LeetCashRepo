## Candy

O método `Candy` resolve o problema de distribuição mínima de doces para crianças em uma linha, atendendo aos seguintes critérios:

1. Cada criança deve receber pelo menos um doce.
2. Crianças com uma classificação maior devem receber mais doces do que seus vizinhos.

**Funcionamento:**

1. Inicializa um array de doces com 1 doce para cada criança.
2. Faz uma passagem da esquerda para a direita, garantindo que cada criança com classificação maior que a anterior receba mais doces.
3. Faz uma passagem da direita para a esquerda, garantindo que cada criança com classificação maior que a próxima receba mais doces.
4. Soma o total de doces distribuídos.

**Exemplo:**

- Entrada: `ratings = [1,0,2]`  
  Saída: `5`  
  Explicação: Aloca 2, 1 e 2 doces respectivamente.

- Entrada: `ratings = [1,2,2]`  
  Saída: `4`  
  Explicação: Aloca 1, 2 e 1 doces respectivamente.

**Complexidade de Tempo:** O(n), onde n é o número de crianças.

**Complexidade de Espaço:** O(n), devido ao array auxiliar de doces.
