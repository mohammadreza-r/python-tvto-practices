import tkinter as tk
from tkinter import ttk, messagebox


class ClassManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Class and Student Management System")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')

        # Dictionary to store students for each class
        self.classes = {
            "Math": set(),
            "Physics": set(),
            "Chemistry": set()
        }

        # Create UI widgets
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title = tk.Label(self.root, text="Class Management System",
                         font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        # Frame for class input
        class_frame = tk.Frame(self.root, bg='#f0f0f0')
        class_frame.pack(pady=5)

        tk.Label(class_frame, text="Class Name:", font=("Arial", 11),
                 bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.class_entry = tk.Entry(class_frame, width=20, font=("Arial", 11))
        self.class_entry.pack(side=tk.RIGHT, padx=5)

        tk.Button(class_frame, text="Add Class", command=self.add_class,
                  font=("Arial", 10), bg='#3498db', fg='white',
                  padx=10, pady=5).pack(side=tk.RIGHT, padx=5)

        # Frame for student input
        student_frame = tk.Frame(self.root, bg='#f0f0f0')
        student_frame.pack(pady=5)

        tk.Label(student_frame, text="Student Name:", font=("Arial", 11),
                 bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.student_entry = tk.Entry(student_frame, width=20, font=("Arial", 11))
        self.student_entry.pack(side=tk.RIGHT, padx=5)

        # Dropdown to select class for adding student
        tk.Label(student_frame, text="In Class:", font=("Arial", 11),
                 bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.class_var = tk.StringVar()
        self.class_combo = ttk.Combobox(student_frame, textvariable=self.class_var,
                                        values=list(self.classes.keys()), width=12)
        self.class_combo.pack(side=tk.RIGHT, padx=5)

        tk.Button(student_frame, text="Add Student", command=self.add_student,
                  font=("Arial", 10), bg='#2ecc71', fg='white',
                  padx=10, pady=5).pack(side=tk.RIGHT, padx=5)

        # Button to show students enrolled in multiple classes
        tk.Button(self.root, text="Show Students in Multiple Classes",
                  command=self.show_common_students,
                  font=("Arial", 11), bg='#e67e22', fg='white',
                  padx=15, pady=8).pack(pady=10)

        # Text widget to display results
        self.result_text = tk.Text(self.root, height=12, width=55,
                                   font=("Arial", 10), bg='white',
                                   wrap=tk.WORD)
        self.result_text.pack(pady=10)

        # Scrollbar for the text widget
        scrollbar = tk.Scrollbar(self.root, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)

        # Display existing classes
        self.update_display()

    def add_class(self):
        """Add a new class to the system"""
        class_name = self.class_entry.get().strip()
        if class_name:
            if class_name in self.classes:
                messagebox.showwarning("Duplicate", "This class already exists!")
            else:
                self.classes[class_name] = set()
                self.class_combo['values'] = list(self.classes.keys())
                self.class_entry.delete(0, tk.END)
                messagebox.showinfo("Success", f"Class '{class_name}' created!")
                self.update_display()
        else:
            messagebox.showerror("Error", "Please enter a class name!")

    def add_student(self):
        """Add a student to a selected class"""
        student_name = self.student_entry.get().strip()
        class_name = self.class_var.get()

        if not student_name:
            messagebox.showerror("Error", "Please enter a student name!")
            return

        if not class_name:
            messagebox.showerror("Error", "Please select a class!")
            return

        if class_name not in self.classes:
            messagebox.showerror("Error", "The selected class doesn't exist!")
            return

        self.classes[class_name].add(student_name)
        self.student_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Student '{student_name}' added to '{class_name}'!")
        self.update_display()

    def show_common_students(self):
        """Find and display students who are in two or more classes"""
        # Track which classes each student is enrolled in
        all_students = {}
        for class_name, students in self.classes.items():
            for student in students:
                if student in all_students:
                    all_students[student].append(class_name)
                else:
                    all_students[student] = [class_name]

        # Filter students who are in more than one class
        common_students = {name: classes for name, classes in all_students.items()
                           if len(classes) >= 2}

        self.result_text.delete(1.0, tk.END)

        if common_students:
            self.result_text.insert(tk.END, "Students enrolled in two or more classes:\n\n")
            for student, classes in common_students.items():
                self.result_text.insert(tk.END, f"• {student}: {', '.join(classes)}\n")
        else:
            self.result_text.insert(tk.END, "No students are enrolled in multiple classes!")

    def update_display(self):
        """Update the display with current class and student information"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Class and Student List:\n\n")
        for class_name, students in self.classes.items():
            self.result_text.insert(tk.END, f"🔹 Class {class_name}:\n")
            if students:
                for student in sorted(students):
                    self.result_text.insert(tk.END, f"   • {student}\n")
            else:
                self.result_text.insert(tk.END, "   (No students)\n")
            self.result_text.insert(tk.END, "\n")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ClassManagementApp(root)
    root.mainloop()