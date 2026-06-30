import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from tkinter import Label, Entry, Button, Frame, StringVar


class DatabaseManager:
    """Manage database connection and operations"""

    def __init__(self, db_name="test.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_table()

    def connect(self):
        """Connect to the database"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return False

    def create_table(self):
        """Create cities table if it doesn't exist"""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS cities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    population INTEGER,
                    men INTEGER,
                    women INTEGER
                )
            ''')
            self.connection.commit()

            # Add sample data
            sample_cities = [
                ("Tehran", 8690000, 4350000, 4340000),
                ("Mashhad", 3200000, 1600000, 1600000),
                ("Isfahan", 2200000, 1100000, 1100000),
                ("Shiraz", 1900000, 950000, 950000),
                ("Tabriz", 1600000, 800000, 800000)
            ]

            for city in sample_cities:
                try:
                    self.cursor.execute('''
                        INSERT OR IGNORE INTO cities (name, population, men, women)
                        VALUES (?, ?, ?, ?)
                    ''', city)
                except:
                    pass

            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            return False

    def get_all_cities(self):
        """Get list of all cities"""
        try:
            self.cursor.execute("SELECT id, name, population, men, women FROM cities ORDER BY name")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving cities: {e}")
            return []

    def get_city_by_name(self, name):
        """Get city information by name"""
        try:
            self.cursor.execute("SELECT * FROM cities WHERE name = ?", (name,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error searching for city: {e}")
            return None

    def add_city(self, name, population, men, women):
        """Add a new city"""
        try:
            self.cursor.execute('''
                INSERT INTO cities (name, population, men, women)
                VALUES (?, ?, ?, ?)
            ''', (name, population, men, women))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", f"City '{name}' already exists in the database!")
            return False
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error adding city: {e}")
            return False

    def search_city(self, name):
        """Search for a city in the database"""
        return self.get_city_by_name(name)

    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()


class AddCityWindow:
    """Form for adding a new city"""

    def __init__(self, parent, db_manager, callback):
        self.parent = parent
        self.db_manager = db_manager
        self.callback = callback

        self.window = Toplevel(parent)
        self.window.title("Add New City")
        self.window.geometry("400x350")
        self.window.configure(bg='#f0f0f0')
        self.window.resizable(False, False)

        # Center the window
        self.center_window()

        self.create_widgets()

    def center_window(self):
        """Center the window on screen"""
        self.window.update_idletasks()
        width = 400
        height = 350
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        # Title
        title = Label(self.window, text="Add New City",
                      font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=15)

        # Main frame
        main_frame = Frame(self.window, bg='#f0f0f0')
        main_frame.pack(pady=10)

        # City name
        Label(main_frame, text="City Name:", font=("Arial", 11),
              bg='#f0f0f0').grid(row=0, column=0, pady=8, padx=10, sticky='e')

        self.name_entry = Entry(main_frame, width=20, font=("Arial", 11))
        self.name_entry.grid(row=0, column=1, pady=8, padx=10)

        # Population
        Label(main_frame, text="Population:", font=("Arial", 11),
              bg='#f0f0f0').grid(row=1, column=0, pady=8, padx=10, sticky='e')

        self.population_entry = Entry(main_frame, width=20, font=("Arial", 11))
        self.population_entry.grid(row=1, column=1, pady=8, padx=10)

        # Number of men
        Label(main_frame, text="Number of Men:", font=("Arial", 11),
              bg='#f0f0f0').grid(row=2, column=0, pady=8, padx=10, sticky='e')

        self.men_entry = Entry(main_frame, width=20, font=("Arial", 11))
        self.men_entry.grid(row=2, column=1, pady=8, padx=10)

        # Number of women
        Label(main_frame, text="Number of Women:", font=("Arial", 11),
              bg='#f0f0f0').grid(row=3, column=0, pady=8, padx=10, sticky='e')

        self.women_entry = Entry(main_frame, width=20, font=("Arial", 11))
        self.women_entry.grid(row=3, column=1, pady=8, padx=10)

        # Buttons
        button_frame = Frame(self.window, bg='#f0f0f0')
        button_frame.pack(pady=20)

        Button(button_frame, text="Save City", command=self.save_city,
               font=("Arial", 10), bg='#2ecc71', fg='white',
               padx=20, pady=8).pack(side=tk.RIGHT, padx=10)

        Button(button_frame, text="Cancel", command=self.window.destroy,
               font=("Arial", 10), bg='#e74c3c', fg='white',
               padx=20, pady=8).pack(side=tk.RIGHT, padx=10)

    def save_city(self):
        """Save the new city to the database"""
        name = self.name_entry.get().strip()
        population = self.population_entry.get().strip()
        men = self.men_entry.get().strip()
        women = self.women_entry.get().strip()

        # Validate input
        if not name:
            messagebox.showerror("Error", "Please enter a city name!")
            return

        if not population:
            messagebox.showerror("Error", "Please enter the population!")
            return

        if not men:
            messagebox.showerror("Error", "Please enter the number of men!")
            return

        if not women:
            messagebox.showerror("Error", "Please enter the number of women!")
            return

        try:
            population = int(population)
            men = int(men)
            women = int(women)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return

        if population != men + women:
            messagebox.showwarning("Warning",
                                   "The sum of men and women does not match the total population!\n"
                                   "Do you want to continue?")

        # Save to database
        if self.db_manager.add_city(name, population, men, women):
            messagebox.showinfo("Success", f"City '{name}' was successfully added!")
            self.window.destroy()
            if self.callback:
                self.callback()


class MainApplication:
    """Main application for city management"""

    def __init__(self, root):
        self.root = root
        self.root.title("City Information Management System")
        self.root.geometry("550x480")
        self.root.configure(bg='#f0f0f0')

        # Connect to database
        self.db_manager = DatabaseManager()

        # Check database connection
        if self.db_manager.connection:
            self.show_connection_status(True)
        else:
            self.show_connection_status(False)

        # Create widgets
        self.create_widgets()

        # Load cities
        self.load_cities()

    def show_connection_status(self, is_connected):
        """Display database connection status"""
        status_frame = Frame(self.root, bg='#f0f0f0')
        status_frame.pack(fill=tk.X, padx=10, pady=5)

        status_text = "✅ Connected to database" if is_connected else "❌ Not connected to database"
        status_color = '#27ae60' if is_connected else '#e74c3c'

        Label(status_frame, text=status_text, font=("Arial", 10),
              bg='#f0f0f0', fg=status_color).pack()

    def create_widgets(self):
        """Create form widgets"""

        # Main title
        title = Label(self.root, text="City Information Management System",
                      font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        # Frame for city selection
        select_frame = Frame(self.root, bg='#f0f0f0')
        select_frame.pack(pady=10, padx=20, fill=tk.X)

        Label(select_frame, text="Select City:", font=("Arial", 11),
              bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.city_var = StringVar()
        self.city_combo = ttk.Combobox(select_frame, textvariable=self.city_var,
                                       font=("Arial", 10), width=20)
        self.city_combo.pack(side=tk.RIGHT, padx=5)
        self.city_combo.bind('<<ComboboxSelected>>', self.show_city_info)

        # Frame for displaying city information
        info_frame = tk.LabelFrame(self.root, text="City Information",
                                   font=("Arial", 11, "bold"), bg='#f0f0f0',
                                   fg='#2c3e50')
        info_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

        # Create info labels
        self.info_labels = {}
        info_fields = [
            ("City Name:", "name", ""),
            ("Population:", "population", ""),
            ("Number of Men:", "men", ""),
            ("Number of Women:", "women", "")
        ]

        for i, (label_text, key, value) in enumerate(info_fields):
            Label(info_frame, text=label_text, font=("Arial", 11),
                  bg='#f0f0f0').grid(row=i, column=0, pady=8, padx=10, sticky='e')

            self.info_labels[key] = Label(info_frame, text=value,
                                          font=("Arial", 11),
                                          bg='#f0f0f0', fg='#2c3e50')
            self.info_labels[key].grid(row=i, column=1, pady=8, padx=10, sticky='w')

        # Frame for action buttons
        action_frame = Frame(self.root, bg='#f0f0f0')
        action_frame.pack(pady=10, padx=20, fill=tk.X)

        # Add new city button
        Button(action_frame, text="Add New City", command=self.open_add_city_window,
               font=("Arial", 10), bg='#3498db', fg='white',
               padx=15, pady=8).pack(side=tk.RIGHT, padx=5)

        # Search section
        search_frame = Frame(self.root, bg='#f0f0f0')
        search_frame.pack(pady=10, padx=20, fill=tk.X)

        Label(search_frame, text="Search City:", font=("Arial", 11),
              bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.search_entry = Entry(search_frame, width=20, font=("Arial", 11))
        self.search_entry.pack(side=tk.RIGHT, padx=5)

        Button(search_frame, text="Search", command=self.search_city,
               font=("Arial", 10), bg='#e67e22', fg='white',
               padx=15, pady=5).pack(side=tk.RIGHT, padx=5)

        # Label for displaying search results
        self.search_result_label = Label(self.root, text="",
                                         font=("Arial", 10),
                                         bg='#f0f0f0')
        self.search_result_label.pack(pady=5)

    def load_cities(self):
        """Load city list into dropdown menu"""
        cities = self.db_manager.get_all_cities()
        city_names = [city[1] for city in cities]
        self.city_combo['values'] = city_names

        if city_names:
            self.city_combo.set(city_names[0])
            self.show_city_info(None)

    def show_city_info(self, event):
        """Display information for the selected city"""
        city_name = self.city_var.get()
        if not city_name:
            return

        city_data = self.db_manager.get_city_by_name(city_name)
        if city_data:
            # city_data: (id, name, population, men, women)
            self.info_labels['name'].config(text=city_data[1])
            self.info_labels['population'].config(text=f"{city_data[2]:,}")
            self.info_labels['men'].config(text=f"{city_data[3]:,}")
            self.info_labels['women'].config(text=f"{city_data[4]:,}")

            # Clear search message
            self.search_result_label.config(text="", fg='#2c3e50')

    def search_city(self):
        """Search for a city in the database"""
        search_term = self.search_entry.get().strip()

        if not search_term:
            messagebox.showwarning("Warning", "Please enter a city name to search!")
            return

        city_data = self.db_manager.search_city(search_term)

        if city_data:
            self.search_result_label.config(
                text=f"✅ City '{search_term}' found! Population: {city_data[2]:,} people",
                fg='#27ae60'
            )
            # Select city in dropdown
            self.city_var.set(search_term)
            self.show_city_info(None)
        else:
            self.search_result_label.config(
                text=f"❌ City '{search_term}' not found in the database!",
                fg='#e74c3c'
            )

    def open_add_city_window(self):
        """Open the add city form"""
        AddCityWindow(self.root, self.db_manager, self.load_cities)

    def on_closing(self):
        """Close the application and database connection"""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.db_manager.close()
            self.root.destroy()


# Run the main application
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)

    # Window closing event
    root.protocol("WM_DELETE_WINDOW", app.on_closing)

    root.mainloop()