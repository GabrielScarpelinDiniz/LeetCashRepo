# Palindrome Number

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Longest Common Prefix é identificar o maior prefixo entre as palavras inseridas.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```java
class longestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        // Cria uma nova árvore Trie
        Trie trie = new Trie();

        // Adiciona todos as palavras do array na árvore
        for (int i = 0; i < strs.length; i++) {
            trie.insert(strs[i]);
        }

        // Retorna o maior prefixo
        return trie.longestCommonPrefix();
    }
}

// Cria class Node da árvore Trie
class TrieNode {
    // Adiciona Hashmap com Caracteres e seus respectivo nodes
    HashMap<Character, TrieNode> children = new HashMap<>();
    // Adiciona identificador de fim da palavra
    boolean endOfWord;

    // Construtor da classe
    public TrieNode(){
        children = new HashMap<>();
        endOfWord = false;
    }
    
}

// Cria a árvore Trie
class Trie{
    // Cria a raiz da árvore
    TrieNode root;

    // Construtor da classe
    public Trie(){
        root = new TrieNode();
    }

    //Método de inserção de palavras
    public void insert(String word) {
        // Define o nó atual como a raiz
        TrieNode current = root;
        // Itera sobre os caracteres da palavra
        for (char c : word.toCharArray()) {
            // Verifica se o caractere já existe
            if (!current.children.containsKey(c)) {
                // Caso não exista o caractere é adicionado
                current.children.put(c, new TrieNode());
            }
            // Atualiza o nó para o caractere atual
            current = current.children.get(c);
        }

        // Marca o nó final como fim da palavra
        current.endOfWord = true;
    }

    //Método que verifica o maior prefixo
    public String longestCommonPrefix() {
        // Cria string builder para montar o prefixo
        StringBuilder prefix = new StringBuilder();
        // Define o nó atual como a raiz
        TrieNode current = root;
    
        // Loop que percorre os nós enquanto o nó atual não for nulo, tiver exatamente um filho e não for o final de uma palavra
        while (current != null && current.children.size() == 1 && !current.endOfWord) {
            // Pega o filho do nó atual
            char c = current.children.keySet().iterator().next();
            
            // Adiciona no string builder
            prefix.append(c);
            
            // Atualiza o nó atual para o próximo caractere 
            current = current.children.get(c);
        }

        // retorna o prefixo
        return prefix.toString();
    }
}
```

## Lógica do Algoritmo
- Após a criação da árvore, o método `longestCommonPrefix()` adiciona caracteres à variável `prefix` até que haja uma bifurcação na árvore, ou o fim de uma palavra, pois isso indica que os próximos caracteres já não serão mais em comum, determinando assim o fim do prefixo.    

## Complexidade
- Tempo: O algoritmo possui complexidade O(${n \times m}$), onde n é a quantidade de palavras no array e m é o comprimento de cada palavra.

- Espaço: O uso de espaço adicional é O(${n \times m}$), onde n é a quantidade de palavras no array e m é o comprimento de cada palavra.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata4.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
