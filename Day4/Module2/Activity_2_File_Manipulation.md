
# Activity: File Manipulation

To better understand exceptions and appropriate error handling, we will be practicing our technique on file manipulation.

Use [Activity_2_File_Manipulation.py](Activity_2_File_Manipulation.py) to code your solution.

## 1. Getting Started

First, let's explore the code we already have. We have provided you with some starter code that asks for a file name, reads the file line by line, closes the file, and then prints the stored content.

Unfortunately, this program is far from complete. What happens if, for example, the file name given by the user is spelled wrong or doesn't exist? The `open()` function can raise a `FileNotFoundError`, a `TypeError`, or an `OSError`. We need to fix the program to handle any of those errors gracefully.

## 2. Error Handling

Your task for this activity is to complete the program by gracefully handling any errors that might come your way. There are many ways to do this, but for this activity you will be creating a class to manipulate files, called `FileManipulator`. To successfully create this class, complete the following steps:

Create the `FileManipulator` class and implement the constructor. The constructor should accept the name of a file to read in and should continually prompt for input if the name given causes an error. Make sure that you give an informative message if an error is raised.
Implement the `reverse()` function. This function should accept the name of a file to write to and should write each line of the original file to this new file. However, in the new file, although the line order will be the same, the string that makes each line will be reversed. So "cheese" will become "eseehc". Be careful not to add an extra newline character at the beginning of the file. Make sure that errors are handled elegantly, and appropriate error messages are given.

## 3. Testing your FileManipulator class

After you have created it, test your `FileManipulator` class by running the given code. Your output should be:

```text
>>> fileManipulator = FileManipulator("tm.txt")
<class 'FileNotFoundError'> [Errno 2] No such file or directory: 'tm.txt'
Please enter a valid file name: tmp.txt
print(fileManipulator.contents)
['I like cheese', 'Do You?']
>>> fileManipulator.reverse("tmp2.txt")
```

At this point, the contents of `tmp.txt` should be:

```text
I like cheese
Do You?
```

And the contents of `tmp2.txt` should be:

```text
eseehc ekil I
?uoY oD
```

## Solution

If you need extra help, the solution code can be found [here](Activity_2_File_Manipulation_Solution.py).

## Bonus: Implement the upper() Function for Your Class

For the bonus activity, create the `upper()` function for your `FileManipulator` class. This function will be similar to the `reverse()` function but has a different result.

This function should accept the name of a file to write to and should write each line of the original file to this new file. However, in the new file, the string that makes each line will be in uppercase. So "cheese" will become "CHEESE". Be careful not to add an extra newline character at the beginning of the file. Make sure that errors are handled smoothly, and appropriate error messages are given.

After you have created it, add the following line to your test code (you should not expect command-line output):

```python
>>>fileManipulator.upper("tmp3.txt")
```

At this point, the contents of `tmp3.txt` should be:

```text
I LIKE CHEESE
DO YOU?
```

It would also be interesting to look into the with keyword in Python. This will handle many of the errors that inherently come with file manipulation, eliminating the need to create big try/except blocks each time you want to use a file.
