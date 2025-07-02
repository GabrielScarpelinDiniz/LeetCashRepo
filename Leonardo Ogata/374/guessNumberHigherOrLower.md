# Guess Number Higher or Lower

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Guess Number Higher or Lower é adivinhar qual número a máquina escolheu com as dicas se seu chute foi maior ou menor

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def guessNumber(self, n: int) -> int:
        # Limite superior
        high = n
        # Limite inferior
        low = 0

        # Loop para encontrar o valor
        while True:

            # Define meio entre superior e inferior
            mid = (low + high)//2

            # Se o resultado for 0 mid é o número escolhido pela máquina
            if guess(mid) == 0:
                return mid
            
            # Se o resultado for -1 o valor está abaixo do chutado pela máquina portanto o limite infeior é movido para o meio
            elif guess(mid) == -1:
                high = mid - 1
            
            # Se o resultado for 1 o valor está acima do chutado pela máquina portanto o limite supeiror é movid/o para o meio
            elif guess(mid) == 1:
                low = mid + 1
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$).

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata64.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
