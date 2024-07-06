# import pickle
# import tempfile
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation, FFMpegWriter

# def create_function_from_string(equation):
#     allowed_functions = {
#         'sin': np.sin,
#         'cos': np.cos,
#         'tan': np.tan,
#         'log': np.log,
#         'exp': np.exp,
#         'sqrt': np.sqrt,
#         'power': np.power,
#         'pi': np.pi,
#         'e': np.e
#     }
    
#     equation = equation.replace('^', '**')
    
#     def fx_equal_0(x):
#         try:
#             return eval(equation, {"__builtins__": None}, {**allowed_functions, 'x': x})
#         except Exception as e:
#             print(f"Error in evaluating the equation: {e}")
#             return None
    
#     return fx_equal_0

# def derivative(f, x):
#     h = 1e-6
#     return (f(x + h) - f(x)) / h

# def newton_raphson(f, df, x0, tol=1e-8, max_iter=1000):
#     x = x0
#     steps = [(x, f(x))]
#     errors = []
#     for i in range(max_iter):
#         fx = f(x)
#         dfx = df(x)
#         if abs(fx) < tol:
#             return x, errors, steps
#         if dfx == 0:
#             raise ValueError("Derivative is zero. No solution found.")
#         x_new = x - fx / dfx
#         steps.append((x_new, f(x_new)))
#         errors.append(abs(x_new - x))
#         x = x_new
#     raise ValueError("Maximum iterations exceeded. No solution found.")

# def secant_method(f, x0, x1, tol=1e-8, max_iter=1000):
#     steps = [(x0, f(x0)), (x1, f(x1))]
#     errors = []
#     for i in range(max_iter):
#         fx0 = f(x0)
#         fx1 = f(x1)
#         if abs(fx1) < tol:
#             return x1, errors, steps
#         if (fx1 - fx0) == 0:
#             raise ValueError("Division by zero encountered.")
#         x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
#         steps.append((x_new, f(x_new)))
#         errors.append(abs(x_new - x1))
#         x0, x1 = x1, x_new
#     raise ValueError("Maximum iterations exceeded. No solution found.")

# def bisection_method(f, a, b, tol=1e-8, max_iter=1000):
#     steps = [(a, f(a)), (b, f(b))]
#     errors = []
#     if f(a) * f(b) >= 0:
#         raise ValueError("The function must have different signs at the endpoints a and b.")
#     for i in range(max_iter):
#         c = (a + b) / 2
#         fc = f(c)
#         steps.append((c, fc))
#         errors.append(abs(b - a) / 2)
#         if abs(fc) < tol or abs(b - a) < tol:
#             return c, errors, steps
#         if f(a) * fc < 0:
#             b = c
#         else:
#             a = c
#     raise ValueError("Maximum iterations exceeded. No solution found.")

# def false_position_method(f, a, b, tol=1e-8, max_iter=1000):
#     steps = [(a, f(a)), (b, f(b))]
#     errors = []
#     if f(a) * f(b) >= 0:
#         raise ValueError("The function must have different signs at the endpoints a and b.")
#     for i in range(max_iter):
#         c = a - (f(a) * (b - a)) / (f(b) - f(a))
#         fc = f(c)
#         steps.append((c, fc))
#         errors.append(abs(b - a) / 2)
#         if abs(fc) < tol or abs(b - a) < tol:
#             return c, errors, steps
#         if f(a) * fc < 0:
#             b = c
#         else:
#             a = c
#     raise ValueError("Maximum iterations exceeded. No solution found.")

# def animate_newton_raphson(f, steps, root):
#     fig, ax = plt.subplots(figsize=(12, 8))  # Increased figure size for better visibility
#     x_vals = np.linspace(root-1, root+1, 400)
#     y_vals = f(x_vals)
    
#     ax.plot(x_vals, y_vals, label='f(x)')
#     ax.axhline(0, color='black', linewidth=0.5)
    
#     line, = ax.plot([], [], 'ro-', label='Newton-Raphson steps')
#     point, = ax.plot([], [], 'bo', label='Current point')
    
