# Valid Perfect Square

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Intersection of Valid Perfect Square é identificar se um número é um quadrado perfeito ou não

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Define limite inferior
        low = 0
        # Define limite superior
        high = num
        # Define meio inicial
        mid = 0
        
        # Enquanto o valor do limite inferior for menor ou igual ao limite superior o loop ocorrerá
           while low <= high:
            
            # Define o meio com base na média do limite inferior e superiror
            mid = (low + high) // 2

            # Caso o valor do meio ao quadrado seja o num é retornado verdadeiro
            if mid * mid == num:
                return True
            
            # Caso o valor do meio ao quadrado seja maior que num o valor superior é limitado ao meio
            elif mid * mid > num:
                high = mid - 1

            # Caso o valor do meio ao quadrado seja menor que num o valor inferior é limitado ao meio
            elif mid * mid < num:
                low = mid + 1

        # Caso nenhum valor seja encontrado esse valor não possui um quadrado perfeito
        return False
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$), onde n é o valor de num.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata55.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
