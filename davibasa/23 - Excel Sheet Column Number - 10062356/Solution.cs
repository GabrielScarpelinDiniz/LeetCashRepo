public class Solution {
    public int TitleToNumber(string columnTitle) {
        int result = 0;
        
        // Percorre cada caractere da string
        foreach (char c in columnTitle) {
            // Multiplica o resultado atual por 26 (base do sistema)
            result = result * 26;
            // Adiciona o valor do caractere (A=1, B=2, ..., Z=26)
            result = result + (c - 'A' + 1);
        }
        
        return result;
    }
}
