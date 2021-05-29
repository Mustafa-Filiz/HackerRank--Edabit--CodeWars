# Convert string to camel case
"""
Complete the method/function so that it converts dash/underscore 
delimited words into camel casing. The first word within the output 
should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    #your code here
    import string

    for i in text:
        if i in string.punctuation:
            text = text.replace(i, " ")
            
    arr = text.split()         
    new_arr = [arr[i].title() if i > 0 else arr[i] for i in range(len(arr))]
    
    return "".join(new_arr)