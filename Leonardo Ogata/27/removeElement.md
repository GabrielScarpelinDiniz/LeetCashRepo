# Remove Element

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Remove Element é remover os número escolhidos de um array ordenado. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public int removeElement(int[] nums, int val) {

        // Cria um array dinâmico para guardar a lista filtrada
        ArrayList<Integer> filteredList = new ArrayList<>();

        // Loop que itera sobre o array
        for (int i = 0; i < nums.length; i++) {

            // Caso o número seja diferente do valor que deve ser removido ele é adicionado ao array dinamico
            if (nums[i] != val) {
                filteredList.add(nums[i]);
            }
        }


        // Os itens do array dinâmico são colados por cima do array original
        for (int i = 0; i < filteredList.size(); i++) {
            nums[i] = filteredList.get(i);
        }

        // O tamanho do array dinâmico é retornado
        return filteredList.size();
    }
```

## Lógica do Algoritmo
- Após a criação do array dinâmico o loop itera sobre o array `nums`
    - Caso o valor de  `nums[i]` seja diferente do valor `val` (Valor que deve ser removido) o valor de `nums[i]` é adicionado ao array dinâmico
- Ao fim do loop os itens do array dinâmico são colados em ordem por cima dos itens do array original
> Deixando claro que o problema deixa explicito que os itens após os números ordenados não são levados em consideração, por isso o array fica "bagunçado" no final
- É retornado o tamanho do array dinâmico que representa a quantidade de números diferentes de `val`.

## Complexidade
- Tempo: O algoritmo possui complexidade O(${n}$), onde n é o tamanho do array.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é o tamanho do array.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata8.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
