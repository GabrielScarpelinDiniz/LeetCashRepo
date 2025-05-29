public class Solution
{
    public string ReformatDate(string date)
    {
        // Mapeamento dos meses para seus valores numéricos
        Dictionary<string, string> monthMap = new Dictionary<string, string>()
        {
            {"Jan", "01"}, {"Feb", "02"}, {"Mar", "03"}, {"Apr", "04"},
            {"May", "05"}, {"Jun", "06"}, {"Jul", "07"}, {"Aug", "08"},
            {"Sep", "09"}, {"Oct", "10"}, {"Nov", "11"}, {"Dec", "12"}
        };

        // Quebra da string em partes
        string[] parts = date.Split(' ');
        string day = parts[0].Substring(0, parts[0].Length - 2); // Remove "st", "nd", etc.
        string month = monthMap[parts[1]];
        string year = parts[2];

        // Formata o dia com dois dígitos
        if (day.Length == 1)
            day = "0" + day;

        return $"{year}-{month}-{day}";
    }
}
