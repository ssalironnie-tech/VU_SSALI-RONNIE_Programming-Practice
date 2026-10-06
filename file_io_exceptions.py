# ==========================================
# Topic 4: File I/O Operations & Exception Handling
# ==========================================

filename = "sample_output.txt"

# --- File Writing ---
try:
    with open(filename, "w") as file:
        file.write("Python for Data Science - Practice Log\n")
        file.write("File I/O operations and Exception handling completed successfully.\n")
    print(f"Successfully written to {filename}")
except IOError as e:
    print(f"Error writing to file: {e}")

# --- File Reading & Exception Handling ---
try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation process finished.")