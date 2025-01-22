# #1.Addition
# a = 5
# b = 3
# sum = a + b
# print("Sum:", sum)
# print(5+3)
# #---------------------------------------------------------------
# #2. Subtraction
# a = 10
# b = 4
# difference = a - b
# print("Difference:", difference)
# print(10-4)
# #---------------------------------------------------------------
# # #3. Multiplication
# a = 2
# b = 6
# product = a * b
# print("Product:", product)
# #---------------------------------------------------------------
# #4. Division
# a = 15
# b = 4
# # quotient = a / b
# # print("Quotient:", quotient)
# #
# # Floor division (returns integer result)
# floor_quotient = a // b
# print("Floor Quotient:", floor_quotient)
# #---------------------------------------------------------------
# #5. In-place Operations
# x = 5
# x+=3  # x=x+3
# # x += 3  # Equivalent to x = x + 3
# print("x after += 3:", x)  # Output: x after += 3: 8

# y = 10
# y -= 2  # Equivalent to y = y - 2
# print("y after -= 2:", y)  # Output: y after -= 2: 8
#
# z = 4
# z *= 2  # Equivalent to z = z * 2
# print("z after *= 2:", z)  # Output: z after *= 2: 8
# #---------------------------------------------------------------
# #6. Modulus (Remainder)
#
# a = 8
# b = 2
# remainder = a % b
# print("Remainder:", remainder)
# #---------------------------------------------------------------
# #7. Exponential (Power)
#
# base = 2
# exponent = 3
# # result = pow(base, exponent)  # Or
# result = 2**3
# print("Result:", result)
# #---------------------------------------------------------------
# #8. Logarithms
#
# import math
#Syntax
# Natural logarithm (base e)
# x = 2
# natural_log = math.log(8,x)
# natural_log = math.log(9,3)
#
# print("Natural Logarithm is ", natural_log)
#-------------------------------------------------------
# # Base-10 logarithm
# y = 100
# base10_log = math.log10(y)
# # print(math.log10(100))
# print("Base-10 Logarithm of 100:", base10_log)  # Output: Base-10 Logarithm of 100: 2.0
# #---------------------------------------------------------------------------------------
# ##Exponantional:
# #1. pow() Built-in Function
#
# #Usage: Calculates the value of base raised to the power of exponent.
#
# result = pow(2, 3)  # 2 raised to the power of 3
# print(result)  # Output: 8
#
# #2. pow() with 3 Arguments
#
# #Usage: Calculates base raised to the power of exponent, and then finds the modulus with respect to mod.
#
# result = pow(2, 3, 5)  # 2 raised to the power of 3 (8) modulo 5
# print(result)  # Output: 3
# #3. Exponentiation using math.pow()
#
# #Usage: From the math module, calculates base raised to the power of exponent.
#
# import math
#
# result = math.pow(2, 3)
# print(result)  # Output: 8.0 (returns a float)
#
# #4. Square Root: math.sqrt()
#
# #Usage: Calculates the square root of a number.
# #
# # import math
# #
# # result = math.sqrt(25)
# # print(result)  # Output: 5.0
#---------------------------------------------------------------------------------------------
#if,else condition:
# Syntax:
# if condition:
#     Do something
# elif:
#     something Do
#-------
# a=3
# if(a==3):
#     print("a == 3")
#-------
# name = "Mohamed"
# if(name == "ibrahim"):
#     print("Hello ibrhaim")
# elif name == "mohamed":
#     print("Hello Mohamed")
#----------------------------------
# x=3
# if(x==2):
#     print("x==2")
# elif(x==4):
#     print("x==4")
# else:
#     print("x==3")
#--------------------------

#Boolean operator:
# #1. and
#
# #Usage: Returns True if both operands are True, otherwise returns False.
#
# a = True
# b = False
#
# result1 = a and a  # True and True -> True
# result2 = a and b  # True and False -> False
# result3 = b and b  # False and False -> False
#
# print(result1, result2, result3)
# #2. or
#
# #Usage: Returns True if at least one of the operands is True, otherwise returns False.
#
# a = True
# b = False
#
# result1 = a or a  # True or True -> True
# result2 = a or b  # True or False -> True
# result3 = b or b  # False or False -> False
#
# print(result1, result2, result3)
# #3. not
#
# #Usage: Reverses the logical state of its operand. If the operand is True, it returns False, and vice versa.
#
# a = True
# b = False
#
# result1 = not a  # Not True -> False
# result2 = not b  # Not False -> True
#
# print(result1, result2)
#
# #4. Combining Boolean Operators:
#
# #You can combine these operators to create more complex expressions:
#
# a = True
# b = False
# c = True
#
# result = (a and b) or (a and c)  # (False) or (True) -> True
# print(result)
##------------------------------------------------------------------------
# #1. Chain Comparisons
#
# #Chain comparisons allow you to express multiple comparisons in a more concise way.
#
#
# x = 5
#
# # Check if x is between 1 and 10 (inclusive)
# result = 1 <= x <= 10
# print(result)  # Output: True
#
# # Check if x is greater than 0 and less than 10
# result = 0 < x < 10
# print(result)  # Output: True
# #2. Comparison by is vs ==
#
# #is: Checks for object identity (whether two variables refer to the same object in memory).
#
# # a = [1, 2, 3]
# # b = a
# # c = [1, 2, 3]
# a=2
# b=a
# c=2
# print(a is b)  # Output: True (a and b refer to the same list object)
# print(a is c)  # Output: False (a and c refer to different list objects, even if they have the same values)
# print(a == c)  # Output: True (a and c have the same values)
# #==: Checks for value equality (whether two objects have the same value).
#
# x = 5
# y = 5
# print(x == y)  # Output: True (both x and y have the same value)
# #3. Greater Than or Less Than
#
# x = 10
# y = 5
#
# print(x > y)  # Output: True (x is greater than y)
# print(x < y)  # Output: False (x is not less than y)
# print(x >= y)  # Output: True (x is greater than or equal to y)
# print(x <= y)  # Output: False (x is not less than or equal to y)
# #4. Equal To and Not Equal To
#
# x = 5
# y = 5
# z = 6
#
# print(x == y)  # Output: True (x is equal to y)
# print(x != z)  # Output: True (x is not equal to z)
#---------------------------------------------------------
