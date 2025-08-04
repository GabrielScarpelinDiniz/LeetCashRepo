# 904. Fruit Into Baskets

## Problema

Você está visitando uma fazenda que tem uma única fileira de árvores frutíferas organizadas da esquerda para a direita. As árvores são representadas por um array de inteiros `fruits`, onde `fruits[i]` é o tipo de fruta que a árvore `i` produz.

Você quer coletar o máximo de frutas possível. No entanto, o dono tem algumas regras estritas que você deve seguir:

1. Você só tem duas cestas, e cada cesta só pode conter um único tipo de fruta.
2. Não há limite para a quantidade de frutas que cada cesta pode conter.
3. Começando de qualquer árvore de sua escolha, você deve pegar exatamente uma fruta de cada árvore (incluindo a árvore inicial) enquanto se move para a direita. As frutas colhidas devem caber em uma das suas cestas.
4. Assim que você alcançar uma árvore com frutas que não podem caber em suas cestas, você deve parar.

Dado o array de inteiros `fruits`, retorne o número máximo de frutas que você pode colher.

### Exemplo 1:

**Entrada:**

```
fruits = [1,2,1]
```

**Saída:**

```
3
```

**Explicação:**
Podemos colher de todas as 3 árvores.

### Exemplo 2:

**Entrada:**

```
fruits = [0,1,2,2]
```

**Saída:**

```
3
```

**Explicação:**
Podemos colher das árvores `[1,2,2]`. Se tivéssemos começado na primeira árvore, colheríamos apenas das árvores `[0,1]`.

### Exemplo 3:

**Entrada:**

```
fruits = [1,2,3,2,2]
```

**Saída:**

```
4
```

**Explicação:**
Podemos colher das árvores `[2,3,2,2]`. Se tivéssemos começado na primeira árvore, colheríamos apenas das árvores `[1,2]`.

### Restrições:

- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

## Solução

A solução utiliza a técnica de janela deslizante (sliding window) para encontrar o maior subarray que contém no máximo dois tipos de frutas. Usamos um dicionário para rastrear a contagem de cada tipo de fruta na janela atual.

### Complexidade

- **Tempo:** O(n), onde `n` é o tamanho do array `fruits`.
- **Espaço:** O(1) para armazenar no máximo dois tipos de frutas no dicionário.
