# Transform Array by Parity

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Transform Array by Parity substituir os número pares de um array por 0, os impares por 1 e retornar o array ordenado

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
def transformArray(self, nums: List[int]) -> List[int]:
    # Array da respota
    ans = []
    # Número de zeros
    zeroes = 0
    # Número de ums
    ones = 0

    # Itera sobre o array
    for i in nums:
        # Caso o número seja par adiciona um ao número de zeros
        if i % 2 == 0:
            zeroes += 1
        # Caso o número seja impar adiciona um ao número de ums
        else:
            ones += 1

    # Adiciona primeiro os zeros ao array de resposta 
    for i in range(zeroes):
        ans.append(0)
    
    # Adiciona os ums ao array de resposta
    for i in range(ones):
        ans.append(1)

    return ans
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n), em que n é o tamanho do array nums.
- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata88.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
