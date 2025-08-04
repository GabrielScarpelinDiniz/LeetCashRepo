# Fibonacci Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Fibonacci Number é calcular a soma dos valores de fibonacci de n-1 + n-2

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def fib(self, n: int) -> int:
        # Casos base
        if n == 0:
            return 0
        elif n == 1 or n == 2:
                return 1

        # Calcula fibonacci
        def fibonacci(n: int):
            if n == 0:
                return 0

            elif n == 1 or n == 2:
                return 1

            else:
                return fibonacci(n-1) + fibonacci(n-2)

        # Variável para armazenar soma
        summer = 0

        # Soma o resultado de n-1 + n-2
        summer = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Retorna a soma
        return summer
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($2^n$), onde n é o valor de n.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata98.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
