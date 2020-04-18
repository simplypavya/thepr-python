# This is a Master file for the Code and Notes prepared from the Course of Python
# The code has the reference comments


#Printing the different
print((("Hisssssss...")))
# The below command is written in one line but it will print the message in Two line by use of newline character "\n"
print("Pussy cat, Pussy cat \nwhere have you been")
print()
print("I've been to London \nto look at the queen.")
print("#################################################")

print("Pussy cat","Pussy cat","where have you been")

print("#################################################")
print("My name is", "Python",end=" ")
print("Monty Python")

print("My name is", "Python",end="\n")
print("Monty Python")

print("#################################################")
print("My", "name", "is", "Monty", "Python", sep="-")


print("#################################################")
print("My", "name", "is",sep="-", end="*")
print("Monty", "Python",sep="*",end="*\n")

print("#################################################")
print("2")
print(2)
print(-2)
print("#################################################")
print("Octal Value of 0o123")
print(0o123)
print("Hexadecimal Value of 0x123")
print(0x123)

print("#################Literal Float################################")
print("float value of 0.4")
print(0.4)
print("Float Value of .4")
print(.4)

print("float value of 4.")
print(4.)
print("Float Value of 4.0")
print(4.0)

print("Exponential Value")
print(3E8)
print(6.67806E34)
print(0.0000000000000000000000012)
print("################# String ################################")
print("I Like \"Monty Python\"")
print('I Like "Monty Python"')
print('I\'m Monty Python')
print("I\'m Monty Python")

print ("################# Learning Math ###################")

print("Addition Operator  (2+2):")
print(2+2)
print("Multiplication Operator ( 2 * 3 ):")
print(2*3)
print("Square Values (2**3):")
print(2**3)
print("Square Values of Float (2.**3.):")
print(2.**3.)

# The result produced by the division operator is always a float.
print("Divisional Operator (12 / 4) Returns float:")
print(12 / 4)

# A // (double slash) sign is an integer divisional operator.
print("Divisional Operator (12 / 6) Returns Integer:")
print(12 // 6)

print("Divisional Operator (13. / 6) Returns Integer:")
print(13. / 6)

print("Divisional Operator (13. // 6) Returns Float:")
print(13. // 6)

print("Divisional Operator (13. / -4):")
print(13. / -4)

print("Divisional Operator (13. // -4):")
print(13. // -4)

print("Divisional Operator (-13. // 4):")
print(-13. // 4)

#the operator is sometimes called modulo in other programming languages
print("Modulo Operator (14 % 4):")
print(14%4)

print("Modulo Operator (12 % 4.5):")
print(12%4.5)

print("Operator's Addition (-4 + 4):")
print(-4 + 4)

print("Operator's Addition (-4. + 8):")
print(-4. + 8)

print("Operator's Substraction (-4 - 4):")
print(-4 - 4)

print("Operator's Substraction (-4. - 8):")
print(-4. - 8)


print("Operator's to Numbers (+2):")
print(+2)

print("Operator's to Numbers (-2):")
print(-2)

print("Operator's to Numbers (-2.):")
print(-2.)

print("Operator's and their bindings (9 % 6 % 2)")
print(9 % 6 % 2)

print("Operator's and their bindings (2 ** 2 ** 3)")
print (2 ** 2 ** 3)
#2 ** 2 → 4; 4 ** 3 → 64
#2 ** 3 → 8; 2 ** 8 → 256
#the exponentiation operator uses right-sided binding

print(" List of Priorities")
print("List of Priorities (2 * 3 % 5)")
print (2 * 3 % 5)

#subexpressions in parentheses are always calculated first.
print("List of Priorities (5 *  ((25 % 13) + 100) / (2 * 13) // 2)")
print (5 *  ((25 % 13) + 100) / (2 * 13) // 2)



print ("########################################################")
print ("###################### Variables #######################")


#Variable Name Rules:
# It must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
# it must begin with a letter;
# the underscore character is a letter;
# upper- and lower-case letters are treated as different
# the name of the variable must not be any of Python’s reserved words

#Note that the same restrictions apply to function names
# Python lets you use not only Latin letters but also characters specific to languages that use other alphabets
# Python incorrect variables names:
# 10t (does not begin with a letter)
# Exchange Rate (contains a space)

 
# You can not name an variable as "import"
# However you can name any variable as "Import"


# You can store any thin in Variable
var=1
account_no= 11223344
ClientName= 'John Doe'
#print("value of (var=1):")
print(var,account_no,ClientName)

var=var+1
#print(var)
print('var after incremnt =', var)
#Python treats the sign = not as equal to, but as assign a value

print(" Shortcut variables with Operators")
x=1
x *= 2
print('x *= 2', x)


print ("########################################################")
print ("###################### input #######################")

print("Tell me anything ...")
anything = input()
print (" Hmmmm", anything, "... Really")

anything = float(input("Give me a Number \n"))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

lega = float(input("Input first leg length:"))
legb = float(input("Input Second leg length:"))
hypo = (lega ** 2 + legb ** 2) ** .5
print("Hypotenuse length is", hypo)


print ("########################################################")
print ("###################### String Operators #######################")

string1 = input ("Type in name of pearson")
string2 = input ("Type his / her conuntry name")
complete_string = string1 + string2
print(complete_string)


print ( "###### Replication Operator ######" )

print("James" * 3)

print (3 * "an" )

print(5 * "2")
 

print("Drawgin Rectangle")
print("+" + 10 * '-' + '+')
print(("|" + ' ' * 10 + '|\n') * 5, end='')
print("+" + 10 * '-' + '+')


# convert a number into a string
str(10)
#10 + str(1)



print("##################################### Module 2 ######################################################")
print("##################################### Module 2 ######################################################")
print("##################################### Module 2 ######################################################")

# = is an assignment operator (a = b assigns a with the value of b)
# == is the question are these values equal? (a == b compares a and b)
# It is a binary operator with left-sided binding. It needs two arguments and checks if they are equal.

print(" Check the condition for (2 == 2)")
print(2 == 2)
print(" Check the condition for (2 == 2.)")
print(2 == 2.)
print(" Check the condition for (1 == 2)")
print(1 == 2)

BlackSheep = 2
WhiteSheep = BlackSheep * 2
print('Count of WhiteSheep')
print(WhiteSheep)
print('Count of BlackSheep')
print(BlackSheep)
print ("Compare results of BalckSheep with WhiteSheep")
print(BlackSheep > WhiteSheep)



