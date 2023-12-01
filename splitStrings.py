'''
Given an array of strings words and a character separator, split each string in words by separator.

Return an array of strings containing the new strings formed after the splits, excluding empty strings.
'''

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        #iterate over each string in words
        for word in words:
            #use split() method to split those strings into other strings and remove the seperator
            for i in word.split(separator):
                if i:
                    ans.append(i)
        #return the words array 
        return ans