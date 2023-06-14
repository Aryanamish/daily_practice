import java.util.*;

class LetterCombination {

    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<String>();
        if (digits.length() == 0) {
            return ans;
        }
        HashMap<String, String> data = new HashMap<>();
        data.put("2", "abc");
        data.put("3", "def");
        data.put("4", "ghi");
        data.put("5", "jkl");
        data.put("6", "mno");
        data.put("7", "pqrs");
        data.put("8", "tuv");
        data.put("9", "wxyz");
        String emp = "";
        combination(digits, ans, data, emp);
        return ans;
    }

    private static void combination(String digits, List<String> ans, HashMap<String, String> mapping, String curr) {
        if (digits.length() == 0) {
            return;
        }
        String chars = mapping.get(Character.toString(digits.charAt(0)));
        if (digits.length() == 1) {
            for (int i = 0; i < chars.length(); i++) {
                ans.add(curr + chars.charAt(i));
            }
        } else {
            for (int i = 0; i < chars.length(); i++) {
                combination(digits.substring(1), ans, mapping, curr + chars.charAt(i));
            }
        }
    }
}

class Main {

    public static void main(String args[]) {
        LetterCombination s = new LetterCombination();
        List<String> ans = s.letterCombinations("23");

        System.out.println(ans);
    }

}