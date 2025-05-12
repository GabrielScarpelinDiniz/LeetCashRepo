# Three Consecutive Odds

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Three Consecutive Odds é retornar true caso existam 3 números impares consecutivos. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public boolean threeConsecutiveOdds(int[] arr) {

        // Itera sobre o array até que não seja possível olhar 3 números a frente
        for (int i = 0; i < arr.length - 2; i++) {
            // Verifica se os valores de i, i+1 e i+2 são impares
            if (arr[i] % 2 != 0 && arr[i + 1] % 2 != 0 && arr[i + 2] % 2 != 0) {
                return true;
            }
        }

        return false;
        
    }
```

## Lógica do Algoritmo
- O loop itera pelo array até que i + 2
    - Caso os números i, i+1 e i+2 sejam impares é retornado true
- Caso o loop chegue ao fim é retornado false

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n$), em que n representa o tamanho do.
- Espaço: O uso de espaço adicional é O($1$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata15.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
