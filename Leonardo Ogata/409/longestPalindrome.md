# Longest Palindrome

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Longest Palindrome é determinar o tamanho do maior palindromo que pode ser contruido a partir da string s

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def longestPalindrome(self, s: str) -> int:
    # Cria dicionário para contagem de caracteres
    dic = {}

    # Loop que determina quantas vezes cada caractere aparece na string
    for i in s:
        if i not in dic:
            dic[i] = 1 
        else:
            dic[i] += 1 

    # Variável que armazena soma da quantiadade caracteres simétricos
    summer = 0
    # Variável que armazena a existência (ou inexistência) de número que aparecem uma qunatidade ímpar de vezes
    isEven = False

    # Itera sobre o dicionário
    for i in dic:
        # Caso o valor seja par ele é adicionado a soma pois ele é simétrico
        if dic[i] % 2 == 0:
            summer += dic[i]
        # Caso o valor seja impar ele é adicionado na soma -1 para torna-lo simétrico e a variável isEven se torna verdadeira
        else:
            isEven = True
            summer += dic[i] - 1

    # Caso a variável even seja verdadeira é somado um a summer pois podemos ter um número não simétrico no meio do palindromo, caso o contrário é retornado summer
    return summer + 1 if isEven else summer
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho de s.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata77.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
