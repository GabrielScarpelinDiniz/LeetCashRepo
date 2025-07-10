# Divisible and Non-divisible Sums Difference

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Divisible and Non-divisible Sums Difference é retornar a diferença entre num1 (a soma de todos os números de [1, n] não divisíveis por m) e num2 (a soma de todos os números de [1, n] divisíveis por m)

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
    def differenceOfSums(self, n: int, m: int) -> int:
        # Armazena soma dos números não divisíveis por m
        num1 = 0
        # Armazena soma dos números divisíveis por m
        num2 = 0
         
        # Itera sobre o intervalor
        for i in range(1, n + 1):
            # Caso o número não seja divisível ele é adicionado a num1
            if i % m != 0:
                num1 += i
            # Caso o número seja divisível ele é adicionado a num2
            else:
                num2 += i
        
        # Retorna a subtração de ambos
        return num1 - num2
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n), em que n representa é o tamanho do intervalo.
- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata74.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
