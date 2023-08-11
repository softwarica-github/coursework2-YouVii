import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

class TextEncryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Encryptor/Decryptor")
        self.root.configure(bg="#f0f0f0")  # Set background color

        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        self.title_label = tk.Label(root, text="Advanced Text Encryptor/Decryptor", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.label = tk.Label(root, text="Enter Text:", font=("Helvetica", 12), bg="#f0f0f0")
        self.label.pack()

        self.text_entry = tk.Text(root, wrap=tk.WORD, height=5, width=40, font=("Helvetica", 12))
        self.text_entry.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt, font=("Helvetica", 12, "bold"), bg="#4caf50", fg="white")
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt, font=("Helvetica", 12, "bold"), bg="#008CBA", fg="white")
        self.decrypt_button.pack(pady=5)

        self.result_text = tk.Text(root, wrap=tk.WORD, height=5, width=40, font=("Helvetica", 12))
        self.result_text.pack(pady=10)

    def encrypt(self):
        text = self.text_entry.get("1.0", "end-1c")
        encrypted_text = self.cipher_suite.encrypt(text.encode())
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, "Encrypted Text:\n" + encrypted_text.decode())

    def decrypt(self):
        encrypted_text = self.result_text.get("1.0", "end-1c").strip()
        if "Encrypted Text:" in encrypted_text:
            encrypted_text = encrypted_text.split("Encrypted Text:\n")[1]
            try:
                decrypted_text = self.cipher_suite.decrypt(encrypted_text.encode()).decode()
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert(tk.END, "Decrypted Text:\n" + decrypted_text)
            except:
                messagebox.showerror("Error", "Invalid encrypted text.")
        else:
            messagebox.showerror("Error", "No valid encrypted text found.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = TextEncryptor(root)
    root.mainloop()
