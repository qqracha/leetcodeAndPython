'''
Any 
Return True if bool(x) is True for any x in the iterable.
If the iterable is empty, return False.
'''

x = [0, 0, 0, 1]

if any(x):
    print('yes')
else: 
    print('no')

# yes

# any() function returns True if at least one of the arguments is True