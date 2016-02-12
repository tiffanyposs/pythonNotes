#Python

[Python Website](http://www.python.org)

[Files](http://www.pythonlearn.com/code/)

To start and exit Python

```
$ python

exit()

```

Reserved Words in Python

```

and       del       from      not       while    
as        elif      global    or        with     
assert    else      if        pass      yield    
break     except    import    print              
class     exec      in        raise              
continue  finally   is        return             
def       for       lambda    try

```

Booleans are capitalized:


```
my_bool = True

```


things need to be indented

```
def spam():
    eggs = 12
    return eggs
        
print spam()

```

Comments are done by a hashtag or tripple quotes


```
#this is a comment
"""This is another way to comment """


```


###String Methods

```
parrot = "Norwegian Blue"
print len(parrot) #14 - like .length
print parrot.lower() # makes lowercase
print parrot.upper() # make uppercase

pi = 3.14
print str(pi) # "3.14" makes to a string

```

* Methods that use dot notations can only be used with strings
* len() and str() can be used with other data types

###Concatination

Just like other programming languages

```
print "Spam " + "and " + "eggs"

```

But this might be a cleaner way:

```
first_name = "Tiffany"
last_name = "Poss"

print "My name is %s %s." % (first_name, last_name)

```

####Raw Input

This will prompt you in terminal

```
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

```

### Datetime

You can get the current date or time

```
from datetime import datetime
now = datetime.now()
print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

print '%s/%s/%s' % (now.month, now.day, now.year)

```

###Control Flow

See the content below for the if else statements

* notice the colons that come after the if statements

```
def matrix():
    print "You've entered the matrix"
    print "Do you pick the red pill or the blue pill?"
    answer = raw_input("Do you pick the red pill or the blue one. type then press enter: ").lower()
    if answer == 'red' or answer == 'r':
        print "you picked the red pill"
    elif answer == 'blue' or answer == 'b':
        print "you picked the blue pill, idiot"
    else:
        print "Thats not an option, try again"
        matrix()

matrix()

```


###Compare Things

* Uses `==` to compare things, 


###Boolean Operators

with booliean operators, `not` is evaluated first, then `and` then `or` . For example:

```
True or not False and False
"""True""""

```

```

"""
     Boolean Operators
------------------------      
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

```

###Generic Import

You must Import some modules, like the math modual for example:

```
import math
print math.sqrt(25)

```

You can also import certain parts so you don't have to keep writing math:

```
from math import sqrt
print sqrt(25)

```

You can also import everything, but this might be dangerous because it takes up a lot of variables.

```
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

```

##Datatypes

###Lists

```

zoo_animals = ["pangolin", "cassowary", "sloth", ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]
	
```

####Appending list items

```
suitcase = []
suitcase.append("sunglasses")

```

####Slicing

#####Lists

```
stuff = [1, 2, 3, 4]
first_half = stuff[0:2] #[1, 2]
second_half = stuff[2:4]

```

#####Strings

```
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]   # From the seventh character to the end

```

####Index

```
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation

```

###For Loops

```
my_list = [1,9,3,8,5,7]

for number in my_list:
    print 2 * number

```

###Sorting

```
start_list = [5, 3, 1, 2, 4]
square_list = []


for num in start_list:
    square_list.append(num**2)
    
square_list.sort()

print square_list

```

###Removing items

```
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

```

###Dictionaries

####Basics

```
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number
print residents["Sloth"]
print residents["Burmese Python"]

```

####Setting & Deleting Values

```
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu['Eggplant Parm'] = 12.25
menu['French Fries'] = 4.50
menu['Ice-Cream'] = 3

print "There are " + str(len(menu)) + " items on the menu."
print menu

del menu['Clicken Alfredo'] #deletes items

```

###For Loops

####Lists

```
var numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print number

```

####Dictionary

```
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}


for key in webster:
    print webster[key]

```


####Examples

```

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for nom in food:
        if stock[nom] >= 1:
            total += prices[nom]
            stock[nom] -= 1
    return total

```



```
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total/len(numbers)
    return total
    
```


###Modifying Lists

`.pop()` `.remove()` `del()`

####pop

`n.pop(index)` will remove that element from the list and return it to you

####remove

`n.remove(element)` will remove the element that matches it and return it

####del

`del(n[1])` will remove the element at that index but not return it


###Ranges

`range(start)` `range(start, stop)` `range(start, stop, step)`

```
range(6) #[0, 1, 2, 3, 4, 5]
range(1,4) #[1, 2, 3]
range(1, 6, 2) #[1, 4]

```

#### Concatinating lists

You can just add two lists together to make one

```
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
    return x+y
    

```


####Look withing a Loop

```
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for list in lists:
        for item in list:
            results.append(item)
    return results

print flatten(n)

```


###While Loops

```
count = 1
while count < 9:
    print count
    count+=1

```

```
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

```

####Breaks

```

count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break
        
```

####While / Else

While / Else loops through until a while is false then it will exicute the else

```
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

```



```
from random import randint

random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left-=1
else:
    print "you lose."

```


###More For Loops

```

hobbies = []

for i in range(3):
    hobby = raw_input("Your hobby: ")
    hobbies.append(hobby)
    
```

You can use it to loop through strings as well

```
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

for w in word:
    print w

```


####Trailing Commas

Add a `,` at the end of a print statement so it prints on the same line. 

```

phrase = "A bird in the hand..."

for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',
    else:
        print char,

```

####Looping through Lists

You can loop through lists

```
numbers = [1, 2, 3]
for num in numbers:
    print num

```

####Looping with Dictionaries

You can loop through dictionaries using the key value

```
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print "%s %s" % (key, d[key])

```


####Looping with Enumerate

Passes the coorisponding index to the looped item.

See the list items below:

```
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item

```

####Zip - Looping Through Multiple Lists

You can loop through multiple lists at once:

```

```


#### For / Else

The else will exicute only if the for loop is not broken by a 'break'

```
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

```


##Advanced Topics

###Iterators for Dictionaries

####.items()

`.items()` makes an array of tuples

```
my_dict = {
   "Name" : "Tiffany",
   "Age" : 27,
   "BDFL" : True
}

print my_dict.items()

```

####.keys() and .values()
Makes an array of the keys or values from a dictionary

```
my_dict = {
   "Name" : "Tiffany",
   "Age" : 27,
   "BDFL" : True
}

print my_dict.keys()
print my_dict.values()

```


####for loops with dictionaries

```
my_dict = {
   "Name" : "Tiffany",
   "Age" : 27,
   "BDFL" : True
}


for key in my_dict:
    print key, my_dict[key]

```

####List Comprehension
`double_by_3` below will double all the numbers from 1-5 if they are evenly divisible by 3

```
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

```


###Lists

####List Slicing

`[start:end:stride]` is the formatting for list slicing, first number represents the start index, second represents the end index and the stride is how many indexes it goes up per step

```
listSlice = range(20)

print listSlice
print listSlice[4:15:2]

```

You can also omit parts of the indices

```
my_list = range(1, 11) # List of numbers 1 - 10


print my_list[2:] #two and after

print my_list[:3] #up until 3

print my_list[::2] #every other

```

#####Reversing a List, negative stride
You can also go through the array backwards by having a negative stride.

```
my_list = range(1,11)

print my_list[::-1] #counts down from 10

```

