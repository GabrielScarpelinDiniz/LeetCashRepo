# Number of 1 Bits

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Number of 1 Bits é retornar quantas vezes o número 1 aparece no binário de um número

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Converte o valor do número para binário
        binary_value = int(bin(n)[2:])

        # Inicia contador dos números 1
        counter = 0 

        while binary_value > 0:
            #Verifica se o número de trás é 1
            if binary_value % 10 == 1:
                counter += 1

            # Remove o número de trás
            binary_value /= 10

        # Retorna quantas vezes o número 1 aparece
        return counter
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$), onde n é o tamanho do número.

- Espaço: O uso de espaço adicional é O($\log{n}$), onde n é o tamanho do número.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata37.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
