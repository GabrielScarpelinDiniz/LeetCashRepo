public class Solution 
{
    public string LongestCommonPrefix(string[] strs) 
    {
        if (strs == null || strs.Length == 0) 
        {
            return "";
        }
        
        // Usar a primeira string como referência
        string prefix = strs[0];
        
        // Comparar com cada string subsequente
        for (int i = 1; i < strs.Length; i++) 
        {
            // Reduzir o prefixo até encontrar uma correspondência
            while (!strs[i].StartsWith(prefix)) 
            {
                prefix = prefix.Substring(0, prefix.Length - 1);
                if (prefix == "") 
                {
                    return "";
                }
            }
        }
        
        return prefix;
    }
}

// Versão alternativa usando abordagem vertical
public class SolutionVertical 
{
    public string LongestCommonPrefix(string[] strs) 
    {
        if (strs == null || strs.Length == 0) 
        {
            return "";
        }
        
        // Iterar através de cada posição de caractere
        for (int i = 0; i < strs[0].Length; i++) 
        {
            char currentChar = strs[0][i];
            
            // Verificar se todas as strings têm o mesmo caractere na posição i
            for (int j = 1; j < strs.Length; j++) 
            {
                if (i >= strs[j].Length || strs[j][i] != currentChar) 
                {
                    return strs[0].Substring(0, i);
                }
            }
        }
        
        return strs[0];
    }
}

// Programa de teste
class Program 
{
    static void Main(string[] args) 
    {
        Solution solution = new Solution();
        
        // Teste 1
        string[] test1 = {"flower", "flow", "flight"};
        Console.WriteLine($"Teste 1: {solution.LongestCommonPrefix(test1)}"); // Output: "fl"
        
        // Teste 2
        string[] test2 = {"dog", "racecar", "car"};
        Console.WriteLine($"Teste 2: {solution.LongestCommonPrefix(test2)}"); // Output: ""
        
        // Teste 3
        string[] test3 = {"interspecies", "interstellar", "interstate"};
        Console.WriteLine($"Teste 3: {solution.LongestCommonPrefix(test3)}"); // Output: "inters"
    }
}
