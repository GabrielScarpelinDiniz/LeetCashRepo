public class Solution
{
    public bool IsValidSudoku(char[][] board)
    {
        // Conjuntos para verificar linhas, colunas e blocos 3x3
        HashSet<char>[] rows = new HashSet<char>[9];
        HashSet<char>[] cols = new HashSet<char>[9];
        HashSet<char>[] boxes = new HashSet<char>[9];

        // Inicializa os conjuntos
        for (int i = 0; i < 9; i++)
        {
            rows[i] = new HashSet<char>();
            cols[i] = new HashSet<char>();
            boxes[i] = new HashSet<char>();
        }

        // Percorre todo o tabuleiro
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                char num = board[i][j];

                // Se for uma célula vazia, continua
                if (num == '.') continue;

                // Índice do bloco 3x3: (i/3)*3 + j/3
                int boxIndex = (i / 3) * 3 + j / 3;

                // Verifica se o número já existe na linha, coluna ou bloco
                if (rows[i].Contains(num) || cols[j].Contains(num) || boxes[boxIndex].Contains(num))
                {
                    return false;
                }

                // Adiciona o número aos conjuntos
                rows[i].Add(num);
                cols[j].Add(num);
                boxes[boxIndex].Add(num);
            }
        }

        return true;
    }
}
