# The Two Sneaky Numbers of Digitville


&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema The Two Sneaky Numbers of Digitville é retornar os itens que se repetem na lista

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Dicionário para verificar itens da lista
        dic = {}
        # Array com números repetidos
        ans = []

        # Itera pelo array
        for i in nums:
            # Caso o número não esteja no dicionário ele é adicionado
            if i not in dic:
                dic[i] = 1
            # Caso ele já esteja no dicionário ele é adicionado ao array de número repetidos
            else:
                ans.append(i)
        
        # Retorna o array de número repetidos
        return ans
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n), em que n representa é o tamanho do array.
- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata93.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
