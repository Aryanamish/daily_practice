import java.util.*;

class mxStart {
    public int maxStarSum(int[] vals, int[][] edges, int k) {
        if (vals.length == 0) {
            return 0;
        }
        PriorityQueue<Integer>[] graph = new PriorityQueue[vals.length];
        int max_sum = Integer.MIN_VALUE;
        for (int i = 0; i < graph.length; i++) {
            max_sum = Math.max(vals[i], max_sum);
            graph[i] = new PriorityQueue<Integer>(new MaxPriority());
        }
        if (k == 0) {
            return max_sum;
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(vals[edge[1]]);
            graph[edge[1]].add(vals[edge[0]]);
        }
        for (PriorityQueue pq : graph) {
            System.out.println(pq);
        }
        for (int i = 0; i < vals.length; i++) {
            int curr_sum = vals[i];
            int j = 0;
            while (graph[i].size() > 0 && j < k) {
                curr_sum += graph[i].poll();
                max_sum = Math.max(max_sum, curr_sum);
            }
        }
        return max_sum;
    }
}

class MaxPriority implements Comparator<Integer> {
    public int compare(Integer a, Integer b) {
        if (a < b) {
            return 1;
        } else {
            return -1;
        }
    }
}

public class MaxStarSumOfGraph {
    public static void main(String args[]) {

        int[] vals = { 17, 49, -34, -17, -7, -23, 24 };
        int[][] edges = {
                { 3, 1 }, { 5, 1 },
                { 0, 3 }, { 4, 6 },
                { 1, 4 }, { 3, 4 },
                { 6, 3 }, { 2, 6 },
                { 5, 2 }, { 1, 6 },
                { 6, 0 }, { 2, 3 },
                { 3, 5 }, { 2, 1 },
                { 0, 2 }, { 5, 0 },
                { 0, 4 }
        };

        mxStart s = new mxStart();
        System.out.println(s.maxStarSum(vals, edges, 6));

    }
}