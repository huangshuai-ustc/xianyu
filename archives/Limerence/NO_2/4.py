import numpy as np

# Define the system matrix A and the right-hand side vector b
A = np.array([[1, 2],
              [2, 4.01]])
b = np.array([1, 2])

# Define the approximate solutions
approx_solutions = [np.array([-1, 1]), np.array([3, -1]), np.array([2, -1/2])]

# Initialize lists to store forward errors, backward errors, and error magnification factors
forward_errors = []
backward_errors = []
error_magnification_factors = []

# Calculate the actual solution using numpy's linear algebra solver
actual_solution = np.linalg.solve(A, b)

# Calculate errors and error magnification factors for each approximate solution
for solution in approx_solutions:
    # Forward error: ||x_approx - x_exact||
    forward_error = np.linalg.norm(solution - actual_solution)
    forward_errors.append(forward_error)

    # Backward error: ||Ax_approx - b||
    backward_error = np.linalg.norm(np.dot(A, solution) - b)
    backward_errors.append(backward_error)

    # Error magnification factor: ||Ax_approx - b|| / ||A|| * ||x_approx||
    # error_magnification_factor = backward_error / (np.linalg.norm(A) * np.linalg.norm(solution))
    error_magnification_factor = forward_error / np.linalg.norm(actual_solution) * backward_error / np.linalg.norm(solution)
    error_magnification_factors.append(error_magnification_factor)

# Print results
for i, solution in enumerate(approx_solutions):
    print(f"Approximate Solution (a, b): {solution}")
    print(f"Forward Error: {forward_errors[i]}")
    print(f"Backward Error: {backward_errors[i]}")
    print(f"Error Magnification Factor: {error_magnification_factors[i]}\n")
