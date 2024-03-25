def print_fibonacci(length):
    fibonacci_sequence = []  # Initialize with an empty list
    
    # Generate Fibonacci sequences up to the specified length
    for i in range(length):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    # Print the Fibonacci sequence
    print("Fibonacci Sequence:")
    print(fibonacci_sequence)

# Example usage:
print_fibonacci(0)  # Print Fibonacci sequence up to length 0
