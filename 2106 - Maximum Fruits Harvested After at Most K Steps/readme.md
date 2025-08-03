# 2106. Maximum Fruits Harvested After at Most K Steps

## Problema

Frutas estão disponíveis em algumas posições em um eixo x infinito. Você recebe um array 2D `fruits` onde `fruits[i] = [positioni, amounti]` descreve `amounti` frutas na posição `positioni`. O array `fruits` já está ordenado por `positioni` em ordem crescente, e cada `positioni` é único.

Você também recebe um inteiro `startPos` e um inteiro `k`. Inicialmente, você está na posição `startPos`. De qualquer posição, você pode andar para a esquerda ou para a direita. Leva um passo para mover uma unidade no eixo x, e você pode andar no máximo `k` passos no total. Para cada posição que você alcançar, você colhe todas as frutas naquela posição, e as frutas desaparecerão daquela posição.

Retorne o número máximo total de frutas que você pode colher.

### Exemplo 1:

**Entrada:**

```
fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
```

**Saída:**

```
9
```

**Explicação:**

- Mova para a direita até a posição 6 e colha 3 frutas.
- Mova para a direita até a posição 8 e colha 6 frutas.
  Você se moveu 3 passos e colheu 3 + 6 = 9 frutas no total.

### Exemplo 2:

**Entrada:**

```
fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
```

**Saída:**

```
14
```

**Explicação:**

- Colha as 7 frutas na posição inicial 5.
- Mova para a esquerda até a posição 4 e colha 1 fruta.
- Mova para a direita até a posição 6 e colha 2 frutas.
- Mova para a direita até a posição 7 e colha 4 frutas.
  Você se moveu 1 + 3 = 4 passos e colheu 7 + 1 + 2 + 4 = 14 frutas no total.

### Exemplo 3:

**Entrada:**

```
fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
```

**Saída:**

```
0
```

**Explicação:**
Você pode andar no máximo `k = 2` passos e não pode alcançar nenhuma posição com frutas.

### Restrições:

- `1 <= fruits.length <= 10^5`
- `fruits[i].length == 2`
- `0 <= startPos, positioni <= 2 * 10^5`
- `positioni-1 < positioni` para qualquer `i > 0` (indexado em 0).
- `1 <= amounti <= 10^4`
- `0 <= k <= 2 * 10^5`

## Solução

A solução utiliza prefixos acumulados para calcular a soma de frutas em intervalos específicos de forma eficiente. Para cada posição inicial, calculamos o número máximo de frutas que podem ser colhidas dentro do limite de passos `k`.

### Complexidade

- **Tempo:** O(n), onde `n` é o número de posições em `fruits`.
- **Espaço:** O(n) para armazenar os prefixos acumulados.
