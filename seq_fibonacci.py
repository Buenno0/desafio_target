def is_in_fibonacci(number):
    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]
    
    # Generate Fibonacci numbers until the last number is greater than or equal to the input number
    while sequence[-1] < number:
        # Append the next Fibonacci number to the sequence
        sequence.append(sequence[-1] + sequence[-2])
    
    # Check if the input number is in the generated Fibonacci sequence
    return number in sequence

# Read an integer input from the user
number = int(input("Digite um número"))

# Check if the input number is in the Fibonacci sequence and print the appropriate message
if is_in_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")
