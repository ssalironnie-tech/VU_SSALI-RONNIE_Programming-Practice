# ==========================================
# Topic 2: Functions, Recursion & Lambdas
# ==========================================

# --- Modular Functions ---
def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle."""
    return length * width

# --- Recursion ---
def factorial(n: int) -> int:
    """Computes factorial recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# --- Lambda Functions ---
square_lambda = lambda x: x ** 2
add_lambda = lambda a, b: a + b

# --- Execution ---
if __name__ == "__main__":
    print(f"Rectangle Area (5x4): {calculate_area(5, 4)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Lambda Square of 6: {square_lambda(6)}")
    print(f"Lambda Addition (3+7): {add_lambda(3, 7)}")