public class Solution
{
    public IList<string> LetterCombinations(string digits)
    {
        if (string.IsNullOrEmpty(digits))
        {
            return new List<string>();
        }

        // Mapeamento de dígitos para letras
        Dictionary<char, string> phoneMap = new Dictionary<char, string>() {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
            {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
        };

        List<string> combinations = new List<string>();

        void Backtrack(int index, string currentCombination)
        {
            if (index == digits.Length)
            {
                combinations.Add(currentCombination);
                return;
            }

            string letters = phoneMap[digits[index]];
            foreach (char letter in letters)
            {
                Backtrack(index + 1, currentCombination + letter);
            }
        }

        Backtrack(0, "");
        return combinations;
    }
}
