# This is a Master file for the Code and Notes prepared from the Course of Python
# The code has the reference comments
# Chapter 1
# Notes:
#                   Python is an interpreted language
#                   If you want to program in Python, you’ll need the Python interpreter
#
#       Histroy of Python
#                   Python programming language comes from an old BBC television comedy sketch series called Monty Python’s Flying Circus
#                   Python was created by Guido van Rossum, born in 1956 in Haarlem, the Netherlands
#                   Python isn’t a young language. It is mature and trustworthy.
#       What all Pythons?
#                   There are two main kinds of Python, called Python 2 and Python 3
#                   Python 2 is an older version of the original Python
#                   Python 2’s development path has reached a dead end already, but Python 2 itself is still very much alive
#                   Python 3 is the newer (to be precise, the current) version of the language
#                   It’s going through its own evolution path, creating its own standards and habits
#       Error Message about Python?
#                   These two versions of Python aren’t compatible with each other
#                   Python 2 scripts won’t run in a Python 3 environment and vice versa
#                   So if you want the old Python 2 code to be run by a Python 3 interpreter,the only possible solution is to rewrite it, not from scratch
#                   Python 3 isn’t just a better version of Python 2 – it is a completely different language
#                   When you look at them from a distance, they appear to be the same, but when you look closely, though, you notice a lot of differences
#                   If you’re going to start a new Python project, you should use Python 3
#       Different Pythons Exist on IT Land?
#                   CPython:
#                       The PSF (Python Software Foundation); The PSF’s president is Guido von Rossum
#                       The PSF used the “C” programming language to implement the very first version of his language and this decision is still in force
#                       This is why the PSF implementation is often referred to as CPython
#                       This is the most influential Python among all the Pythons in the world
#                   Cython:
#                       One solution is to write your mathematical ideas using Python
#                       And when you’re absolutely sure that your code is correct and produces valid results, you can translate it into “C”
#                   Jython:
#                       Jython can communicate with existing Java infrastructure more effectively
#                       The current Jython implementation follows Python 2 standards
#                       There is no Jython conforming to Python 3, so far
#                   PyPy : A Python within a Python [RPython] - Restricted Python
#                       The source code of PyPy is translated into the “C” programming language and then executed separately
#                       PyPy is compatible with the Python 3 language
#       Get the Python on your System
#                   Linux users most probably have Python already installed
#                   Test on the Linux system with command $python3
#                   Rest system can download Python from https://www.python.org/downloads/
#                   MacOS will have Python 2 by default
#                   Python 3 comes with "IDLE is an acronym: Integrated Development and Learning Environment"
#                   Python needs its files to have the .py extension


# **************************************************************************
# ********************* Programming with Python ****************************
# **************************************************************************
#
#Press F5, or click Run from the window’s menu and select Run module
#The editor window will not provide any useful information regarding the error, but the console windows might
#Error in python reports 
#traceback, location of the error, content of the errornous file & name of the error
# *********************** Functaion in Python *****************************
#In spite of the number of needed/provided arguments, Python functions strongly demand the presence of a pair of parentheses – opening and closing ones, respectively
# ********************* Printing Function in Python ********************** #
#The backslash (\) has a very special meaning when used inside strings – this is called the escape character
#lets try using \
print("\\");
#output: \
# print() is a function name
# Even we have multiple bracktes Python will treat as same
print("thrpr with single bracket");
#output: thrpr with single bracket
print(("thrpr with double bracket"));
#output: thrpr with single bracket
print((("thrpr with tripple bracket")));
#output: thrpr with single bracket

# The below command is written in one line but it will print the message in Two line by use of newline character "\n"
print("thepr\nPython learning session");
#output:
#       thepr
#       Python learning session

# The null print function; this null printing will have a newline insert on screen output
print();
#output: new line
print("the above output is of print function print()");

print("the  output is in conjuction of null print function", print());

# output:
#           the  output is in conjuction of null print function None

# The print fucntion with seperation of "," will print the three differnt values 
print("Printing the below values which are comma seperated");
print("thepr","Pravin Reddy","How is Python Learning");
print();
#output: thepr Pravin Reddy How is Python Learning

#The print() function has two keyword arguments that you can use for your purposes. The first of them is named end
#Here we passed the end of print statement ammendment by *
print("Use of end Keyword for the function print \n");
print("thepr","Pravin Reddy","How is Python Learning", end="*");
#output: thepr Pravin Reddy How is Python Learning*

