# String to Integer (atoi)

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema String to Integer (atoi) é transformar uma string em um inteiro seguindo a seguinte lista de critérios:

* **Whitespace**: Ignore any leading whitespace (" ").
* **Signedness**: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
* **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
* **Rounding**: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def myAtoi(self, s: str) -> int:
        # Armazena o resulta
        result = 0
        # Variável para identificar se é negativo
        isNegative = False

        # Remove o primeiro white space
        s = s.lstrip()

        # Verifica se restou algo
        if not s:
            return 0

        # Verifica se o número é negativo ou positivo
        if s[0] == "-": 
            # Define como negativo
            isNegative = True
            # Remove símbolo de negativo
            s = s[1:len(s)]
        elif s[0] == "+":
            # Remove símbolo de positivo
            s = s[1:len(s)]

        # Itera sobre a string
        for i in s:
            # Caso o item seja um digito é adicionado ao resultado
            if i.isdigit():
                result *= 10
                result += int(i)
            # Caso o item não seja um digito o loop é quebrado
            else:
                break
        
        # Transforma o número em negativo
        if isNegative:
            result *= -1

        # Garante o limite superior
        if result > 2**31 -1:
            result = 2**31 - 1

        # Garante o limite inferior
        elif result < -2**31:
            result = -2**31
        
        # Retorna o resultado
        return result  
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho da string.

- Espaço: O uso de espaço adicional é O(n), onde n é o tamanho da string.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata68.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
