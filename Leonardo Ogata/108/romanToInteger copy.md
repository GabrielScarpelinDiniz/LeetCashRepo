# Convert Sorted Array to Binary Search Tree

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Convert Sorted Array to Binary Search Tree é converter um array ordenado de forma crescente pra uma arvore equilibrada

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```java
def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
```


## Complexidade
- Tempo: O algoritmo possui complexidade O(${n \log{n}}$), onde n é tamanho da string s.

- Espaço: O uso de espaço adicional é O(n), pois o algoritmo cria arrays auxiliares.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata26.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
