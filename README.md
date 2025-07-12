Task 1 
 Step-by-Step Functionality
- User Input:
- Prompts the user to enter two numbers.
- These inputs are initially stored as strings.
N1 = input("Enter First Number : ")
N2 = input("Enter Second Number : ")
- Type Conversion:
- Converts the string inputs into integers using int().
N1 = int(N1)
N2 = int(N2)
- Arithmetic Operations:
- Performs and prints the result of:
- Addition: N1 + N2
- Subtraction: N1 - N2
- Multiplication: N1 * N2
- Division: N1 / N2 (returns a float)


Task 2

 Step-by-Step Functionality
- User Input:
- Prompts the user to enter their first name and last name.
- Stores the inputs as strings.
input1 = input("Enter your first name : ")
input2 = input("Enter your last name : ")
- String Concatenation:
- Combines the first and last name with a space in between to form the full name.
full_name = input1 + " " + input2
- Personalized Greeting:
- Prints a welcome message using the full name.
print("Hello, ", full_name, "! Welcome to the Python Program.")


Task 2_1
 Step-by-Step Functionality
- Input from User
- The line x = int(input("Enter a number :")) prompts the user to enter a number.
- The input is read as a string and then converted to an integer using int().
- Check Even or Odd
- The condition if x % 2 == 0 checks whether the number is divisible by 2.
- % is the modulo operator—it returns the remainder when x is divided by 2.
- If the remainder is 0, the number is even.
- If the remainder is not 0, the number is odd.
- Print the Result
- If the number is even, it executes print(x, "is an even number").
- If the number is odd, it executes print(x, "is an odd number").
- Final Message
- Regardless of the input, it ends by printing "Thank You".

Task 2_2

 Step-by-Step Functionality
- Initialization
- sum = 0: Starts with a variable sum set to zero—this will hold the running total.
- counter = 1: Begins counting from 1.
- Looping with while
- while counter <= 50: This loop will run as long as counter is less than or equal to 50.
- Inside the loop:
- sum = counter + sum: Adds the current counter value to the total sum.
- counter += 1: Increases counter by 1 for the next iteration.
- Final Output
- print("Sum:", sum): Once the loop ends (when counter reaches 51), it prints the final value of sum.







