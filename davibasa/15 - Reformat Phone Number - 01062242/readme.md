## Reformatar Número de Telefone (Reformat Phone Number)

O método `ReformatNumber` formata um número de telefone de acordo com as seguintes regras:

1. Remove todos os espaços e traços do número.
2. Agrupa os dígitos da esquerda para a direita em blocos de comprimento 3 até restarem 4 ou menos dígitos.
3. Os dígitos finais são agrupados da seguinte forma:
   - 2 dígitos: Um único bloco de comprimento 2.
   - 3 dígitos: Um único bloco de comprimento 3.
   - 4 dígitos: Dois blocos de comprimento 2 cada.
4. Os blocos são unidos por traços.

**Exemplo:**

- Entrada: "123 4-567"
- Saída: "123-45-67"

**Complexidade de Tempo:** O(n), onde n é o comprimento do número.

**Complexidade de Espaço:** O(n), para armazenar os blocos formatados.
