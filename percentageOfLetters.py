'''
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.
'''

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        #create count variable
        count = 0
        #iterate over each letter in s
        for l in s:
            #if that letter equals letter variable
            if l == letter:
                #increase count by 1
                count += 1
        #return count // len(s) * 100  
        return (count * 100) // len(s)