'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

'''
Step 1 clarify the constraints - does haystack only contain lowercase letters? no numbers? 
Step 2 come up with examples - haystack = doggo, needle = dog, output = 0 - haystack = vibecheck, needle = check, output = 4
Step 3 discuss the approach , ask a permission question to move forward - using the .find() method should return the first instance of the 
Step 4 pseudo code
Step 5 Code
Step 6 discussing space and time complexity
Step 7 Debugging
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)