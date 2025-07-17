# Number Complement

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Number Complement é encontrar o número complementar de `num`

&nbsp;&nbsp;&nbsp;&nbsp; O complementar de um número é esse número em binário com os 0s e 1s trocados de lugar

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def findComplement(self, num: int) -> int:
    # Transforma o número em binário
    num = bin(num)
    # Recebe valor da resposta
    ans = ""
    
    # Itera sobre o número binário pulando '0b'
    for i in range(2, len(num)):
        # Caso o número seja 0, 1 é adicionado na string
        if num[i] == "0":
            ans += "1"
        # Caso o número seja 1, 0 é adicionado na string
        else:
            ans += "0"
    
    # Retorna a resposta no formato inteiro e converte da base 2
    return int(ans, 2)
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o valor n.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata80.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
