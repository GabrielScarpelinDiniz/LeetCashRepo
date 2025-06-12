public class Solution {
    public int MyAtoi(string s) {
        if (string.IsNullOrEmpty(s)) {
            return 0;
        }
        
        int index = 0;
        int sign = 1;
        int result = 0;
        int n = s.Length;
        
        // Passo 1: Ignora espaços em branco iniciais
        while (index < n && s[index] == ' ') {
            index++;
        }
        
        // Passo 2: Determina o sinal
        if (index < n && (s[index] == '+' || s[index] == '-')) {
            sign = s[index] == '+' ? 1 : -1;
            index++;
        }
        
        // Passo 3: Converte dígitos para inteiro
        while (index < n && char.IsDigit(s[index])) {
            int digit = s[index] - '0';
            
            // Passo 4: Verifica overflow
            // Se result > INT_MAX/10 ou (result == INT_MAX/10 e digit > 7), haverá overflow
            if (result > int.MaxValue / 10 || (result == int.MaxValue / 10 && digit > 7)) {
                return sign == 1 ? int.MaxValue : int.MinValue;
            }
            
            result = result * 10 + digit;
            index++;
        }
        
        return result * sign;
    }
}
