import matplotlib.pyplot as plt
import numpy as np                                                                      

def newton_raphson(func, deriv_func, x0, tol, max_iter):
    x = x0
    iterations = [x0]
    for i in range(max_iter):
        fx = func(x)
        fpx = deriv_func(x)
        
        if abs(fpx) < tol:
            print("Turunan mendekati nol, metode gagal.")
            return None, iterations
        
        x_new = x - fx / fpx
        iterations.append(x_new)
        
        if abs(x_new - x) < tol:
            return x_new, iterations
        
        x = x_new
        
    print("Tidak konvergen setelah iterasi maksimal")
    return None, iterations

# Contoh penggunaan:
def func(x):
    return x**2 - 2

def deriv_func(x):
    return 2*x

x0 = 1.0
tol = 1e-6
max_iter = 100

root, iterations = newton_raphson(func, deriv_func, x0, tol, max_iter)
if root is not None:
    print(f"Akar yang ditemukan: {root}")
else:
    print("Akar tidak ditemukan.")

# Plotting
x_vals = np.linspace(0, 2, 400)
y_vals = func(x_vals)
iter_x_vals = np.array(iterations)
iter_y_vals = func(iter_x_vals)

plt.plot(x_vals, y_vals, label='f(x) = x^2 - 2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter(iter_x_vals, iter_y_vals, color='red', zorder=5)
plt.plot(iter_x_vals, iter_y_vals, color='red', linestyle='--', marker='o', label='Iterasi Newton-Raphson')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Metode Newton-Raphson untuk f(x) = x^2 - 2')
plt.grid(True)
plt.show()
