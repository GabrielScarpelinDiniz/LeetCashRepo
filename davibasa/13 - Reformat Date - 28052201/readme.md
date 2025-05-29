## Reformatar Data (Reformat Date)

O método `ReformatDate` converte uma string de data no formato "dia mês ano" (por exemplo, "1st Jun 2023") para o formato ISO "ano-mês-dia" (por exemplo, "2023-06-01").

A função realiza as seguintes operações:
1. Mapeia os nomes dos meses para seus valores numéricos de dois dígitos
2. Divide a string de entrada em dia, mês e ano
3. Remove os sufixos do dia (como "st", "nd", "rd", "th")
4. Formata o dia com dois dígitos quando necessário
5. Retorna a data no formato "YYYY-MM-DD"

**Complexidade de Tempo:** O(1), pois a operação de split e manipulações de string são feitas em um tamanho fixo.

**Complexidade de Espaço:** O(1), pois utiliza uma quantidade fixa de espaço adicional.
