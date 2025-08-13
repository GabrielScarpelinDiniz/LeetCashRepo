# Set Mismatch

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Set Mismatch é retornas o número repetido no array e o número que está faltando

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```go
    func findErrorNums(nums []int) []int {
    
    // Cria dicionário para armazenar valores
    dic := make(map[int]int)

    // Itera sobre o dicionário
    for _, v := range nums {
        // Caso o número exista no dicionário incrementa sua contagem
        if _ , exist := dic[v]; exist {
            dic[v] += 1
        // Caso não adiciona ele na contagem
        } else {
            dic[v] = 1
        }
    }

    // Cria variável para armazenar soma do array
    var arrSum int = 0
    // Calcula a soma de 1 a len(nums)
    var paSum int = len(nums) * (len(nums) + 1) / 2
    // Cria variável que armazena o número repetido
    ans := 0
    
    // Itera sobre as chaves do dicionário
    for key := range dic {
        // Soma todos valores uma única vez
        arrSum += key

        // Caso o número se repita atribui ele a variável ans
        if dic[key] == 2 {
            ans = key
        }
    }
    
    // retorna o número repetido e número que falta que pode ser calculado subtraindo a soma dos valores unicos da soma da PA
    return []int{ans, paSum - arrSum}
}
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho da string s.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata108.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
