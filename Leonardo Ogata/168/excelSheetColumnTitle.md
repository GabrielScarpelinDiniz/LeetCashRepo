# Excel Sheet Column Title

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Excel Sheet Column Title é dado um número identificar qual conjunto de letras ele representa em uma linha no excel

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # String que vai receber o resultado
        result = "" 

        # Itera enquanto número for maior que 0
        while columnNumber > 0:
            # Ajuste do valor
            columnNumber -= 1  
            # Atribui o valor do número atual em letra e adiciona no resultado
            result = chr((columnNumber % 26) + 65) + result
            # Atualiza o valor do número
            columnNumber //= 26

        return result
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$), onde n é o tamanho da entrada.

- Espaço: O uso de espaço adicional é O($\log{n}$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata33.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
