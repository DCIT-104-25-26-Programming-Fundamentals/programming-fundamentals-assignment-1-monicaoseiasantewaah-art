# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_matrix(matrix):
    """Displays a 2D matrix in a clean, aligned grid format."""
    for row in matrix:
        print("  ".join(str(val) for val in row))


def read_matrix(rows, cols):
    """Reads a matrix row by row from user input."""
    matrix = []
    for i in range(1, rows + 1):
        while True:
            line = input(f"Enter row {i}: ").strip()
            row = [int(x) for x in line.split()]
            if len(row) == cols:
                matrix.append(row)
                break
            print(f"Error: Please enter exactly {cols} numbers separated by spaces.")
    return matrix


def transpose_matrix(matrix):
    """Transposes an m x n matrix into an n x m matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Adds two matrices of the same size element-wise."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Multiplies an m x n matrix A with an n x p matrix B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            row.append(total)
        result.append(row)
    return result


def main():
    # --- PART A: Transpose a Matrix ---
    print("--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = read_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    
    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix))
    print()

    # --- PART B: Add Two Matrices ---
    print("--- PART B: Add Two Matrices ---")
    rows_b = int(input("Enter number of rows: "))
    cols_b = int(input("Enter number of columns: "))
    
    print("Enter Matrix A:")
    mat_a = read_matrix(rows_b, cols_b)
    
    print("Enter Matrix B:")
    mat_b = read_matrix(rows_b, cols_b)
    
    print("\nSum of Matrices:")
    print_matrix(add_matrices(mat_a, mat_b))
    print()

    # --- PART C: Multiply Two Matrices ---
    print("--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter number of rows for Matrix A (m): "))
    n = int(input("Enter number of columns for Matrix A / rows for Matrix B (n): "))
    p = int(input("Enter number of columns for Matrix B (p): "))
    
    print("Enter Matrix A:")
    mat_c1 = read_matrix(m, n)
    
    print("Enter Matrix B:")
    mat_c2 = read_matrix(n, p)
    
    print("\nProduct of Matrices (A x B):")
    print_matrix(multiply_matrices(mat_c1, mat_c2))


if __name__ == "__main__":
    main()
    
