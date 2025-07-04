# Max Consecutive Ones

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Max Consecutive Ones é identificar a maior sequência de 1's no array

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Melhor global
        ans = 0
        # Melhor local
        current = 0

        # Itera sobre o array
        for i in range(len(nums)):
            # Se o item for 1 é somado um ao melhor local
            if nums[i] == 1:
                current += 1
            # Se o item for 0 é verificado se o melhor local é melhor que o global e o local é zerado
            elif nums[i] == 0:
                # Se o local for melhor que o global o global recebe o valor do local
                if current > ans:
                    ans = current
                current = 0
        
        # Após a última iteração é retornado o maior entre o local e o global
        return current if current > ans else ans
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o valor n.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata67.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
