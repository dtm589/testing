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

    def find_matches(self, document):
        final_set = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break 
                level = level[ch]
                if self.end_symbol in level:
                    final_set.add(document[i : j + 1])
        return final_set

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"