#     def init():
#         line.set_data([], [])
#         point.set_data([], [])
#         return line, point
    
#     def update(frame):
#         x_data, y_data = zip(*steps[:frame+1])
#         line.set_data(x_data, y_data)
#         point.set_data(x_data[-1], y_data[-1])
#         return line, point
    
#     ani = FuncAnimation(fig, update, frames=len(steps), init_func=init, blit=True, repeat=False)
    
#     plt.title('Newton-Raphson Method Steps')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.legend()
#     plt.grid(True)
    
#     # Save the animation as a video file
#     writer = FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=1800)  # Adjust fps for slower iteration
#     ani.save("newton_raphson_animation.mp4", writer=writer)
#     plt.show()

# def animate_secant_method(f, steps, root):
#     fig, ax = plt.subplots(figsize=(12, 8))
#     x_vals = np.linspace(min(steps)[0]-1, max(steps)[0]+1, 400)
#     y_vals = f(x_vals)
    
#     ax.plot(x_vals, y_vals, label='f(x)')
#     ax.axhline(0, color='black', linewidth=0.5)
    
#     line, = ax.plot([], [], 'ro-', label='Secant steps')
#     point, = ax.plot([], [], 'bo', label='Current point')
    
#     def init():
#         line.set_data([], [])
#         point.set_data([], [])
#         return line, point
    
#     def update(frame):
#         x_data, y_data = zip(*steps[:frame+1])
#         line.set_data(x_data, y_data)
#         point.set_data(x_data[-1], y_data[-1])
#         return line, point
    
#     ani = FuncAnimation(fig, update, frames=len(steps), init_func=init, blit=True, repeat=False)
    
#     plt.title('Secant Method Steps')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.legend()
#     plt.grid(True)
    
#     writer = FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=1800)
#     ani.save("secant_method_animation.mp4", writer=writer)
#     plt.show()

# def animate_bisection_method(f, steps, root):
#     fig, ax = plt.subplots(figsize=(12, 8))
#     x_vals = np.linspace(min(steps, key=lambda x: x[0])[0]-1, max(steps, key=lambda x: x[0])[0]+1, 400)
#     y_vals = f(x_vals)
    
#     ax.plot(x_vals, y_vals, label='f(x)')
#     ax.axhline(0, color='black', linewidth=0.5)
    
#     line, = ax.plot([], [], 'ro-', label='Bisection steps')
#     point, = ax.plot([], [], 'bo', label='Current point')
    
#     def init():
#         line.set_data([], [])
#         point.set_data([], [])
#         return line, point
    
#     def update(frame):
#         x_data, y_data = zip(*steps[:frame+1])
#         line.set_data(x_data, y_data)
#         point.set_data(x_data[-1], y_data[-1])
#         return line, point
    
#     ani = FuncAnimation(fig, update, frames=len(steps), init_func=init, blit=True, repeat=False)
    
#     plt.title('Bisection Method Steps')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.legend()
#     plt.grid(True)
    
#     writer = FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=1800)
#     ani.save("bisection_method_animation.mp4", writer=writer)
#     plt.show()

# def animate_false_position_method(f, steps, root):
#     fig, ax = plt.subplots(figsize=(12, 8))
#     x_vals = np.linspace(min(steps, key=lambda x: x[0])[0]-1, max(steps, key=lambda x: x[0])[0]+1, 400)
#     y_vals = f(x_vals)
    
#     ax.plot(x_vals, y_vals, label='f(x)')
#     ax.axhline(0, color='black', linewidth=0.5)
    
#     line, = ax.plot([], [], 'ro-', label='False Position steps')
#     point, = ax.plot([], [], 'bo', label='Current point')
    
#     def init():
#         line.set_data([], [])
#         point.set_data([], [])
#         return line, point
    
#     def update(frame):
#         x_data, y_data = zip(*steps[:frame+1])
#         line.set_data(x_data, y_data)
#         point.set_data(x_data[-1], y_data[-1])
#         return line, point
    
#     ani = FuncAnimation(fig, update, frames=len(steps), init_func=init, blit=True, repeat=False)
    
