import tkinter as tk
from tkinter import ttk, messagebox, StringVar, IntVar, DoubleVar


class ConditionalExercisesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conditional Statements Exercises")
        self.root.geometry("650x600")
        self.root.configure(bg='#f0f0f0')

        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create each exercise in a separate tab
        self.create_exercise1_tab()
        self.create_exercise2_tab()
        self.create_exercise3_tab()
        self.create_exercise4_tab()
        self.create_exercise5_tab()
        self.create_exercise6_tab()
        self.create_exercise7_tab()

    def create_exercise1_tab(self):
        """Exercise 1: Identify if a number is positive or negative"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 1")

        tk.Label(tab, text="Identify Positive or Negative Number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex1_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex1_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Check", command=self.exercise1,
                  font=("Arial", 10), bg='#3498db', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex1_result = tk.Label(tab, text="", font=("Arial", 12),
                                   bg='#f0f0f0', fg='#2c3e50')
        self.ex1_result.pack(pady=20)

    def exercise1(self):
        try:
            num = float(self.ex1_entry.get())
            if num > 0:
                result = f"✅ {num} is a positive number."
            elif num < 0:
                result = f"✅ {num} is a negative number."
            else:
                result = "✅ The number is zero (neither positive nor negative)."
            self.ex1_result.config(text=result, fg='#2c3e50')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def create_exercise2_tab(self):
        """Exercise 2: Identify if a number is zero, negative, or positive"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 2")

        tk.Label(tab, text="Identify Zero, Negative, or Positive",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex2_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex2_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Check", command=self.exercise2,
                  font=("Arial", 10), bg='#2ecc71', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex2_result = tk.Label(tab, text="", font=("Arial", 12),
                                   bg='#f0f0f0', fg='#2c3e50')
        self.ex2_result.pack(pady=20)

    def exercise2(self):
        try:
            num = float(self.ex2_entry.get())
            if num > 0:
                result = f"✅ {num} is positive."
            elif num < 0:
                result = f"✅ {num} is negative."
            else:
                result = "✅ The number is zero."
            self.ex2_result.config(text=result, fg='#2c3e50')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def create_exercise3_tab(self):
        """Exercise 3: Check if a number is even or odd"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 3")

        tk.Label(tab, text="Check Even or Odd Number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter an integer:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex3_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex3_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Check", command=self.exercise3,
                  font=("Arial", 10), bg='#e67e22', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex3_result = tk.Label(tab, text="", font=("Arial", 12),
                                   bg='#f0f0f0', fg='#2c3e50')
        self.ex3_result.pack(pady=20)

    def exercise3(self):
        try:
            num = int(self.ex3_entry.get())
            if num % 2 == 0:
                result = f"✅ {num} is even."
            else:
                result = f"✅ {num} is odd."
            self.ex3_result.config(text=result, fg='#2c3e50')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise4_tab(self):
        """Exercise 4: Find the largest and smallest number among three"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 4")

        tk.Label(tab, text="Find Largest and Smallest Number",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        # Input for three numbers
        nums = []
        for i in range(3):
            row_frame = tk.Frame(input_frame, bg='#f0f0f0')
            row_frame.pack(pady=5)

            tk.Label(row_frame, text=f"Number {i + 1}:",
                     font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

            entry = tk.Entry(row_frame, width=15, font=("Arial", 11))
            entry.pack(side=tk.RIGHT, padx=5)
            nums.append(entry)

        self.ex4_entries = nums

        tk.Button(tab, text="Find", command=self.exercise4,
                  font=("Arial", 10), bg='#9b59b6', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex4_result = tk.Label(tab, text="", font=("Arial", 11),
                                   bg='#f0f0f0', fg='#2c3e50', justify=tk.LEFT)
        self.ex4_result.pack(pady=20)

    def exercise4(self):
        try:
            nums = [float(entry.get()) for entry in self.ex4_entries]

            # Find the largest
            if nums[0] >= nums[1] and nums[0] >= nums[2]:
                largest = nums[0]
            elif nums[1] >= nums[0] and nums[1] >= nums[2]:
                largest = nums[1]
            else:
                largest = nums[2]

            # Find the smallest
            if nums[0] <= nums[1] and nums[0] <= nums[2]:
                smallest = nums[0]
            elif nums[1] <= nums[0] and nums[1] <= nums[2]:
                smallest = nums[1]
            else:
                smallest = nums[2]

            nums.sort()
            result = f"Largest: {largest}\nSmallest: {smallest}\nSorted: {nums[0]} < {nums[1]} < {nums[2]}"
            self.ex4_result.config(text=result, fg='#2c3e50')

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

    def create_exercise5_tab(self):
        """Exercise 5: Identify the day of the week based on a number"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 5")

        tk.Label(tab, text="Identify Day of the Week (1-7)",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter a number (1-7):",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex5_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex5_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Check", command=self.exercise5,
                  font=("Arial", 10), bg='#1abc9c', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex5_result = tk.Label(tab, text="", font=("Arial", 12),
                                   bg='#f0f0f0', fg='#2c3e50')
        self.ex5_result.pack(pady=20)

    def exercise5(self):
        try:
            num = int(self.ex5_entry.get())

            if num == 1:
                day = "Saturday"
            elif num == 2:
                day = "Sunday"
            elif num == 3:
                day = "Monday"
            elif num == 4:
                day = "Tuesday"
            elif num == 5:
                day = "Wednesday"
            elif num == 6:
                day = "Thursday"
            elif num == 7:
                day = "Friday"
            else:
                self.ex5_result.config(text="❌ Number must be between 1 and 7!", fg='#e74c3c')
                return

            self.ex5_result.config(text=f"✅ Number {num} corresponds to {day}.", fg='#2c3e50')

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")

    def create_exercise6_tab(self):
        """Exercise 6: Identify the day number from the day name"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 6")

        tk.Label(tab, text="Find Day Number from Day Name",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter the day name:",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex6_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex6_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Check", command=self.exercise6,
                  font=("Arial", 10), bg='#e74c3c', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex6_result = tk.Label(tab, text="", font=("Arial", 12),
                                   bg='#f0f0f0', fg='#2c3e50')
        self.ex6_result.pack(pady=20)

    def exercise6(self):
        day_name = self.ex6_entry.get().strip().lower()
        day_name = day_name.capitalize()

        if day_name in ["Saturday", "saturday"]:
            day_number = 1
        elif day_name in ["Sunday", "sunday"]:
            day_number = 2
        elif day_name in ["Monday", "monday"]:
            day_number = 3
        elif day_name in ["Tuesday", "tuesday"]:
            day_number = 4
        elif day_name in ["Wednesday", "wednesday"]:
            day_number = 5
        elif day_name in ["Thursday", "thursday"]:
            day_number = 6
        elif day_name in ["Friday", "friday"]:
            day_number = 7
        else:
            self.ex6_result.config(text="❌ Invalid day name entered!", fg='#e74c3c')
            return

        self.ex6_result.config(text=f"✅ {day_name} is day number {day_number} of the week.", fg='#2c3e50')

    def create_exercise7_tab(self):
        """Exercise 7: Determine student's grade based on score"""
        tab = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(tab, text="Exercise 7")

        tk.Label(tab, text="Determine Student Grade Based on Score",
                 font=("Arial", 14, "bold"), bg='#f0f0f0', fg='#2c3e50').pack(pady=15)

        input_frame = tk.Frame(tab, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter score (0-20):",
                 font=("Arial", 11), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.ex7_entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.ex7_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(tab, text="Check", command=self.exercise7,
                  font=("Arial", 10), bg='#f39c12', fg='white',
                  padx=20, pady=8).pack(pady=10)

        self.ex7_result = tk.Label(tab, text="", font=("Arial", 12),
                                   bg='#f0f0f0', fg='#2c3e50', justify=tk.LEFT)
        self.ex7_result.pack(pady=20)

    def exercise7(self):
        try:
            score = float(self.ex7_entry.get())

            if 0 <= score <= 20:
                if score >= 18:
                    grade = "A (Excellent)"
                    emoji = "🌟🌟🌟"
                    message = "Outstanding performance! Congratulations!"
                elif score >= 16:
                    grade = "B (Good)"
                    emoji = "🌟🌟"
                    message = "Good performance, keep it up!"
                elif score >= 14:
                    grade = "C (Average)"
                    emoji = "🌟"
                    message = "Acceptable performance, you can do better!"
                elif score >= 12:
                    grade = "D (Below Average)"
                    emoji = "⚠️"
                    message = "You need to put in more effort!"
                elif score >= 10:
                    grade = "E (Weak)"
                    emoji = "⚠️"
                    message = "You need serious studying!"
                else:
                    grade = "F (Fail)"
                    emoji = "❌"
                    message = "You need to work very hard!"

                result = f"📊 Score: {score}\n"
                result += f"📈 Grade: {grade}\n"
                result += f"{emoji} {message}"

                self.ex7_result.config(text=result, fg='#2c3e50')
            else:
                self.ex7_result.config(text="❌ Score must be between 0 and 20!", fg='#e74c3c')

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ConditionalExercisesApp(root)
    root.mainloop()