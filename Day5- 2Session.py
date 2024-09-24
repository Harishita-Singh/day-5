Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add(a,b):
    return a+b


print(add(5,7))
SyntaxError: invalid syntax
def add(a,b):
    return a+b

print(add(5+7))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(add(5+7))
TypeError: add() missing 1 required positional argument: 'b'
sum(8,5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sum(8,5)
TypeError: 'int' object is not iterable
s="Roshni"
len(s)
6
def add(a,b);
SyntaxError: expected ':'
def num=(n):
    
SyntaxError: expected '('
def num(n):
    n=5
    return n

print(num(20))
5
def add(a,b):
    return a+b

print(add(5,+7))
12
def num(x,y=4)
SyntaxError: expected ':'
def num(x,y=4):
    return (x,y)
print(num(5))
SyntaxError: invalid syntax
def num(x,y=4):
    return (x,y)
print(nums(5))
SyntaxError: invalid syntax
def num(x,y=4):
    return (x,y)

print(nums(5))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(nums(5))
NameError: name 'nums' is not defined. Did you mean: 'num'?
def num(x,y=4):
    return (x,y)

print(num(5))
(5, 4)
print(num(10,20))
(10, 20)
def cgpa(a,b):
    return a,b

>>> print(cgpa(b=8.7,a=9.2))
(9.2, 8.7)
>>> def num(x,y=10):
...     return (x,y)
... 
>>> print(num(25))
(25, 10)
>>> def function(*args_list):
...     return(args_list)
... 
>>> print (function(6,7,8,9))
(6, 7, 8, 9)
>>> def function(*args_list):
...     return(args_list)
... 
>>> print (function(6,7,8,9,10,11,99,77,66,88,44,22,11,33,55,00))
(6, 7, 8, 9, 10, 11, 99, 77, 66, 88, 44, 22, 11, 33, 55, 0)
>>> print (function("Rose","Riya","Rakhi"))
('Rose', 'Riya', 'Rakhi')
>>> def value():
...     num=10
...     print("Value inside function:",num)
... 
...     
>>> num=20
>>> value()
Value inside function: 10
>>> print("Value inside function:",num)
Value inside function: 20
>>> global n
>>> n=20
>>> def value(n):
...     print("Value inside function:",n)
... 
...     
>>> print("In function:",value(n))
Value inside function: 20
In function: None
>>> print(n)
20
>>> def is_vowel(char):
...     vowels='aeiou'
... 
...     
>>> return char in vowels
SyntaxError: 'return' outside function
>>> def is_vowel(char):
...     vowels='aeiou'
... 
