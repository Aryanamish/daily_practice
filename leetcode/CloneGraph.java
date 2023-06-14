import java.util.*;

public class CloneGraph {
    public static void main(String args[]) {
        GraphClone gc = new GraphClone();
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        node1.neighbors.add(node2);
        node1.neighbors.add(node4);
        node2.neighbors.add(node1);
        node2.neighbors.add(node3);
        node3.neighbors.add(node2);
        node3.neighbors.add(node4);
        node4.neighbors.add(node1);
        node4.neighbors.add(node3);

        gc.cloneGraph(node1);

    }
}

// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

class GraphClone {
    public Node cloneGraph(Node node) {
        if (node == null)
            return null;
        HashMap<Node, Node> set = new HashMap<>();
        Node new_node = new Node(node.val);
        dfs(node, set, new_node);
        return new_node;
    }

    private Node dfs(Node node, HashMap<Node, Node> set, Node new_node) {
        if (node == null || set.containsKey(node)) {
            if (set.containsKey(node))
                return set.get(node);
            return null;
        }
        new_node.val = node.val;
        set.put(node, new_node);
        for (int i = 0; i < node.neighbors.size(); i++) {
            Node x = dfs(node.neighbors.get(i), set, new Node());
            if (x != null) {
                new_node.neighbors.add(x);
            }
        }
        return new_node;
    }
}