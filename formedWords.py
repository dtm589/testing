'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = {}

        for c in chars:
            ch[c] = 1 + ch.get(c, 0)

        res = 0
        for word in words:
            copy = ch.copy()

            for c in word:
                if c in copy and copy[c] != 0:
                    copy[c] -= 1
                else:
                    res -= len(word)                    
                    break
            
            res += len(word)
        
        return res