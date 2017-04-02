Hello. This document is meant to serve as a written version of a UOHack session first given in the fall of 2016 at the University of Oregon. While I don't expect the topics wherein to change dramatically over time, please know that this content could become stale.

The concepts listed below should give you a very basic understanding of the basics of programming. These are very high-level examples given in Python. It may seem like the examples are overly simplistic and that's the point. I am not writing this to teach you how to program things, I'm writing it to introduce you to the tools necessary to begin learning about programming. That said, if these concepts do not come easy to you that's ok. For most, this is an entirely different way of thinking that requires practice to become comfortable with. Give it time, read other sources, start building simple scripts and keep working at it. Let's get started.

# What is code?

Everyone has their own idea of what "code" is. I'm not going to explain all the ways popular media has taken a simple concept and blown it out of proportion. I'd like you to try and put those pre-concieved notions aside for a minute and let me give you a new definition.

Coding, or programming, is nothing more than a human giving a series of instructions to a computer. That's it.

Sometimes there are a lot of instructions linked together. Sometimes different sets of instructions work together to do different things. But at the end of the day, programming, as we know it today, is just a series of instructions and complex code is nothing more than a large collection of simple instructions.

*Note: It's very important that **journalists** and the public understand that most coding is the process of giving simple instructions to a computer. When reporting on code or programming it is imperative that you not perpetuate the stereotypes that pop culture has created about programming.*

### Languages

In order to give a computer instructions we have to talk to it in a language that it can understand. There are many different types of programming languages, each with certain benefits and drawbacks. These languages act as a sort of translator between us and a computer.

You see, at the end of the day a computer truly only deals in ones and zeros. Those ones and zeros are called binary and anything that you do on a computer is eventually deconstructed into binary for a computer to execute.

