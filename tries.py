class Trie:
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True


    def __init__(self):
        self.root = {}
        self.end_symbol = "*"