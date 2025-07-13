# Is Subsequence

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Ransom Note é determinar se s for uma subquência de t

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def isSubsequence(self, s: str, t: str) -> bool:
        # Casos base
        if s == "":
            return True
        elif t == "":
            return False

        # Ponteiro S
        first = 0
        # Ponteiro T
        second = 0

        # Itera por toda a string t
        while second < len(t):
            # Se o valor de s e t forem o mesmo os ponteiros avançam em ambas strings
            if s[first] == t[second]:
                first += 1
                second += 1
            # Se o valor de s e t não forem o mesmo apenas o ponteiro t avança
            else:
                second += 1
            
            # Se toda string s for iterada é subsequência
            if first == len(s):
                return True

        # Caso ainda faltem caracteres de s não é subsquência
        return False 
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n + m), onde n é o tamanho de s e m é o tamanho de t.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata76.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
