import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Convert language codes to display names and vice versa
lang_codes = list(LANGUAGES.keys())
lang_names = list(LANGUAGES.values())
lang_name_to_code = {v: k for k, v in LANGUAGES.items()}

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    source_lang_name = source_lang_var.get()
    target_lang_name = target_lang_var.get()

    if not text or not target_lang_name:
        messagebox.showwarning("Input Error", "Please provide text and select target language.")
        return

    src_code = lang_name_to_code.get(source_lang_name, 'auto')
    tgt_code = lang_name_to_code[target_lang_name]

    try:
        translated = translator.translate(text, src=src_code, dest=tgt_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("🌍 Language Translator")
root.geometry("700x600")
root.config(bg="#f0f8ff")  # Alice blue background

# Title Label
title_label = tk.Label(root, text="🌐 Language Translator", font=("Helvetica", 20, "bold"), fg="#333", bg="#f0f8ff")
title_label.pack(pady=20)

# Input Section
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter text to translate:", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w")
input_text = tk.Text(input_frame, height=7, width=70, font=("Arial", 11), bd=2, relief="groove", bg="#ddefff")
input_text.pack(pady=5)

# Language selection section
lang_frame = tk.Frame(root, bg="#f0f8ff")
lang_frame.pack(pady=15)

tk.Label(lang_frame, text="From:", font=("Arial", 11, "bold"), bg="#f0f8ff").grid(row=0, column=0, padx=10)
source_lang_var = tk.StringVar(value="Auto Detect")
source_dropdown = ttk.Combobox(lang_frame, textvariable=source_lang_var, values=["Auto Detect"] + lang_names, state="readonly", width=25)
source_dropdown.grid(row=0, column=1)

tk.Label(lang_frame, text="To:", font=("Arial", 11, "bold"), bg="#f0f8ff").grid(row=0, column=2, padx=10)
target_lang_var = tk.StringVar(value="French")
target_dropdown = ttk.Combobox(lang_frame, textvariable=target_lang_var, values=lang_names, state="readonly", width=25)
target_dropdown.grid(row=0, column=3)

# Button style
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=15)

translate_btn = tk.Button(button_frame, text="🔄 Translate", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10, relief="raised", bd=3, cursor="hand2", activebackground="#45a049")
translate_btn.pack()
translate_btn.config(command=translate_text)

# Button hover effect
def on_enter(e):
    translate_btn.config(bg="#45a049")

def on_leave(e):
    translate_btn.config(bg="#4CAF50")

translate_btn.bind("<Enter>", on_enter)
translate_btn.bind("<Leave>", on_leave)

# Output Section
output_frame = tk.Frame(root, bg="#f0f8ff")
output_frame.pack(pady=10)

tk.Label(output_frame, text="Translated text:", font=("Arial", 12), bg="#f0f8ff").pack(anchor="w")
output_text = tk.Text(output_frame, height=6, width=70, font=("Arial", 11), bd=2, relief="groove", bg="#ddefff")
output_text.pack(pady=5)

# Run the app
root.mainloop()