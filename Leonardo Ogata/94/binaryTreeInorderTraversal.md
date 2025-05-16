# Binary Tree Inorder Traversal

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Binary Tree Inorder Traversal é retornar uma árvore inorder ao receber seu nó raiz. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    // Cria lista para armazenar os valores
    List<Integer> ans = new ArrayList<>();

    public List<Integer> inorderTraversal(TreeNode root) {
        // Chama o método inorder
        inOrder(root);
        // Retornar a lista
        return ans;
    }

    private void inOrder(TreeNode node){
        // Caso o nó seja nulo retorna para a próxima iteração
        if (node == null) {
            return;
        }
        // Explora até o nó mais a esquerda
        inOrder(node.left);
        // Adiciona o valor a lista 
        ans.add(node.val);
        // Explora o valor a direita 
        inOrder(node.right);
    }
```

## Lógica do Algoritmo
- Honestamente n sei nem o que explicar nessa aqui é literalmente só fazer a inOrder Traversal

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n$), onde n é o tamanho da árvore.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é o tamanho da árvore.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata9.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
