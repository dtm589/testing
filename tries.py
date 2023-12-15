class Trie:
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True
        
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter in current:
                current = current[letter]
            else:
                return False
        if self.end_symbol in current:
            return True
        else:
            return False


    def __init__(self):
        self.root = {}
        self.end_symbol = "*"