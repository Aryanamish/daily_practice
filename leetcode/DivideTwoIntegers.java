class Solution {
    public int divide(int dividend, int divisor) {
        int ans = 0;
        int sign = 1;

        if (divisor == 0) {
            return 0;
        }
        if (divisor < 0 || dividend < 0) {
            if (divisor < 0 && dividend < 0) {
                sign = 1;
            } else {
                sign = -1;
            }
        }
        divisor = Math.abs(divisor);
        dividend = Math.abs(dividend);
        if (dividend < 0) {
            int temp = divisor;
            int count = 0;
            while (dividend < -1 * temp) {
                temp = temp << 1;
                count++;
            }

            dividend = dividend - (temp >> 1);
            ans += count;
            dividend = Math.abs(dividend);
        }
        // -2147483648 -1
        //
        while (dividend >= divisor) {
            int temp = divisor;
            int count = 0;
            while (dividend >= temp) {
                temp = temp << 1;
                count++;
            }

            dividend = dividend - (temp >> 1);
            ans += count;

        }

        ans *= sign;
        return ans;
    }
}

public class DivideTwoIntegers {
    public static void main(String args[]) {
        Solution s = new Solution();
        int dividend = -2147483648;
        int divisor = -1;
        System.out.println(s.divide(dividend, divisor));
    }
}