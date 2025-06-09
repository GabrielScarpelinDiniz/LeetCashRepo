public class Solution
{
    public int Tribonacci(int n)
    {
        // Casos base
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;

        // Array para memorização
        int[] trib = new int[n + 1];
        trib[0] = 0;
        trib[1] = 1;
        trib[2] = 1;

        // Calcula os números Tribonacci usando programação dinâmica
        for (int i = 3; i <= n; i++)
        {
            trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3];
        }

        return trib[n];
    }
}
