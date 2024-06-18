import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random
import string
import pyautogui


ventana = tk.Tk()
ventana.title("Password Generator")
ventana.geometry("400x250")
ventana.resizable(width=False, height=False)


logo = tk.PhotoImage(file="icons/icono.png")
ventana.iconphoto(False, logo)

def generar_func():
    tam = tam_variable.get()
    use_lower = lower_var.get()
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    
    if tam < 1:
        pyautogui.alert(text="Password length should be at least 1.", title="Password Generator")
        return

    caja_contra.delete('1.0', tk.END)

    char_pool = ''
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
    
    if not char_pool:
        pyautogui.alert(text="Select at least one character type.", title="Password Generator")
        return

    password = ''.join(random.choice(char_pool) for _ in range(tam))

    caja_contra.insert(tk.END, password)
    ventana.clipboard_clear()
    ventana.clipboard_append(password)
    
    pyautogui.alert(text="Generated password copied to clipboard.", title="Password Generator")

tk.Label(ventana, text="Length of Password:").place(relx=0.1, rely=0.1)
tam_variable = tk.IntVar()
tam_entry = ttk.Entry(ventana, justify="center", textvariable=tam_variable, width=10)
tam_entry.place(relx=0.5, rely=0.1)


lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(ventana, text="Lowercase", variable=lower_var).place(relx=0.1, rely=0.25)
tk.Checkbutton(ventana, text="Uppercase", variable=upper_var).place(relx=0.5, rely=0.25)
tk.Checkbutton(ventana, text="Digits", variable=digits_var).place(relx=0.1, rely=0.35)
tk.Checkbutton(ventana, text="Symbols", variable=symbols_var).place(relx=0.5, rely=0.35)


generar_button = ttk.Button(ventana, text='Generate Password', command=generar_func)
generar_button.place(relx=0.3, rely=0.5)


caja_contra = ScrolledText(ventana, height=4, width=40)
caja_contra.place(relx=0.1, rely=0.7)

if __name__ == "__main__":
    ventana.mainloop()
