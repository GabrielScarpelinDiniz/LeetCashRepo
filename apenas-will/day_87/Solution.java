class TrieNode {
    boolean validWord = false;
    HashMap<Character, TrieNode> children = new HashMap<>();
}

class Trie {
    TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode current = this.root;
        for(int i = 0; i < word.length(); i ++){
            char c = word.charAt(i);
            current.children.putIfAbsent(c, new TrieNode());            
            current = current.children.get(c);
            if(i == word.length() - 1) current.validWord = true;
        }
    }
    
    public boolean search(String word) {
        TrieNode current = this.root;
        for(int i = 0; i < word.length(); i ++){
            char c = word.charAt(i);
            
            if(current.children.containsKey(c)){
                current = current.children.get(c);
            } else {
                return false;
            }

            if(current.validWord && i == word.length() - 1) return true;
        }

        return false;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode current = root;

        for(int i = 0; i < prefix.length(); i++){
            char c = prefix.charAt(i);

            if(current.children.containsKey(c)){
                current = current.children.get(c);
            } else {
                return false;
            }
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */