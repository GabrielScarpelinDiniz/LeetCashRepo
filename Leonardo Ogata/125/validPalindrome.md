# Valid Palindrome

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Valid Palindrome é receber uma string, remover todos espaços, caracteres especiais e letras maiúsculas e validar se essa string é um palindromo ou não. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
 def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remover todos caracteres não alfa numéricos
        s = ''.join([char for char in s if char.isalnum()])
        # Transforma todos caracteres em minusculo
        s = s.lower()

        print(s)

        # Cria versão invertida para comparação
        inverted = s[::-1]
        
        print(inverted)

        # Retorna se é um palindromo ou não
        return s == inverted
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n$), onde n é o tamanho do array.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é o tamanho do array.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata22.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
