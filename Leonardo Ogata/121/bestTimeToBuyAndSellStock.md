# Best Time to Buy and Sell Stock

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Best Time to Buy and Sell Stock é receber um array de dias contendo o valor de ações e definir qual o melhor dia para comprar ou vender essas ações. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    # Cria ponteiro pra dia de compra
    left = 0
    # Cria ponteiro pra dia de venda
    right = 1
    # Armazena o valor máximo de lucro
    maxValue = 0

    # Itera pelo array até que o dia de venda alcance a última posição
    while right < len(prices):
        # Caso o dia de venda tenha um valor menor que o dai de compra dia de venda se torna o novo dia de compra 
        if prices[left] > prices[right]:
            left = right
        # Caso o contrário é verificado se o lucro é maior do que o lucro registrado
        else: 
            # Caso sim o novo lucro é salvo
            if prices[right] - prices[left] > maxValue:
                maxValue = prices[right] - prices[left]
        # Ponteiro de venda anda um para frenete
        right += 1

    # Retorna o maior valor 
    return maxValue
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n$), onde n é o tamanho do array.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é o tamanho do array.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata29.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
