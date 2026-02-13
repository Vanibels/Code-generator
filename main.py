import string
import random
from tkinter import *
from tkinter import messagebox

# Colors
COLOR_BG = '#1E1E2E'
COLOR_CARD = '#313244'
COLOR_TEXT = '#CDD6F4'
COLOR_ACCENT = '#89B4FA'
COLOR_GENERATE = '#A6E3A1'
COLOR_DANGER = '#F38BA8'
COLOR_ENTRY_BG = '#11111B'

def generate_password():
    try:
        length = length_slider.get()
        chars = string.ascii_lowercase
        if var_upper.get(): chars += string.ascii_uppercase
        if var_nums.get():  chars += string.digits
        if var_syms.get():  chars += string.punctuation
        if not chars:
            messagebox.showwarning("Erreur", "Sélectionne au moins une option !")
            return
        password = random.choice(string.ascii_letters) + "".join(random.choice(chars) for _ in range(length))
        pass_entry.config(state='normal')
        pass_entry.delete(0, END)
        pass_entry.insert(0, password)
        pass_entry.config(state='readonly') 
        with open("passwords", "a+") as file:
            file.write(f"ans : {password}\n")

    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur : {e}")

def copy_to_clipboard():
    password = pass_entry.get()
    if password:
        windows.clipboard_clear()
        windows.clipboard_append(password)
        # Feedback
        messagebox.showinfo("Copié", "Mot de passe envoyé dans le presse-papier !")

# Effects
def on_enter(e):
    e.widget['background'] = '#45475A'

def on_leave(e):
    if e.widget.cget('text') == "GÉNÉRER":
        e.widget['background'] = COLOR_GENERATE
    elif e.widget.cget('text') == "RESET":
        e.widget['background'] = COLOR_DANGER
    else:
        e.widget['background'] = COLOR_ACCENT

# Root
windows = Tk()
windows.title("PassGen Modern v2.1")
windows.geometry("450x600")
windows.configure(bg=COLOR_BG)

# Container
main_frame = Frame(windows, bg=COLOR_BG)
main_frame.pack(expand=YES, fill=BOTH, padx=30, pady=30)

# Title
Label(main_frame, text="PASSWORD", font=("Segoe UI", 24, "bold"), bg=COLOR_BG, fg=COLOR_ACCENT).pack()
Label(main_frame, text="GENERATOR", font=("Segoe UI", 14), bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=(0, 20))

# Result
pass_entry = Entry(main_frame, font=("Consolas", 18), bg=COLOR_ENTRY_BG, fg=COLOR_GENERATE, bd=0, justify='center', insertbackground=COLOR_TEXT, state='readonly')
pass_entry.pack(fill=X, pady=10, ipady=10)

# Settings
settings_card = Frame(main_frame, bg=COLOR_CARD, bd=0, padx=20, pady=20)
settings_card.pack(fill=X, pady=20)

# Lenght
Label(settings_card, text="Longueur du mot de passe", bg=COLOR_CARD, fg=COLOR_TEXT, font=("Segoe UI", 10)).pack(anchor=W)
length_slider = Scale(settings_card, from_=8, to=32, orient=HORIZONTAL, bg=COLOR_CARD, fg=COLOR_ACCENT, highlightthickness=0, troughcolor=COLOR_BG, bd=0)
length_slider.set(16)
length_slider.pack(fill=X, pady=(0, 15))

# Options
options_frame = Frame(settings_card, bg=COLOR_CARD)
options_frame.pack(fill=X)

var_upper = IntVar(value=1)
var_nums = IntVar(value=1)
var_syms = IntVar(value=1)

def styled_check(text, variable):
    return Checkbutton(options_frame, text=text, variable=variable, bg=COLOR_CARD, fg=COLOR_TEXT, activebackground=COLOR_CARD, activeforeground=COLOR_ACCENT,selectcolor=COLOR_BG, bd=0, font=("Segoe UI", 10))

styled_check("Inclure Majuscules", var_upper).pack(anchor=W)
styled_check("Inclure Chiffres", var_nums).pack(anchor=W)
styled_check("Inclure Symboles", var_syms).pack(anchor=W)

# Buttons
btn_style = {"font": ("Segoe UI", 11, "bold"), "fg": COLOR_BG, "bd": 0, "cursor": "hand2", "activeforeground": "white"}

btn_gen = Button(main_frame, text="GÉNÉRER", bg=COLOR_GENERATE, **btn_style, command=generate_password)
btn_gen.pack(fill=X, pady=(10, 5), ipady=8)

btn_copy = Button(main_frame, text="COPIER", bg=COLOR_ACCENT, **btn_style, command=copy_to_clipboard)
btn_copy.pack(fill=X, pady=5, ipady=8)

btn_reset = Button(main_frame, text="RESET", bg=COLOR_DANGER, **btn_style, command=lambda: [pass_entry.config(state='normal'), pass_entry.delete(0, END), pass_entry.config(state='readonly')])
btn_reset.pack(fill=X, pady=5, ipady=8)

for btn in [btn_gen, btn_copy, btn_reset]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

windows.mainloop()