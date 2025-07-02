# Find All Numbers Disappeared in an Array

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Find All Numbers Disappeared in an Array é identificar os número que estão ausentes em no array

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Cria dicionário para consulta
        has = {}
        # Cria array para resposta
        ans = []

        # Itera sobre o array
        for i in nums:
            # Caso o item não esteja presente no dicionáro ele é adicionado
            if i not in has:
                has[i] = 1
        
        # Itera sobre os número de  1 a n   
        for i in range(1, len(nums) + 1):
            # Caso o número não esteja presente no dicionário ele é adicionado ao array de resposta
            if i not in has:
                ans.append(i)
        
        # Retorna o array de resposta
        return ans
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o valor n.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata65.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
