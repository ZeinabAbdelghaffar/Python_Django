#Q1 : Write a Python program which accepts the user's first and last name and print them inreverse order with a space between them.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)

#Q2 : Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn).
#Sample value of n is ​5
#Expected Result : ​615
n = int(input("Enter an integer value for n: "))
result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print("Result of the value of (n + nn + nnn) : ", result)

#Q3 : Write a Python program to print the following here document.Samplestring​:
#a string that you "don't" have to escape
#This 
#is a ....... multi-line 
#heredoc string --------> example
print('''
a string that you "don't" have to escape
This 
is a ....... multi-line
heredoc string --------> example
''')
#another answer
print(f'a string that you \"don\'t\" have to escape is\nThis\nis a ........ multi-time\nheredoc string --------> example')

#Q4  : Write a Python program to get the volume of a sphere with radius 6.
import math
radius = 6
volume = (4/3) * math.pi * (radius**3)
print(f'The volume of the sphere is: {volume}')

#Q5 : Write a Python program that will accept the base and height of a triangle and compute the area.
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle with base {base} and height {height} is: {area}")

#Q6 : Write a Python program to construct the following pattern, using a nested for loop.
#Search about method end=””
for i in range(0,5):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range(5, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

#Q7 : Write a Python program that accepts a word from the user and reverses it.
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

#Q8 : Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(0, 7):
    if i != 3 and i != 6:
        print(i, end=' ')
#another answer
for i in range(0, 6):
    if (i == 3):
        continue
    print(i, end=" ")

#Q9 : Write a Python program to get the Fibonacci series between 0 to 50
#Note : The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34
a, b = 0, 1
while b < 50:
    print(b, end=' ')
    a, b = b, a + b

#Q10 : Write a Python program that accepts a string and calculates the number of digits and letters.
string = input("Enter a string: ")
digits = sum(c.isdigit() for c in string)
letters = sum(c.isalpha() for c in string)
print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")