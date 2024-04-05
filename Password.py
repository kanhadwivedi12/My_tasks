import tkinter as tk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.length_label = tk.Label(master, text="Enter password length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_display = tk.Label(master, text="", borderwidth=2, relief="groove", width=30)
        self.password_display.grid(row=2, column=1, padx=10, pady=10)
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choices(characters, k=length))
            self.password_display.config(text=generated_password)
        except ValueError:
            self.password_display.config(text="Invalid input")
def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()