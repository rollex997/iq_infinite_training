import pyfiglet
# operators related imports
from operators.calculator import *

class DriverOperator:
    def driver_operator(self):
        for i in range (0,9999):
            T = "operator"
            ASCII_art_1 = pyfiglet.figlet_format(T,font="doh")
            print(f"\033[95m{ASCII_art_1}\033[97m")
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>> OPERATOR SECTION <<<                                |
|  1.                                                                                   |
|                                                                                       |
-----------------------------------------------------------------------------------------

               \033[91m
-----------------------------------------------------------------------------------------
|                                                                                       |
|                              >>> TYPE 0 TO EXIT <<<                                   |
|                                                                                       |
-----------------------------------------------------------------------------------------
               \033[97m
            """)
            choice_sets = input("Enter your choice: ")
            if choice_sets =='0':
                T = "Exit"
                ASCII_art_exit = pyfiglet.figlet_format(T,font="doh")
                print(f"\033[91m{ASCII_art_exit}\033[97m")
                break

            elif choice_sets == '1':
                print(f"\033[94mOption 1 \033[97m")

            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print("\n")