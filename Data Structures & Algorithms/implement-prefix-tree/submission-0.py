class TrieNode:
    """A single node in the trie.

    `children` maps a character -> the child TrieNode you reach
    by appending that character to the current prefix.

    `endOfWord` flags "if you stop walking HERE, you've spelled a
    complete inserted word." Without this flag, search and
    startsWith would be indistinguishable.
    """

    def __init__(self):
        self.children: dict[str, 'TrieNode'] = {}
        self.endOfWord: bool = False


class PrefixTree:

    def __init__(self):
        # The root represents the EMPTY prefix. It never has
        # endOfWord set unless someone inserts the empty string.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for character in word:
            # Lazily create the child if this is a new path. Each
            # call allocates exactly one new TrieNode per character
            # NOT already shared with a previously inserted word.
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]

        # Mark the FINAL node (reached AFTER consuming the last char)
        # as a word terminus.
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for character in word:
            # Any missing child means the word was never inserted.
            if character not in current.children:
                return False
            current = current.children[character]

        # CRITICAL: a path can exist without the word having been
        # inserted (it might just be a prefix of a longer word).
        # The endOfWord flag is what distinguishes the two cases.
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]

        # Reaching ANY valid node confirms some word uses this prefix.
        # We DO NOT check endOfWord here — that's the whole difference
        # between startsWith and search.
        return True
