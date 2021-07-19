'''
Changing case in a string in python
'''

name = "ada lovelace"
print(name.title())

#.title() makes it so that when you print the string, in this case 
#it goes from "ada lovelace" to "Ada Lovelace"

#There is also .upper() which puts all caps
    #i.e. you can have a message like this, "hELLo wOrlD" but if you do something like:
        #name = "hELLo wOrlD", and do print(name.upper())
            #output = HELLO WORLD
#then .lower() which put it in all lowercase. 
    #i.e. you can have a message like this, "hELLo wOrlD" but if you do something like:
        #name = "hELLo wOrlD", and do print(name.lower())
            #the output will just be hello world

'''
Combining/Concatenating Strings
'''

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name

print(full_name.title())

#in this case, if you were to greet her:
    #it would be print("hello " + full_name.title() + "!")
        #to create the output of "hello Ada Lovelace!"


