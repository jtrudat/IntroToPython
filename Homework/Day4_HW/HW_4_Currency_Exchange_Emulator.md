# Currency Exchange Emulator

Your task for this activity is to complete the necessary magic methods to allow the provided code to function. We will first walk through what a magic method is, and then walk through the specific magic methods that you need to add to your code.

## Step 1: Understanding Magic Methods

Magic methods are a special piece of Python programming. They are specific to Object Oriented Programming in Python, meaning that they can only be implemented in, and will only work in, classes.

They allow actions to be performed on class instance objects that are otherwise impossible, such as printing and comparing.

Magic methods will always take the `__<>__()` form. For example, in the following code snippet the `__str__()` magic method is defined for the `Car` class.

```python
class Car:
    # [...]

    def __str__(self):
        return f"make: {self.make}, model: {self.model}"

myCar = Car("Hyundai","Sonata")
print(myCar) #make: Hyundai, model: Sonata
```

We have already seen and worked with one magic method: the `__init__(self,...)` function. This is a magic method! We have already discussed some of its special features, but for this conversation, it is important that it gets called behind the scenes without us needing to call it explicitly.

**Magic methods are never called directly. They are always called behind the scenes when specific events trigger them.**

### Magic Methods Example

Source: [Python Docs](https://docs.python.org/2/reference/datamodel.html#special-method-names)

There are many magic methods that can be implemented for any class we write. Some of them, such as those shown here, are implemented by default. However, they can also be overwritten, such as in our example of the `__str__()` function in the `Car` class, shown above. Remember, overwriting a function means that the function may already exist, but we write over what is there by re-defining the function.

Whenever we create a new class, Python creates a `__str__()` function for us by default. The default implementation is often not very useful, since it only prints out the address in memory of our object. By overwriting the `__str__()` function, we make our class more usable.

Magic methods help our classes to be more useful. They enable us to use some common functions, such as `print()` and `len()`. They also allow us to perform comparisons, such as `<`, `>`, `<=`, `>=`, and `==`.

To use these operators, the following shorthand guide may be useful:

```python
__lt__(self, other) # <
__gt__(self, other) # >
__le__(self, other) # <=
__ge__(self, other) # >=
__eq__(self, other) # ==
__ne__(self, other) # !=
```

By default, comparisons including instances of any user-defined classes are based on the address where the objects are stored. This is rarely desired behavior. Instead, by implementing the comparison magic methods shown above, the program writer can control how their objects interact with other objects.

For example, consider the following code:

```python
class Car:
    #[...]

    def __eq__(self,other): # ==
        if self.make == other.make and self.model == other.model:
            return True
        else:
            return False

    def __ne__(self,other): # !=
        if self == other:
            return False
        else:
            return True

car1 = Car("Hyundai", "Sonata")
car2 = Car("Hyundai", "Sonata")
car3 = Car("Honda",   "Accord")

print(car1 == car2)   #True  (self is car1, other is car2)
print(car1 == car3)   #False (self is car1, other is car3)
print(car2 != car3)   #True  (self is car2, other is car3)
```

**Note: Each of the comparison methods MUST return a `Boolean`, or `True`/`False`, value. It is assumed that the 'other' will be another object of the same class, but sometimes including a check for that and throwing an error otherwise is a good idea. (In our example, if we had tried to compare `car1 == 3`, we would get an error rather than a `False`.**

```python
__repr__(self) # string conversions
__str__(self)  # string representations
```

The `__repr__(self)` and `__str__(self)` functions should almost always both be implemented and should both return identical strings.

These functions must return strings. It is best practice to have the same strings returned for each method. The syntactical difference between these two methods may be unclear at the start. That is okay, just make sure that both get implemented and return the same string.

See the following code for an example:

```python
class Car:
    #[...]

    def __str__(self):
        return f"make: {self.make}, model: {self.model}"

    def __repr__(self):
        return f"make: {self.make}, model: {self.model}"
```

In conclusion, magic methods are special methods that can be defined on custom classes that are designed to help certain operations be easier. Every magic method has its own pre-defined behavior and expected return value. Care should be taken to make sure that vital requirements and assumptions about parameters and return values are not broken.

## Step 2: Creating a Currency Exchange Emulator

To better understand magic methods and how they are used, we will be creating a Currency Exchange Emulator.

The starter code for this assignment is in [HW_4_Currency_Exchange_Emulator.py](HW_4_Currency_Exchange_Emulator.py).

If you try to run [HW_4_Currency_Exchange_Emulator.py](HW_4_Currency_Exchange_Emulator.py) before making any changes, you will get an error. This is intentional - the test code at the bottom is using operators that will only be defined for the class after you have implemented them.

### 1. Getting Started

First, let's explore the code we already have. We have provided you with a base `Currency` class that contains a class dictionary called `currencies`, which contains some currency exchange rates, using USD as a base value. Feel free to update this table if you desire. Note that doing so will change the expected output of the program.

We have also provided you with the class constructor and a `changeTo()` function for converting between currencies. Feel free to play with these elements.

### 2. Building Magic Methods

Your task for this activity is to complete the necessary magic methods to allow the provided code to function. The first three have been outlined for you, the others you will need to add manually from scratch. For the pre-defined functions, make sure to remove the `pass` statement before coding the desired return values, or they may not work. These methods are:

|                    Name |                                                                                                                                                                                        Description |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `__repr__(self)`        | This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.                                                                          |
| `__str__(self)`         | This method returns the same value as `__repr__(self)`.                                                                                                                                            |
| `__add__(self, other)`  | Defines the '+' operator. If other is a Currency object, the currency values are added, and the result will be the unit of self. If other is an int or a float, it will be treated as a USD value. |
| `__iadd__(self, other)` | This is the same as (calls) `__add__(self, other)`.                                                                                                                                                |
| `__radd__(self, other)` | This method is similar to `__add__(self, other)`, but occurs when an int or float tries to add a Currency object. (Treat the int/float as having a USD value.)                                     |
| `__sub__(self, other)`  | All `__sub__(self, other)` type functions are parallel to `__add__(self, other)` type functions.                                                                                                   |
| `__isub__(self, other)` |                                                                                                                                                                                                    |
| `__rsub__(self, other)` |                                                                                                                                                                                                    |

### 3. Testing Your Currency Class

After you have defined your magic methods, test your `Currency` class by running the given code (starter code included). It should run with no errors if you have implemented all of the magic methods correctly.

In case you changed it, the test code is:

```python
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
```

Your output should be:

```text
40.65 EUR
47.14 USD
26.02 EUR
30.17 USD
20.84 EUR
10.03 USD
```

**Remember, if you changed the values of the currency exchange rates, this output will also be different.**

If you need extra help, the solution code can be found in [HW_4_Currency_Exchange_Emulator_Solution.py](HW_4_Currency_Exchange_Emulator_Solution.py).

## Acceptance Criteria

- There should be no errors displayed in the console.
  - If there are errors you could not solve, comment out the lines throwing errors and explain what steps you used to try and fix them.
- When running, the output in the console should be as shown in the code snippet above.

Before submitting, make sure you do a self-review of your code, check for formatting and spelling, and include comments in your code.

Make sure to submit your [HW_4_Currency_Exchange_Emulator.py](HW_4_Currency_Exchange_Emulator.py) link on the submission page.
