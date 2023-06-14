
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {
    public ListNode createLinkedList(int[] list) {
        if (list.length == 0) {
            return null;
        }
        ListNode head = new ListNode(list[0]);
        ListNode node = head;
        for (int i = 1; i < list.length; i++) {
            node.next = new ListNode(list[i]);
            node = node.next;
        }

        return head;
    }

    public static void println(ListNode head) {
        if (head != null) {

            while (head.next != null) {
                System.out.print(head.val + "=>");
                head = head.next;
            }
            System.out.println(head.val);
        }
    }
}

class kSorted {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        ListNode ans = lists[0];
        for (int i = 0; i < lists.length; i++) {
            if (ans == null) {
                ans = lists[i];
            }
            if (lists[i] != null && ans != null) {
                if (ans.val > lists[i].val) {
                    ans = lists[i];
                }
            }
        }
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] == null || ans == lists[i]) {
                continue;
            }
            print(ans, lists[i]);
            ListNode pt1 = ans;
            ListNode tempNode = lists[i];
            if (pt1 == null) {
                pt1 = new ListNode(lists[i].val);
                ans = pt1;
                tempNode = tempNode.next;
            }
            ListNode pt2 = pt1.next;
            if (pt2 == null) {
                pt1.next = tempNode;
                print(ans, lists[i]);

                continue;
            }
            while (pt2 != null && tempNode != null) {
                if (pt2.val >= tempNode.val) {
                    ListNode temp = tempNode;
                    tempNode = tempNode.next;
                    pt1.next = temp;
                    temp.next = pt2;
                    pt1 = temp;
                    print(ans, tempNode);
                } else {

                    pt1 = pt2;
                    pt2 = pt2.next;
                }

            }
            if (tempNode != null) {
                pt1.next = tempNode;
                print(ans, tempNode);

            }
        }
        return ans;
    }

    public static void print(ListNode main, ListNode current) {
        System.out.print("Main: ");
        LinkedList.println(main);
        System.out.print("current: ");
        LinkedList.println(current);
        System.out.println();
    }
}

class MergeKSortedList {
    public static void main(String args[]) {
        kSorted s = new kSorted();
        LinkedList linked_list = new LinkedList();
        int[][] data = { {}, { -2 }, { -3, -2, 1 } };

        ListNode[] lists = new ListNode[data.length];
        for (int i = 0; i < data.length; i++) {
            lists[i] = linked_list.createLinkedList(data[i]);
        }
        LinkedList.println(s.mergeKLists(lists));

    }
}