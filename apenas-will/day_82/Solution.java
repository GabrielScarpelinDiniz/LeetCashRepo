class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> numbers = new HashSet<>(Arrays.asList('1', '2', '3', '4', '5', '6', '7', '8', '9'));

        for(int i = 0; i < 9; i++){
            Set<Character> row = new HashSet<>();
            Set<Character> col = new HashSet<>();
            for(int j = 0; j < 9; j++){
                if(row.contains(board[i][j]) && numbers.contains(board[i][j])){
                    return false;
                } else if(numbers.contains(board[i][j])) {
                    row.add(board[i][j]);
                }

                if(col.contains(board[j][i]) && numbers.contains(board[j][i])){
                    return false;
                } else if(numbers.contains(board[j][i])) {
                    col.add(board[j][i]);
                }
            }
        }

        int[] p = {0, 3, 6};
        for(int k : p){
            for(int l : p){
                Set<Character> box = new HashSet<>();
                for(int i = 0; i < 3; i++){
                    for(int j = 0; j < 3; j++){
                        System.out.println(board[i + k][j + l]);
                        if(box.contains(board[i + k][j + l]) && numbers.contains(board[i + k][j + l])){
                            return false;
                        } else if(numbers.contains(board[i + k][j + l])) {
                            box.add(board[i + k][j + l]);
                        }
                    }
                }
            }
        }
        
        return true;
    }
}