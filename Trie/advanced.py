class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete_node = _delete(node.children[char], word, depth + 1)
            if should_delete_node:
                del node.children[char]
                return len(node.children) == 0
            return False
        
        return _delete(self.root, word, 0)

    def suggestions(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._dfs(node, prefix)

    def _dfs(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for char, child in node.children.items():
            result.extend(self._dfs(child, prefix + char))
        return result

# Example usage:
trie = Trie()
words = ["apple", "app", "banana", "ball", "bat"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("bana"))   # Output: False

trie.delete("apple")
print(trie.search("apple"))  # Output: False

print(trie.suggestions("ba"))  # Output: ['ball', 'banana']

