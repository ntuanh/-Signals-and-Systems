import numpy as np
import matplotlib.pyplot as plt

y_val = [-4/9 , -1/3]

n = 7
for i in range(n):
  y_val.append( pow(3 , i - 2) +  3 * y_val[i - 1 + 2] - 2 * y_val[i - 2 + 2])

# print(y_val)
y_true = []
for i in range(n) :
  y_true.append((pow(3 , i) - 1)/2)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# First subplot: Computed values
axs[0].stem(range(len(y_val)), y_val, use_line_collection=True)
axs[0].set_title("Giá trị tính toán")
axs[0].set_xlabel("Giá trị n")

# Second subplot: True values
axs[1].stem(range(len(y_true)), y_true, use_line_collection=True)
axs[1].set_title("Giá trị thực")
axs[1].set_xlabel("Giá trị n")

plt.tight_layout()
plt.savefig("LinearDifferenceEquation.png")
plt.show()


# import numpy as np 
# import matplotlib.pyplot as plt

# import sympy as sp

# # declare 
# y = [1 , -3 , 2]     # y(n) - 3y(n-1) + 2y(n-2) = 0 

# y_condition = [-4/9 , -1/3] 

# X  , Y  = 1 , 1


# def z_transform(x, z):
#     """
#     Hàm tính biến đổi Z một phía của tín hiệu rời rạc x[n].
#     Args:
#         x: list hoặc numpy array chứa tín hiệu rời rạc x[n], n từ 0 đến len(x)-1
#         z: số phức hoặc biểu tượng (biến z)
#     Returns:
#         Giá trị biến đổi Z X(z)
#     """
#     Xz = 0
#     for n in range(len(x)):
#         Xz += x[n] * (z ** (-n))
#     return Xz


# z = sp.symbols('z')
# x = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

# Xz = z_transform(x, z)

# print(Xz)   

# def compute_yn(n):
#     """
#     Compute y(n) for the difference equation: y(n) - 3y(n-1) + 2y(n-2) = 3^(n-2)
#     with initial conditions: y(-1) = -1/3, y(-2) = -4/9
    
#     Parameters:
#     n : int
#         The time index to compute y(n)
        
#     Returns:
#     float
#         The value of y(n)
#     """
#     # Initialize the solution array
#     y_n = np.zeros(n + 3)  # +3 to account for n=-2, -1, 0
    
#     # Set initial conditions
#     y_n[0] = -4/9  # y(-2)
#     y_n[1] = -1/3  # y(-1)
    
#     # Compute y(n) for n >= 0
#     for i in range(2, n + 3):
#         # y(n) = 3y(n-1) - 2y(n-2) + 3^(n-2)
#         y_n[i] = 3 * y_n[i-1] - 2 * y_n[i-2] + (3 ** (i-4))  # i-4 because we start from n=-2
    
#     return y_n[n+2]  # Return y(n)

# # Example usage
# if __name__ == "__main__":
#     # Compute y(n) for n = 0 to 10
#     n_values = range(11)
#     y_values = [compute_yn(n) for n in n_values]
    
#     # Plot the results
#     plt.figure(figsize=(10, 6))
#     plt.stem(n_values, y_values)
#     plt.title('Solution of y(n) - 3y(n-1) + 2y(n-2) = 3^(n-2)')
#     plt.xlabel('n')
#     plt.ylabel('y(n)')
#     plt.grid(True)
#     plt.show()
    
#     # Print some values
#     print("First few values of y(n):")
#     for n in range(20):
#         print(f"y({n}) = {y_values[n]:.4f}")   