Generally what happens is you have some bit of code in a high-level language like Python. High-level languages are pretty easy for humans to use but are further away from binary (AKA: machine language). That high-level code is [compiled](https://www.reddit.com/r/explainlikeimfive/comments/233dq5/eli5_what_does_it_mean_to_compile_code/) into machine language that the computer can understand.

*Note:* `01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100` *is "Hello world" in binary.*

### Python

Today we will use the Python programming language for our examples. Python is a high-level language that a lot of computer science programs are using to teach introduction classes.

Python is also easier to read and write than a lot of other languages. Some people prefer Ruby, which is very comparable to Python. In fact, Ivar Vong used to use Ruby in some UOHack sessions. *(Shh... Don't tell Ivar I'm doing Python and not Ruby.)*

Some projects lend themselves more to one language than another. For instance, Swift is the language used to create iOS applications. You cannot build an Android app with Swift. However, if you want to build an app for both, there are some [JavaScript platforms](https://www.nativescript.org/about) that will render out iOS and Android app code. It depends on what you're trying to do.

### So, what language should you learn as your first language?

That's always everyone's first question. Well, it doesn't really matter.

There are certainly some employers that use one language over another, but it is **much** more important that you simply become comfortable with one language, any language. If you can get comfortable with one language, it is much easier to pick up another.

It's just like learning a foreign language. For instance, if you learn Spanish, then there are other languages like French and Italian that would be pretty easy for you to pick up. But learning Russian may still be difficult.

*Note: There are a lot of programmers who don't consider HTML a coding language. If you know HTML I don't say this to disparage web development, I just think you should know that it's more like structured data than programming. It's kind of like Pluto not being a planet. I love Pluto, but it just doesn't meet the standard. Please don't think that this means you shouldn't learn HTML. On the contrary, think of HTML as a gateway drug to programming.*

# Data types (and variables)

So programming is all about simple instructions right? Well, usually that means taking some bit of data and modifying it.

The problem is that humans don't really think about everything being data. That's one of the reasons programming seems difficult at first. Trust me, it gets easier. If you've ever done any data reporting, this should feel somewhat familiar.

### Definitions

There are different names for different types of data in different programming languages. I'm going to simplify them as much as possible and when in doubt, I'm erring on the side of Python.

Here are the different types of data I will talk about:

* **Boolean:** This is just a fancy word for true or false.
* **Integer:** This is just a fancy word for numbers.
  * Example: 1, 35, -1938273, 2
* **Strings:** This is just a way to say a word or strings of words. These could be a single word, sentence, paragraph or any combination of words.
  * "Hello"
  * "The sky is blue."
  * *Note: Strings are generally in quotes to signify these words are all in this single string. Usually it doesn't matter if they are enclosed with single or double quotes, but that depends on the language syntax.*
* **List:** This is just a list of items, but in Python a list must have square brackets (`[]`) around it. An example of a list of grocery items might look like this.
  * `['eggs', 'milk', 'butter', 'bread']`
  * *Note: This is a list of strings. You can also have a list of integers or other data types.*
* **Key-value pair:** These are like specific pairs of items. So let's say you wanted to associate your name with your employee ID. The value to the left of the colon is called a key and the value to the right is the value. In other words, you're associating the value with the unique key.
  * "Rob Denton": 123456789
  * *Note: This key is a string, while the value is an integer.*

There are more types and formats but numbers, words, lists and key-values are fundamental to almost every programming language.

# Variables

Variables are a way to assign specific data to a single value. That value can be changed later, that's why a variable is variable and not static. Let's look at how this might work in Python.

```python
# Here are some booleans
blue_sky = True
red_sky = False
# Note: Booleans must be either "True" or "False"
# ... and those must be capitalized.
burritos_good = True

# Here are some integers
one = 1
thirty_five = 35
some_crazy_number = -1938273
simple_number = 2

# Here are some strings
hi = "Hello"
name = "Rob"
longer_string = "The sky is blue."

# Here's our grocery list
grocery_list = ['eggs', 'milk', 'butter', 'bread']

# Key-value pairs are used a little differently
# ... in Python. We may come back to that later.
```

**PAUSE:** Whew. That was a lot. Let's break it down.

### Comments

All of the lines that start with `#` are a comment. That means that those lines are ignored
by the computer.

Programmers use comments to make notes about why they do certain things; it makes things a lot easier for other programmers to understand the code.

Each language uses different ways to comment out code, but in Python you use a `#` at the start of a line and everything after that `#` is ignored.

### Variable names

Next, why do all of the variables have `_` in them? Well, variables have to be single, lowercased words in Python, but you can use the underscore if you want easy to read variable names.

Variable names can be almost anything you want. There are a few [reserved words](https://docs.python.org/2.5/ref/keywords.html) in every programming language that cannot be used for a variable name. Other than those, you can use whatever makes sense to you. However, it's often helpful to make the names blatantly obvious so that other programmers can figure out your naming structure.

## Manipulating data

Ok, so you're starting to think about data and variables. Hopefully that stuff is starting to make sense. But that's pretty boring. Let's use computers for what computers are good at, computing data.

### Math

Math is the classic example of working with data and Python makes doing math super easy. Let's take a look at how that might look.

```python
# You can do simple math right in the Python interpreter
1+1
> 2 # This is what Python would print out as an output

# You can even do math with variables
two = 2
three = 3
two + three
> 5
two - three
> -1
two * two + three
> 7

# You can also set variables to the solution of a math equation
solution = (two + three) * 2 # Remember PEMDAS
print solution
> 10
```

I snuck in a new concept there at the end. The `print` command tells Python to simply print out the value of the variable. This also works with any other data type. Printing is a good way to check variables and or your work.

### Concatenation

Concatenation is a big word for combining strings and it works just like the math does in Python. Let's take a look.

```python
# Set some variables
hi = "Hello"
name = "Rob"
print hi
> "Hello."
new_string = hi + " " + name
print new_string
> "Hello Rob"

# You can re-set variables and do some math
hi = "hey " # Note I added a space after the word
print hi * 3 + name
> "hey hey hey Rob"
```

*Note: There's so much more about [data](https://docs.python.org/2/tutorial/datastructures.html) that I would like to talk about. There's [string formatting](https://pyformat.info/). And [creating dictionaries](https://docs.python.org/2/tutorial/datastructures.html#dictionaries). But we have a lot more to get through so let's stop there.*

# Conditionals

Like variables, conditionals are a fundamental part of programming. Conditionals will do some sort of test to see what the program should do.

Conditional statements are often called if-else statements because that is how the testing works. Basically, you tell the program, if something is this way, do this, otherwise (else) do this. Let's take a look at an example.

```python
# Let's set a variable to test
sky_blue = True

# Let's set up a conditional
if (sky_blue == True):
    print "You're on Earth." # This will print if the conditional is true
else:
    print "You're somewhere else." # This will print if false

> "You're on Earth."
```

**PAUSE:** Let's break that down. So we set a variable named `sky_blue` to be `True` because, well, it is. Then we use a conditional to test that variable. If `sky_blue` is `True` then we want to print `"You're on Earth"`, otherwise we want to print `"You're somewhere else."`. And, of course, the conditional prints out `"You're on Earth."` because we set the variable to `True.`

### Spacing

You'll note that the the `print` statements in the conditional are nested within the conditional. This is some specific formatting that Python requires. In fact, you **must** have four spaces before nested lines. Python also requires colons at the end of the conditional rules. You'll see these at the end of the if and else lines.

If you're interested in learning more about Python syntax, that's great! Unfortunately, I don't have any good links for you. Syntax documentation is super dry and you'll pick it up as you learn more.

## Another example

Let's try something a little more advanced. Let's say you're a teacher and you just finished grading 300 tests. Each test has a percentage value but you want to see how many people got As, Bs, Cs and so on. Instead of counting these by hand, a computer could do that for you! But, before you write that script, you need a conditional to test the percentages.

### Else if

Beyond just if and else there is third option, else if. So you can say if this happens do this, else if this happens do this, else do this.

In Python, this is shortened to `elif` but different languages do it differently.

```python

# Let's set a variable to a number between 0 and 100
# ... and pretend a student got an 84 on the test.
score = 84

# Now let's test to see what grade you got
if (score < 70):
    print "Failing"
elif (score < 80):
    print "C"
elif (score < 90):
    print "B"
elif (score <= 100):
    print "A"
elif (score > 100) :
    print "A+"
else:
    print "Error: Not a number"

> "B"

```

**PAUSE:** Let's roll back the tape a little bit and explain what's going on here. We're saying the student got an 84 percent on the test. We open our conditional on the low end of the percentage scale but we could have done the opposite, opening on the high end.

If the student got less than a 70 on the test, I want to print out `"DF"`. Then we test to see if you got less than an 80 and if this is true we print `"B"`. Then we do the same with less than 90. Let's stop here and see why I chose this testing structure.

To be even more specific I could have tested for `elif (80 <= test < 90):` but this is not necessary because I already tested for less than 80. So when I say less than 90 we can safely assume that score is between 80 and 89.

Continuing down the conditional, I test for less than or equal to 100 and then greater than 100 because I want to see if the student got an A or if they went above and beyond to get extra credit too.

Finally, at the end I say if the score is equal to anything else there is some sort of error. By doing this testing structure I ensure that any number is tested for. Even negatives are less than 70 and even millions are more than 100. But, I could have set `score = "This test sucks"`. Technically that is a valid variable assignment, it's just not what we're expecting. **It's always good to test for things that you don't expect.** You never know when a user is going to do something weird like enter a string instead of an integer.

# Loops

Loops are another fundamental part of programming. They're an easy way to say, this is a thing I want to do a bunch of times but I don't want to tell you to do it each time, I just want you to do it in this order and tell me when you're done.

There are two types of loops in Python but I only suggest you use one of them.

### `for` loops

Let's say you have a list of movies that you want to watch and you want to print out them in order so you can go find their IMDB pages.

```python
# These are all great movies that you should watch
movies = "The Dark Knight", "Treasure of Sierra Madre", "The Great Escape", "Restrepo"

# Let's loop through them and print them out
for film in movies:
    print film

> "The Dark Knight"
> "Treasure of Sierra Madre"
> "The Great Escape"
> "Restrepo"
```

**PAUSE:** This for loop takes the variable `movies` and prints out each name. Actually pretty simple. Let's break it down some more. For instance, where does `film` come frome?

What we're doing here is essentially creating a variable that's local to this for loop. While we're not directly assigning the `film` variable, it's an implicit assignment on each loop. Here's another way to look at that code above:

* Ok, my list of favorite `movies` includes The Dark Knight, Treasure of Sierra Madre, The Great Escape, Restrepo
* For each `film` in my list of `movies` do something:
  * `print "The Dark Knight"`
    * The Dark Knight
  * `print "Treasure of Sierra Madre"`
    * Treasure of Sierra Madre
  *  `print "The Great Escape"`
    * The Great Escape
  * `print "Restrepo"`
    * Restrepo
* Ok, there are no more movies so the loop is over, moving on to the next instruction

### `while` loops and infinite loops

Let's say you're having your friend count gumballs. When you tell them to count all the gumballs what you're really saying is, while there are still gumballs left add one to your count. This could backfire if there are infinite gumballs though. Your friend would count gumballs forever until they passed out from exhaustion. :/ That's not good.

Computers will do the same thing. `while` loops are a good idea in theory but you never want to use them unless you are 100 percent sure that there is some sort of end condition. Otherwise your script will run forever and you don't want your computer crashing.

*Note: [This is a good blog post on loops in Python](http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/).*

# Functions

I doubt I'll cover this in the session due to lack of time but functions are fundamental to programming.

A function is some sort of block of code that you can call to run. It's kind of like setting data to a variable name so that you don't need to write that data over and over. You can define a function and then just call that code block using the name of the function.

Let's look at an example.

```python
# First we define the function
# Note: We end the line with a colon
def four():
    # Note that we add four spaces when nested
    # ... inside function, just like a conditional.
    return 2+2

# Then we call a function like this
four()
> 4
# And it can return a value
```

*Note: Functions can also be called methods. There is a [difference](http://stackoverflow.com/a/155655) but for the purposes of this introduction, we'll pretend they're the same.*

### Arguments

You probably noticed that functions are written with parentheses at the end of the name. Within these parens you can define **arguments**. Arguments are variables that you would like to pass into the function. Let's look at an example of that.

```python
# First you have to define the function
# x and y will be our variables
def add(x,y):
    # Make sure you space in four spaces
    return x + y

# Call the function and pass in
# ... 3 as x and 4 as y
add(3,4)
> 7
# The function returns 7

some = 5
more = 6
# You can pass in variable
add(some, more)
> 11

# Since x and y are variables you can
# ... set them to strings and concatenate
hi = "Hello "
name = "Rob"
add(hi, name)
> "Hello Rob"

# You can even set a function to a variable
solution = add(10,20)
print solution
> 30
```

### Built-in functions

Python has a number of handy **built-in functions** that come for free.

Two built-in methods of lists are `append()` and `remove()`. They do pretty much what you'd expect. They take a single argument that should be an item to be appended or removed. Let's look at an example.

```python
# Ok, let's go grocery shopping.
# Before we left the house we made this list:
grocery_list = ['eggs', 'milk', 'butter', 'bread']

# While driving to the store you remember that
# ... you also need to pick up some granola
grocery_list.append("granola")
print grocery_list
>['eggs', 'milk', 'butter', 'bread', 'granola']

# Now you're in the story and you pick up milk first
grocery_list.remove('milk')
print grocery_list
>['eggs', 'butter', 'bread', 'granola']
```

# Wrap up

Yes, this was a lot of information and, yes, it probably seems overwhelming. Not only were there a lot of new topics, we're also talking about an entirely [new way of thinking](https://www.youtube.com/watch?v=UScm9avQM1Y).

Take your time. Understand the basics and try to start with simple Python scripts. Read books. Google a lot. Find projects that are really interesting to work on.

Remember that a lot of programming is standing on the shoulders of giants. If you have a question, chances are it's been answered on StackOverflow. If you have a need, chances are someone has already written a Python module to fulfill that need. Use the tools that are out there to be as efficient as possible.

And have fun.

# More stuff

### Additional resources

* [Learn Python the Hard Way](https://learnpythonthehardway.org/) (free) - This book is free online but you can order a hard copy that comes with videos for pretty cheap. It's a great introduction if you **really** want to learn. It takes work to get through but it's a great book.
* [Official Python tutorial](https://docs.python.org/2.7/tutorial/) (free) - This is the official Python documentation. It's pretty good, a little dry though.
* [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/intro/learning/) (free) - I haven't read this whole book but I stumbled across it **a lot** when I was first learning.
* CodeCademy, Khan, etc.

### Monty Python

Yes, Python was named after Monty Python and yes, there are Monty Python jokes in the documentation. [Confirmation](https://docs.python.org/2/faq/general.html#why-is-it-called-python)

### Disclaimer on playing along from home

If you're on a Mac, getting to play with Python is super simple because Python comes pre-installed. If you're on a PC it's a bit more tricky because it's not installed. And, frankly, I have never installed Python on a PC so I'll have to refer you to [documentation](https://docs.python.org/2/using/windows.html).

A word of warning: Installing or removing Python from your machines may have dramatic and fatal consequences for your machine. Everything I do in this document does not require any special downloads and will not ruin your computer. If you want to do anything more complex with Python I would refer you to [virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/).

And, if you're unfamiliar with the command line, I would refer you to [Learn Python the Hard Way's appendix crash course](https://learnpythonthehardway.org/book/appendixa.html).