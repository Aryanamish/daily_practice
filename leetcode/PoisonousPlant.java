import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class PP {

    /*
     * Complete the 'poisonousPlants' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY p as parameter.
     */

    public static int poisonousPlants(List<Integer> p) {
        // Write your code here
        int day = 0;
        Stack<int[]> stack = new Stack<>();
        for (int i = p.size() - 1; i > -1; i--) {
            int kills = 0;
            while (stack.size() > 0 && p.get(i) < stack.peek()[0]) {
                kills = Math.max(kills + 1, stack.pop()[1]);
            }
            day = Math.max(day, kills);
            int[] temp = { p.get(i), kills };
            stack.push(temp);
        }
        return day;
    }

    public static String printStack(Stack<int[]> stack) {
        Stack<int[]> stack2 = new Stack<>();
        String s = new String("[");
        while (stack.size() > 0) {
            int[] temp = stack.pop();
            s += "( " + Integer.toString(temp[0]) + ", " + Integer.toString(temp[1]) + "), ";
            stack2.push(temp);
        }
        while (stack2.size() > 0) {
            stack.push(stack2.pop());
        }
        s += ']';
        return s;
    }

}

public class PoisonousPlant {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        List<Integer> p = Stream.of(sc.nextLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = PP.poisonousPlants(p);
        sc.close();
        System.out.println(result);
    }
}
