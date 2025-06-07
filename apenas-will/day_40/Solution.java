class Solution {
    public String tictactoe(int[][] moves) {
        if(moves.length < 5) return "Pending";
        char[][] board = new char[3][3];

        for(int i = 0; i < moves.length; i++){
            if(i % 2 == 0){
                board[moves[i][0]][moves[i][1]] = 'A';
            } else {
                board[moves[i][0]][moves[i][1]] = 'B';
            }
        }

        for(int i = 0; i < board.length; i++){
            if(board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != '\0') return Character.toString(board[i][0]);
        }

        for(int i = 0; i < board.length; i++){
            if(board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != '\0') return Character.toString(board[0][i]);
        }

        if(board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != '\0') return Character.toString(board[1][1]);

        if(board[2][0] == board[1][1] && board[1][1] == board[0][2] && board[2][0] != '\0') return Character.toString(board[1][1]);

        if(moves.length < 9) return "Pending";
        return "Draw";
    }
}