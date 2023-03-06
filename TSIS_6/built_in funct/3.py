str_1 = input()
str_1 = str_1.casefold()
rev_str = reversed (str_1)
if (list(str_1))==list(rev_str):
    print("String is palindrome")
else:
    print("String is not pelindrome")