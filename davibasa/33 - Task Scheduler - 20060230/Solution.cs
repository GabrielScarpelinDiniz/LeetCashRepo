public class Solution
{
    public int LeastInterval(char[] tasks, int n)
    {
        // Conta a frequência de cada tarefa
        int[] freq = new int[26];
        foreach (char task in tasks)
        {
            freq[task - 'A']++;
        }

        // Encontra a frequência máxima
        int maxFreq = freq.Max();
        // Conta quantas tarefas têm a frequência máxima
        int maxCount = freq.Count(f => f == maxFreq);

        // Fórmula: (maxFreq - 1) * (n + 1) + maxCount
        int intervals = (maxFreq - 1) * (n + 1) + maxCount;

        // O resultado é o maior entre o número de tarefas e o cálculo acima
        return Math.Max(intervals, tasks.Length);
    }
}
