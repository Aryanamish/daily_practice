import java.util.*;
import java.io.*;

class Solution {
    public int[] getOrder(int[][] tasks) {
        Arrays.sort(tasks, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(tasks.length, (a, b) -> Integer.compare(a[1], b[1]));
        int time = 0;
        int i = 0;
        List<Integer> ans = new ArrayList<Integer>();
        while (i < tasks.length) {
            if (tasks[i][0] <= time) {
                int[] temp = { tasks[i][0], tasks[i][1], i };
                pq.add(temp);
                i++;
            } else {
                if (pq.size() > 0) {
                    time += processCPU(pq, ans);
                } else {
                    time = tasks[i][0];
                }
            }
        }
        if (pq.size() > 0) {
            processCPU(pq, ans);
        }
        System.out.println(ans);
        int[] a = new int[ans.size()];
        for (i = 0; i < ans.size(); i++) {
            a[i] = ans.get(i);
        }
        return a;
    }

    private int processCPU(PriorityQueue<int[]> pq, List<Integer> ans) {
        int time = 0;
        while (pq.size() > 0) {
            int[] a = pq.poll();
            time += a[1];
            ans.add(a[2]);
        }
        return time;
    }
}

class SingleThreadedCPU {
    public static void main(String args[]) {
        Solution s = new Solution();
        int[][] q = {
                { 1, 2 },
                { 2, 4 },
                { 3, 2 },
                { 4, 1 }
        };
        s.getOrder(q);
    }
}