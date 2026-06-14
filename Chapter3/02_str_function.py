a = "Hello world"

print(len(a))  #length of function

print(a.capitalize())  #capitalize first letter of only first word

print(a.endswith("ld"))  #check string ends with specific letter
print(a.startswith("el"))  #check string starts with specific letter

print(a.upper()) #return all string letters in capitalize
print(a.lower()) #return all string letters in smallercase

print(a.count("l")) #counts occurence of character

print(a.find("ld")) #returns the index of first occurence

print(a.replace("world", "india")) #replace old word with new world

b = " Hello "
print(b)
print(b.strip()) #remove the space from both ends

c = "apple, banana, chery"
print(c)
print(c.split(",")) #convert string into list
