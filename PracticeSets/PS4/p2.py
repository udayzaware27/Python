#Write a Python program to accept marks of 6 students and display them in a sorted manner.

marks = []

s1 = int(input("Enter syudent1 marks: "))
marks.append(s1)
s2 = int(input("Enter syudent2 marks: "))
marks.append(s2)
s3 = int(input("Enter syudent3 marks: "))
marks.append(s3)
s4 = int(input("Enter syudent4 marks: "))
marks.append(s4)
s5 = int(input("Enter syudent5 marks: "))
marks.append(s5)
s6 = int(input("Enter syudent6 marks: "))
marks.append(s6)

marks.sort() #sort marks in ascending order

print(marks)