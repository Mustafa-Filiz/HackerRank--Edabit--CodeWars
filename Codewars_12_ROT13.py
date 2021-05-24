# ROT13
"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

def rot13(message):
    import string
    cipher = ""
    for i in message:
        if i in string.ascii_uppercase:
            if string.ascii_uppercase.index(i) < 13:
                cipher += string.ascii_uppercase[string.ascii_uppercase.index(i) + 13]
            else:
                cipher += string.ascii_uppercase[string.ascii_uppercase.index(i) - 13]
        elif i in string.ascii_lowercase:
            if string.ascii_lowercase.index(i) < 13:
                cipher += string.ascii_lowercase[string.ascii_lowercase.index(i) + 13]
            else:
                cipher += string.ascii_lowercase[string.ascii_lowercase.index(i) - 13]
        else:
            cipher += i
    return cipher