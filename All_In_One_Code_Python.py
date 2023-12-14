#menu and user input
def Main(enter_menu):
    while True:
        # Prompt the user to enter a choice (1-5) from the menu
        num = input("CHOOSE (1-5):\n1. IS PALINDROME \n2. SUM OF EVEN NUMBER\n3. REVERSE STRING\n4.FIZZ_BUZZ\n5. CHECK PRIME\n\n")
        

        if num == '1':
            # 1: Check palindrome
            string = input("Enter a string: ")
            is_palindrome(string)
        elif num == '2':
            # 2: sum of even numbers
            numbers = input("Enter num separated by spaces: ").split()
            numbers = [int(num) for num in numbers]
            print("Sum of even numbers:", sum_of_even(numbers))
        elif num == '3':
            # 3: Reverse a string
            string = input("Enter a string: ")
            print("Reversed string:", reverse_string(string))
        elif num == '4':
            # 4: Fizz Buzz
            fizz_buzz()
        elif num == '5':
            # 5: Check prime
            number = int(input("Enter a number: "))
            if is_prime(number):
                print(number, "is a prime number\n")
            else:
                print(number, "is not a prime number\n")
        else:
            # Invalid input
            print("Invalid choice. Please enter a number from 1 to 5.")

# palindrome
def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        print("Palindrome:", string)
    else:
        print("Not a palindrome:", string)

# sum of even numbers
def sum_of_even(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum

# function to reverse
def reverse_string(string):
    return string[::-1]

# function to fizz_buzz
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
#function for prime number
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Prompt the user to press the enter key
Enter = input("Press enter key")

# Call the main function
Main(Enter)

#Zelalem Desta /ZOLA