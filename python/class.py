# print(max(3,4))
# print(min(3,4))
# print(len("hello"))
#
# r = range(3,20,2)
# for n in r:
#    print(n)
#
# print(round(7.8))
# print(chr(65))
# print(float(5))
# print(int(5.2))
# print(pow(3,5))
# print(type(5.3))
# print("good morning")
# t = tuple([1,2,3,5])
# print(t)
# input("enter your name")


# def add():
#    a = int(input("enter first value: "))
#    b = int(input("enter second value: "))
#    c= a+b
#    print(c)
#
# def sub():
#    a = int(input("enter first value: "))
#    b = int(input("enter second value: "))
#    c= a-b
#    return c
#
# def mul(a,b):
#
#    c= a*b
#    print(c)
#
# def div(a,b):
#
#    c= a/b
#    return c
#
# add()
# print(sub())
# a = int(input("enter first value: "))
# b = int(input("enter second value: "))
# mul(a,b)
# a = int(input("enter first value: "))
# b = int(input("enter second value: "))
# print(div(a,b))


# def my_details(name,age):
#    print("name :", name)
#    print("age :", age)
#    return
#
# my_details("vaishaal",  18)
#
# def my_details(name,age):
#    print("name :", name)
#    print("age :", age)
#    return
#
# my_details( age = 18,name="vaishaal")
#
# def my_details(name,age=40):
#    print("name :", name)
#    print("age :", age)
#    return
#
# my_details( "vaishaal")
#
# def my_details(*name):
#    print(*name)
#
# my_details("vsv", "vajhd", "iregndos")

# import math as m
# from math import sqrt
# import math
#
# print(math.ceil(3.14))
# print(math.floor(3.14))
# print(math.factorial(3))
# print(math.gcd(12, 15))
# print(math.sqrt(25))
# print(math.log(2))
# print(math.log10(2))
# print(math.log2(2))
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
# print(math.pi)
# print(math.e)
#
# print(sqrt(25))
#
# print(m.ceil(3.14))
# print(m.floor(3.14))
# print(m.factorial(3))
# print(m.gcd(12, 15))
# print(m.sqrt(25))
# print(m.log(2))
# print(m.log10(2))
# print(m.log2(2))
# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))
# print(m.pi)
# print(m.e)
# swapping
# a = int(input())
# b = int(input())
# print(a, b)
# c = a
# a = b
# b = c
# print(a, b)
# circulating
#
#


# def circulate(lis, n):
#    for i in range(1, n+1):
#        b = lis[i:]+lis[:i]
#        print("the circulated value", i, "=", b)
#        return
#
#
# lis = [10, 20, 30, 40, 50, 60]
# n = int(input("enter value: "))
# circulate(lis, n)

#
#
# distance between 2 points
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

# print(distance)

#
####################################### leap year #########################################

#year = int(input())
# if(year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("it is a leap year")
#        else:
#            print("it is not a leap year")
#    else:
#        print("it is a leap year")
# else:
#    print("it is not a leap year")
#############################################################################################

################################## Temprature in celsius degree #############################

#celsius = int(input())
#fahrenheit = (celsius * 1.8) + 32
#print(f"The ans is {fahrenheit}")

###############################################################################################

############################### squareroot ####################################################

# import math as m

# a = int(input("First no: "))
# b = int(input("Second no: "))

# print(m.sqrt(a))
# print(m.sqrt(b))

################################################################################################

# list1 = [1, "hi", "Python", 2]
# print(list1[0:2])
# print(list1 * 3)
# del list1[2]
# print(list1)

#################################################################################################

# a = input("Enter a word")
# b = input("Enter a char")
# c = int(input("Enter a number"))

# d = a[:c] + b + a[c:]

# print(d)

#################################################################################################

#a = int(input("Enter the no: "))
#b = int(input("Enter the divisor: "))
#c = divmod(a, b)
# print(c)

# a = float(input("Enter the first no: "))
# b = float(input("Enter the second no: "))
# print("press 1 for addition")
# print("press 2 for subtraction")
# print("press 3 for multiplication")
# print("press 4 for division")
# c = int(input("Your Option: "))

# if c == 1:
#    d = a+b
# if c == 2:
#    d = a-b
# if c == 3:
#    d = a*b
# if c == 4:
#    d = a/b

# print(d)

################################# Greatest of three ##############################################

#a = int(input("First number: "))
#b = int(input("Second number: "))
#c = int(input("Third number: "))

# if a > b:
#   if a > c:
#       print(f"{a} is the greatest")
# elif b > c:
#   print(f"{b} is the greatest")
# else:
#   print(f"{c} is the greatest")

#################################################################################################

# print(7/2)
# print(7//2)
# print(7**2)
#print(7 % 2)
#tup = ("hi", "Python", 2)
#t[2] = "hi"
#list1 = [1, "hi", "Python", 2]
# print(list1[0:2])
#print(list1 * 3)
#del list1[2]
# print(list1)
#hi = "Welcome to India"
# print(hi[3])
# print(hi[:6])
# print(hi[-3])
# print(hi[:])
#x = 12
#y = 15
#print(x and y)
#print(x | y)
#college = "Sri krishna"
#college[1] = college[5] = "K"
#college[12] = " * "
# print(college)

######################################### Boolean ##############################################

#a = True
# print(a)
#b = False
# print(b)
#
#print(2 == 5)
#print(5 == 5)
#
# print(a+b)
# print(a*b)
# print(a+a)

#################################################################################################

########################## positive or negative #################################################

#a = int(input())
# if a > 0:
#    print("it is positive")
# else:
#    print("it is negative")

#################################################################################################

############################# odd or even #######################################################

#a = int(input())
# if a % 2 == 0:
#    print("it is even")
# else:
#    print("it is odd")

#################################################################################################

########################### Student mark system #################################################

#a = int(input())
#
# if a >= 90:
#    print("grade s")
# elif a >= 80:
#    print("grade a")
# elif a >= 70:
#    print("grade b")
# elif a >= 60:
#    print("grade c")
# elif a >= 50:
#    print("grade d")
# else:
#    print("fail")

#################################################################################################

############################ Traffic system #####################################################

#a = input()
#
# if a = "green":
#    print("go")
# elif a = "yellow":
#    print("ready")
# else:
#    print("stop")

#################################################################################################

########################### Amstrong number #####################################################

#a = int(input())
#c = 0
#m = a
# while a > 0:
#    b = a % 10
#    a = a / 10
#    c += pow(b, 3)
#
# if (c == m):
#    print(" it is an amstromg no")
# else:
#    print("it is not an amstromg no")

##################################################################################################

################################ Palindrome ######################################################

#a = int(input())
#c = 0
#m = a
# while a > 0:
#    b = a % 10
#    a = a / 10
#    c = 10 * c + b
#
# if m == a:
#    print("it is palindrome")
# else:
#    print("it is not palindrome")

#####################################################################################################
