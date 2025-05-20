import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def solve_homogeneous_equation(coefficients, initial_conditions):
    """
    Solve homogeneous linear difference equation of the form:
    a₀y[n] + a₁y[n-1] + ... + aₙy[n-N] = 0
    
    Parameters:
    coefficients (list): List of coefficients [a₀, a₁, ..., aₙ]
    initial_conditions (list): List of initial conditions [y[0], y[1], ..., y[N-1]]
    
    Returns:
    numpy.ndarray: Solution sequence
    """
    # Convert to numpy array for easier manipulation
    coeffs = np.array(coefficients)
    init_conds = np.array(initial_conditions)
    
    # Find the roots of the characteristic equation
    roots = np.roots(coeffs)
    
    # Generate the solution sequence
    n = len(init_conds)
    solution = np.zeros(n + 10)  # Generate 10 more points for visualization
    solution[:n] = init_conds
    
    # Calculate remaining points using the difference equation
    for i in range(n, len(solution)):
        solution[i] = -np.sum(coeffs[1:] * solution[i-1:i-n:-1]) / coeffs[0]
    
    return solution

def solve_nonhomogeneous_equation(coefficients, input_sequence, initial_conditions):
    """
    Solve non-homogeneous linear difference equation of the form:
    a₀y[n] + a₁y[n-1] + ... + aₙy[n-N] = x[n]
    
    Parameters:
    coefficients (list): List of coefficients [a₀, a₁, ..., aₙ]
    input_sequence (numpy.ndarray): Input sequence x[n]
    initial_conditions (list): List of initial conditions [y[0], y[1], ..., y[N-1]]
    
    Returns:
    numpy.ndarray: Solution sequence
    """
    # Convert to numpy arrays
    coeffs = np.array(coefficients)
    x = np.array(input_sequence)
    init_conds = np.array(initial_conditions)
    
    # Initialize solution array
    n = len(init_conds)
    solution = np.zeros(len(x))
    solution[:n] = init_conds
    
    # Calculate remaining points using the difference equation
    for i in range(n, len(solution)):
        solution[i] = (x[i] - np.sum(coeffs[1:] * solution[i-1:i-n:-1])) / coeffs[0]
    
    return solution

def plot_solution(solution, title="Solution of Linear Difference Equation"):
    """
    Plot the solution sequence
    
    Parameters:
    solution (numpy.ndarray): Solution sequence to plot
    title (str): Title for the plot
    """
    plt.figure(figsize=(10, 6))
    plt.stem(solution)
    plt.title(title)
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.grid(True)
    plt.show()

def find_impulse_response(coefficients, length=50):
    """
    Find the impulse response of the system
    
    Parameters:
    coefficients (list): List of coefficients [a₀, a₁, ..., aₙ]
    length (int): Length of the impulse response to calculate
    
    Returns:
    numpy.ndarray: Impulse response sequence
    """
    # Create impulse input
    impulse = np.zeros(length)
    impulse[0] = 1
    
    # Use scipy's lfilter to find impulse response
    b = [1.0]  # Numerator coefficients
    a = coefficients  # Denominator coefficients
    h = signal.lfilter(b, a, impulse)
    
    return h

# Example usage
if __name__ == "__main__":
    # Example 1: Homogeneous equation
    # y[n] - 1.5y[n-1] + 0.5y[n-2] = 0
    coeffs_homogeneous = [1, -1.5, 0.5]
    init_conds = [1, 2]
    solution_homogeneous = solve_homogeneous_equation(coeffs_homogeneous, init_conds)
    plot_solution(solution_homogeneous, "Solution of Homogeneous Equation")
    
    # Example 2: Non-homogeneous equation
    # y[n] - 0.5y[n-1] = x[n]
    coeffs_nonhomogeneous = [1, -0.5]
    input_seq = np.ones(50)  # Step input
    init_conds = [0]
    solution_nonhomogeneous = solve_nonhomogeneous_equation(
        coeffs_nonhomogeneous, input_seq, init_conds)
    plot_solution(solution_nonhomogeneous, "Solution of Non-homogeneous Equation")
    
    # Example 3: Impulse response
    h = find_impulse_response(coeffs_nonhomogeneous)
    plot_solution(h, "Impulse Response")
