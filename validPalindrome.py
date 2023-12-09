'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create empty string to push to
        string = ''
        #iterate though s
        for char in s:
            #check if the character is alphanumeric .isalnum
            if char.isalnum() == True:
                #if alphanumber, conver to lowercase and append to the empty string
                string += char.lower()
        #check if the modified string matches itself backwords
        return string == string[::-1]