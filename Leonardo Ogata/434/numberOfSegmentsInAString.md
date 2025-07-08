# Number of Segments in a String

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Number of Segments in a String é identificar quantos segmentos da string são separados por espaço

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def countSegments(self, s: str) -> int:
        # Caso a string seja vazi é retornado 0
        if not s:
            return 0
        
        # Array para armazenar todas palavras
        arr = []
        # Array para armazenar palavra atual
        aux = []

        # Itera sobre a string
        for i in range(len(s)):
            # Se o item atual for diferente de espaçamento ele é adicionado a palavra atual
            if s[i] != " ":
                aux.append(s[i])
            # Se o item for um espaçamento e o array com a palavra atual não estiver vazio a palavra é adicionado ao array principal e o array auxiliar é limpo
            elif s[i] == " " and aux:
                arr.append(aux)
                aux = []
        # Adiciona valor da última palavra caso ela seja existente
        if aux:
            arr.append(aux)
        
        # Retorna a quantidade de palavras
        return len(arr)
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o valor n.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata72.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
