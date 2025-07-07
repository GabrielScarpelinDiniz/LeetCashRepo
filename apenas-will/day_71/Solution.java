/*
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
*/

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null) return null;
        Node ans = new Node();

        Queue<Node> nextToVisit = new ArrayDeque<>();
        Map<Node, Node> oldToNew = new HashMap<>();

        nextToVisit.add(node);

        while(!nextToVisit.isEmpty()){
            Node currentNode = nextToVisit.remove();

            oldToNew.putIfAbsent(currentNode, new Node(currentNode.val));
            
            if(oldToNew.size() == 1){
                ans = oldToNew.get(currentNode);
            }

            for(Node neighbour : currentNode.neighbors){
                if(!oldToNew.keySet().contains(neighbour)){
                    oldToNew.put(neighbour, new Node(neighbour.val));
                    nextToVisit.add(neighbour);
                }

                oldToNew.get(currentNode).neighbors.add(oldToNew.get(neighbour));
            }
        }
       
        return ans;
    }
}