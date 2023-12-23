'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        for word in words:
            w = set(word.lower())
            if w <= set1 or w <= set2 or w <= set3:
                result.append(word)
        return result