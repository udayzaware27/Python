a = ["Akash", "Apple", 27, 3.14, False, "King"]
print(a)

a.append(9) #Adds an element at the end
print(a) 

a.insert(3, 3333) #Adds an element at a specific index.
print(a)

value = a.pop(2) #Removes and returns an element.
print(value)
print(a)

a.remove(3.14) #Removes the specified value.
print(a)

b = [20, 3, 34, 1, 21, 5]

b.sort() #Sorts the list in ascending order.
print(b)

c = [1, 2, 3, 4]
c.reverse() #reverse the list
print(c)

d = [1, 4, 1, 6, 4, 1] 
print(d.count(1)) #Counts occurrences of an element.

l1 = [1, 4]
l2 = [3, 5]
l1.extend(l2) #Adds multiple elements from another list.
print(l1)
