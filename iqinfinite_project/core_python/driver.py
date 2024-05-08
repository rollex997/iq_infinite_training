from strings.palindrom import *
from strings.symmetry import *
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

