# Intersection of Two Arrays

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Intersection of Two Arrays é identificar os número que estão presentes em ambos arrays

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Define qual o maior e o menor array
        if len(nums1) > len(nums2):
            longer, shorter = nums1, nums2
        else:
            shorter, longer = nums1, nums2

        # Cria array auxiliar para armazenar resposta
        auxArr = []

        # Itera sobre o array menor
        for i in range(len(shorter)): 
            # Verifica se o item i está presente no array maior e remove ele do array maior
            if shorter[i] in longer:
                auxArr.append(shorter[i])
                longer.pop(longer.index(shorter[i]))

        # Retorna o array auxiliar  
        return auxArr
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n1 * n2), onde n1 é o tamanho do array1 e n2 é o tamanho do array2.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata55.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
