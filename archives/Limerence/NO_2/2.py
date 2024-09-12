import numpy as np


# Function to calculate the condition number of a matrix
def condition_number(matrix):
    return np.linalg.cond(matrix)


# Function to calculate the number of accurate digits
def num_accurate_digits(approx, exact):
    return -np.log10(np.linalg.norm(approx - exact) / np.linalg.norm(exact))


# Define N values
Ns = [6, 10]

for N in Ns:
    # Generate the Hilbert matrix
    H = np.array([[1.0 / (i + j + 1) for j in range(N)] for i in range(N)])

    # Create the exact solution x as an array of ones
    x = np.ones(N)

    # Calculate the right-hand side vector b = Hx
    b = np.dot(H, x)

    # Solve the system using numpy.linalg.solve
    xa = np.linalg.solve(H, b)

    # Calculate the condition number of H
    cond_number = condition_number(H)

    # Calculate the number of accurate digits
    accurate_digits = num_accurate_digits(xa, x)

    # Print the results
    print(f"For N = {N}:")
    print(f"Condition Number of Hilbert Matrix: {cond_number}")
    print(f"Exact Solution (x): {x}")
    print(f"Approximate Solution (xa): {xa}")
    print(f"Number of Accurate Digits: {accurate_digits}\n")
