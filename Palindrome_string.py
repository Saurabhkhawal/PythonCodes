# Check if a string is a palindrome.
String = input("Enter a String :") # Level
Reverse = (String[::-1]).lower()
if Reverse == String.lower():
    print("String is palindrome.")
else:
    print("String is not palindrome")