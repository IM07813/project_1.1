import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    try:
        trans1 = trans.translate(text, src=src, dest=dest)
        return trans1.text
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))
        return ""

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END).strip()
    if masg:
        textget = change(text=masg, src=s, dest=d)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, textget)
    else:
        messagebox.showwarning("Input Error", "Please enter text to translate")

def clear_text():
    Sor_txt.delete(1.0, END)
    dest_txt.delete(1.0, END)

# UI elements and main loop
root = Tk()
root.title("Translator")
root.geometry("600x500")
root.config(bg='#87CEEB')  # Set background color to light blue

# Title
title_label = Label(root, text="Translator", font=("Arial", 24, "bold"), bg="#4b4b4b", fg="white")
title_label.pack(pady=20, fill=X)

# Source Text Label
source_label = Label(root, text="Source Text", font=("Arial", 14), bg="#87CEEB")
source_label.place(x=10, y=70)

# Translated Text Label
dest_label = Label(root, text="Translated Text", font=("Arial", 14), bg="#87CEEB")
dest_label.place(x=310, y=70)

# Text widgets
Sor_txt = Text(root, font=("Arial", 12), wrap=WORD, height=10, width=25, bd=2, relief=SOLID)
Sor_txt.place(x=10, y=100)

dest_txt = Text(root, font=("Arial", 12), wrap=WORD, height=10, width=25, bd=2, relief=SOLID)
dest_txt.place(x=310, y=100)

# Comboboxes
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, values=list_text, font=("Arial", 10))
comb_sor.place(x=10, y=300, height=30, width=150)
comb_sor.set("english")

comb_dest = ttk.Combobox(root, values=list_text, font=("Arial", 10))
comb_dest.place(x=310, y=300, height=30, width=150)
comb_dest.set("hindi")

# Buttons
button_translate = Button(root, text="Translate", font=("Arial", 12, "bold"), command=data, bg="#4CAF50", fg="white", activebackground="#45a049")
button_translate.place(x=200, y=350, height=40, width=200)

button_clear = Button(root, text="Clear", font=("Arial", 12, "bold"), command=clear_text, bg="#f44336", fg="white", activebackground="#e41e1e")
button_clear.place(x=200, y=400, height=40, width=200)

root.mainloop()
