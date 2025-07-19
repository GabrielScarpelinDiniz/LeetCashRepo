# Defanging an IP Address

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Defanging an IP Address é substituir os "." de um IP por "[.]"


&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def defangIPaddr(self, address: str) -> str:
    # String que recebe a resposta
    ans = ""

    # Itera sobre o IP
    for i in address:
        # Caso o caractere seja "." é adicionado um "[.]" a resposta
        if i == ".":
            ans += "[.]"
        # Caso o caractere seja qualquer outro valor ele é adicionado a resposta
        else:
            ans += i
    
    # Retorna a resposta
    return ans
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho do IP.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata83.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
