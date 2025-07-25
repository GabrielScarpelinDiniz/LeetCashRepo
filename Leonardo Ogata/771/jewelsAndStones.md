# Jewels and Stones

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Jewels and Stones é descobrir quantas joias (caracteres da string jewels) existem entre as pedras (caracteres da string stones)

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Dicionário para armazenar quantidades de cada pedra
        dic = {}
        # Vaiável para armazenar a quantidade de joias
        summer = 0

        # Itera sobre a string stones
        for i in stones:
            # Caso o caractere não esteja no dicionário ele é adicionado
            if i not in dic:
                dic[i] = 1
            # Caso ele esteja no dicionário é adicionado um ao seu valor
            else:
                dic[i] += 1

        # Itera sobre a string joias
        for i in jewels:
            # Se uma das joias estiver no dicionário a quantidade de joias presentes é adicionada na variável
            if i in dic:
                summer += dic[i]
        
        # Retorna variável de soma
        return summer
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n$), onde n é o valor n.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata89.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
