'''
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
'''

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # built in counter function returns a dictionary with occurences of each iterable in the words list
        dict1 = Counter(words1)
        dict2 = Counter(words2)
        count = 0
        for word in dict2:
            if dict1[word] == 1 and dict2[word] == 1:
                count += 1
        return count