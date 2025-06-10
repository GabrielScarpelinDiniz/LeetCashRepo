## Inteiro para Romano (Integer to Roman)

O método `IntToRoman` converte um número inteiro em sua representação em algarismos romanos. Os algarismos romanos são representados pelos seguintes símbolos:
- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

Além disso, existem formas subtrativas especiais:
- IV = 4 (5-1)
- IX = 9 (10-1)
- XL = 40 (50-10)
- XC = 90 (100-10)
- CD = 400 (500-100)
- CM = 900 (1000-100)

**Funcionamento:**
1. Utiliza dois arrays: um com os valores em ordem decrescente e outro com os símbolos romanos correspondentes.
2. Percorre os valores, começando pelo maior, e para cada valor:
   - Enquanto o número for maior ou igual ao valor atual, adiciona o símbolo correspondente ao resultado e subtrai o valor do número.
3. Continua até que o número seja reduzido a zero.

**Exemplos:**
- Entrada: 3749
- Saída: "MMMDCCXLIX"
- Explicação: 3000 (MMM) + 700 (DCC) + 40 (XL) + 9 (IX)

**Complexidade de Tempo:** O(1), pois o número máximo de iterações é limitado pela constante 3999.

**Complexidade de Espaço:** O(1), pois o tamanho da saída é limitado.
