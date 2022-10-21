""" acivity for errors
fileName = input("Please enter hte name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file
"""

class FileManipulator:
    def __init__(self, fileName):
        pass

    def reverse(self, fileName):
        pass

    #bonus
    def upper(self, fileName):
        pass

# Test Code
fileManipulator = FileManipulator("tm.txt")

print(fileManipulator.contents)

fileManipulator.reverse("tmp2.txt")
fileManipulator.upper("tmp3.txt")
