# Perfect Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Perfect Number é identificar se um número é perfeito ou não. Um número perfeito é um número cujo a soma dos seus divisores, sem contar o próprio número, é igual a ele mesmo.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def checkPerfectNumber(self, num: int) -> bool:
        # Caso Base
        if num <= 1:
            return False

        # Variável para armazenar a soma dos divisores
        summer = 0

        # Itera de 1 até a raiz quadrada de num truncada
        for i in range(1, int(num**0.5) + 1):
            # Caso i seja divisível por num é adicionado a soma
            if num % i == 0:
                summer += i
                # num divido por i também é adicionado  não ser que seja o próprio número
                if num//i != num:
                    summer += num//i 

        # Retorna se summer e nums possuem o mesmo valor
        return summer == nums
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\sqrt{n}$), onde n é o valor de num.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata100.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
