## Prefix and Suffix Search

A classe `WordFilter` implementa um dicionário especializado que busca palavras por prefixo e sufixo.

### Funcionamento:

1. **Pré-processamento**: Para cada palavra, gera todas as combinações possíveis de prefixo e sufixo.
2. **Mapeamento**: Usa um dicionário com chave "prefixo#sufixo" e valor sendo o índice da palavra.
3. **Sobrescrita**: Quando há múltiplas palavras válidas, mantém o maior índice (última palavra processada).
4. **Busca**: Consulta O(1) no dicionário usando a chave "prefixo#sufixo".

### Métodos:

- **`WordFilter(words)`**: Inicializa o objeto com as palavras do dicionário.
- **`F(pref, suff)`**: Retorna o índice da palavra com o prefixo e sufixo dados.

### Exemplo:

```
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.F("a", "e"); // return 0
```

### Complexidade:

- **Construção:** O(N × L³), onde N é o número de palavras e L é o comprimento máximo.
- **Busca:** O(1) para cada consulta.
- **Espaço:** O(N × L³) para armazenar todas as combinações.

### Nota:

Esta solução troca espaço por velocidade de consulta, sendo ideal quando há muitas consultas.
