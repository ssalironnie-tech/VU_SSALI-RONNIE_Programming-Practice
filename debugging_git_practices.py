# ==========================================
# Topic 9: Debugging & Best Practices
# ==========================================

import logging

# Set up logging for professional debugging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def safe_divide(a: float, b: float) -> float:
    """Demonstrates error handling, debugging, and clean coding practices."""
    logging.info(f"Attempting division: {a} / {b}")
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        logging.error("Division by zero encountered!")
        return float('nan')

if __name__ == "__main__":
    print("Result 1 (10 / 2):", safe_divide(10, 2))
    print("Result 2 (10 / 0):", safe_divide(10, 0))