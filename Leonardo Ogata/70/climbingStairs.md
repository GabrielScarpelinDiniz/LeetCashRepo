# Climbing stairs

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Climbing stairs é encontrar a quantidade de formas que uma pessoa pode subir uma escada com n números de degraus utilizando 1 ou 2 passos.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```java
public int climbStairs(int n) {
        // Cria o array pra programação dinâmica
        int[] DP = new int[n + 1];

        // Define os valores iniciais
        DP[0] = 1;
        DP[1] = 1;

        // Itera sobre o array para definir os novos valores
        for(int i = 2; i < n + 1; i++){
            // Os valores de DP[n] é definido pela soma de possibilidades de DP[n-1] + DP[n-2]
            DP[i] = DP[i - 1] + DP[i - 2];
        }

        // Retorna o valor
        return DP[n];
    }       
```

## Lógica do Algoritmo
- Cria o array para programação dinâmica
- Define os valores iniciais
- Com base nos valores iniciais calcula os valores futuros
- Retorna o número de possibilidades para n degraus


## Complexidade
- Tempo: O algoritmo possui complexidade O(${n}$), onde n é o valor do número `n`.

- Espaço: O uso de espaço adicional é O(n), onde n é o valor do número `n`.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata16.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
