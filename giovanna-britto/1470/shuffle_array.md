# Mais um dia de LeetCash

Hoje resolvi o exercício 1470, que pede para embaralhar um array no seguinte formato: dado um array `nums` com `2n` elementos, preciso retornar um novo array no formato `x1, y1, x2, y2, ..., xn, yn`, onde os `x` são os primeiros `n` elementos e os `y` são os últimos `n`. Para isso eu segui os seguintes passos:

1. Criei três listas vazias: `arrX` para guardar os `x`, `arrY` para os `y` e `arrF` para o resultado final.
2. Passei pelo array `nums` usando um for:

    2.1. Se o índice for menor que `n`, adiciono o elemento em `arrX`.

    2.2. Senão, adiciono em `arrY`.

3. Depois, faço outro for de 0 até `n`:
    3.1. Adiciono o elemento de `arrX` e depois o de `arrY` em `arrF`, intercalando.
4. No final, retorno `arrF` com o array embaralhado do jeito pedido.

E pronto! Mais um exercício resolvido!