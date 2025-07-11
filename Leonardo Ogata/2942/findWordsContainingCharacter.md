# Find Words Containing Character

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Find Words Containing Character é retornar os índices de todas as palavras do array words que possuem o caractere x

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Array de resposta
        arr = []

        # Itera sobre o array
        for i in range(len(words)):
            # Se a palavra conter o caractere o seu índice é adicionanado ao array de respota
            if x in words[i]:
                arr.append(i)
        
        # Retorna o array de resposta
        return arr
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n * m), em que n representa é o tamanho do array e m o tamanho da string.
- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata75.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
