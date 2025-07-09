# Third Maximum Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Third Maximum Number é identificar o terceiro número distinto de um array, e caso o array não possua 3 números distintos retornar o maior

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def thirdMax(self, nums: List[int]) -> int:
        # Cria dicionário para armazenar números
        dic = {}

        # Itera sobre os números adicionando os números apenas uma vez
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        # Array da resposta
        arr = []

        # Adiciona os valores unicos ao array
        for i in dic:
            arr.append(i)

        # Ordena eles em ordem decrescente
        arr.sort(reverse=True)

        # Se o array tiver exatamente 3 itens é retornado o último valor
        if len(dic) == 3:
            return arr[-1] 
        # Caso o array tenha mais de 3 itens é retornado o terceiro valor
        elif len(dic) > 3:
            return arr[2]
        # Caso o array tenha menos de 3 itens é retornado o maior valor geral
        else:
            return max(arr)
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\nlog_{n}$), onde n é o tamanho do array.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata71.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
