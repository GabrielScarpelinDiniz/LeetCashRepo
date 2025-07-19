# Assign Cookies

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Assign Cookies é satisfazer a maior quantidade de crinças de acordo com sua ganancia e o tamanho do cookie 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Ordena o array das crianças e dos cookies
        g.sort()
        s.sort()

        # Cria ponteiro para as crianças 
        pointerG = 0
        # Cria ponteiro para os cookies
        pointerS = 0
        
        # Itera pelos arrays
        while pointerS < len(s) and pointerG < len(g):
            # Caso o cookie satisfaça a criança o ponteiro da criança é movido para frente
            if s[pointerS] >= g[pointerG]:
                pointerG += 1
            # Ponteiro do cookie é movido para frente após cada iteração
            pointerS += 1

        # Retorna o ponteiro da criança que representa quantas crianças foram atendidas
        return pointerG
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n\log_{n} + m\log_{m}$), onde n é tamanho do array g e m é o tamanho do array s.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata82.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
