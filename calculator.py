import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    entry.delete(0, tk.END)

    if button_value == "=":
        try:
            result = eval(current_text)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, current_text + str(button_value))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20,
              command=lambda btn=button: on_click(btn)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()
