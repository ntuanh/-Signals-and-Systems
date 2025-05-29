import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, Eq, Function, dsolve, Symbol, simplify, sin, cos, exp
from sympy.abc import n

# Khai báo các hằng số C1, C2
C1, C2 = symbols('C1 C2')

class InputSignal:
    """Lớp xử lý các dạng tín hiệu đầu vào khác nhau"""
    
    @staticmethod
    def exponential(a, n0=0):
        """Tín hiệu dạng mũ: x(n) = a^(n-n0)"""
        def signal(n):
            return a**(n-n0) if n >= n0 else 0
        return signal
    
    @staticmethod
    def sine(omega, phi=0, n0=0):
        """Tín hiệu dạng sin: x(n) = sin(omega*n + phi)"""
        def signal(n):
            return np.sin(omega*n + phi) if n >= n0 else 0
        return signal
    
    @staticmethod
    def cosine(omega, phi=0, n0=0):
        """Tín hiệu dạng cos: x(n) = cos(omega*n + phi)"""
        def signal(n):
            return np.cos(omega*n + phi) if n >= n0 else 0
        return signal
    
    @staticmethod
    def step(n0=0):
        """Tín hiệu bước nhảy đơn vị: x(n) = u(n-n0)"""
        def signal(n):
            return 1 if n >= n0 else 0
        return signal
    
    @staticmethod
    def impulse(n0=0):
        """Tín hiệu xung đơn vị: x(n) = delta(n-n0)"""
        def signal(n):
            return 1 if n == n0 else 0
        return signal
    
    @staticmethod
    def combined(signals):
        """Tổng hợp nhiều tín hiệu"""
        def signal(n):
            return sum(s(n) for s in signals)
        return signal

def find_characteristic_roots(coefficients):
    """
    Tìm nghiệm đặc trưng của phương trình phân sai tuyến tính
    
    Tham số:
    coefficients (list): Danh sách các hệ số của phương trình [a_n, a_{n-1}, ..., a_0]
    
    Trả về:
    list: Danh sách các nghiệm đặc trưng
    """
    # Tạo đa thức đặc trưng
    r = Symbol('r')
    poly = sum(coef * r**i for i, coef in enumerate(coefficients))
    
    # Giải phương trình đặc trưng
    roots = solve(poly, r)
    return roots

def find_particular_solution(coefficients, input_signal_type, params):
    """
    Tìm nghiệm riêng của phương trình phân sai tuyến tính
    
    Tham số:
    coefficients (list): Danh sách các hệ số của phương trình
    input_signal_type (str): Loại tín hiệu đầu vào
    params (dict): Các tham số của tín hiệu đầu vào
    
    Trả về:
    str: Công thức nghiệm riêng
    """
    n = Symbol('n')
    
    if input_signal_type == 'exponential':
        a = params.get('a', 3)
        n0 = params.get('n0', 2)
        # Thử nghiệm riêng dạng y_p(n) = A*a^n
        A = Symbol('A')
        y_p = A * a**n
        equation = sum(coef * y_p.subs(n, n-i) for i, coef in enumerate(coefficients))
        equation = equation - a**(n-n0)
        A_value = solve(equation, A)[0]
        return f"{A_value}*{a}^n"
    
    elif input_signal_type == 'sine':
        omega = params.get('omega', 1)
        phi = params.get('phi', 0)
        # Thử nghiệm riêng dạng y_p(n) = A*sin(omega*n + phi) + B*cos(omega*n + phi)
        A, B = symbols('A B')
        y_p = A * sin(omega*n + phi) + B * cos(omega*n + phi)
        equation = sum(coef * y_p.subs(n, n-i) for i, coef in enumerate(coefficients))
        equation = equation - sin(omega*n + phi)
        constants = solve([equation.coeff(sin(omega*n + phi)), equation.coeff(cos(omega*n + phi))], [A, B])
        return f"{constants[A]}*sin({omega}*n + {phi}) + {constants[B]}*cos({omega}*n + {phi})"
    
    elif input_signal_type == 'cosine':
        omega = params.get('omega', 1)
        phi = params.get('phi', 0)
        # Thử nghiệm riêng dạng y_p(n) = A*sin(omega*n + phi) + B*cos(omega*n + phi)
        A, B = symbols('A B')
        y_p = A * sin(omega*n + phi) + B * cos(omega*n + phi)
        equation = sum(coef * y_p.subs(n, n-i) for i, coef in enumerate(coefficients))
        equation = equation - cos(omega*n + phi)
        constants = solve([equation.coeff(sin(omega*n + phi)), equation.coeff(cos(omega*n + phi))], [A, B])
        return f"{constants[A]}*sin({omega}*n + {phi}) + {constants[B]}*cos({omega}*n + {phi})"
    
    else:
        return "y_p(n)"  # Trả về dạng tổng quát nếu không xác định được dạng cụ thể

def get_general_solution(coefficients, input_signal_type=None, params=None):
    """
    Tìm nghiệm tổng quát của phương trình phân sai tuyến tính
    
    Tham số:
    coefficients (list): Danh sách các hệ số của phương trình
    input_signal_type (str): Loại tín hiệu đầu vào
    params (dict): Các tham số của tín hiệu đầu vào
    
    Trả về:
    str: Công thức nghiệm tổng quát
    """
    roots = find_characteristic_roots(coefficients)
    
    # Xây dựng phần nghiệm thuần nhất
    homogeneous = ""
    for i, root in enumerate(roots):
        if i > 0:
            homogeneous += " + "
        if isinstance(root, complex):
            homogeneous += f"C{i+1}*({root})^n"
        else:
            homogeneous += f"C{i+1}*{root}^n"
    
    # Thêm phần nghiệm riêng nếu có tín hiệu đầu vào
    particular = ""
    if input_signal_type is not None:
        particular = " + " + find_particular_solution(coefficients, input_signal_type, params or {})
    
    return f"y(n) = {homogeneous}{particular}"

