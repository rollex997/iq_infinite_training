# String related imports
from strings.palindrom import *
from strings.symmetry import *
from strings.reverse import *
from strings.length_string import *
from strings.length_without_spaces import *
from strings.find_even_length_words import *

welcome_message = """
**      **  ********  **       **          **
**      **  **        **       **        **  **
**********  ********  **       **       **    **
**********  ********  **       **       **    **
**      **  **        *******  *******   **  **
**      **  ********  *******  *******     **
"""
print(welcome_message)
print(r"""\

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   ಠ ಠ. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)

#Driving loop
for i in range(0,9999):
    #Enter choice
    print("Choose the items in the menu by using numbers : ")
    print("Press 'n' or 'N' to exit program")
    print("--------------------------------------------------")
    print("--- String Section ---")
    print("1. Check Palindrome ")
    print("2. Check Symmetry ")
    print("3. Reverse String ")
    print("4. Length of a String ")
    print("5. Length of a String (EXCLUDING WHITE SPACES) ")
    print("6. Even Length words in a String ")
    choice_input = input("Enter your choice: ")
    print('\n')

    #driving palindrome
    if choice_input == '1':
        print("Option 1 Check Palindrome -->")
        word = input("Enter the word that you want to check :")
        pd = Palindrome(word)
        print(f"The entered word is : {pd.get_ch_string()}")
        pd.check_palindrome()
        print('\n')

    elif choice_input == '2':
        print("Option 2 Check Symmetry -->")
        word = input("Enter the word that you want to check :")
        sm = Symmetry(word)
        print(f"The entered word is : {sm.get_ch_string()}")
        sm.check_symmetry()
        print('\n')

    elif choice_input == '3':
        print('Option 3 Reverse the given string -->')
        word = input("Enter the string to be reversed :")
        rv = Reverse(word)
        print(f"the entered string : {rv.get_word()}")
        rv.reverse_word()
        print('\n')

    elif choice_input == '4':
        print('Option 4 Length of a given string -->')
        word = input("Enter the string to get it's length :")
        len = Length(word)
        print(f"the entered string : {len.get_word()}")
        length = len.length_of_string()
        print(f"The length of the string is : {length}")
        print('\n')
    
    elif choice_input == '5':
        print('Option 5 Length of a given string (EXCLUDING WHITE SPACES) -->')
        word = input("Enter the string to get it's length :")
        lws = LengthWithoutSpaces(word)
        print(f"the entered string : {lws.get_word()}")
        len_without_spaces = lws.length_without_spaces()
        print(f"The length of the string is (EXCLUDING WHITE SPACES) : {len_without_spaces}")
        print('\n')

    elif choice_input == '6':
        print('Option 6 Get the string that has even length -->')
        word = input("Enter the string :")
        few = FindEvenLengthWords(word)
        print(f"the entered string : {few.get_word()}")
        few.find_even_length_words()
        print('\n')

    elif choice_input == 'n' or choice_input == 'N':
        print("Terminating program")
        welcome_message = """
        *******      *       *    *********
        *      *      *     *     *
        *       *      *   *      *
        *      *        * *       *
        *******          *        *********
        *      *        *         *
        *       *      *          *
        *      *      *           *
        *******      *            **********
        """
        print(welcome_message)
        print('\n')
        break
    else:
        print("Wrong input")
        print('\n')

