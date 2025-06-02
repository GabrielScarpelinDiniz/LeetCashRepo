# Fizz Buzz

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Fizz Buzz é printar um array até um número `n`, porém se o número for divisível por 3 printar Fizz, por 5 Buzz e caso ele seja divisível por ambos ao mesmo tempo printar FizzBuzz.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Cria array para receber valores
        arr = []

        # Itera até o número n 
        for x in range(1, n + 1):
            # Caso o número seja divisível por 3 
            if x % 3 == 0:
                # Verifica se é divisível por 5
                if x % 5 == 0:
                    arr.append("FizzBuzz")
                else:
                    arr.append("Fizz")
            # Verifica se o númerpo só é divisível por 5
            elif x % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(x))
            
        return arr
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o valor de `n`.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata34.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
