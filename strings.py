import os

os.system("clear")

#DATA TYPES
#Strings

mom = "Alice"
yell = f"My mom {mom} yelled: \n'Clean your room!'"
myname = "my name is John Doe"

# Print strings
print (yell)

# String manupulation
print (myname.split(" ")) # Split string into list
print (myname.upper()) # Uppercase string
print (myname.lower()) # Lowercase string
print (myname.replace("John", "Jane")) # Replace string content
print (myname.capitalize()) # Capitalize string
print (myname.title()) # Title case string
print (myname.find("John")) # Find string position
print (myname.index("Doe")) # Find string position
