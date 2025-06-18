public class Solution
{
    public bool IsIsomorphic(string s, string t)
    {
        // Verifica se as strings têm o mesmo tamanho
        if (s.Length != t.Length)
        {
            return false;
        }

        // Dicionários para mapear caracteres
        Dictionary<char, char> sToT = new Dictionary<char, char>();
        Dictionary<char, char> tToS = new Dictionary<char, char>();

        // Percorre as strings simultaneamente
        for (int i = 0; i < s.Length; i++)
        {
            char charS = s[i];
            char charT = t[i];

            // Verifica mapeamento de s para t
            if (sToT.ContainsKey(charS))
            {
                if (sToT[charS] != charT)
                {
                    return false;
                }
            }
            else
            {
                sToT[charS] = charT;
            }

            // Verifica mapeamento de t para s
            if (tToS.ContainsKey(charT))
            {
                if (tToS[charT] != charS)
                {
                    return false;
                }
            }
            else
            {
                tToS[charT] = charS;
            }
        }

        return true;
    }
}
