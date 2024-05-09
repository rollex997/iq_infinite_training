# String related imports

#utility related imports
from list_package import ListPackageFiles

#string relataed imports
from strings.palindrom import *
from strings.symmetry import *
from strings.reverse import *
from strings.length_string import *
from strings.length_without_spaces import *
from strings.find_even_length_words import *
from strings.half_string import *
from strings.cap_first_last import *
from strings.count_alpha_num import *
from strings.matching_chars import *
from strings.count_vowels import *

welcome_message = """
\033[95m **      **  ********  **       **          **       \033[91m   ---------    \033[97m
\033[95m **      **  **        **       **        **  **     \033[91m  /         \   \033[97m
\033[95m **********  ********  **       **       **    **    \033[91m  |  /\ /\  |   \033[97m
\033[95m **********  ********  **       **       **    **    \033[91m  |    -    |   \033[97m
\033[95m **      **  **        *******  *******   **  **     \033[91m  |  \___/  |   \033[97m
\033[95m **      **  ********  *******  *******     **       \033[91m  \         /   \033[97m
                                                     \033[91m   ---------    \033[97m
"""
print(welcome_message)
print(r"""

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
    print("")
    print("""
          \033[91m
-----------------------------------------------------------------------------------------
|                                                                                       |
|                           Press 'n' or 'N' to exit program                            |
|                                                                                       |
-----------------------------------------------------------------------------------------
          \033[97m
    """)
    print("""
          \033[94m
-----------------------------------------------------------------------------------------
|                                                                                       |
|            0. Check the list of files present in a package (FOR DEVS ONLY)            |
|                                                                                       |
-----------------------------------------------------------------------------------------
          \033[97m
    """)
    print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                        >>> String Section <<<                                         |
|  1.  Check Palindrome                                                                 |
|  2.  Check Symmetry                                                                   |
|  3.  Reverse String                                                                   |
|  4.  Length of a String                                                               |
|  5.  Length of a String (EXCLUDING WHITE SPACES)                                      |
|  6.  Even Length words in a String                                                    |
|  7.  Half String (Converts the characters to upper case of half of the string passed) |
|  8.  Convert first and last characters in a string to capital letters                 |
|  9.  Count number of alphabets and numbers present in a string                        |
|  10. It will tell the characters that are common in two strings                       |
|  11. Count vowels in a string                                                         |
-----------------------------------------------------------------------------------------
    """)
    choice_input = input("Enter your choice: ")
    print('\n')
    #driving list_package_files
    if choice_input == '0':
        print("""
      \033[91m      **         *  **     \033[97m  **     ******  *     *       **    **      *  *     *       *
      \033[91m     **         *    **    \033[97m  * *    *       *     *      *  *   * *     *  *      *     *
      \033[91m    **         *      **   \033[97m  *  *   *       *     *     *    *  *  *    *  *       *   * 
      \033[91m   **         *        **  \033[97m  *   *  *****   *     *     *    *  *   *   *  *        * *
      \033[91m    **       *        **   \033[97m  *  *   *        *   *      *    *  *    *  *  *         *
      \033[91m      **    *        **    \033[97m  * *    *         * *        *  *   *     * *  *         *
      \033[91m       **  *        **     \033[97m  **     ******     *          **    *      **  ********  *
              

                   \033[92m        .---------------------------------.
                   \033[92m        |  .---------------------------.  |
                   \033[92m        |[]|\033[94m         __   __   *       \033[92m|[]|
                   \033[92m        |  |\033[94m        /  | /  | /        \033[92m|  |
                   \033[92m        |  |\033[94m       (___|(___|(         \033[92m|  |
                   \033[92m        |  |\033[94m       |   )|    |         \033[92m|  |
                   \033[92m        |  |\033[94m       |  / |    |         \033[92m|  |
                   \033[92m        |  |\033[94m /              |         |\033[92m|  |
                   \033[92m        |  |\033[94m(  ___  ___  ___| ___  ___|\033[92m|  |
                   \033[92m        |  |\033[94m| |   )|   )|   )|___)|   )\033[92m|  |
                   \033[92m        |  |\033[94m| |__/ |__/||__/ |__  |__/ \033[92m|  |
                   \033[92m        |  '---------------------------'  |
                   \033[92m        |                                 |
                   \033[92m        |                                 |
                   \033[92m        |  '---------------------------'  |
                   \033[92m        |  | .------.         |      | |  |
                   \033[92m        |  | |      |         |      | |  |
                   \033[92m        |  | |      |         |      | |  |
                   \033[92m        |  | |      |         |      | |  |
                   \033[92m        |  | '------'         |      | |  |
                   \033[92m        -----------------------------------
\033[97m
        """) 
        package_name = input("Enter your package name:")
        lpf = ListPackageFiles(package_name)
        try:
            files = lpf.list_package_files()
            print("\033[93mFiles in package \033[95m'{}':\033[97m".format(package_name))
            for file in files:
                print(f"\033[92m-{file}\033[97m")
            print("\n")
        except Exception as e: 
            print(str(e))
            print("\033[91m!!! PACKAGE NOT FOUND !!!\033[97m")
            print("\n")

    #driving palindrome
    if choice_input == '1':
        print("\033[94mOption 1 Check Palindrome -->\033[97m")
        word = input("Enter the word that you want to check :")
        pd = Palindrome(word)
        print(f"The entered word is : {pd.get_ch_string()}")
        pd.check_palindrome()
        print('\n')

    elif choice_input == '2':
        print("\033[94mOption 2 Check Symmetry -->\033[97m")
        word = input("Enter the word that you want to check :")
        sm = Symmetry(word)
        print(f"The entered word is : {sm.get_ch_string()}")
        sm.check_symmetry()
        print('\n')

    elif choice_input == '3':
        print('\033[94mOption 3 Reverse the given string -->\033[97m')
        word = input("Enter the string to be reversed :")
        rv = Reverse(word)
        print(f"the entered string : {rv.get_word()}")
        rv.reverse_word()
        print('\n')

    elif choice_input == '4':
        print('\033[94mOption 4 Length of a given string -->\033[97m')
        word = input("Enter the string to get it's length :")
        len = Length(word)
        print(f"the entered string : {len.get_word()}")
        length = len.length_of_string()
        print(f"\033[92mThe length of the string is : {length}\033[97m")
        print('\n')
    
    elif choice_input == '5':
        print('\033[94mOption 5 Length of a given string (EXCLUDING WHITE SPACES) -->\033[97m')
        word = input("Enter the string to get it's length :")
        lws = LengthWithoutSpaces(word)
        print(f"the entered string : {lws.get_word()}")
        len_without_spaces = lws.length_without_spaces()
        print(f"\033[92mThe length of the string is (EXCLUDING WHITE SPACES) : {len_without_spaces}\033[97m")
        print('\n')

    elif choice_input == '6':
        print('\033[94mOption 6 Get the string that has even length -->\033[97m')
        word = input("Enter the string :")
        few = FindEvenLengthWords(word)
        print(f"the entered string : {few.get_word()}")
        few.find_even_length_words()
        print('\n')

    elif choice_input == '7':
        print('\033[94mOption 7 Half String (Converts the characters to upper case of half of the string passed)\033[97m ')
        word = input("Enter the string :")
        hs = HalfString(word)
        print(f"the entered string : {hs.get_word()}")
        half_string_var = hs.half_string()
        if not half_string_var == -1:
            print(f"\033[92mHalf String Result : {half_string_var}\033[97m")
        else:
            print("\033[91mThe Half String class Failed to return a result\033[97m")
        print('\n')
    
    elif choice_input == '8':
        print("\033[94mOption 8 Convert first and last characters in a string to capital letters\033[97m ")
        word = input("Enter the string :")
        cfl = CapFirstLast(word)
        print(f"the entered string : {cfl.get_word()}")
        result = cfl.cap_first_and_last_letter()
        print(f"\033[92mCapitalized first and last characters of a string : {result}\033[97m")
        print('\n')
    
    elif choice_input == '9':
        print("\033[94mOption 9 Count number of alphabets and numbers present in a string\033[97m ")
        word = input("Enter the string :")
        can = CountAlphaNum(word)
        print(f"the entered string : {can.get_word()}")
        result = can.count_alpha_and_num()
        print(f"\033[92mNumber of Alphabets : {result['count_alpha']}\033[97m")
        print(f"\033[92mNumber of Digits : {result['count_num']}\033[97m")
        print(f"\033[92mTotal Characters : {result['total']}\033[97m")
        print('\n')

    elif choice_input == '10':
        print("\033[94mOption 10 It will tell the characters that are common in two strings\033[97m ")
        first_word = input("Enter the first string :")
        second_word = input("Enter the second string :")
        mc = MatchingChar(first_word,second_word)
        print(f"the first entered string : {mc.get_first_word()}")
        print(f"the second entered string : {mc.get_second_word()}")
        result = mc.match_char()
        print(f"\033[92mCommon Characters : {result['common_char']}\033[97m")
        print(f"\033[92mNumber of common characters : {result['common_char_count']}\033[97m")
        print('\n')
        
    elif choice_input == '11':
        print("\033[94mOption 11 Count vowels in a string\033[97m ")
        word = input("Enter the string :")
        cvw = CountVowels(word)
        print(f"the entered string : {cvw.get_word()}")
        result = cvw.count_vowels()
        print(f"\033[92mNumber of Vowels in the string : {result}\033[97m")
        print('\n')

    elif choice_input == 'n' or choice_input == 'N':
        print("Terminating program")
        welcome_message = """
\033[91m
        *******      *       *    *********               
        *      *      *     *     *
        *       *      *   *      *
        *      *        * *       *
        *******          *        *********
        *      *        *         *
        *       *      *          *
        *      *      *           *
        *******      *            **********
\033[97m
        """
        msg = """
\033[93m                          $$$$$$$$$$$$$$$$$$$$                                                              
\033[93m                       $$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                      
\033[93m                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$         $$   $$$$$                                                        
\033[93m    $$$$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$$$$$$$                                                            
\033[93m $$ $$$$$$      $$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$       $$$$$$$$                                                                  
\033[93m $$$$$$$$$     $$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$    $$$$$$$$                                                               
\033[93m   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$                                                                
\033[93m   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  $$$$$$                                                                        
\033[93m    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$                                                                       
\033[93m     $$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$$                                                                
\033[93m    $$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$                                                                   
\033[93m    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$                                                            
\033[93m   $$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$                                                                    
\033[93m   $$$$$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$$$$$                                                                        
\033[93m  $$$$       $$$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      $$$$                                                                                       
\033[93m             $$$$$     $$$$$$$$$$$$$$$$$$$$$$$$$         $$$                                                                                         
\033[93m               $$$$          $$$$$$$$$$$$$$$           $$$$                                                                                          
\033[93m                $$$$$                                $$$$$                                                                                             
\033[93m                 $$$$$$      $$$$$$$$$$$$$$        $$$$$                                                                                                      
\033[93m                   $$$$$$$$     $$$$$$$$$$$$$   $$$$$$$                                                                                                     
\033[93m                      $$$$$$$$$$$  $$$$$$$$$$$$$$$$$                                                                                                       
\033[93m                         $$$$$$$$$$$$$$$$$$$$$$                                                                                                            
\033[93m                                 $$$$$$$$$$$$$$$                                                                                                    
\033[93m                                     $$$$$$$$$$$$                                                                                                          
\033[93m                                      $$$$$$$$$$$                                                                                                
\033[93m                                       $$$$$$$$                                                                 
\033[97m
"""
        print(welcome_message)
        print(msg)
        print('\n')
        break
    else:
        if choice_input == '0':
            print("Dev only operation!!")
            print('\n')
        else:
           print("Wrong input")
           print('\n')

