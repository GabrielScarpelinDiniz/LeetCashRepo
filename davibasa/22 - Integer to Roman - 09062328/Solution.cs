public class Solution {
    public string IntToRoman(int num) {
        // Arrays com os valores e símbolos romanos
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        StringBuilder result = new StringBuilder();
        
        // Percorre os arrays de valores e símbolos
        for (int i = 0; i < values.Length; i++) {
            // Enquanto o número for maior ou igual ao valor atual
            while (num >= values[i]) {
                // Adiciona o símbolo romano correspondente ao resultado
                result.Append(symbols[i]);
                // Subtrai o valor do número
                num -= values[i];
            }
        }
        
        return result.ToString();
    }
}
