import java.util.HashMap;

class longestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        Trie trie = new Trie();
        for (int i = 0; i < strs.length; i++) {
            trie.insert(strs[i]);
        }

        return trie.longestCommonPrefix();
    }
}

class TrieNode {
    HashMap<Character, TrieNode> children = new HashMap<>();
    boolean endOfWord;

    public TrieNode(){
        children = new HashMap<>();
        endOfWord = false;
    }
    
}

class Trie{
    TrieNode root;

    public Trie(){
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode current = root;
        for (char c : word.toCharArray()) {
            if (!current.children.containsKey(c)) {
                current.children.put(c, new TrieNode());
            }
            current = current.children.get(c);
        }
        current.endOfWord = true;
    }

    public String longestCommonPrefix() {
        StringBuilder prefix = new StringBuilder();
        TrieNode current = root;
    
        while (current != null && current.children.size() == 1 && !current.endOfWord) {
            char c = current.children.keySet().iterator().next();
            prefix.append(c);
            current = current.children.get(c);
        }
    
        return prefix.toString();
    }
}