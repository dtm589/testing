'''
The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
'''

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        #create max value varaible
        max_value = 0
        #iterate over each item in strs
        for string in strs:
            #if item is alphanumeric or item is alpha
            if string.isalpha() or string.isalnum():
                #if len(item) > max value
                if len(string) > max_value:
                    #max value = len(item)
                    max_value = len(string)
            #else
            else:
                #if item > max value
                if int(string) > max_value:
                    #max value = item
                    max_value = int(string)
        #return max value
        return max_value