def solve_linear_difference_equation(coefficients, initial_conditions, n_steps, input_signal=None):
    """
    Giải phương trình phân sai tuyến tính với các điều kiện ban đầu
    
    Tham số:
    coefficients (list): Danh sách các hệ số của phương trình [a_n, a_{n-1}, ..., a_0]
    initial_conditions (list): Danh sách các điều kiện ban đầu
    n_steps (int): Số bước cần tính
    input_signal (function): Hàm tính giá trị của tín hiệu đầu vào x(n)
    
    Trả về:
    list: Giá trị của dãy số tại các bước
    """
    # Kiểm tra tính hợp lệ của đầu vào
    if len(coefficients) != len(initial_conditions) + 1:
        raise ValueError("Số lượng hệ số phải bằng số điều kiện ban đầu + 1")
    
    # Khởi tạo mảng kết quả với các điều kiện ban đầu
    result = list(initial_conditions)
    
    # Tính các giá trị tiếp theo
    for i in range(len(initial_conditions), n_steps):
        next_value = 0
        # Tính phần hệ số của y(n)
        for j in range(len(coefficients) - 1):
            next_value -= coefficients[j] * result[i - j - 1]
        
        # Thêm phần tín hiệu đầu vào nếu có
        if input_signal is not None:
            next_value += input_signal(i)
            
        next_value /= coefficients[-1]
        result.append(next_value)
    
    return result

def plot_solution(sequence, title="Nghiệm của phương trình phân sai tuyến tính"):
    """
    Vẽ đồ thị của dãy số
    
    Tham số:
    sequence (list): Dãy số cần vẽ
    title (str): Tiêu đề của đồ thị
    """
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, 'b-o')
    plt.grid(True)
    plt.title(title)
    plt.xlabel('n')
    plt.ylabel('y(n)')
    plt.show()

# Ví dụ sử dụng
if __name__ == "__main__":
    # Ví dụ 1: x(n+2) - 5x(n+1) + 6x(n) = 0 với x(0) = 1, x(1) = 2
    print("Ví dụ 1:")
    coefficients1 = [1, -5, 6]  # Hệ số của x(n+2), x(n+1), x(n)
    initial_conditions1 = [1, 2]  # x(0) = 1, x(1) = 2
    n_steps1 = 10
    
    print("Nghiệm tổng quát của ví dụ 1:")
    print(get_general_solution(coefficients1))
    print("\nNghiệm số của phương trình:")
    solution1 = solve_linear_difference_equation(coefficients1, initial_conditions1, n_steps1)
    for i, value in enumerate(solution1):
        print(f"x({i}) = {value}")
    
    plot_solution(solution1, "Ví dụ 1: x(n+2) - 5x(n+1) + 6x(n) = 0")
    
    # Ví dụ 2: y(n) - 3y(n-1) + 2y(n-2) = x(n) với x(n) = 3^(n-2)
    print("\nVí dụ 2:")
    input_signal2 = InputSignal.exponential(3, 2)  # x(n) = 3^(n-2)
    
    coefficients2 = [1, -3, 2]  # Hệ số của y(n), y(n-1), y(n-2)
    initial_conditions2 = [-4/9, -1/3]  # y(-2) = -4/9, y(-1) = -1/3
    n_steps2 = 15
    
    print("Nghiệm tổng quát của ví dụ 2:")
    general_solution = get_general_solution(coefficients2, 'exponential', {'a': 3, 'n0': 2})
    print(general_solution)
    
    # Tìm các hằng số C1, C2 từ điều kiện ban đầu
    roots = find_characteristic_roots(coefficients2)
    n = Symbol('n')
    y_n = C1 * roots[0]**n + C2 * roots[1]**n + find_particular_solution(coefficients2, 'exponential', {'a': 3, 'n0': 2})
    
    # Giải hệ phương trình với điều kiện ban đầu
    eq1 = Eq(y_n.subs(n, -2), -4/9)
    eq2 = Eq(y_n.subs(n, -1), -1/3)
    constants = solve([eq1, eq2], [C1, C2])
    
    print("\nCác hằng số được xác định từ điều kiện ban đầu:")
    print(f"C1 = {constants[C1]}")
    print(f"C2 = {constants[C2]}")
    
    print("\nNghiệm số của phương trình:")
    solution2 = solve_linear_difference_equation(coefficients2, initial_conditions2, n_steps2, input_signal2)
    for i, value in enumerate(solution2):
        print(f"y({i-2}) = {value}")
    
    plot_solution(solution2, "Ví dụ 2: y(n) - 3y(n-1) + 2y(n-2) = 3^(n-2)")
    
    # Ví dụ 3: y(n) - 2y(n-1) + y(n-2) = sin(n)
    print("\nVí dụ 3:")
    input_signal3 = InputSignal.sine(1)  # x(n) = sin(n)
    
    coefficients3 = [1, -2, 1]  # Hệ số của y(n), y(n-1), y(n-2)
    initial_conditions3 = [0, 0]  # y(0) = 0, y(1) = 0
    n_steps3 = 20
    
    print("Nghiệm tổng quát của ví dụ 3:")
    general_solution3 = get_general_solution(coefficients3, 'sine', {'omega': 1})
    print(general_solution3)
    
    print("\nNghiệm số của phương trình:")
    solution3 = solve_linear_difference_equation(coefficients3, initial_conditions3, n_steps3, input_signal3)
    for i, value in enumerate(solution3):
        print(f"y({i}) = {value}")
    
    plot_solution(solution3, "Ví dụ 3: y(n) - 2y(n-1) + y(n-2) = sin(n)")