#     plt.title('False Position Method Steps')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.legend()
#     plt.grid(True)
    
#     writer = FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=1800)
#     ani.save("false_position_method_animation.mp4", writer=writer)
#     plt.show()


# def generate_animation(steps, f):
#     fig, ax = plt.subplots()
#     x_data, y_data = [], []
#     ln, = plt.plot([], [], 'ro')

#     def init():
#         ax.set_xlim(min([step[0] for step in steps]) - 1, max([step[0] for step in steps]) + 1)
#         ax.set_ylim(min([f(step[0]) for step in steps]), max([f(step[0]) for step in steps]))
#         return ln,

#     def update(frame):
#         x_data.append(frame[0])
#         y_data.append(frame[1])
#         ln.set_data(x_data, y_data)
#         return ln,

#     ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=True)
#     writer = FFMpegWriter(fps=10)
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmpfile:
#         ani.save(tmpfile.name, writer=writer)
#         return tmpfile.name

'''
import pickle
import tempfile
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

def create_function_from_string(equation):
    allowed_functions = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'log': np.log,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'power': np.power,
        'pi': np.pi,
        'e': np.e
    }
    
    equation = equation.replace('^', '**')
    
    def fx_equal_0(x):
        try:
            return eval(equation, {"__builtins__": None}, {**allowed_functions, 'x': x})
        except Exception as e:
            print(f"Error in evaluating the equation: {e}")
            return None
    
    return fx_equal_0

def derivative(f, x):
    h = 1e-6
    return (f(x + h) - f(x)) / h

def newton_raphson(f, df, x0, tol=1e-8, max_iter=1000):
    x = x0
    steps = [(x, f(x))]
    errors = []
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, errors, steps
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / dfx
        steps.append((x_new, f(x_new)))
        errors.append(abs(x_new - x))
        x = x_new
    raise ValueError("Maximum iterations exceeded. No solution found.")

def secant_method(f, x0, x1, tol=1e-8, max_iter=1000):
    steps = [(x0, f(x0)), (x1, f(x1))]
    errors = []
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tol:
            return x1, errors, steps
        if (fx1 - fx0) == 0:
            raise ValueError("Division by zero encountered.")
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        steps.append((x_new, f(x_new)))
        errors.append(abs(x_new - x1))
        x0, x1 = x1, x_new
    raise ValueError("Maximum iterations exceeded. No solution found.")

def bisection_method(f, a, b, tol=1e-8, max_iter=1000):
    steps = [(a, f(a)), (b, f(b))]
    errors = []
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        steps.append((c, fc))
        errors.append(abs(b - a) / 2)
        if abs(fc) < tol or abs(b - a) < tol:
            return c, errors, steps
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum iterations exceeded. No solution found.")

def false_position_method(f, a, b, tol=1e-8, max_iter=1000):
    steps = [(a, f(a)), (b, f(b))]
    errors = []
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    for i in range(max_iter):
        c = a - (f(a) * (b - a)) / (f(b) - f(a))
        fc = f(c)
        steps.append((c, fc))
        errors.append(abs(b - a) / 2)
        if abs(fc) < tol or abs(b - a) < tol:
            return c, errors, steps
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum iterations exceeded. No solution found.")

def generate_animation(steps, f, filename):
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    ln, = plt.plot([], [], 'ro')

    x_vals = np.linspace(min([step[0] for step in steps]) - 10, max([step[0] for step in steps]) + 10, 400)
    y_vals = [f(x) for x in x_vals]
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.axhline(0, color='gray', lw=0.5)

    def init():
        ax.set_xlim(min([step[0] for step in steps]) - 1, max([step[0] for step in steps]) + 1)
        ax.set_ylim(min(y_vals), max(y_vals))
        return ln,

    def update(frame):
        x_data.append(frame[0])
        y_data.append(frame[1])
        ln.set_data(x_data, y_data)
        return ln,

    ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=True)
    writer = FFMpegWriter(fps=10)
    ani.save(filename, writer=writer)

def animate_newton_raphson(f, steps, root):
    filename = "newton_raphson.mp4"
    generate_animation(steps, f, filename)
    return filename

def animate_secant_method(f, steps, root):
    filename = "secant_method.mp4"
    generate_animation(steps, f, filename)
    return filename

def animate_bisection_method(f, steps, root):
    filename = "bisection_method.mp4"
    generate_animation(steps, f, filename)
    return filename

def animate_false_position_method(f, steps, root):
    filename = "false_position_method.mp4"
    generate_animation(steps, f, filename)
    return filename
'''

