# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def generate_fibonacci(n):
    """Generates the first n terms of the Fibonacci sequence using a loop."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def is_fibonacci(number):
    """Checks if a given non-negative integer belongs to the Fibonacci sequence."""
    if number < 0:
        return False
    
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number


def print_first_n_terms():
    """Handles Part A: Ask user for N and print first N terms."""
    print("--- PART A: Print the First N Terms ---")
    try:
        n = int(input("How many terms? "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return

        terms = generate_fibonacci(n)
        print("Fibonacci sequence:", " ".join(str(x) for x in terms))
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


def check_if_fibonacci():
    """Handles Part B: Check if a user's number is a Fibonacci number."""
    print("\n--- PART B: Check if a Number Belongs to the Sequence ---")
    try:
        num = int(input("Enter a number to check: "))
        if num < 0:
            print("Error: Please enter a non-negative integer.")
            return

        if is_fibonacci(num):
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


def main():
    print_first_n_terms()
    check_if_fibonacci()


if __name__ == "__main__":
    main()
    
