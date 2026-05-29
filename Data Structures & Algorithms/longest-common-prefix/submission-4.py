# create a TrieNode
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.endOfWord = True

    def containsWord(self, word: str) -> bool:
        current = self.root

        for character in word:
            if character not in children:
                return False
            current = current.children[character]
        return current.endOfWord
    
    def startsWithPrefix(self, word: str) -> bool:
        current = self.root

        for character in word:
            if character not in children:
                return False
            current = current.children[character]
        return True

    def longestCommonPrefix(self) -> str:
        current = self.root
        prefix = []

        while len(current.children) == 1 and not current.endOfWord:
            char = list(current.children.keys())[0]
            prefix.append(char)
            current = current.children[char]
        
        return "".join(prefix)
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # firstStr = strs[0]

        # for i in range(len(firstStr)):
        #     for j in range(1, len(strs)):
        #         if i == len(strs[j]) or firstStr[i] != strs[j][i]:
        #             return strs[j][:i]

        newTrie = Trie()
        for word in strs:
            newTrie.insert(word)

        return newTrie.longestCommonPrefix()
        

