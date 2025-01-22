# x=123

#if x is even do
# if x%2==0 :

#condition!!!


#docstring
def greet(name):
    """
    This function returns a welcome message.
    
    variables:
    name (str):user name.
    
    return:
    str:Welcome message containing username.
    """
    return f"Welcome, {name}!"


#sphinx
def add(a, b):
    """
    Adds two numbers together.

    :param a: num1
    :type a: int
    :param b: num2
    :type b: int
    :return: sum
    :rtype: int
    """
    return a + b



#google python style guide
def subtract(a, b):
    """
    subtracting two numbers

    Args:
        a (int): num1
        b (int): num2

    Returns:
        int: result of subtract
    """
    return a - b



x=12  #int
x=23435345656
x=0

y=12.5  #float
y=1.0
y=3657436955.596674

z='dfg kld3434jfjf'  #string
z="dsf"

w=True  #bool
w=False


f="234"
f=float(f)
print(type(f))




print("hello in adding program!!")
#input
num1=float(input("enter first number : "))
num2=float(input("enter second number : "))
result=0.0

#process
result=num1+num2

#output

print(f"the sum is {result}")
