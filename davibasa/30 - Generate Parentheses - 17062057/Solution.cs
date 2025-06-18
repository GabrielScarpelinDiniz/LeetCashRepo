public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        List<string> result = new List<string>();
        Backtrack(result, new System.Text.StringBuilder(), 0, 0, n);
        return result;
    }
    
    private void Backtrack(List<string> result, System.Text.StringBuilder current, int open, int close, int max) {
        // Quando o comprimento da combinação atual é 2*n, adicionamos à lista de resultados
        if (current.Length == max * 2) {
            result.Add(current.ToString());
            return;
        }
        
        // Podemos adicionar um parêntese de abertura se ainda não usamos todos
        if (open < max) {
            current.Append('(');
            Backtrack(result, current, open + 1, close, max);
            current.Remove(current.Length - 1, 1); // backtrack
        }
        
        // Podemos adicionar um parêntese de fechamento se houver parênteses de abertura não fechados
        if (close < open) {
            current.Append(')');
            Backtrack(result, current, open, close + 1, max);
            current.Remove(current.Length - 1, 1); // backtrack
        }
    }
}
