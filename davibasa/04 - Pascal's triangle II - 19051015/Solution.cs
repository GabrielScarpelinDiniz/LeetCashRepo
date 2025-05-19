public class Solution
{
    public IList<int> GetRow(int rowIndex)
    {
        IList<IList<int>> result = new List<IList<int>>();

        for (int i = 0; i <= rowIndex; i++)
        {
            IList<int> row = new List<int>();

            var linhaAnterior = i != 0 ? result[i - 1] : new List<int>();
            for (int j = 0; j <= i; j++)
            {
                if (j == 0 || j == i)
                {
                    row.Add(1);
                    continue;
                }

                row.Add(linhaAnterior[j - 1] + linhaAnterior[j]);

            }

            result.Add(row);
        }

        return result[rowIndex];
    }
}