public class Solution
{
    public string CapitalizeTitle(string title)
    {
        // Divide o título em palavras
        string[] words = title.Split(' ');

        for (int i = 0; i < words.Length; i++)
        {
            if (words[i].Length <= 2)
            {
                // Palavras com 1 ou 2 letras ficam em minúsculas
                words[i] = words[i].ToLower();
            }
            else
            {
                // Primeira letra maiúscula, restante minúsculas
                words[i] = char.ToUpper(words[i][0]) + words[i].Substring(1).ToLower();
            }
        }

        // Junta as palavras novamente com espaço
        return string.Join(" ", words);
    }
}
