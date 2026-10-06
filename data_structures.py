# ==========================================
# Topic 3: Lists, Tuples, Sets, and Dictionaries
# ==========================================

# --- 1. Lists ---
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("List:", fruits)

# --- 2. Tuples ---
coordinates = (10.0, 20.0, 30.0)
print("Tuple:", coordinates)

# --- 3. Sets ---
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print("Set (Unique Values):", unique_numbers)

# --- 4. Dictionaries ---
student_profile = {
    "name": "SSALI Ronnie",
    "course": "Python for Data Science",
    "score": 92
}
student_profile["grade"] = "A"
print("Dictionary:")
for key, value in student_profile.items():
    print(f"  {key}: {value}")