# Levou minha tarde toda!

## Desafio dia 04/200

Diferente do pessoal de CC, eu tenho que estudar estrutura e algoritmos por conta próprio, é como se eu tivesse atirando no escuro, então se você chegasse e batesse o olho nesse exercício e falasse "Ah é só usar sliding window", eu lhe dou os meus sinceros parabéns, porque não foi o meu caso!

Depois de um tempo que aprendi que quando tem problemas envolvendo substrings, na maioria das vezes se resolve com o sliding window, e esse foi o caso.

Vamos lá, basicamente está pedindo que dado uma string `s`, retorne uma substring que o caractere se repete no máximo duas vezes e o tamanho máximo dela.

A ideia principal é usar dois ponteiros (`l` e `r`) para definir uma janela que se ajusta dinamicamente enquanto percorre a string.

### Como fiz (fiz uma doc feia aí pedi pro gpt deixar ela mais organizadinha):

1. **Inicialização**:
   - Começamos com dois ponteiros (`l` e `r`) no início da string.
   - Usamos um `Map` para rastrear a contagem de cada caractere na janela atual.
   - Uma variável `max` é usada para armazenar o comprimento máximo da substring válida encontrada.

2. **Expansão da janela**:
   - Movemos o ponteiro direito (`r`) para expandir a janela e adicionamos o caractere atual ao `Map`, incrementando sua contagem.

3. **Ajuste da janela**:
   - Se algum caractere na janela aparecer mais de duas vezes, movemos o ponteiro esquerdo (`l`) para reduzir a janela até que a restrição seja atendida.

4. **Atualização do resultado**:
   - Após ajustar a janela, calculamos o comprimento da substring atual e atualizamos o valor de `max` se for maior que o anterior.

5. **Finalização**:
   - Quando o laço termina, `max` contém o comprimento da maior substring que atende à restrição.

### Código:

```javascript
var maximumLengthSubstring = function(s) {
    let l = 0;
    let r = 0;
    let max = 0;
    let dict = new Map();

    while (r < s.length) {
        dict.set(s[r], (dict.get(s[r]) || 0) + 1);

        while (dict.get(s[r]) > 2) {
            dict.set(s[l], dict.get(s[l]) - 1);
            if (dict.get(s[l]) === 0) {
                dict.delete(s[l]);
            }
            l++;
        }

        max = Math.max(max, r - l + 1);
        r++;
    }

    return max;
};

```

## (Engenheiro de Software detonando a concorrência)[https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/submissions/1623085471]