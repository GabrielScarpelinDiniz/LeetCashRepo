# Search Insert Position

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Search Insert Position é encontrar o index do item procurado e caso ele não exista no array o programa deve retornar o index de onde ele deveria ser posicionado no array. Tudo isso deve ser feito com uma complexidade de O(${\log{n}}$). 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public int searchInsert(int[] nums, int target) {

        //Cria variável para armazenar o início do array
        int low = 0;
        
        //Cria variável para armazenar o fim do array
        int high = nums.length - 1;

        //Cria variável para armazenar o meio do array
        int mid = 0;


        // Loop até que não exista espaço entre o fim e o começo
        while (low <= high) {

            // Calcula o meio do array
            mid = low + (high - low) / 2;

            // Caso o meio seja igual ao target o valor desse índice é retornado
            if (nums[mid] == target){
                return mid;
            }

            // Caso o meio seja menor que o target o valor de low é redefinido para a maior metade do array
            if (nums[mid] < target){
                low = mid + 1;
            }

            // Caso o contrário o valor de high é redefinido para a menor metade do array
            else{
                high = mid - 1;
            }
        }

        // Caso o numéro não tenha sido encontrado e ele seja maior que o mid atual, logo ele seria inserido uma casa a frente
        if (target > nums[mid]) {
            return mid + 1;
        }
        
        // Caso o contrário ele seria inserido na posição do mid atual
        else{
            return mid;
        }
        
        
    }
```

## Lógica do Algoritmo
- É aplicado um bubble sort no array `nums`.
- Caso o `target` não seja encontrado é analisado se ele é maior ou menor que o último valor `mid`
    - Caso o valor seja maior que mid ele deverá ser inserido uma posição a frente
    - Caso o contrário ele deve ser inserido na posição desse item
    > Essa última parte foi um pouco contra intuitiva, mas é como o exemplo de corrida, se eu ultrapasso o segundo lugar eu sou o novo segundo lugar e não o primeiro.

## Complexidade
- Tempo: O algoritmo possui complexidade de O(${\log{n}}$), onde n é o tamanho do array `nums`, deixando claro que só fiz essa complexidade pq era oque pedia pq por mim eu só iterava sobre o array é isso, pra que essa qualidade toda papai?
- Espaço: O uso de espaço adicional é O(${1}$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata10.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
