import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


class LoopExercisesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Loop Exercises")
        self.root.geometry("700x650")
        self.root.configure(bg='#f0f0f0')

        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create tabs for each exercise
        self.create_exercise1_tab()
        self.create_exercise2_tab()
        self.create_exercise3_tab()
        self.create_exercise4_tab()
        self.create_exercise5_tab()
        self.create_exercise6_tab()
        self.create_exercise7_tab()
        self.create_exercise8_tab()
        self.create_exercise9_tab()
        self.create_exercise10_tab()

    def create_exercise_tab(self, title, exercise_func):
        """Helper function to create tabs"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text=title)
        return tab

    def create_exercise1_tab(self):
        """Exercise 1: Print numbers less than a given number"""
        tab = self.create_exercise_tab("Exercise 1", self.exercise1)

        tk.Label(tab, text="Print numbers less than the entered number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex1_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex1_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Show", command=self.exercise1,
                  font=("Arial", 10), bg='#3498db', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex1_result = scrolledtext.ScrolledText(tab, height=8, width=50,
                                                    font=("Arial", 10))
        self.ex1_result.pack(pady=10, padx=20)

    def exercise1(self):
        try:
            num = int(self.ex1_entry.get())
            result = f"Numbers less than {num}:\n"
            numbers = [str(i) for i in range(num)]
            result += " ".join(numbers)
            self.ex1_result.delete(1.0, tk.END)
            self.ex1_result.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise2_tab(self):
        """Exercise 2: Print divisors of a number"""
        tab = self.create_exercise_tab("Exercise 2", self.exercise2)

        tk.Label(tab, text="Print Divisors of a Number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex2_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex2_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Show", command=self.exercise2,
                  font=("Arial", 10), bg='#2ecc71', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex2_result = scrolledtext.ScrolledText(tab, height=8, width=50,
                                                    font=("Arial", 10))
        self.ex2_result.pack(pady=10, padx=20)

    def exercise2(self):
        try:
            num = int(self.ex2_entry.get())
            result = f"Divisors of {num}:\n"
            divisors = [str(i) for i in range(1, num + 1) if num % i == 0]
            result += " ".join(divisors)
            self.ex2_result.delete(1.0, tk.END)
            self.ex2_result.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise3_tab(self):
        """Exercise 3: Check if a number is prime"""
        tab = self.create_exercise_tab("Exercise 3", self.exercise3)

        tk.Label(tab, text="Check if a Number is Prime",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex3_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex3_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Check", command=self.exercise3,
                  font=("Arial", 10), bg='#e67e22', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex3_result = tk.Label(tab, text="", font=("Arial", 14),
                                   bg='#f0f0f0')
        self.ex3_result.pack(pady=20)

    def exercise3(self):
        try:
            num = int(self.ex3_entry.get())

            if num < 2:
                self.ex3_result.config(text=f"❌ {num} is not prime.", fg='#e74c3c')
                return

            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                self.ex3_result.config(text=f"✅ {num} is a prime number.", fg='#27ae60')
            else:
                self.ex3_result.config(text=f"❌ {num} is not prime.", fg='#e74c3c')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise4_tab(self):
        """Exercise 4: Print even numbers less than a given number"""
        tab = self.create_exercise_tab("Exercise 4", self.exercise4)

        tk.Label(tab, text="Print Even Numbers Less Than Entered Number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex4_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex4_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Show", command=self.exercise4,
                  font=("Arial", 10), bg='#9b59b6', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex4_result = scrolledtext.ScrolledText(tab, height=8, width=50,
                                                    font=("Arial", 10))
        self.ex4_result.pack(pady=10, padx=20)

    def exercise4(self):
        try:
            num = int(self.ex4_entry.get())
            result = f"Even numbers less than {num}:\n"
            numbers = [str(i) for i in range(0, num, 2)]
            result += " ".join(numbers)
            self.ex4_result.delete(1.0, tk.END)
            self.ex4_result.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise5_tab(self):
        """Exercise 5: Print prime numbers less than a given number"""
        tab = self.create_exercise_tab("Exercise 5", self.exercise5)

        tk.Label(tab, text="Print Prime Numbers Less Than Entered Number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex5_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex5_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Show", command=self.exercise5,
                  font=("Arial", 10), bg='#1abc9c', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex5_result = scrolledtext.ScrolledText(tab, height=8, width=50,
                                                    font=("Arial", 10))
        self.ex5_result.pack(pady=10, padx=20)

    def exercise5(self):
        try:
            num = int(self.ex5_entry.get())
            result = f"Prime numbers less than {num}:\n"
            primes = []
            for n in range(2, num):
                is_prime = True
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(str(n))
            result += " ".join(primes)
            self.ex5_result.delete(1.0, tk.END)
            self.ex5_result.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise6_tab(self):
        """Exercise 6: Print two-digit even numbers less than a given number"""
        tab = self.create_exercise_tab("Exercise 6", self.exercise6)

        tk.Label(tab, text="Print Two-Digit Even Numbers Less Than Entered Number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex6_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex6_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Show", command=self.exercise6,
                  font=("Arial", 10), bg='#e74c3c', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex6_result = scrolledtext.ScrolledText(tab, height=8, width=50,
                                                    font=("Arial", 10))
        self.ex6_result.pack(pady=10, padx=20)

    def exercise6(self):
        try:
            num = int(self.ex6_entry.get())
            result = f"Two-digit even numbers less than {num}:\n"
            numbers = [str(i) for i in range(10, min(num, 100)) if i % 2 == 0]
            result += " ".join(numbers)
            self.ex6_result.delete(1.0, tk.END)
            self.ex6_result.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise7_tab(self):
        """Exercise 7: Print common divisors of two numbers"""
        tab = self.create_exercise_tab("Exercise 7", self.exercise7)

        tk.Label(tab, text="Print Common Divisors of Two Numbers",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="First Number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)
        self.ex7_entry1 = tk.Entry(input_frame, width=15, font=("Arial", 11))
        self.ex7_entry1.pack(side=tk.RIGHT, padx=5)

        tk.Label(input_frame, text="Second Number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)
        self.ex7_entry2 = tk.Entry(input_frame, width=15, font=("Arial", 11))
        self.ex7_entry2.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Show", command=self.exercise7,
                  font=("Arial", 10), bg='#f39c12', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex7_result = scrolledtext.ScrolledText(tab, height=8, width=50,
                                                    font=("Arial", 10))
        self.ex7_result.pack(pady=10, padx=20)

    def exercise7(self):
        try:
            num1 = int(self.ex7_entry1.get())
            num2 = int(self.ex7_entry2.get())

            limit = min(num1, num2)
            result = f"Common divisors of {num1} and {num2}:\n"
            divisors = [str(i) for i in range(1, limit + 1)
                        if num1 % i == 0 and num2 % i == 0]

            if not divisors:
                result += "No common divisors found!"
            else:
                result += " ".join(divisors)

            self.ex7_result.delete(1.0, tk.END)
            self.ex7_result.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers!")

    def create_exercise8_tab(self):
        """Exercise 8: Print even or odd numbers between two numbers"""
        tab = self.create_exercise_tab("Exercise 8", self.exercise8)

        tk.Label(tab, text="Print Even or Odd Numbers Between Two Numbers",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="First Number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)
        self.ex8_entry1 = tk.Entry(input_frame, width=15, font=("Arial", 11))
        self.ex8_entry1.pack(side=tk.RIGHT, padx=5)

        tk.Label(input_frame, text="Second Number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)
        self.ex8_entry2 = tk.Entry(input_frame, width=15, font=("Arial", 11))
        self.ex8_entry2.pack(side=tk.RIGHT, padx=5)

        # Select even or odd
        select_frame = tk.Frame(tab, bg='#f0f0f0')
        select_frame.pack(pady=10)

        self.ex8_var = tk.StringVar(value="Even")
        tk.Radiobutton(select_frame, text="Even", variable=self.ex8_var,
                       value="Even", bg='#f0f0f0', font=("Arial", 10)).pack(side=tk.RIGHT, padx=10)
        tk.Radiobutton(select_frame, text="Odd", variable=self.ex8_var,
                       value="Odd", bg='#f0f0f0', font=("Arial", 10)).pack(side=tk.RIGHT, padx=10)

        tk.Button(tab, text="Show", command=self.exercise8,
                  font=("Arial", 10), bg='#2980b9', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex8_result = scrolledtext.ScrolledText(tab, height=8, width=50,
                                                    font=("Arial", 10))
        self.ex8_result.pack(pady=10, padx=20)

    def exercise8(self):
        try:
            num1 = int(self.ex8_entry1.get())
            num2 = int(self.ex8_entry2.get())

            if num1 > num2:
                num1, num2 = num2, num1

            choice = self.ex8_var.get()
            result = f"{choice} numbers between {num1} and {num2}:\n"

            if choice == "Even":
                numbers = [str(i) for i in range(num1, num2 + 1) if i % 2 == 0]
            else:
                numbers = [str(i) for i in range(num1, num2 + 1) if i % 2 != 0]

            result += " ".join(numbers)
            self.ex8_result.delete(1.0, tk.END)
            self.ex8_result.insert(tk.END, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers!")

    def create_exercise9_tab(self):
        """Exercise 9: Input numbers and calculate largest, sum, and average"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 9")

        tk.Label(tab, text="Input Numbers and Calculate Largest, Sum, and Average",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        tk.Label(tab, text="(Enter 0 or 01 to finish)",
                 font=("Arial", 10), bg='#f0f0f0', fg='#7f8c8d').pack()

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex9_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex9_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(input_frame, text="Add", command=self.exercise9_add,
                  font=("Arial", 10), bg='#27ae60', fg='white',
                  padx=15, pady=5).pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Calculate", command=self.exercise9_calculate,
                  font=("Arial", 10), bg='#e67e22', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex9_numbers = []
        self.ex9_result = scrolledtext.ScrolledText(tab, height=10, width=55,
                                                    font=("Arial", 10))
        self.ex9_result.pack(pady=10, padx=20)

    def exercise9_add(self):
        try:
            num = float(self.ex9_entry.get())
            if num == 0 or num == 1:  # Stop condition
                messagebox.showinfo("Info", "Enter 0 or 01 to finish!")
                return
            self.ex9_numbers.append(num)
            self.ex9_entry.delete(0, tk.END)
            self.ex9_result.delete(1.0, tk.END)
            self.ex9_result.insert(tk.END, f"Numbers entered:\n{self.ex9_numbers}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def exercise9_calculate(self):
        if not self.ex9_numbers:
            messagebox.showwarning("Warning", "No numbers have been entered!")
            return

        total = sum(self.ex9_numbers)
        largest = max(self.ex9_numbers)
        average = total / len(self.ex9_numbers)

        result = f"📊 Results:\n"
        result += f"Count: {len(self.ex9_numbers)}\n"
        result += f"Sum: {total}\n"
        result += f"Largest: {largest}\n"
        result += f"Average: {average:.2f}\n"
        result += f"Numbers: {self.ex9_numbers}"

        self.ex9_result.delete(1.0, tk.END)
        self.ex9_result.insert(tk.END, result)

    def create_exercise10_tab(self):
        """Exercise 10: Convert between decimal and binary"""
        tab = self.create_exercise_tab("Exercise 10", self.exercise10)

        tk.Label(tab, text="Convert Between Decimal and Binary",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        # Select conversion type
        select_frame = tk.Frame(tab, bg='#f0f0f0')
        select_frame.pack(pady=10)

        self.ex10_var = tk.StringVar(value="Decimal to Binary")
        tk.Radiobutton(select_frame, text="Decimal to Binary",
                       variable=self.ex10_var, value="Decimal to Binary",
                       bg='#f0f0f0', font=("Arial", 10)).pack(side=tk.RIGHT, padx=10)
        tk.Radiobutton(select_frame, text="Binary to Decimal",
                       variable=self.ex10_var, value="Binary to Decimal",
                       bg='#f0f0f0', font=("Arial", 10)).pack(side=tk.RIGHT, padx=10)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex10_entry = tk.Entry(input_frame, width=25, font=("Arial", 11))
        self.ex10_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Convert", command=self.exercise10,
                  font=("Arial", 10), bg='#8e44ad', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex10_result = scrolledtext.ScrolledText(tab, height=8, width=55,
                                                     font=("Arial", 10))
        self.ex10_result.pack(pady=10, padx=20)

    def exercise10(self):
        choice = self.ex10_var.get()
        value = self.ex10_entry.get().strip()

        if not value:
            messagebox.showerror("Error", "Please enter a number!")
            return

        try:
            if choice == "Decimal to Binary":
                decimal = int(value)
                if decimal < 0:
                    messagebox.showerror("Error", "Please enter a positive number!")
                    return

                # Method 1: Using built-in function
                binary1 = bin(decimal)[2:]

                # Method 2: Manual algorithm
                binary2 = ""
                temp = decimal
                if temp == 0:
                    binary2 = "0"
                else:
                    while temp > 0:
                        binary2 = str(temp % 2) + binary2
                        temp //= 2

                result = f"Decimal number {decimal}:\n"
                result += f"Binary (built-in): {binary1}\n"
                result += f"Binary (algorithm): {binary2}"

            else:  # Binary to Decimal
                binary = value
                if not all(c in '01' for c in binary):
                    messagebox.showerror("Error", "Please enter a valid binary number (only 0s and 1s)!")
                    return

                # Method 1: Using built-in function
                decimal1 = int(binary, 2)

                # Method 2: Manual algorithm
                decimal2 = 0
                for i, digit in enumerate(reversed(binary)):
                    if digit == '1':
                        decimal2 += 2 ** i

                result = f"Binary number {binary}:\n"
                result += f"Decimal (built-in): {decimal1}\n"
                result += f"Decimal (algorithm): {decimal2}"

            self.ex10_result.delete(1.0, tk.END)
            self.ex10_result.insert(tk.END, result)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = LoopExercisesApp(root)
    root.mainloop()