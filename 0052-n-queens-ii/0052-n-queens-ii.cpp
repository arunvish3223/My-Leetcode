class Solution {
public:
bool isSafe(vector<string>& board, int row, int col, int n) {
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
        }
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') return false;
        }
        return true;
    }

    void solve(int row, int n, vector<string>& board, int& ans) {
        if (row == n) {
            ans++;
        }
        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col, n)) {
                board[row][col] = 'Q';
                solve(row + 1, n, board, ans);
                board[row][col] = '.';
            }
        }
    }
    int totalNQueens(int n) {
        int ans=0;
        vector<string> board(n, string(n, '.'));
        solve(0, n, board, ans);
        return ans;
        
    }
};