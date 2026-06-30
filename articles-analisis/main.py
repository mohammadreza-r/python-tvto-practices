import tkinter as tk
from tkinter import messagebox
import string


class ArticleAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Article Analyzer")
        self.root.geometry("650x550")
        self.root.configure(bg='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Article Analysis & Comparison",
                         font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        # Frame for first article
        frame1 = tk.LabelFrame(self.root, text="Article 1",
                               font=("Arial", 11), bg='#f0f0f0')
        frame1.pack(pady=5, padx=10, fill=tk.X)

        self.text1 = tk.Text(frame1, height=6, width=60, font=("Arial", 11))
        self.text1.pack(pady=5, padx=5)

        # Frame for second article
        frame2 = tk.LabelFrame(self.root, text="Article 2",
                               font=("Arial", 11), bg='#f0f0f0')
        frame2.pack(pady=5, padx=10, fill=tk.X)

        self.text2 = tk.Text(frame2, height=6, width=60, font=("Arial", 11))
        self.text2.pack(pady=5, padx=5)

        # Buttons
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Show Common Words",
                  command=self.show_common_words,
                  font=("Arial", 10), bg='#3498db', fg='white',
                  padx=15, pady=8).pack(side=tk.RIGHT, padx=5)

        tk.Button(button_frame, text="Show Unique Words",
                  command=self.show_unique_words,
                  font=("Arial", 10), bg='#e67e22', fg='white',
                  padx=15, pady=8).pack(side=tk.RIGHT, padx=5)

        # Section for selecting which article to show unique words for
        select_frame = tk.Frame(self.root, bg='#f0f0f0')
        select_frame.pack(pady=5)

        tk.Label(select_frame, text="Select article for unique words:",
                 font=("Arial", 10), bg='#f0f0f0').pack(side=tk.RIGHT, padx=5)

        self.article_var = tk.StringVar(value="Article 1")
        tk.Radiobutton(select_frame, text="Article 1", variable=self.article_var,
                       value="Article 1", bg='#f0f0f0', font=("Arial", 10)).pack(side=tk.RIGHT, padx=5)
        tk.Radiobutton(select_frame, text="Article 2", variable=self.article_var,
                       value="Article 2", bg='#f0f0f0', font=("Arial", 10)).pack(side=tk.RIGHT, padx=5)

        # Text widget for displaying results
        self.result_text = tk.Text(self.root, height=10, width=65,
                                   font=("Arial", 10), bg='white',
                                   wrap=tk.WORD)
        self.result_text.pack(pady=10, padx=10)

        # Scrollbar for results
        scrollbar = tk.Scrollbar(self.root, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)

    def clean_text(self, text):
        """Clean text and extract words"""
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Split into words
        words = text.lower().split()
        return words

    def show_common_words(self):
        """Display words that appear in both articles"""
        text1_content = self.text1.get(1.0, tk.END).strip()
        text2_content = self.text2.get(1.0, tk.END).strip()

        if not text1_content or not text2_content:
            messagebox.showerror("Error", "Please enter both articles!")
            return

        # Extract words
        words1 = set(self.clean_text(text1_content))
        words2 = set(self.clean_text(text2_content))

        # Find common words
        common_words = words1 & words2

        self.result_text.delete(1.0, tk.END)

        if common_words:
            self.result_text.insert(tk.END, f"🔍 Common words in both articles ({len(common_words)} words):\n\n")
            for word in sorted(common_words):
                self.result_text.insert(tk.END, f"• {word}\n")
        else:
            self.result_text.insert(tk.END, "No common words found between the two articles!")

    def show_unique_words(self):
        """Display words that appear in only one article"""
        text1_content = self.text1.get(1.0, tk.END).strip()
        text2_content = self.text2.get(1.0, tk.END).strip()

        if not text1_content or not text2_content:
            messagebox.showerror("Error", "Please enter both articles!")
            return

        # Extract words
        words1 = set(self.clean_text(text1_content))
        words2 = set(self.clean_text(text2_content))

        # Determine which article was selected
        selected = self.article_var.get()

        if selected == "Article 1":
            unique_words = words1 - words2
            title = "Article 1"
        else:
            unique_words = words2 - words1
            title = "Article 2"

        self.result_text.delete(1.0, tk.END)

        if unique_words:
            self.result_text.insert(tk.END, f"🔑 Unique words in {title} ({len(unique_words)} words):\n\n")
            for word in sorted(unique_words):
                self.result_text.insert(tk.END, f"• {word}\n")
        else:
            self.result_text.insert(tk.END, f"No unique words found in {title}!")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ArticleAnalyzer(root)
    root.mainloop()