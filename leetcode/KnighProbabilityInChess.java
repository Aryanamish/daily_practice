class Probability {
    public double knightProbability(int n, int k, int row, int col) {
        double[][] dp = new double[n][n];
        double[][] dp_prev = new double[n][n];
        double[][] temp;
        int[][] moves = {
                { 2, 1 },
                { 2, -1 },
                { -2, 1 },
                { -2, -1 },
                { 1, 2 },
                { 1, -2 },
                { -1, 2 },
                { -1, -2 },
        };
        dp_prev[row][col] = 1;
        for (int ii = 0; ii < k; ii++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dp_prev[i][j] == 0) {
                        continue;
                    }
                    for (int[] move : moves) {
                        int x = i + move[0];
                        int y = j + move[1];
                        if (valid_move(n, x, y)) {
                            dp[x][y] += 0.125 * dp_prev[i][j];
                        }

                    }
                    dp_prev[i][j] = 0;
                }

            }
            temp = dp_prev;
            dp_prev = dp;
            dp = temp;
        }
        double prob = 0;
        for (double[] dp_row : dp_prev) {
            for (double cell : dp_row) {
                prob += cell;
            }
        }
        return prob;
    }

    private boolean valid_move(int n, int a, int b) {
        if (a < 0 || b < 0) {
            return false;
        }
        if (a >= n || b >= n) {
            return false;
        }
        return true;
    }
}

public class KnighProbabilityInChess {

    public static void main(String args[]) {
        Probability prob = new Probability();
        System.out.println(prob.knightProbability(3, 2, 0, 0));
    }
}