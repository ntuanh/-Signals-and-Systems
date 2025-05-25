import matplotlib.pyplot as plt

def compute_y_true(n, y_val_init=[-4/9, -1/3]):
    """
    Compute y_val using the recurrence:
    y_val[i] = pow(3, i - 2) + 3 * y_val[i - 1 + 2] - 2 * y_val[i - 2 + 2]
    with initial y_val = [-4/9, -1/3]
    
    Args:
        n: number of new values to compute (int)
        y_val_init: initial values for y_val (list)
    Returns:
        y_val: list of computed values
    """
    y_val = y_val_init.copy()
    for i in range(n):
        y_val.append(pow(3, i - 2) + 3 * y_val[i - 1 + 2] - 2 * y_val[i - 2 + 2])
    return y_val

def plot_y_true(y_val):
    """
    Draw a stem plot for the computed y_val values.
    """
    y_val = y_val[2:]
    plt.figure(figsize=(6, 4))
    plt.stem(range(len(y_val)), y_val)
    plt.title("Plot of y_val")
    plt.xlabel("n")
    plt.ylabel("y_val[n]")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

