# Reverse Vowels of a String

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Reverse Vowels of a String é inverter a ordem de todas as vogais de uma palavra

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def reverseVowels(self, s: str) -> str:
            # Array para receber a palavra
            arr = []
            # Array para receber as vogais
            arrV = []   

            # Loop que itera sobre a palavra
            for x in s:
                # Caso a letra seja uma vogal é adicionada no arrV
                if (x == 'a' or x == 'e' or x == 'i' or 
            x == 'o' or x == 'u' or x == 'A' or 
            x == 'E' or x == 'I' or x == 'O' or 
            x == 'U'):
                    arrV.append(x)
                # Adiciona letra no arr
                arr.append(x)

            # Itera sobre o array da palavra
            for i in range(len(arr)):
                # Caso o item seja uma vogal esse item é substituido pelo último item do arrV
                if (arr[i] == 'a' or arr[i] == 'e' or arr[i] == 'i' or 
            arr[i] == 'o' or arr[i] == 'u' or arr[i] == 'A' or 
            arr[i] == 'E' or arr[i] == 'I' or arr[i] == 'O' or 
            arr[i] == 'U'):
                    arr[i] = arrV[-1]
                    # Remove último item do arrV
                    arrV.pop()
            
            # Concatena todos as letras do arr
            string = "".join(arr)

            # Retorna palavra com vogais invertidas
            return string
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho da palavra.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata63.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
