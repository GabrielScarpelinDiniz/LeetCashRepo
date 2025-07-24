# Mais um dia de LeetCash

Hoje eu resolvi o exercício 1773, que dado uma lista de lista de items eu deveria dizer quantos itens atende a: se chave da regra ("type", "color" ou "name"), o item que estava na lista era igual o valor em `ruleValue`. Para isso eu segui os seguintes passos:

1. Defini a variável `cont` para ser o contador.

2. Defini a variável `indice` para armazenar o indice a ser avaliado de acordo com a chave da regra.

3. Fiz um if, para que se caso o `ruleKey` fosse igual a `type` o ``indice`` recebia 0, se fosse igual a `color` recebia 1, se não ele recebia 2.

4. Fiz um for que itera sobre os items da lista, e se o conteúdo de `item[indice]` for igual a `ruleValue` eu adiciono +1 no contador.

5. Por fim, retorno `cont`.

E pronto! Mais um exercício resolvido!!!