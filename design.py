# design.py
import tkinter as tk

class OSInterface:
    def __init__(self, root=None):
        self.root = root if root else tk.Tk()
        self.root.title("Моя Операционная Система")
        self.root.geometry("800x600")
    
    def create_button(self, text, command):
        """Создать кнопку для интерфейса"""
        button = tk.Button(self.root, text=text, command=command)
        button.pack(pady=20)
    
    def create_label(self, text):
        """Создать метку для интерфейса"""
        label = tk.Label(self.root, text=text, font=("Arial", 16))
        label.pack(pady=20)
    
    def run(self):
        """Запустить графический интерфейс"""
        self.root.mainloop()

# Пример функции для изменения дизайна интерфейса
def change_theme(root, background_color, text_color):
    root.configure(bg=background_color)
    for widget in root.winfo_children():
        widget.configure(bg=background_color, fg=text_color)
