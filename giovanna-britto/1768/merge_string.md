# Vigésimo Terceiro dia de LeetCash 

Pois é meus Lindos, hoje eu fui organizadinha e fiz no horário! Hoje eu resolvi o exercício 1768, na qual dado duas strings deveria inserir elas alternadamente em uma nova string. Para fazer isso eu segui os seguintes passos:

1. Criei um array para a nova palavra `neWord`
2. Criei duas variáveis `i` e `j` para funcionar como dois ponteiros
3. Crio um While para poder iterar, nesse while enquanto i for menor do que o tamanho da entrada 1 e enquanto j for menor do que o tamanho da entrada 2, ele começa a executar:
    - Se `i < len(word1)` e vou adicionar o item de word1 na posição i no novo array e incrementar 1 no contador i;
    - Se `j < len(word2)` e vou adicionar o item de word2 na posição j no novo array e incrementar 1 no contador j;
4. Quando a condição do while deixa de ser verdade eu paro a operação
5. Retorno um join da palavra criada, resultando na resposta.

E é isso, exercício resolvido, obrigada pela atenção.
