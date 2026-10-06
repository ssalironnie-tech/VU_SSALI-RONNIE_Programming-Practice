# ==========================================
# Topic 1: Conditional Statements & Loops
# ==========================================

# --- Libraries ---
import math

# --- Variables & Conditions ---
score = 85

# Conditional statements (if-else, nested conditions)
if score >= 90:
    grade = 'A'
elif score >= 80:
    if score >= 85:
        grade = 'A-'
    else:
        grade = 'B+'
else:
    grade = 'B'

print(f"Score: {score}, Grade: {grade}")

# --- Loops and Iteration ---
print("\n--- Iterating with For Loop ---")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Square of {num} is {num**2}")

print("\n--- While Loop Iteration ---")
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1