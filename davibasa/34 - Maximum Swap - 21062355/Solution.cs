public class Solution
{
    public int MaximumSwap(int num)
    {
        char[] digits = num.ToString().ToCharArray();
        int n = digits.Length;
        int[] last = new int[10];

        // Armazena o último índice de cada dígito
        for (int i = 0; i < n; i++)
            last[digits[i] - '0'] = i;

        // Para cada dígito, tenta trocar com o maior possível à direita
        for (int i = 0; i < n; i++)
        {
            for (int d = 9; d > digits[i] - '0'; d--)
            {
                if (last[d] > i)
                {
                    // Troca e retorna o novo número
                    char temp = digits[i];
                    digits[i] = digits[last[d]];
                    digits[last[d]] = temp;
                    return int.Parse(new string(digits));
                }
            }
        }
        return num;
    }
}
