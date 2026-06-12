# Print Contents of a Directory Using os Module Program with Comments

# Import os module
import os

# Get all files and folders from current directory
contents = os.listdir()

# Print each item
for item in contents:
    print(item)