public class Solution
{
    public string ReformatNumber(string number)
    {
        // Remove espaços e traços
        string digits = string.Concat(number.Where(char.IsDigit));

        // Lista para armazenar os blocos formatados
        List<string> blocks = new List<string>();

        int i = 0;
        while (digits.Length - i > 4)
        {
            blocks.Add(digits.Substring(i, 3));
            i += 3;
        }

        // Lida com os últimos 2, 3 ou 4 dígitos
        int remaining = digits.Length - i;
        if (remaining == 4)
        {
            blocks.Add(digits.Substring(i, 2));
            blocks.Add(digits.Substring(i + 2, 2));
        }
        else
        {
            blocks.Add(digits.Substring(i));
        }

        return string.Join("-", blocks);
    }
}
