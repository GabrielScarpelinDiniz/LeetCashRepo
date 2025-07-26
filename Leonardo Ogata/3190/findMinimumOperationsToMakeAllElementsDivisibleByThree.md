# Find Minimum Operations to Make All Elements Divisible by Three

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Find Minimum Operations to Make All Elements Divisible by Three é retornar a quantidade de operações necessárias para tornar todos elementos do array divisíveis por 3

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
    def minimumOperations(self, nums: List[int]) -> int:
        # Variável para contar número de operações
        counter = 0

        # Itera sobre o array
        for i in nums:
            # Caso o número não seja divisível por 3 é adicionado uma operação à variável
            if i % 3 != 0:
                counter += 1
        
        # Retorna a quantidade de operações
        return counter
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n), em que n representa é o tamanho do array .
- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata90.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
