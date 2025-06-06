# Mais um dia de LeetCash

Hoje resolvi o 1108, que era só "desarmar" um endereço de IP, ou seja, trocar os pontos por `[.]`. Para isso, eu segui os  seguintes passos:

1. Criei uma string vazia `addr`.
2. Fui letra por letra do IP:
   * Se fosse `"."`, adicionei `"[.]"`.
   * Se não, adicionei a letra normal.
3. Retornei o `addr` final.

Pronto, mais um exercício resolvido!