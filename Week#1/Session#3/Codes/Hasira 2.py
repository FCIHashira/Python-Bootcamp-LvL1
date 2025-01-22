# #1.Addition
# a = 3
# b= 4
# sum = a+b
# print(sum)

# #2. Subtraction
# a = 10
# b= 4
# difference = a-b
# print(difference)



# # #3. Multiplication
# a=2
# b=3
# multiplication = a * b
# print(multiplication)



# #4. Division
# a=6
# b=4
# result =  (a/b)
# print(result)
# result =  int (a/b)
# print(result)
# result = a//b
# print(result)


# #5. In-place Operations
# a=3
# b=4
# # a=a*b
# a*=b
# print(a)
# # a-=b
# # print(a)



# #6. Modulus (Remainder)
# a=2
# b=6
# result = a%b
# print(result)


# #7. Exponential (Power)
# a= pow(2,3)
# print(a)

# #8. Logarithms && # # Base-10 logarithm:
# import math
# a = math.log10(1000)
# print(a)

#if,else condition:
# name = "ibrahim"
# if name == "mohamed":
#      print("Hello mohamed")
# else:
#     print("wrong name")
#-------------------------------------
# x=4
# if x == 2:
#     print("x is 2")
# elif x == 4:
#     print("x is 4")
# else :
#     print("x is 3")
# x = 3
# if x==32:
#     x+=1 # x+=1 --> x=x+1
#     print(x)
#     print("End of program")


#Boolean operator:

# #1. and

# #Usage: Returns True if both operands are True, otherwise returns False.
# a = True # 1
# b = False # 0
#
# result1 = a and a
# result2 = a and b
# result3 = b and b
#
# print(result1, result2, result3)


# #2. or:
# #Usage: Returns True if at least one of the operands is True, otherwise returns False
# a = True # 1
# b = False # 0
#
# result1 = a or a
# result2 = a or b
# result3 = b or b

# print(result1, result2, result3)


# #3. not:
# # #Usage: Reverses the logical state of its operand. If the operand is True, it returns False, and vice versa.
#
# a = True
# b = False
#
# result1 = not a
# result2 = not b
# print(result1, result2)
#

#4. Combining Boolean Operators:

# a = True
# b = False
# c = True
#
# result = (a and b) or (a and c)
# print(result)


##Comparisons:

# #1. Chain Comparisons:
# x = -5
# # Check if x is between 1 and 10 (inclusive)
# result = 1 <= x <= 4
# print(result)


# #2. Comparison by ==
# x=5
# result = x == 5
# print(result)
# result = x != 5
# print(result)



# #3. Greater Than or Less Than

# x = 10
# y = 10
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)


# #4. Equal To and Not Equal To:

# x = 5
# y = 5
# z = 6
# print(x == y)
# print(x != z)
# print(x == z)



# #4. Square Root: math.sqrt()

#Usage: Calculates the square root of a number.

# import math
#
# result = math.sqrt(25)   #-- > #result = math.pow(25,0.5)
# print(result)


#Simple Operator Precedence :
# import math
# result =((5+1)*2)/(2*5)+math.pow(2,3)
#
# print(result)

# x = 5
#result = 1 <= x <= 5
# if x >= 1 or x <= 4:
#     print ("yes")
# else:
#     print("No")
