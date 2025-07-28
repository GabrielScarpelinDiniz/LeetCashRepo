## Exercício: 38. Count and Say
**Objetivo**: Dado um inteiro $n$, retorne 1 se ele for 1, ou retorne o _Run-Length Encoding_ (RLE) do elemento $n-1$, conseguido de forma recursiva. _Run-Length Encoding_ é uma técnica de compressão que consiste em substituir elementos repetidos pela quantidade de vezes que ele se repete. Nesse sentido, o número "1233333344444444" viraria "111263384", indicando que há 1 número 1, 1 número 2, 6 números 3 e 8 números 4 (número com espaçamento para facilitar a visualização. Os elementos em negrito indicam a quantidade de vezes que o caracter seguinte se repete: **1**1 **1**2 **6**3 **8**4).

## Descrição geral da estratégia
Para resolver implemento a lógica indicada de maneira recursiva. Para isso, crio um array de strings `res`, que armazenará os RLEs de cada elemento até o n-ésimo elemento. Para isso, a cada iteração do loop principal, crio o RLE do elemento anterior e armazeno na posição atual. Para criar o RLE, adiciono dois ponteiros na string do elemento anterior. Um dos ponteiros permanece fixo enquanto o outro avança pela string. Quando os caracteres nas posições dos ponteiros são diferentes, adiciono a diferença entre os ponteiros (quantidade de caracteres iguais) e o caracter no ponteiro fixo (caracter que se repetiu) no array `res`. Esse processo continua até ter-se criado todos os elementos até o inteiro $n$. Por fim, retorna-se o último elemento do array (`res[n-1]`)

## Análise de complexidade
Para um inteiro $n$ e uma string com até $k$ caracteres, tem-se:
- **Time complexity**: $O(n \cdot k)$ 
- **Space complexity**: $O(n)$