#In case we apply end with empty it will not assigne any value
print("I am thepr",end="");
print("Learning Python");
# There will be no even space
#output: I am theprLearning Python
# When you use end function then new line is not added to the next print line by default it will just ammend the output with end argument value
#Note: no newlines have been sent to the output.

#Another Keyword for print() is seperator i.e. sep
print("Use of Seperator Keyword for the function print");
print("thepr","Pravin", "Reddy","How","is","Python", "Learning", sep="-");
#output: thepr-Pravin-Reddy-How-is-Python-Learnin

print("thepr","Pravin", "Reddy","How","is","Python", "Learning", sep="");
#output: theprPravinReddyHowisPythonLearning

print("thepr","Pravin", "Reddy","How","is","Python", "Learning", sep=" ");
#output: thepr Pravin Reddy How is Python Learning
#Note: the sep argument’s value may be an empty string, too
#Both keyword arguments may be mixed in one invocation

print("Use of both Keyword i.e. sep="" & end="" for the function print");
print("thepr","Pravin", "Reddy","How","is","Python", "Learning", sep="-", end="\n");
#output: thepr-Pravin-Reddy-How-is-Python-Learning

#
# **************************************************************************
# ********************* Literals in Python *********************************
# **************************************************************************
#           A literal is data whose values are determined by the literal itself
#           123 is a literal, and c is not
#           As c may represent any value; It can be the symbol of the speed of light, for example. It also can be the constant of integration
#           Lets try printing number 2 in two ways
print("2");
#output : 2
# Here the above 2 with quotes is treated as string whereas the other one as integer
print(2);
#output: 
#Internally, in the computer’s memory, these two values are stored in completely different ways – the string exists as just a string – a series of letters
#In Python negative value is represented with - and for positive value, there is no need of mentioning + sign

#here are two additional conventions in Python;
#If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value e.g. 0o123
print("Octal Value: ", 0o123);
#output: Octal Value:  83
#Note: 0o123 is an octal number with a (decimal) value equal to 83

#If an integer number is preceded by an 0x or 0X prefix (zero-o), it will be treated as an hexadecimal value e.g. 0x123
print("Hexadecimal Value: ", 0x123);
#Note: 0x123 is a hexadecimal number with a (decimal) value equal to 291
#Hexadecimal Value:  291

#Literals - Floats
#Note: your number doesn’t contain any commas at all, Python will not accept that
#As the comma itself has its own reserved meaning in Python
#Note once again – there is a point between 2 and 5 – not a comma

print(2.5);
#output: 2.5
print(.4);
#output: 0.4
#Note you can also represent 0.4 as .4
#However it is not recommended to use like this
#Note:the decimal point is essentially important in recognizing floating-point numbers in Python
#The value of 4.0 could be written as 4.

#You can also use the letter e to represent the floating point like 3 x 10^8 = 3E8
print("Value of 3 x 10 ^8 with 3E8: ", 3E8);
#output: Value of 3 x 10 ^8 with 3E8:  300000000.0
#Note: the exponent (the value after the E) has to be an integer; the base (the value in front of the E) may be an integer

print(0.0000000000000000000001);
#output: 1e-22
print("Above value is Printing of 0.0000000000000000000001");
#Python always chooses the more economical form of the number’s presentation

# **************************************************************************
#Literals - Strings
# **************************************************************************

#Note: The strings need quotes the way floats need points
print("I am a String");
#output: I am a String

#The backslash can escape quotes too. A quote preceded by a backslash changes its meaning – it’s not a delimiter, but just a quote
print("I am in \"Quotes with escape character\" ");
#output: I am in "Quotes with escape character"

#Python can use an apostrophe instead of a quote
print('I am in "Quotes with single quote character"');
#output: I am in "Quotes with single quote character"

#The next two way to put 'in the string
print('I\'m thepr');
#output: I'm thepr

print("I'm thepr");
#output: I'm thepr

#Note: a string can be empty in Python with "" ''
23

# **************************************************************************
#Literals - Boolean Values
# **************************************************************************
# These are used to represent a very abstract value – truthfulness
# values are true or false

