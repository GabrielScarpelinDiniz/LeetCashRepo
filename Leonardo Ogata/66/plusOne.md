# Plus One

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Plus one é receber um array que representa um digito adicionar 1 a esse digito e retorna em forma de array. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public int[] plusOne(int[] digits) {
        // Itera sobre o array e trás pra frente
        for (int i = digits.length - 1; i >= 0; i--) {
            // Se o número for menor que 9 é só adiciona 1
            if (digits[i] < 9) {
                digits[i]++;
                return digits; 
            }
            // Se o digito for 9 ele se torna 0
            digits[i] = 0; 
        }
        
        // Cria um array com um número a mais 
        int[] result = new int[digits.length + 1];
        // Coloca 1 no primeiro item
        result[0] = 1; 
        return result;
    }
```

## Lógica do Algoritmo
- Itera sobre array de trás pra frente
    - Se o digito for menor que 9 é só adicionar um e retornar o array
- Se o loop terminar e o último número for nove é necessário aumentar o tamanho do array e transformar o primeiro número em nove
    

## Complexidade
- Tempo: O algoritmo possui complexidade de O($n$), onde n é o tamanho do array.
- Espaço: O uso de espaço adicional é O($1$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata12.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