import pickle
import tempfile
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

def create_function_from_string(equation):
    allowed_functions = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'log': np.log,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'power': np.power,
        'pi': np.pi,
        'e': np.e
    }
    
    equation = equation.replace('^', '**')
    
    def fx_equal_0(x):
        try:
            return eval(equation, {"__builtins__": None}, {**allowed_functions, 'x': x})
        except Exception as e:
            print(f"Error in evaluating the equation: {e}")
            return None
    
    return fx_equal_0

def derivative(f, x):
    h = 1e-6
    return (f(x + h) - f(x)) / h

def newton_raphson(f, df, x0, tol=1e-8, max_iter=1000):
    x = x0
    steps = [(x, f(x))]
    errors = []
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, errors, steps
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / dfx
        steps.append((x_new, f(x_new)))
        errors.append(abs(x_new - x))
        x = x_new
    raise ValueError("Maximum iterations exceeded. No solution found.")

def secant_method(f, x0, x1, tol=1e-8, max_iter=1000):
    steps = [(x0, f(x0)), (x1, f(x1))]
    errors = []
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tol:
            return x1, errors, steps
        if (fx1 - fx0) == 0:
            raise ValueError("Division by zero encountered.")
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        steps.append((x_new, f(x_new)))
        errors.append(abs(x_new - x1))
        x0, x1 = x1, x_new
    raise ValueError("Maximum iterations exceeded. No solution found.")

def bisection_method(f, a, b, tol=1e-8, max_iter=1000):
    steps = [(a, f(a)), (b, f(b))]
    errors = []
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        steps.append((c, fc))
        errors.append(abs(b - a) / 2)
        if abs(fc) < tol or abs(b - a) < tol:
            return c, errors, steps
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum iterations exceeded. No solution found.")

def false_position_method(f, a, b, tol=1e-8, max_iter=1000):
    steps = [(a, f(a)), (b, f(b))]
    errors = []
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    for i in range(max_iter):
        c = a - (f(a) * (b - a)) / (f(b) - f(a))
        fc = f(c)
        steps.append((c, fc))
        errors.append(abs(b - a) / 2)
        if abs(fc) < tol or abs(b - a) < tol:
            return c, errors, steps
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    raise ValueError("Maximum iterations exceeded. No solution found.")

def generate_animation(steps, f, filename, root):
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    ln, = plt.plot([], [], 'ro')

    x_vals = np.linspace(root - 1, root + 1, 400)
    y_vals = [f(x) for x in x_vals]
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.axhline(0, color='gray', lw=0.5)

    def init():
        ax.set_xlim(root - 1, root + 1)
        ax.set_ylim(min(y_vals), max(y_vals))
        return ln,

    def update(frame):
        x_data.append(frame[0])
        y_data.append(frame[1])
        ln.set_data(x_data, y_data)
        return ln,

    ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=True)
    writer = FFMpegWriter(fps=10)
    ani.save(filename, writer=writer)

def animate_newton_raphson(f, steps, root):
    filename = "newton_raphson.mp4"
    generate_animation(steps, f, filename, root)
    return filename

def animate_secant_method(f, steps, root):
    filename = "secant_method.mp4"
    generate_animation(steps, f, filename, root)
    return filename

def animate_bisection_method(f, steps, root):
    filename = "bisection_method.mp4"
    generate_animation(steps, f, filename, root)
    return filename

def animate_false_position_method(f, steps, root):
    filename = "false_position_method.mp4"
    generate_animation(steps, f, filename, root)
    return filename
