# Happy Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Happy Number é retornar se um número ao repetidamente substituir a soma dos quadrados de seus dígitos por um novo número, eventualmente chega ao número 1.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def isHappy(self, n: int) -> bool:
    # Função que verifica se é um happy number
    def checkHappy(n, limit):
        # Caso o limite de iterações seja atingido o número não é um happy number
        if limit > 20:
            return False

        # Variável que armazena Soma dos dígitos de n
        ans = 0

        # Enquanto n for maior que 0 seus digitos são somatos
        while n > 0:
            # Soma o último digito no número ao quadrado
            ans += (n % 10)**2
            # Atualiza o valor de n
            n = n // 10
        
        # Caso o valor seja um n é um happy number, caso não o novo valor de n é retornado na função incrementando o limite
        return True if ans == 1 else checkHappy(ans, limit + 1)

    # Caso base
    if n == 1:
        return True
    # Chama a função
    else:
        return checkHappy(n, 0)
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log_{n}$), onde n é o tamanho do número.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata77.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
