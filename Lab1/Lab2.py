#Q1 : Given a list of numbers, create a function that returns a list where all similar adjacent elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
#Note:You may create a new list or modify the passed in list.
def reduce_adjacent_elements(nums):
    reduced_list = []
    for num in nums:
        if not reduced_list or num != reduced_list[-1]:
            reduced_list.append(num)
    return reduced_list
nums = [1,2,3,3]
print(reduce_adjacent_elements(nums))

#Q2 :​​ Consider dividing a string into two halves
#Case1:The length is even, the front and back halves are the same length.
#Case2:The length is odd, we’ll say that the extra char goes in the front half.
   #E.g. ‘abced’, the front half is ‘abc’, the back half ’de.
#Given 2 strings, a and b, return a string of the form:(a-front + b-front) + (a-back +b-back)
def front_back_combine(a, b):
    def get_halves(s):
        length = len(s)
        if length % 2 == 0:
            front = s[:length // 2]
            back = s[length // 2:]
        else:
            front = s[:(length // 2) + 1]
            back = s[(length // 2) + 1:]
        return front, back
    a_front, a_back = get_halves(a)
    b_front, b_back = get_halves(b)
    return f"{a_front}{b_front}{a_back}{b_back}"
result = front_back_combine("abced","12345")
print(result)

#Q3 : Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
#[1,5,7,9] -> True        
#[2,4,5,5,7,9] -> False
def are_all_different(numbers):
    return len(numbers) == len(set(numbers))
print(are_all_different([1, 5, 7, 9]))
print(are_all_different([2, 4, 5, 5, 7, 9]))

#Q4 : Given unordered list, sort it using algorithm bubble sort.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))

#Q5 : Gusses game
import random
def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I've selected a random number between 1 and 100. You have 10 tries to guess it.")
    # Generate a random number
    random_number = random.randint(1, 100)
    tries = 10
    guessed_numbers = set()
    while tries > 0:
        #display the current try number
        print(f"\nAttempt #{11 - tries}")
        user_input = input("Enter your guess (1-100): ")
        # Check if input is a valid number
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        user_number = int(user_input)
        # Check if the number is within the valid range
        if user_number < 1 or user_number > 100:
            print("Number out of range (1-100). Try again.")
            continue
        # Check if the number has been guessed before
        if user_number in guessed_numbers:
            print("You've already guessed that number. Try again.")
            continue
        guessed_numbers.add(user_number)
        tries -= 1
        #Displays a congratulations message for correct guesses
        if user_number == random_number:
            print(f"Congratulations! You guessed the number in {10 - tries} tries.")
            break
        #Gets user input and compares it with the random number
        elif user_number < random_number:
            print("Your guess is too low , Try again. ")
        else:
            print("Your guess is too high, Try again. ")
    #Limits the number of tries to 10        
    if tries == 0:
        print(f"\nYou've run out of tries. The number was {random_number}.")
    #Allows the user to play again or not
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        guessing_game()
    else:
        print("Thank you for playing!")
# Start the game
guessing_game()

#Q6 : ​Hacker-rank for problem solving(bonus) https://www.hackerrank.com/challenges/diagonal-difference/problem
import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    n = len(arr)
    primary_sum = sum(arr[i][i] for i in range(n))
    secondary_sum = sum(arr[i][n-i-1] for i in range(n))
    return abs(primary_sum - secondary_sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()