# ********************* Operators in Python ********************** #
# Python can be used as a calculator
print("Printing (2+2):", 2+2);
#output: Printing (2+2): 4
# An operator is a symbol of the programming language, which is able to operate on the values
# Note: Not all Python operators are as obvious as the plus sign
# Data and operators when connected together form expressions. The simplest expression is a literal itself
# A ** (double asterisk) sign is an exponentiation (power) operator

print("The exponenetial operator print 2^3 with (2 ** 3):", 2 ** 3);
#output: The exponenetial operator print 2^3 with (2 ** 3): 8

print("The exponenetial operator print 2^3 with (2. ** 3):", 2. ** 3);
#output: The exponenetial operator print 2^3 with (2. ** 3): 8.0

print("The exponenetial operator print 2^3 with (2 ** 3.):", 2 ** 3.);
#output: The exponenetial operator print 2^3 with (2 ** 3.): 8.0

print("The exponenetial operator print 2^3 with (2. ** 3.):", 2. ** 3.);
#output: The exponenetial operator print 2^3 with (2. ** 3.): 8.0

# Note: when both ** arguments are integers, the result is an integer, too; when at least one ** argument is a float, the result is a float, too.

# **************************************************************************
#Arithmetic operators – multiplication
#An * (asterisk) sign is a multiplication operator
# **************************************************************************

print("The multiplication operator print (2 * 3):", 2 * 3);
#output: The multiplication operator print (2 * 3): 6

print("The multiplication operator print (2. * 3):", 2. * 3);
#output: The multiplication operator print (2. * 3): 6.0

print("The multiplication operator print (2 * 3.):", 2 * 3.);
#output: The multiplication operator print (2 * 3.): 6.0

print("The multiplication operator print (2. * 3.):", 2. * 3.);
#output: The multiplication operator print (2. * 3.): 6.0

# **************************************************************************
# Arithmetic operators – division
# **************************************************************************

print("The division (6 / 3):", (6 / 3));
#output: The division (6 / 3): 2.0

print("The division (6. / 3):", (6. / 3));
#output: The division (6. / 3): 2.0

print("The division (6 / 3.):", (6 / 3.));
#output: The division (6 / 3.): 2.0

print("The division (6. / 3.):", (6. / 3.));
#output: The division (6. / 3.): 2.0

#The result produced by the division operator is always a float, regardless of whether or not the result seems to be a float at first glance

