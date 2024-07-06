# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# from functions import (
#     create_function_from_string,
#     derivative,
#     newton_raphson,
#     secant_method,
#     bisection_method,
#     false_position_method,
#     animate_newton_raphson,
#     animate_secant_method,
#     animate_bisection_method,
#     animate_false_position_method
# )

# st.title("Root Finding App")

# equation = st.text_input("Enter your equation f(x) = 0 in terms of x. Example: 'x**2 - 4*x + 4'")
# method = st.selectbox("Select the method", ["Newton Raphson", "Bisection Method", "Secant Method", "False Position Method"])

# if equation:
#     f = create_function_from_string(equation)
    
#     if method == "Newton Raphson":
#         x0 = st.number_input("Enter initial guess x0")
#         if st.button("Find Root"):
#             try:
#                 root, errors, steps = newton_raphson(f, lambda x: derivative(f, x), x0)
#                 st.write(f"Root: {root}")
#                 x_vals = np.linspace(root - 10, root + 10, 400)
#                 y_vals = [f(x) for x in x_vals]
#                 fig, ax = plt.subplots()
#                 ax.plot(x_vals, y_vals, label='f(x)')
#                 ax.axhline(0, color='gray', lw=0.5)
#                 ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
#                 st.pyplot(fig)
#                 animation_file = animate_newton_raphson(f, steps, root)
#                 st.video(animation_file)
#             except Exception as e:
#                 st.error(str(e))
    
#     elif method == "Bisection Method":
#         a = st.number_input("Enter interval start a")
#         b = st.number_input("Enter interval end b")
#         if st.button("Find Root"):
#             try:
#                 root, errors, steps = bisection_method(f, a, b)
#                 st.write(f"Root: {root}")
#                 x_vals = np.linspace(a, b, 400)
#                 y_vals = [f(x) for x in x_vals]
#                 fig, ax = plt.subplots()
#                 ax.plot(x_vals, y_vals, label='f(x)')
#                 ax.axhline(0, color='gray', lw=0.5)
#                 ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
#                 st.pyplot(fig)
#                 animation_file = animate_bisection_method(f, steps, root)
#                 st.video(animation_file)
#             except Exception as e:
#                 st.error(str(e))

#     elif method == "Secant Method":
#         x0 = st.number_input("Enter first guess x0")
#         x1 = st.number_input("Enter second guess x1")
#         if st.button("Find Root"):
#             try:
#                 root, errors, steps = secant_method(f, x0, x1)
#                 st.write(f"Root: {root}")
#                 x_vals = np.linspace(min(x0, x1) - 10, max(x0, x1) + 10, 400)
#                 y_vals = [f(x) for x in x_vals]
#                 fig, ax = plt.subplots()
#                 ax.plot(x_vals, y_vals, label='f(x)')
#                 ax.axhline(0, color='gray', lw=0.5)
#                 ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
#                 st.pyplot(fig)
#                 animation_file = animate_secant_method(f, steps, root)
#                 st.video(animation_file)
#             except Exception as e:
#                 st.error(str(e))

#     elif method == "False Position Method":
#         a = st.number_input("Enter interval start a")
#         b = st.number_input("Enter interval end b")
#         if st.button("Find Root"):
#             try:
#                 root, errors, steps = false_position_method(f, a, b)
#                 st.write(f"Root: {root}")
#                 x_vals = np.linspace(a, b, 400)
#                 y_vals = [f(x) for x in x_vals]
#                 fig, ax = plt.subplots()
#                 ax.plot(x_vals, y_vals, label='f(x)')
#                 ax.axhline(0, color='gray', lw=0.5)
#                 ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
#                 st.pyplot(fig)
#                 animation_file = animate_false_position_method(f, steps, root)
#                 st.video(animation_file)
#             except Exception as e:
#                 st.error(str(e))

