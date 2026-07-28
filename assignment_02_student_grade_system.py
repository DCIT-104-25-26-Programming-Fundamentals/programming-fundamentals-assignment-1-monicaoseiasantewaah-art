# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter student score (0-100): 85
#   Grade: A
#
#   Enter student score (0-100): 73
#   Grade: B
#
#   Enter student score (0-100): 45
#   Grade: F
#
#   Enter student score (0-100): 110
#   Error: Score must be between 0 and 100.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST use functions (see scaffold below).
# - Validate that the score is within the range 0–100 inside get_grade().
#   If it is not, return None and let main() print the error message.
# - Use if / elif / else to determine the grade.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


def find_minimum(numbers):
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum


def main():
    try:
        count = int(input("How many numbers? "))
        
        # Requirement: N must be a positive integer
        if count <= 0:
            print("Error: Number of elements must be a positive integer.")
            return

        numbers = []
        for i in range(1, count + 1):
            val = float(input(f"Enter number {i}: "))
            numbers.append(val)

        print("\nResults:")
        print(f"Sum:      {calculate_sum(numbers)}")
        print(f"Average:  {calculate_average(numbers)}")
        print(f"Maximum:  {find_maximum(numbers)}")
        print(f"Minimum:  {find_minimum(numbers)}")

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()
    
