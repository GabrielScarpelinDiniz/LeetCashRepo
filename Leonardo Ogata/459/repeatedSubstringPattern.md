# Repeated Substring Pattern

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Repeated Substring Pattern é verificar se a string s é composta por uma repetição de alguma de suas substrings 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def repeatedSubstringPattern(self, s: str) -> bool:
    # Armazena subtring
    ans = ""

    # Itera sobre a string
    for i in s:

        # Adiciona um caractere a subtrstring
        ans += i

        # Verifica as seguintes condições
        # Se a divisão do tamanho da string pela substring é um valor inteiro, caso o contrário a palavra não pode ser formada por uma repetição dessa substring
        # Se a substring repetida até o tamanho da string é igual a s
        # Se isso ocorreu apenas com a string inteira, pois isso não seria uma substring
        if len(s) % len(ans) == 0 and ans * (len(s) // len(ans)) == s and len(s) // len(ans) != 1:
            return True
    
    # Caso não seja encontrada até o final do loop é retornado falso
    return False
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho de s.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata86.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
