#string functions are built-in functions that can be used to manipulate and work with strings in Python. Here are some commonly used string functions:
str1 = "india is the 5th largest economy in the world"
final1 = str1.endswith("st")#true if string ends with substring else false
final2 = str1.startswith("in")#true if string starts with substring else false
final3 = str1.capitalize()#returns a copy of the string with first character capitalized and rest lower case
final4 = str1.lower()#returns a copy of the string with all characters in lower case
final5 = str1.replace("5th","1st")#returns a copy of the string with all occurrences of old substring replaced by new substring
final6 = str1.split()#returns a list of words in the string, using whitespace as the separator
final7 = str1.split("l")#returns a list of substrings in the string, using "l" as the separator
final8 = str1.find("largest")#returns the lowest index of the substring if found, otherwise returns -1
final9 = str1.count("a")#returns the number of occurrences of the substring in the string
print(final1)
print(final2)
print(final3)
print(final4)
print(final5)
print(final6)
print(final7)
print(final8)
print(final9)