print("The division with double operator for integer output (6 // 3):", (6 // 3));
#output: The division with double operator for integer output (6 // 3): 2

print("The division with double operator for output (6. // 3):", (6. // 3));
#output: The division with double operator for output (6. // 3): 2.0

print("The division with double operator for output (6 // 3.):", (6 // 3.));
#output: The division with double operator for output (6 // 3.): 2.0

print("The division with double operator for output (6. // 3.):", (6. // 3.));
#output: The division with double operator for output (6. // 3.): 2.0

# Note: As you can see, integer by integer division gives an integer result
#Now lets see the operator with integer division
print("The division of two integers (6 // 4)", (6 // 4));
#output: The division of two integers (6 // 4) 1

print("The division of one as integer and one as float (6. // 4)", (6. // 4));
#output: The division of of one as integer and one as float (6. // 4) 1.0

# The result of integer division is always rounded to the nearest integer value that is less than the real (not rounded) result
# This is very important – rounding always goes to the lesser integer
print("The division of two integers with negative (-6 // 4)", (-6 // 4));
#output: The division of two integers with negative (-6 // 4) -2

print("The division of two integers with negative (6. // -4)", (6. // -4));
#output: The division of two integers with negative (6. // -4) -2.0

# The real (not rounded) result is −1.5 in both cases. The results are the subjects of rounding. The rounding goes toward the lesser integer value, and the lesser integer value is −2

# **************************************************************************
# Arithmetic Operators – remainder
# **************************************************************************
# The result of the operator is a remainder left after the integer division
# In other words, it’s the value left over after dividing one value by another to produce an integer quotient
# Note: the operator is sometimes called modulo in other programming languages
print("The reminder operator or you can say modulo operator");
print("The result of Remainder or Modulo (14 % 4):", (14 % 4));
#output: The result of Remainder or Modulo (14 % 4): 2

print("The result of Remainder or Modulo with float (12 % 4.5):", (12 % 4.5));
#output:The result of Remainder or Modulo with float (12 % 4.5): 3.0

# Note: not 3 but 3.0 (the rule still works) - Float rule of Python
# As you probably know, division by zero doesn’t work. Do not try to: perform a division by zero; perform an integer division by zero;find a remainder of a division by zero.

# **************************************************************************
# Arithmetic Operators – addition
# **************************************************************************
# The addition operator is the + (plus) sign, which is fully in line with mathematical standards

print("The addition operation for (-4 + 4): ", (-4 + 4));
#output: The addition operation for (-4 + 4):  0

print("The addition operation for (-4 + 4): ", (-4. + 8));
#output:The addition operation for (-4 + 4):  4.0

# **************************************************************************
# Arithmetic Operators – subtraction
# **************************************************************************

print("The subtraction operation for (-4 - 4): ", (-4 - 4));
#output: The subtraction operation for (-4 - 4):  -8

print("The subtraction operation for (-4 - 8): ", (4. - 8));
#output: The subtraction operation for (-4 - 8):  -4.0

print("The subtraction operation for (-1.1): ", (-1.1));
#output:The subtraction operation for (-1.1):  -1.1

# Arithmetic Operators and their priorities
print("The multiple operator operations for (2 + 3 * 5): ", (2 + 3 * 5));   
#output: The multiple operator operations for (2 + 3 * 5):  17

# Note: Most of Python’s operators have left-sided binding, which means that the calculation of the expression is conducted from left to right
# Note: The exponentiation operator uses right-sided binding

# **************************************************************************
#Operators vs parentheses
# **************************************************************************
# Parentheses, which can change the natural order of a calculation


###############################################################################################################################################################################
# **************************************************************************
#Variables – data-shaped boxes
# **************************************************************************
# Python It offers special “boxes” (containers) for that purpose, and these boxes are called:
# variables – the name itself suggests that the content of these containers can be varied in (almost) any way
# Every Python Variable will have
#                               Name
#                               Value
# Rules for Variable Declaration
# Must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
# The name of the variable must begin with a letter
# Note: the underscore character is a letter
#       upper- and lower-case letters are treated as different
#       the name of the variable must not be any of Python’s reserved words
# Moreover, Python lets you use not only Latin letters but also characters specific to languages that use other alphabets
# Incorrect variable values: 10t - variable starting with number; "Exchange Rate" - Variable name with Space in it


# Kaywords in Python : They are reserved because you mustn’t use them as names: neither for your variables, nor functions, nor any other named entities you want to create
# The meaning of the reserved word is predefined, and mustn’t be changed in any way
# Examples are: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from , global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield
# Fortunately, due to the fact that Python is case-sensitive, you can modify any of these words by changing the case of any letter, thus creating a new word, which is not reserved anymore

# In Python you can put anything in variable so no limitation
var=1;
print("Declared the variable like var=1: ", var);
#output: Declared the variable like var=1:  1

# **************************************************************************
# Different type of variable declaration
# **************************************************************************
var = 1;
accoung_balance = 10000.0;
ClientName = 'Pravin Reddy';

# The equal sign is in fact an assignment operator, It assigns the value of its right argument to the left
var = 1;
print(var);
#output: 1
var=var+1;
print(2);
#output: 2
# Other example
var = 100 + 200 ;
print("Printing the var = 100 + 200:", var);
#output: Printing the var = 100 + 200: 300

# **************************************************************************
# Comments on comments
# **************************************************************************
# A remark inserted into the program, which is omitted at runtime, is called a comment.
# In Python, a comment is a piece of text that begins with a # (hash) sign and extends to the end of the line
# If you want a comment that spans several lines, you have to put a hash in front of them all

# **************************************************************************
# Shortcut operators
# **************************************************************************
# Examples is python = python + 1 or say x = x * 2
# The shorten version for above could be python += 1; x *= 2

# **************************************************************************
# Read data for you
# **************************************************************************
# input() Funaction
# The function is able to read data entered by the user and to return the same data to the running program
# Note: A program which doesn’t get a user’s input is a deaf program
# The program prompts the user to input some data from the console
# The input() function is invoked without arguments
# The function will switch the console to input mode
# You’ll see a blinking cursor, and you’ll be able to input some keystrokes, finishing off by hitting the Enter key
# Note: you need to assign the result to a variable; this is crucial – missing out this step will cause the entered data to be lost

# Lets do example
#* print("Tell me Anything");
#* anything = input();
#* print ("The input given is: ", anything);

# Even there is no need of have print to get something from user
#* anything = input("Tell me Anything: ");
#* print ("The input given without print is: ", anything);

# The input() function is invoked with one argument – it’s a string containing a message; then the message will be displayed on the console before the user is given an opportunity to enter anything
# Check input to perform and arithematic operation
#* anything = input("Tell me Anything: ");
#* something = anything * 2.0
#* print ("The operations performed over input is: ", something);

# So here is you observer the operation performed over input has concatinated the string two times

# **************************************************************************
# To overcome such situation Python has two functions one is int () & other is float ()
# **************************************************************************

floatvalue = float(input("Give me a number: "));
floatvalue = floatvalue * 2.0
print ("The operations performed over input as a is (anything * 2.0): ", floatvalue);
#output: Give me a number: 20
#        The operations performed over input as a is (anything * 2.0):  40.0

# With the help of float and int function we can take input and perform the operation over it

# **************************************************************************
#String operators
# **************************************************************************
# The + (plus) sign, when applied to two strings, becomes a concatenation operator
thepr = "Name of instructor";
python = "Pravin Reddy";
print("Concatenate the String thepr + python: ", thepr + python);
#output: Concatenate the String thepr + python:  Name of instructorPravin Reddy

#Lab Example
fname = input("Please Enter Your First Name: ");
lname = input("Please Enter Your Last Name: ");
print ("Your First Name is " + fname + " Your Lasts Name is " + lname );

#output: Please Enter Your First Name: Pravin
#        Please Enter Your Last Name: Yalawar
#        Your First Name is Pravin Your Lasts Name is Yalawar

# The * (asterisk) sign, when applied to a string and number becomes a replication operator

print("Printing first name thrice (fname * 3)" , fname * 3);
#output: Printing first name thrice (fname * 3) PravinPravinPravin


# Code to draw a rectagle
print("+" + 10 * '-' + '+');
print(("|" + ' ' * 10 + '|\n') * 5, end='');
print("+" + 10 * '-' + '+');

#output:
#+----------+
#|          |
#|          |
#|          |
#|          |
#|          |
#+----------+

#You can also convert a number into a string, which is way easier and safer
#A function capable of doing that is called str()



#********************************************************************************************************************
#***************************** Module 2 *****************************************************************************
#********************************************************************************************************************

# Questions and answers
#

# "=" is an assignment operator (a = b assigns a with the value of b)
# "==" is the question are these values equal? (a == b compares a and b)
# It is a binary operator with left-sided binding, It needs two arguments and checks if they are equal
#>>> 2 == 2
#True

#>>> 2 == 3
#False


# **************************************************************************
# Equality
# **************************************************************************
#Note: remember this pair of predefined literals, True and False – they’re Python keywords, too
print("Result for 2 == 2", 2 == 2);
#output: Result for 2 == 2 True

print("Result for 2 == 3", 2 == 3);
#output: Result for 2 == 3 False

print("Result for 2 == 2.", 2 == 2.);
#output: Result for 2 == 2. True

#Note: Luckily, Python is able to convert the integer value into its real equivalent, and consequently, the answer is True
#Note that we cannot find the answer if we do not know what value is currently stored in the variable var
#If the variable has been changed many times during the execution of your program, or its initial value is entered from the console,
#the answer to this question can be given only by Python and only at runtime.

#Multiplication of Strings
Blacksheep = " "
Whitesheep = "  "
print("Result for Blacksheep == 2 * Whitesheep", Blacksheep == (2 * Whitesheep));
print("Result of Blacksheep > Whitesheep", Blacksheep > Whitesheep);
#output: NameError: name 'BlackSheep' is not defined
#Result for Blacksheep == 2 * Whitesheep False
#Result of Blacksheep > Whitesheep False
print("Result of centigradeoutside >= 0.0", centigradeoutside >= 0.0);

# The greater than operator has another special, non-strict variant, but it’s denoted differently than in classical arithmetic notation: >= (greater than or equal to).
# Both of these operators (strict and non-strict),
# As well as the two others discussed in the next section, are binary operators with left-sided binding, and their priority is greater than that shown by == and !=

print("Result of centigradeoutside < 2", centigradeoutside < 2);
print("Result of centigradeoutside <= 0.0", centigradeoutside <= 0.0);

# Unary Operators [+ - * / % ** ]
# Binary Operators [+ - < <= > >= == =!]

# **************************************************************************
# Conditions and conditional execution - Chapter 2.1.13
# **************************************************************************
