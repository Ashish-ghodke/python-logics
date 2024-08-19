import tkinter as tk
from tkinter import messagebox

def calculate_percentage():
    username = entry_username.get().strip().capitalize()
    partner_name = entry_partner_name.get().strip().capitalize()
    gender = gender_var.get().strip().capitalize()

    if not username or not partner_name:
        messagebox.showerror("Input Error", "Please enter both names.")
        return

    if gender not in ["M", "F"]:
        messagebox.showerror("Input Error", "Please select a valid gender.")
        return

    x = int(ord(username[0]))+ int(ord(username[1]))+int(ord(gender[0]))
    y = int(ord(partner_name[0])) + int(ord(partner_name[1]))+int(ord(gender[0]))
    z = x * y/0.5

    percentage = z % 100
    result_label.config(text=f"Hey {username}, yours and {partner_name}'s love percentage is: {percentage:.2f}%")

# Create main window
root = tk.Tk()
root.title("Love Percentage Calculator")

# Gender
tk.Label(root, text="Enter your gender (M/F):").grid(row=0, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_entry = tk.Entry(root, textvariable=gender_var)
gender_entry.grid(row=0, column=1, padx=10, pady=5)

# User name
tk.Label(root, text="Enter your name:").grid(row=1, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=1, column=1, padx=10, pady=5)

# Partner name
tk.Label(root, text="Enter your partner's name:").grid(row=2, column=0, padx=10, pady=5)
entry_partner_name = tk.Entry(root)
entry_partner_name.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Love Percentage", command=calculate_percentage)
calculate_button.grid(row=3, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()
