## Exercício: 36. Valid Sudoku
**Objetivo**: Dado uma matriz de caracteres que representa um tabuleiro de sudoku, determine se esse tabuleiro é válido (ser válido significa que ele não está violando nenhuma regra do sudoku, não significa que ele é resolvível).

## Descrição geral da estratégia
Para resolver primeiro itero pelas linhas e colunas do tabuleiro, adicionando seus valores em um `HashSet` para a linha e em um para a coluna. Caso eu detecte uma duplicata em algum dos conjuntos, retorno `false`. Caso não, sigo para a validação dos blocos. Nessa etapa, crio um `HashSet` representando um bloco (conjunto de 9 elementos do sudoku) e, assim como anteriormente, caso seja detectada uma duplicata, retorno `false`. Caso não encontre elementos repetidos em nenhum dos processos, retorno `true`.
   
## Análise de complexidade
Para uma tabuleiro de sudoku $9 \time 9$ inteiros, tem-se:
- **Time complexity**: $O(1)$ ( $\Theta(162)$ )
- **Space complexity**: $O(1)$ 