class RegularExpression {
    public static void main(String args[]) {
        System.out.println(isMatch("aa", "a*"));
    }

    public static boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[p.length() + 1][s.length() + 1];
        dp[0][0] = true;

        for (int i = 1; i <= p.length(); i++) {
            dp[i][0] = false;
            if (p.charAt(i - 1) == '*') {
                dp[i][0] = dp[i - 2][0];
            }
        }
        for (int i = 1; i < p.length() + 1; i++) {
            for (int j = 1; j < s.length() + 1; j++) {
                char char_p = p.charAt(i - 1);
                char char_s = s.charAt(j - 1);
                if (char_s == char_p || char_p == '.') {
                    dp[i][j] = dp[i - 1][j - 1];

                } else if (char_p == '*') {
                    dp[i][j] = dp[i - 2][j];
                    if (p.charAt(i - 2) == char_s || p.charAt(i - 2) == '.') {
                        dp[i][j] = dp[i - 2][j] || dp[i][j - 1];
                    }
                }
            }
        }
        return dp[p.length()][s.length()];
    }

    public static void prnt(boolean dp[][]) {
        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < dp.length; j++) {
                if (dp[i][j] == false) {

                    System.out.print("0" + " ");
                } else {
                    System.out.print("1" + " ");

                }
            }
            System.out.println("");
        }
        System.out.println("");
    }
}