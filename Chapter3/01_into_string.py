a = "hello" #double quote string
b = 'hello' #single quote string
c = '''hello''' #multi quote string

print(c[0:3]) #start from 0 till 3 (excluding 3)

print(c[:4]) # same as c[0:4]
print(c[0:]) # same as c[0:5] means to the length

# Negative Slicing
print(c[-4 : -1]) #start from -4 till -1 (excluding -1) also same as c[1:4]
print(c[1:4])


# Slicing with skip value
k = "amazing"
print(k[1:6:3])  # it first execute k[1:6], read first letter then skip 3 letters and read next