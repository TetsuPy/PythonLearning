'''
Whitespace pt. 2
Stripping whitespaces. 
'''

#Having extra whitespace is just plain annoying in your program/code. 
#You think, "is this supposed to be here?" or "do I need this for the program to work?"
#Having little to no whitespace also makes your code look cleaner honestly. 

fav_lang = 'python ' 
mark = "!"
print(fav_lang + mark)

#here we have the extra whitespace at the end of 'python' so it outputs 'python !' which looks weird and awkward. 

print(fav_lang.rstrip() + mark)
#this might be a longer process because the original example doesn't work but here, the right whitespace has been stripped from the 'python'
#and now it outputs 'python!' and looks fine

#you can also permanently strip the white space

new_lang = fav_lang.rstrip()
mark = "!"
print(new_lang + mark)
#the one above stores the same message of "fav_lang.rstrip()" into a new variable. So that new variable permanently has "rstrip()" in it 

'''
Syntax Errors
'''

'''message = 'Part of python's strengths is its diverse community"'''
#You don't even have to try printing this, it literally stops writing in orange, which is what a string should be in
#Because it thinks you've ended the string at "python" and everything afterwards is not included. 

#instead, try using the \ character, i.e. python\'s strengths ...

message = 'part of python\'s strength is the diverse community'

#what the "\" does is, it takes away what the next character WOULD do and makes it seem like a regular character. 
#this time, because I used " \' ", the apostrophe, instead of ending the string just continues the string like it should. 

'''
2.3 - Personal Messages:
    store a persons name in a variable and print a message to that person. 
    i.e. "Hello Eric, would you like to learn python today?"
2.4 - Name Cases:
    Store a persons name in a variable, again, but this time print it three times, upper, lower, and titled. 
2.5 - Famous Quote:
    Find a quote from someone you like and write it like so:
        Albert Eintstein once said: "A person who never made a mistake has never tried something new"
2.6 - Famous Quote Pt. 2: 
    Repeat 2.5 but this time, store the person's name in a variable called 'famous_person', then compose the message into a 
    variable called "message" and print out the message.
2.7 - Strip names of white space. 
    Store a person's name including some whitespace at the beginning and end. 
    use \t and \n at least once in this exercise.
        Print the name once so the whitespace is shown, then use:
        .lstrip(), .rstrip(), and .strip() for the whitespace. 
'''

#2.3

# name = "Eric Lam"
# print('Hello ' + name + " would you like to learn Python?")

# #2.4

# name = "Eric Lam"
# print('Hello ' + name.lower() + " would you like to learn Python?")

# name = "Eric Lam"
# print('Hello ' + name.upper() + " would you like to learn Python?")

# name = "Eric Lam"
# print('Hello ' + name.title() + " would you like to learn Python?")


#2.5

print('Nikki said: \'I like ABB\'s')

#2.6
# famous_person = "Nikki"
# message = famous_person + 'I like ABB\'s'

# print(message)

#2.7

name = ' Albert \n Einstein ' + "@"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

