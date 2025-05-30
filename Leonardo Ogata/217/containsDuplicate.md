# Contains Duplicate

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Contains Duplicate é identificar se existem números duplicados em um array.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Array de numeros é ordenado
        nums.sort()

        # Itera sobre o array
        for x in range(1, len(nums)):
            # Caso um número seja igual a seu anterior é retornado verdadeiro
            if nums[x] == nums[x -1]:
                return True
        # caso nenhum número duplicado seja encontrado é retornado Falso
        return False
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n\log{n}$), onde n é o tamanho da string.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata32.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
