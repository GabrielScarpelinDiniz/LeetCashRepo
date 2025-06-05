# Power of Two

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Power of Two é identificar se n pode ser escrito como uma potência de dois.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def isPowerOfTwo(self, n):
            """
            :type n: int
            :rtype: bool
            """
            # Valor da potência
            power = None
            # Contador
            counter = -1

            # Loop enquanto a potência for menor que o valor de n
            while power < n:
                counter += 1 
                power = 2 ** counter
            
            # Caso a potência seja igual a n retorne Verdadeiro, caso o contrário retorne Falso
            return True if power == n else False
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$), onde n é o número.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata39.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
