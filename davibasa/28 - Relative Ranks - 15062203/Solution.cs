public class Solution {
    public string[] FindRelativeRanks(int[] score) {
        int n = score.Length;
        string[] result = new string[n];

        // Clona e ordena em ordem decrescente
        int[] sorted = (int[])score.Clone();
        Array.Sort(sorted);
        Array.Reverse(sorted);

        // Mapeia a pontuação para a posição/rank
        Dictionary<int, int> rankMap = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            rankMap[sorted[i]] = i + 1; // posição 1-based
        }

        // Gera o resultado
        for (int i = 0; i < n; i++) {
            int r = rankMap[score[i]];
            switch (r) {
                case 1:
                    result[i] = "Gold Medal";
                    break;
                case 2:
                    result[i] = "Silver Medal";
                    break;
                case 3:
                    result[i] = "Bronze Medal";
                    break;
                default:
                    result[i] = r.ToString();
                    break;
            }
        }

        return result;
    }
}
