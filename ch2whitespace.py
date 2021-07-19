'''
Whitespace in strings. 
Any space that is NOT a letter, digit or anything of the sort and is just blank, is considered "whitespace"

Full Name has whitespace between "Full" and "Name"
FullName has no whitespace though. 
'''

#the tab character can be used as \t 

print('python')
#this just prints normally:
    #python
print('\tpython')
#this one prints with a tab:
    #   python

'''
There are also other functions built in with "\", such as \n which is the new line character. 
'''

print("Languages:\nPython\nC\nJavaScript")
    #Here we have the \n character saying that AFTER "Languages:", "Python", "C", "JavaScript" there are new lines. 

'''
Output: 

Languages:
Python
C
JavaScript
'''

print("Languages:\n\tPython\n\tC\n\tJavaScript")
    #here is basically the same as the previous, BUT, we have the \n\t which means \n to create a new line, but right after that
    #we have the \t character which means to print this after a tab. 

'''
Output:

Languages:
    Python
    C
    JavaScript
'''
