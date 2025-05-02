# Palindrome Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema validParentheses é determinar se os paranteses, chaves e colchetes de fecham corretamente .

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
public boolean isValid(String s) {

    // Cria uma stack
    Stack<Character> stack = new Stack<>();
    
    // Itera sobre todos itens da String
    for(char c : s.toCharArray()) {

        // Caso seja um caractere de abertura ele é adicionado ao stack
        if (c == '(' || c == '{' || c == '[') {
            stack.push(c);
        }

        // Caso seja um caractere de fechadura e o stack estiver vazio é retornado falso pois seria impossivel ter uma solução correta
        if (c == ')' && stack.isEmpty()|| c == '}' && stack.isEmpty() || c == ']' && stack.isEmpty()) {
            return false;
        }

        // Caso seja um parenteses de fechadura é verificado se o primeiro item do stack é o de abertura
        if (c == ')') {
            char check = stack.peek(); 
                if (check == '(') {
                    stack.pop();
                }else{
                    return false;
                }
        }

        // Caso seja uma chave de fechadura é verificado se o primeiro item do stack é o de abertura
        if (c == '}') {
            char check = stack.peek(); 
                if (check == '{') {
                    stack.pop();
                }else{
                    return false;
                }
        }

        // Caso seja um colchete de fechadura é verificado se o primeiro item do stack é o de abertura
        if (c == ']') {
            char check = stack.peek(); 
                if (check == '[') {
                    stack.pop();
                }else{
                    return false;
                }
        }
    }

    // Caso o fim do loop o stack esteja vazio é retornado veradeiro caso o contrário é retornado falso
    if (stack.isEmpty()) {
        return true;
    }else{
        return false;
    }
}
```

&nbsp;&nbsp;&nbsp;&nbsp; Esse código ficou tão feio que eu senti vergonha de publicar isso aqui, portanto decidi fazer uma implementação mais bonita apesar de que as duas fazem a mesma coisa, com a mesma complexidade de tempo e espaço. A seguir pode-se conferir minha segunda implementação:

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char check = stack.peek();
                if (c == ')' && check == '(' || c == '}' && check == '{' || c == ']' && check == '[') {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
```
&nbsp;&nbsp;&nbsp;&nbsp; Como foi dito anterirormente essa aplicação faz exatamente a mesma coisa da exata mesma forma só que de um jeito bonito.

## Lógica do Algoritmo
- Após a criação do stack a string é iterada
    - Caso a caractere seja um valor de abertura ele é adicionado ao stack
    - Caso o caractere seja um valor de fechadura é verificado o item do topo do stack
        - Caso o item do topo seja a abertura é retornado verdadeiro
        - Caso o item do topo não seja a abertura é retornado falso
- Ao final da itereção é verificado se o stack está vazio
    - Caso sim é retornado verdadeiro
    - Caso não é retornado falso

## Complexidade
- Tempo: O algoritmo possui complexidade O(${n}$), onde n é a quantidade de caracteres da string.
- Espaço: O uso de espaço adicional é O(${n}$), onde n é a quantidade de caracteres da string.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata5.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
