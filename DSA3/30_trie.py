# dt = {'a':1,'b':2,'c':3}
# print(dt['a'])
# dt['f']=4
# print(dt)





class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
        node.is_end_of_word = True


    def print_trie(self):
        self._print_trie(self.root, "")

    def _print_trie(self, node, current_word):
        if node.is_end_of_word:
            print(current_word)

        for char, child_node in node.children.items():
            self._print_trie(child_node, current_word + char)
        

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self,word):
        self._delete(self.root, word, 0)

    def _delete(self, node, word, depth):
        if depth == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
            return
        
        char = word[depth]
        if char not in node.children:
            return  # The word is not present in the trie
        
        self._delete(node.children[char], word, depth + 1)


        # Remove the child node if it has no other children and is not the end of another word
        if not node.children[char].children and not node.children[char].is_end_of_word:
            del node.children[char]


trie = Trie()
words = ["apple","app","apricot"]
for word in words:
    trie.insert(word)

print("Trie after inserting words:")
trie.print_trie()



print("")
print("Search 'apple':", trie.search("apple"))
print("Search 'banana':", trie.search("banana"))


print("")
print("Typing 'b':", trie.starts_with_prefix("b"))



print("")
trie.delete("app")
trie.delete("apple")
print("Trie after deleting word:")
trie.print_trie()



