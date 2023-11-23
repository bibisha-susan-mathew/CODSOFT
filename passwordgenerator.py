import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        password_display.config(state=tk.NORMAL)
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Password Length Label and Entry
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Complexity Label and Dropdown
complexity_label = tk.Label(root, text="Password Complexity:")
complexity_label.grid(row=1, column=0, padx=10, pady=10)
complexity_options = ["Low", "Medium", "High"]
complexity_var = tk.StringVar(root)
complexity_dropdown = tk.OptionMenu(root, complexity_var, *complexity_options)
complexity_var.set("Medium")
complexity_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Display Password Textbox
password_display = tk.Text(root, height=1, width=30, state=tk.DISABLED)
password_display.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()