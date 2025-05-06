# Find the Index of the First Occurrence in a String

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Find the Index of the First Occurrence in a String é encontrar o index da primeira aparição de uma sub string, dentro de uma string maior. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public int strStr(String haystack, String needle) {

        // Itera pelo tamanho da maior string menos o tamanho da menor
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            
            // Se a substring i + o tamanho da substring menor for igual a substring menor o index é retornado
            if (haystack.substring(i, i + needle.length()).equals(needle)) {
                return i; 
            }
        }

        // Caso não tenha a ocorrência da substring menor é retornado -1 
        return -1; 
    }
```

## Lógica do Algoritmo
- O loop itera pelo tamanho de `haystack` menos o tamanho de `needle`, pois é o único espaço onde a `needle` cabe.
    - Se a substring que inicia no índice `i` e termina no índice `i` + tamanho da string `needle`, for igual a `needle` é retornado o index `i`
- Caso não tenha a ocorrência de `needle` no `haystack` é retornado -1

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(${n \times m}$), onde n é o tamanho de `haystack.length() - needle.length()` e m é o tamanho da substring gerada pelo método `haystack.substring`.
- Espaço: O uso de espaço adicional é O(${m}$), onde m é o tamanho da substring gerada pelo método `haystack.substring`.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata9.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
