# Reverse Integer

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Reverse Integer é inverter um inteiro e caso o inteiro ocupe mais que 32 bits retorne 0 .

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0

        if(x > 0):
            while(x > 0):
                reverse = (reverse * 10) + (x % 10)
                x = x/10
        else:
            x = x * -1
            while(x > 0):
                reverse = (reverse * 10) + (x % 10)
                x = x/10
            reverse = reverse * -1

        if (abs(reverse) > 2147483647):
            return 0
        return reverse
```

## Lógica do Algoritmo
- O número é mutiplicado por 10 e o resto da sua divisão por 10 é somado assim substuindo o lugar do 0
- Caso o número seja maior que 2147483647 é retornado 0

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho do inteiros.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata23.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
