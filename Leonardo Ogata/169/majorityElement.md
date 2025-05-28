# Majority Element

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Majority Element é encontrar o número mais frequente numa lista

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Cria um dicionário com a quantidade de vezes que o número aparece
        dic = Counter(nums)
        
        # Retorna o item que mais aparece
        return dic.most_common(1)[0][0]
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho da string.

- Espaço: O uso de espaço adicional é O(n), onde n é o tamanho da string.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata30.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
