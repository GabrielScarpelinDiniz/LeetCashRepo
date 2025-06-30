# First Unique Character in a String

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema First Unique Character in a String é identificar qual o primeiro caractere que não se repete em uma string

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def firstUniqChar(self, s: str) -> int:
        # Cria dicionário com quantidade de vezes que cada letra aparece
        dick = Counter(s)

        # Itera sobre o dicionário
        for i in dick:
            # Se o caractere aparecer só uma vez é retornado pois o dicionário está em oredm
            if dick[i] == 1:
                return s.index(i) 
        # Caso nenhum seja único é retornado -1
        return -1
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho da string.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata61.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
