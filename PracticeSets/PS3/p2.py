'''Write a Python program to fill in the following letter template with a user's name and date:
letter = 
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter a name: ")
date = input("Enter a date: ")

print(f"Dear {name}, \nYou are selected! \n{date}") 

letter = '''
Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", name).replace("<|Date|>", date)) #another way