# Merge Sorted Array

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Merge Sorted Array é mergear dois arrays ordenados de forma que eles continuem ordenados.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```java
public void merge(int[] nums1, int m, int[] nums2, int n) {

        // Copia o números do array 2 no final do array 1
        for (int i = 0; i < n; i++) {
            nums1[m + i] = nums2[i];
        }

        // Reordena o array 1
        Arrays.sort(nums1);
    }     
```

## Lógica do Algoritmo
- Copia o array 2 ao fim do array 1
- Reordena o array 1


## Complexidade
- Tempo: O algoritmo possui complexidade O(${n\log{n}}$), devido ao `.sort` do java.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata17.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
