# 97. Interleaving String

## Problema

Dadas as strings `s1`, `s2` e `s3`, determine se `s3` é formada por uma intercalação de `s1` e `s2`.

Uma intercalação de duas strings `s` e `t` é uma configuração onde `s` e `t` são divididas em `n` e `m` substrings, respectivamente, de forma que:

- `s = s1 + s2 + ... + sn`
- `t = t1 + t2 + ... + tm`
- `|n - m| <= 1`

A intercalação é `s1 + t1 + s2 + t2 + s3 + t3 + ...` ou `t1 + s1 + t2 + s2 + t3 + s3 + ...`.

### Exemplo 1:

**Entrada:**

```
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
```

**Saída:**

```
true
```

**Explicação:**
Uma forma de obter `s3` é:
Divida `s1` em `"aa" + "bc" + "c"` e `s2` em `"dbbc" + "a"`.
Intercalando as divisões, obtemos `"aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac"`.

### Exemplo 2:

**Entrada:**

```
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
```

**Saída:**

```
false
```

**Explicação:**
Não é possível intercalar `s2` com qualquer outra string para obter `s3`.

### Exemplo 3:

**Entrada:**

```
s1 = "", s2 = "", s3 = ""
```

**Saída:**

```
true
```

### Restrições:

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2` e `s3` consistem em letras minúsculas do alfabeto inglês.

## Solução

A solução utiliza programação dinâmica para verificar se `s3` pode ser formada intercalando `s1` e `s2`. A matriz `dp` armazena os estados intermediários, onde `dp[i, j]` indica se os primeiros `i` caracteres de `s1` e os primeiros `j` caracteres de `s2` podem formar os primeiros `i + j` caracteres de `s3`.

### Complexidade

- **Tempo:** O(n \* m), onde `n` é o tamanho de `s1` e `m` é o tamanho de `s2`.
- **Espaço:** O(n \* m) para a matriz `dp`.
