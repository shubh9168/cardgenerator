import tkinter as tk
from tkinter import ttk

class CardGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Generator")

        # Card details
        self.card_label = ttk.Label(root, text="Card Details:")
        self.card_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.name_label = ttk.Label(root, text="Full Name:")
        self.name_label.grid(row=1, column=0, padx=20)
        self.name_entry = ttk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=20)

        self.age_label = ttk.Label(root, text="Age:")
        self.age_label.grid(row=2, column=0, padx=20)
        self.age_entry = ttk.Entry(root)
        self.age_entry.grid(row=2, column=1, padx=20)

        self.email_label = ttk.Label(root, text="Email:")
        self.email_label.grid(row=3, column=0, padx=20)
        self.email_entry = ttk.Entry(root)
        self.email_entry.grid(row=3, column=1, padx=20)

        self.company_label = ttk.Label(root, text="Company Name:")
        self.company_label.grid(row=4, column=0, padx=20)
        self.company_entry = ttk.Entry(root)
        self.company_entry.grid(row=4, column=1, padx=20)

        self.package_label = ttk.Label(root, text="Package:")
        self.package_label.grid(row=5, column=0, padx=20)
        self.package_entry = ttk.Entry(root)
        self.package_entry.grid(row=5, column=1, padx=20)

        # Generate button
        self.generate_button = ttk.Button(root, text="Generate Card", command=self.generate_card)
        self.generate_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Output
        self.output_label = ttk.Label(root, text="Generated Card:")
        self.output_label.grid(row=7, column=0, columnspan=2, pady=10)

        self.generated_card = tk.StringVar()
        self.generated_card_label = ttk.Label(root, textvariable=self.generated_card)
        self.generated_card_label.grid(row=8, column=0, columnspan=2, pady=10)

    def generate_card(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        company_name = self.company_entry.get()
        package = self.package_entry.get()

        if name and age and email and company_name and package:
            generated_card = f"Full Name: {name}\nAge: {age}\nEmail: {email}\nCompany Name: {company_name}\nPackage: {package}"
            self.generated_card.set(generated_card)
        else:
            self.generated_card.set("Please enter all details.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CardGeneratorApp(root)
    root.mainloop()

