# Richest Customer Wealth

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Richest Customer Wealth é iterar sobre uma matriz em que cada linha representa quanto cada cliente ganhou em cada mês e retornar o valor que cliente mais rico possui


&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Armazena o valor do cliente mais rico possui
        big = 0
        # Armazena o valor que o cliente atual possui
        aux = 0

        # Itera sobre a matirz
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                # Conta quanto o cliente atual tem
                aux += accounts[i][j]
            
            # Caso o cliente atual tenha um valor maior que o mais rico o valor big é atualizado
            if aux > big:
                big = aux
            
            # Zera o valor do cliente atual para o próximo loop
            aux = 0
        
        # Retorna o valor que o cliente mais rico possui
        return big
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n^2$), onde n é o tamanho da matriz.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata92.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
