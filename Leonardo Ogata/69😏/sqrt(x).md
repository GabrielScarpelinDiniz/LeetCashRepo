# Sqrt(x)

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Sqrt(x) é receber um valor x e retornar o valor do número inteiro arredondado para baixo mais próximo da sua raiz quadrada.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```java
    public int mySqrt(int x) {
        // Cria variável que vai armazenar a raiz
        int sqrt = 0;

        // Loop infinito para encontrar a raiz
        while (true) {
            // Verifica se sqrt ao quadrado passou de x
            if((long)sqrt * sqrt > x){
                // Caso tenha passado retorna o valor anterior de x
                return sqrt - 1;
            }

            // Soma 1 a sqrt
            sqrt++;
        }

    }
```

## Lógica do Algoritmo
- Cria variável para armazenar o valor da raiz quadrada
- Inicia um loop infinito 
    - Se sqrt ao quadrado for maior que x significa que o valor inteiro mais próximo da raiz quadrade de x arrendonda para baixo era o número anterior a sqrt, logo retonra sqrt-1
- Soma mais um a sqrt
    

## Complexidade
- Tempo: O algoritmo possui complexidade de O($\sqrt{n}$), onde n é o valor de x.
- Espaço: O uso de espaço adicional é O($1$).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata14.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos e feliz dia das mães, vejo vocês amanhã!</p>
    </div>
</div>
