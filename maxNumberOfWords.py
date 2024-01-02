'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
'''

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0
        #iterate over each sentence
        for sentence in sentences:
            #split each sentence by space
            sent = sentence.split()
            #get the length of the split sentence
            #if the length is more than output, set output to legth
            if len(sent) > output:
                output = len(sent)

        return output