'''
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from functions import (
    create_function_from_string,
    derivative,
    newton_raphson,
    secant_method,
    bisection_method,
    false_position_method,
    animate_newton_raphson,
    animate_secant_method,
    animate_bisection_method,
    animate_false_position_method
)

st.title("Root Finding App")

equation = st.text_input("Enter your equation f(x) = 0 in terms of x. Example: 'x**2 - 4*x + 4'")
method = st.selectbox("Select the method", ["Newton Raphson", "Bisection Method", "Secant Method", "False Position Method"])

if equation:
    f = create_function_from_string(equation)
    
    if method == "Newton Raphson":
        x0 = st.number_input("Enter initial guess x0")
        if st.button("Find Root"):
            try:
                root, errors, steps = newton_raphson(f, lambda x: derivative(f, x), x0)
                st.write(f"Root: {root}")
                x_vals = np.linspace(root - 10, root + 10, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_newton_raphson(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))
    
    elif method == "Bisection Method":
        a = st.number_input("Enter interval start a")
        b = st.number_input("Enter interval end b")
        if st.button("Find Root"):
            try:
                root, errors, steps = bisection_method(f, a, b)
                st.write(f"Root: {root}")
                x_vals = np.linspace(a, b, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_bisection_method(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))

    elif method == "Secant Method":
        x0 = st.number_input("Enter first guess x0")
        x1 = st.number_input("Enter second guess x1")
        if st.button("Find Root"):
            try:
                root, errors, steps = secant_method(f, x0, x1)
                st.write(f"Root: {root}")
                x_vals = np.linspace(min(x0, x1) - 10, max(x0, x1) + 10, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_secant_method(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))

    elif method == "False Position Method":
        a = st.number_input("Enter interval start a")
        b = st.number_input("Enter interval end b")
        if st.button("Find Root"):
            try:
                root, errors, steps = false_position_method(f, a, b)
                st.write(f"Root: {root}")
                x_vals = np.linspace(a, b, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_false_position_method(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))
'''

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from functions import (
    create_function_from_string,
    derivative,
    newton_raphson,
    secant_method,
    bisection_method,
    false_position_method,
    animate_newton_raphson,
    animate_secant_method,
    animate_bisection_method,
    animate_false_position_method
)

st.title("Root Finding App")

equation = st.text_input("Enter your equation f(x) = 0 in terms of x. Example: 'x**2 - 4*x + 4'")
method = st.selectbox("Select the method", ["Newton Raphson", "Bisection Method", "Secant Method", "False Position Method"])

if equation:
    f = create_function_from_string(equation)
    
    if method == "Newton Raphson":
        x0 = st.number_input("Enter initial guess x0")
        if st.button("Find Root"):
            try:
                root, errors, steps = newton_raphson(f, lambda x: derivative(f, x), x0)
                st.write(f"Root: {root}")
                x_vals = np.linspace(root - 10, root + 10, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_newton_raphson(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))
    
    elif method == "Bisection Method":
        a = st.number_input("Enter interval start a")
        b = st.number_input("Enter interval end b")
        if st.button("Find Root"):
            try:
                root, errors, steps = bisection_method(f, a, b)
                st.write(f"Root: {root}")
                x_vals = np.linspace(a, b, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_bisection_method(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))

    elif method == "Secant Method":
        x0 = st.number_input("Enter first guess x0")
        x1 = st.number_input("Enter second guess x1")
        if st.button("Find Root"):
            try:
                root, errors, steps = secant_method(f, x0, x1)
                st.write(f"Root: {root}")
                x_vals = np.linspace(min(x0, x1) - 10, max(x0, x1) + 10, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_secant_method(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))

    elif method == "False Position Method":
        a = st.number_input("Enter interval start a")
        b = st.number_input("Enter interval end b")
        if st.button("Find Root"):
            try:
                root, errors, steps = false_position_method(f, a, b)
                st.write(f"Root: {root}")
                x_vals = np.linspace(a, b, 400)
                y_vals = [f(x) for x in x_vals]
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label='f(x)')
                ax.axhline(0, color='gray', lw=0.5)
                ax.axvline(root, color='red', linestyle='--', label=f'Root: {root}')
                st.pyplot(fig)
                animation_file = animate_false_position_method(f, steps, root)
                st.video(animation_file)
            except Exception as e:
                st.error(str(e))
