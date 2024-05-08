# Palindrome 
'''
Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome
'''
# Palindrome : Solution

class Palindrome:
    def __init__(self, ch_string):
        self.__ch_string = ch_string
    def get_ch_string(self):
        return self.__ch_string
    def set_ch_string(self,ch_string):
        self.__ch_string = ch_string
    def check_palindrome(self):
        word = self.__ch_string
        mid = (len(word))//2
        start = 0
        last = len(word)-1
        flag = 0
        while(start<=mid):
            if word[start] == word[last]:
                start+=1
                last-=1
                flag=0
            else:
                flag=1
                break
        if flag==0:
            print(f" The word '{word}' is a Palindrome ")
        else:
            print(f" the word '{word}' is not a Palindrome ")