# Count the Number of Consistent Strings

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Count the Number of Consistent Strings é iterar sobre um array de palavras e contar as palavras que possuem todos os caracteres da string allowed


&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```go
func countConsistentStrings(allowed string, words []string) int {

    // Armazena a quantidade de palavras do array
    counter := len(words)
    
    // Cria um dicionário para armazenara caracteres
    dic := make(map[rune]struct{})
    
    // Itera sobre a string allowed
    for _, r := range allowed {
        // Adiciona os caracteres ao dicionário
        dic[r] = struct{}{}
    }

    // Itera sobre o array words
    for _, word := range words {
        // Itera sobre a palavra do array
        for _, char := range word {
            // Caso a palavra tenha alguma letra que não está na string allowed ela é subtraída do counter
            if _, exists := dic[char]; !exists{
                counter--
                break
            }
        }
    }

    // Retorna a contagem de palavras que possuem apenas as letras de allowed
    return counter
}
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n * m), onde n é o tamanho do array e m é o tamanho das palavras.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata103.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
