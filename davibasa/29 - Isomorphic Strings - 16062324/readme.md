## Strings Isomórficas (Isomorphic Strings)

O método `IsIsomorphic` determina se duas strings são isomórficas.

**Definição:**
Duas strings `s` e `t` são isomórficas se os caracteres em `s` podem ser substituídos para obter `t`, com as seguintes condições:
1. Todas as ocorrências de um caractere devem ser substituídas pelo mesmo caractere.
2. A ordem dos caracteres deve ser preservada.
3. Nenhum caractere pode mapear para o mesmo caractere que outro já mapeou.

**Funcionamento:**
1. Verifica se as strings têm o mesmo tamanho.
2. Utiliza dois dicionários para rastrear mapeamentos bidirecionais entre caracteres.
3. Percorre as strings simultaneamente, verificando consistência nos mapeamentos.

**Exemplos:**
- Entrada: s = "egg", t = "add" → **true** (e→a, g→d)
- Entrada: s = "foo", t = "bar" → **false** (o mapearia para a e r simultaneamente)
- Entrada: s = "paper", t = "title" → **true** (p→t, a→i, p→t, e→l, r→e)

**Complexidade de Tempo:** O(n), onde n é o comprimento das strings.

**Complexidade de Espaço:** O(k), onde k é o número de caracteres distintos nas strings.
