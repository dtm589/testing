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
        
    def words_with_prefix(self, prefix):
        result = []
        current = self.root
        for letter in prefix:
            if letter in current:
                current = current[letter]
            else:
                return result
        final_result = self.search_level(current, prefix, result)
        return final_result

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        for key in sorted(cur):
            if key != self.end_symbol:
                self.search_level(cur[key], cur_prefix + key, words)   
        return words


    def __init__(self):
        self.root = {}
        self.end_symbol = "*"