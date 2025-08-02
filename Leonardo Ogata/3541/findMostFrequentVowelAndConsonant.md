# Find Most Frequent Vowel and Consonant

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Find Most Frequent Vowel and Consonant é encontrar a consoante e a vogal mais frequente em uma string e retornar a soma da frequência delas.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
def maxFreqSum(self, s: str) -> int:
        # Dicionário com todas as vogais
        vowels = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }

        # Dicionário com todas as consoantes
        consonants = {
            'b': 0,
            'c': 0,
            'd': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        
        # Itera sobre a string
        for i in s:
            # Caso o caractere seja uma vogal, a frequência dessa vogal é incrementada
            if i in vowels:
                vowels[i] += 1
            # Caso o caractere seja uma consoante, a frequência dessa consoante é incrementada
            else: 
                consonants[i] += 1
        
        # Retorna a soma da vogal e consoante mais frequente
        return max(vowels.values()) + max(consonants.values())
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n), em que n é o tamanho da string s.
- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata95.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
