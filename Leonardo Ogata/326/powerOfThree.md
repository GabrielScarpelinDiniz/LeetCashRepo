# Power of Three

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Power of Three é verificar se n é uma potência de 3.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def isPowerOfThree(self, n: int) -> bool:
    # Loop enquanto n for maior que um
    while n > 1:
        # Divide n por 3
        n /= 3
    
    # Caso após as divisões n seja igual a 1 é retornado verdadeiro, caso o contrário é retornado falso
    return True if n == 1 else False
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$), onde n é o número.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata52.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
