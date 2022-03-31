# Aim:-  Program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()    # make it suitable for caseless comparison

rev_str = reversed(my_str)    # reverse the string

if list(my_str) == list(rev_str):         # check if the string is equal to its reverse
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")