import tkinter as tk

m_to_inch = 39.37
inch_to_m = 0.0254
feet_to_m = 0.3048
m_to_feet = 3.28084
inch_to_feet = 0.0833333
feet_to_inch = 12

root = tk.Tk()
root.title("Units Converter")
root.geometry("450x300")
root.config(bg="#dfe6e9")
root.resizable(0, 0)
text_color = "#2d3436"

def meters_to_inches():
    result.set(float(eval(entry1.get())) * m_to_inch)

def inches_to_meters():
    result.set(float(eval(entry1.get())) * inch_to_m)

def feet_to_meters():
    result.set(float(eval(entry1.get())) * feet_to_m)

def meters_to_feet():
    result.set(float(eval(entry1.get())) * m_to_feet)

def inches_to_feet():
    result.set(float(eval(entry1.get())) * inch_to_feet)

def feet_to_inches():
    result.set(float(eval(entry1.get())) * feet_to_inch)

label1 = tk.Label(root, text="Enter value:", font=("Arial", 16), bg=root["bg"], fg=text_color)
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root, font=("Arial", 16))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Result:", font=("Arial", 16), bg=root["bg"], fg=text_color)
label2.grid(row=1, column=0, padx=10, pady=10)

result = tk.DoubleVar()
result.set(0.0)

result_entry = tk.Entry(root, textvariable=result, state="readonly", font=("Arial", 16))
result_entry.grid(row=1, column=1, padx=10, pady=10)

# Define the buttons for the conversion operations
m_to_inch_button = tk.Button(root, text="Meters to Inches", command=meters_to_inches,
                             font=("Arial", 14), bg="#74b9ff", fg=text_color)
m_to_inch_button.grid(row=2, column=0, padx=10, pady=10)

inch_to_m_button = tk.Button(root, text="Inches to Meters", command=inches_to_meters,
                             font=("Arial", 14), bg="#74b9ff", fg=text_color)
inch_to_m_button.grid(row=2, column=1, padx=10, pady=10)

feet_to_m_button = tk.Button(root, text="Feet to Meters", command=feet_to_meters,
                             font=("Arial", 14), bg="#74b9ff", fg=text_color)
feet_to_m_button.grid(row=3, column=0, padx=10, pady=10)

m_to_feet_button = tk.Button(root, text="Meters to Feet", command=meters_to_feet,
                             font=("Arial", 14), bg="#74b9ff", fg=text_color)
m_to_feet_button.grid(row=3, column=1, padx=10, pady=10)

inch_to_feet_button = tk.Button(root, text="Inches to Feet", command=inches_to_feet,
                                font=("Arial", 14), bg="#74b9ff", fg=text_color)
inch_to_feet_button.grid(row=4, column=0, padx=10, pady=10)

feet_to_inch_button = tk.Button(root, text="Feet to Inches", command=feet_to_inches,
                                font=("Arial", 14), bg="#74b9ff", fg=text_color)
feet_to_inch_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
