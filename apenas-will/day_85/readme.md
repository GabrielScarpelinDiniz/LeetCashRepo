## Exercício: 69. Sqrt(x)
**Objetivo**: Dado um inteiro `x`, retorne sua a raiz quadrada arredondada para baixo sem utilizar a função de raiz quadrada e potenciação.

## Descrição geral da estratégia
Para resolver utilizo a lógica de uma busca binária. Inicialmente, determino 3 valores: `lo`, que começa com 0, `hi`, que começa sendo igual a `x` e `mid` que é a média de `lo` e `hi`. Em seguida, confiro se o valor de `mid` é maior que `x`, se for, faço com que `hi` receba o valor de `mid`, recalculo `mid` e faço outra iteração. Se o valor de `mid * mid` for menor que `x`, `lo` recebe o valor de `mid` e `mid` é reatribuído para ser o valor que está entre `lo` e `hi`. Repito isso enquanto o valor de `mid * mid` for diferente de `x` ou se `x` estiver entre `mid * mid` e `(mid + 1) * (mid + 1)`. Ao final, retorno `mid`. Um detalhe, devido ao tamanho dos valores de entrada, `lo`, `hi` e `mid` são variáveis do tipo `long`.
   
## Análise de complexidade
Para um inteiro com valor $n$, tem-se:
- **Time complexity**: $O(\log(n))$ 
- **Space complexity**: $O(1)$ 