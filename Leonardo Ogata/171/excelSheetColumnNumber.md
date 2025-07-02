# Excel Sheet Column Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Excel Sheet Column Number é receber uma string com letras e retornar o número dessa coluna no excel

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def titleToNumber(self, columnTitle: str) -> int:
        # Resposta
        ans = 0

        # Dicionário com valores das letras
        dic = {"A": 1,
               "B": 2,
               "C": 3,
               "D": 4,
               "E": 5,
               "F": 6,
               "G": 7,
               "H": 8,
               "I": 9,
               "J": 10,
               "K": 11,
               "L": 12,
               "M": 13,
               "N": 14,
               "O": 15,
               "P": 16,
               "Q": 17,
               "R": 18,
               "S": 19,
               "T": 20,
               "U": 21,
               "V": 22,
               "W": 23,
               "X": 24,
               "Y": 25,
               "Z": 26,
                    }

        
        # Itera sobre a string
        for i in range(len(columnTitle)):
            # Adiciona a resposta o valor da letra vezes 26 elevado ao tamanho da string -1 - o número da iteração
            ans += dic[columnTitle[i]] * (26 ** (len(columnTitle) - 1 - i))
        
        # Retorna a resposta
        return ans
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho da string.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata66.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
