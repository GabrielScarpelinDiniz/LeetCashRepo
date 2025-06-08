# Valid Anagram

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Valid Anagram é identificar se a string t pode ser um anagrama da string s.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Cria dicionário com itens da string s
        dicS = Counter(s)
        # Cria dicionário com itens da string t
        dicT = Counter(t)

        # Verifica se todos itens do dicionário S estão presentes no dicionário T
        return dicS == dicT
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n + m), onde n e m são o tamaho da string s e t.

- Espaço: O uso de espaço adicional é O(n + m).

<!-- <div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata41.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div> -->

Hoje sem foto pelo luto