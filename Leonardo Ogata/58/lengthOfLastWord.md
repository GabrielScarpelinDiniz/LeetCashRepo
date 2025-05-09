# Length of Last Word

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Length of Last Word é retornar o tamanho da última palavra da String. 

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public int lengthOfLastWord(String s) {

        // Salva espaçamento como uma string
        String regex = "[\\s]";

        // Divide a String em um array de acordo com o regex
        String[] stringarray = s.split(regex);

        // Retorna o tamanho do último item do array
        return stringarray[stringarray.length - 1].length();
    }
```

## Lógica do Algoritmo
- Divide o array utilizando o método split através da variável Regex
- Retorna o tamanho do último item do array
    

## Complexidade
- Tempo: O algoritmo possui complexidade de O($n$), onde n é o tamanho da string.
- Espaço: O uso de espaço adicional é O($n$), onde n é o tamanho da string.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata11.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
