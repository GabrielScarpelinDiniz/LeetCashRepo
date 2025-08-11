# Kids With the Greatest Number of Candies

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Kids With the Greatest Number of Candies é retornar um array contendo true para cada criança que quando adicionado o doces extras ao seus doces atuais se torna a criança com mais doce do grupo e false para o contrário


&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```go
func kidsWithCandies(candies []int, extraCandies int) []bool {
    // Criar array para armazenar resposta
    arr := make([]bool, len(candies))

    // Armazena maior número do array
    biggest := 0

    // Itera sobre o array para definir a maior quantidade de doces
    for _, v := range candies {
        if v > biggest {
            biggest = v
        }
    }

    // Itera sobre o array
    for i, v := range candies {
        // Caso a criança se torne a criança com mais doces é adicionado True
        if v + extraCandies >= biggest{
            arr[i] = true
        // Caso o contrário é adicionado false
        } else {
            arr[i] = false
        }
    }

    // Retorna o array booleano
    return arr
}
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n), onde n é o tamanho do candies.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata105.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
