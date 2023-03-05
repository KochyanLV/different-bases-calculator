import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")
        master.configure(bg="#292D3E")
        self.master.resizable(0, 0)
        # Create entry widget
        self.entry = tk.Entry(master, width=30, borderwidth=5, bg="#44475A", fg="white")
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Define buttons
        buttons = [
            "1", "2", "3", "+", "-", "bin",
            "4", "5", "6", "*", "/", "oct",
            "7", "8", "9", "^", "NS", "dec",
            "0", ".", "=", "AC", "del", "hex"
        ]

        # Create buttons and add them to the grid
        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                bg = "#F07178"
                fg = "white"
            elif button in ["AC", "del"]:
                bg = "#4E5C6E"
                fg = "white"
            elif button in ["bin", "dec", "hex", "oct"]:
                bg = "#4E5C6E"
                fg = "white"
            else:
                bg = "#E0E2DB"
                fg = "#292D3E"
            command = lambda x=button: self.handle_click(x)
            tk.Button(master, text=button, width=7, height=3, bg=bg, fg=fg, command=command).grid(row=row, column=col)
            col += 1
            if col > 5:
                row += 1
                col = 0

        # Initialize number system to decimal
        self.number_system = "10"
        self.old_number_system = self.number_system

    # Handle button clicks
    def handle_click(self, value):
        if value == "=":
            try:
                result = self.evaluate(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif value == "AC":
            self.number_system = "10"
            self.old_number_system = self.number_system
            self.entry.delete(0, tk.END)
        elif value == "del":
            self.entry.delete(len(self.entry.get())-1)
        elif value in ["bin", "dec", "hex", "oct"]:
            if value == "bin":
                self.old_number_system = self.number_system
                self.number_system = 2
            if value == "oct":
                self.old_number_system = self.number_system
                self.number_system = 8
            if value == "hex":
                self.old_number_system = self.number_system
                self.number_system = 16
            if value == "dec":
                self.old_number_system = self.number_system
                self.number_system = 10
        elif value == "NS":
            self.old_number_system = self.number_system
            self.new_window = tk.Toplevel(self.master)
            self.new_window.resizable(0, 0)
            self.new_window.grab_set()
            self.entry_2 = tk.Entry(self.new_window, width=15, borderwidth=5, bg="#44475A", fg="white")
            self.entry_2.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
            self.button_2 = "Enter"
            self.command_2 = lambda x=self.button_2: self.handle_click_2(x)
            tk.Button(self.new_window, text=self.button_2, width=7, height=3, bg="#E0E2DB", fg="#292D3E", command=self.command_2).grid(row=1, column=0, columnspan=6)

        else:
            current = self.entry.get()
            if value == "." and "." in current:
                return
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + value)

    def to_base_n(self, num, base):
        digits = '0123456789abcdef'
        num = int(num)
        base = int(base)
        if base > len(digits):
            return None
        result = ''
        if num == 0:
            result = "0"
        while num > 0:
            result = digits[num % base] + result
            num //= base
        return result

    def base_float(self, number_string, base):
        n = number_string.split('.')
        number = int(n[0], base)
        if len(n) > 1 and len(n[1]):
            frac_part = float(int(n[1], base)) / base ** len(n[1])
            if number < 0:
                frac_part = -frac_part
            number += frac_part
        return number

    # Define a function to convert a float to any base
    def float_to_base(self, num, base):
        integer_part = int(num)
        fractional_part = num - integer_part

        integer_part_base = str(self.to_base_n(integer_part, base))

        fractional_part_base = ""
        for i in range(8):
            fractional_part *= base
            digit = int(fractional_part)
            fractional_part_base += str(digit)
            fractional_part -= digit

        if len(fractional_part_base) == 0:
            return integer_part_base
        else:
            return integer_part_base + "." + fractional_part_base

    def handle_click_2(self, value):
        self.number_system = self.entry_2.get()
        self.new_window.destroy()

    # Evaluate expression in the current number system
    def evaluate(self, expression):
        flag = 0
        wrd = ""
        x, y = 0, 0
        for i in ["+", "-", "*", "/", "^"]:
            if i in expression:
                x, y = expression.split(i)
                operand = i
                x = self.base_float(x, int(self.old_number_system))
                y = self.base_float(y, int(self.old_number_system))
                if isinstance(x, float) or isinstance(y, float):
                    flag = 1
                else:
                    flag = 0
                if operand == "^":
                    operand = "**"
                wrd = str(x)+operand+str(y)
        if wrd:
            if flag == 0:
                return self.to_base_n(eval(wrd), self.number_system)
            else:
                return self.float_to_base(eval(wrd), int(self.number_system))
        else:
            if type(int(expression)) is int:
                expression = int(expression, int(self.old_number_system))
                return self.to_base_n(expression, int(self.number_system))
            else:
                expression = self.base_float(str(expression), int(self.old_number_system))
                return self.float_to_base(expression, int(self.number_system))


root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
