# -*- coding: utf-8 -*-
"""
IF ELSE STATEMENT AND DICTIONARY
IF ELSE , WHILE STATEMENT AND DICTIONARY

"""

def perform_action (input_str):
    
    actions = {
        "print ": lambda x: print(x),
        "uppercase": lambda x: print(x.upper()),
        "lowercase": lambda x: print(x.lower())
    }
    while input_str != "quit":
        action = actions.get(input_str, None)
        if action:
            action("Hello World!")
        
        else:
            print("Invalid Input.")
        input_str = input("Enter an action to perform (print/uppercase/lowercase): ('Quit' to 'Exit'): ")
        
    print("Exiting Program...")
    
user_input = input ("Enter an action to perform (print/uppercase/lowercase):('Quit' to 'Exit'): ")
perform_action(user_input)