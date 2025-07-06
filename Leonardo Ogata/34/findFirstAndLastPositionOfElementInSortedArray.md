# Find First and Last Position of Element in Sorted Array

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Find First and Last Position of Element in Sorted Array é encontrar a primeira e a última ocorrência de um target no array, porém o algoritmo precisa ter a complexidade de $\log_{n}$. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
def searchRange(self, nums: List[int], target: int) -> List[int]:
    # Caso base
    if not nums:
        return [-1, -1]

    # Define limite inferior 
    low = 0
    # Define limite superior
    high = len(nums)
    # Array para armazenar a resposta
    arr = []
    
    # Loop de binary search
    while low <= high:
        
        # Define o meio
        mid = low + (high - low) // 2

        # Caso o meio seja maior que o tamanho do array o loop é quebrado
        if mid >= len(nums):
            break
        
        # Caso o valor de mid seja igual ao target é verificado até onde ele aparece
        if nums[mid] == target:
            # Itera do meio para trás para procurar a primeira aparição
            for i in range(mid -1, -1, -1):
                # Caso o número seja igual ao target seu index é armazenado
                if nums[i] == target:
                    arr.append(i)
                # Caso o número não seja igual ao target o loop é quebrado
                else:
                    break
            
            # Itera do meio para frente para procurar a última aparição
            for i in range(mid, len(nums)):
                # Caso o número seja igual ao target seu index é armazenado
                if nums[i] == target:
                    arr.append(i)
                # Caso o número não seja igual ao target o loop é quebrado
                else:
                    break
            
            # Caso o item apareça apenas uma vez é retornado a mesma posição para primeira e última aparição
            if len(arr) == 1:
                return [arr[0], arr[0]]
            # Caso o item apareça mais de uma vez é retornado o menor index e o maior
            else:
                return(min(arr), max(arr))
        
        # Caso o valor de mid seja menor que o target o limite inferior é atualizado
        elif nums[mid] < target:
            low = mid + 1
        
        # Caso o valor de mid seja maior que o target o limite superior é atualizado
        elif nums[mid] > target:
            high = mid - 1

    # Caso o array esteja vazio o target não está presente
    if not arr:
        return [-1, -1]
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($\log_{n} + k$), onde n é o tamanho do array.
- Espaço: O uso de espaço adicional é O(${n}$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata70.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
