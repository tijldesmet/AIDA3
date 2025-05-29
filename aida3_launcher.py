import os
import shutil
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import subprocess

def select_credentials():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("AIDA3 Setup", "Selecteer je Google Drive 'credentials.json'-bestand")
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        shutil.copy(file_path, "credentials.json")
    else:
        messagebox.showerror("Fout", "Geen bestand geselecteerd. Installatie afgebroken.")
        exit()

def ask_openai_key():
    return simpledialog.askstring("AIDA3 Setup", "Voer je OpenAI API sleutel in (sk-...):", show="*")

def ask_folder_id():
    return simpledialog.askstring("AIDA3 Setup", "Voer je Google Drive folder-ID in:")

def write_env(api_key):
    with open(".env", "w") as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")

def patch_folder_id(folder_id):
    files = ["main.py", "backend/drive_loader.py"]
    for fname in files:
        with open(fname, "r") as f:
            content = f.read()
        content = content.replace('FOLDER_ID = "VUL_HIER_JE_GOOGLE_DRIVE_FOLDER_ID_IN"', f'FOLDER_ID = "{folder_id}"')
        with open(fname, "w") as f:
            f.write(content)

def run_app():
    subprocess.run(["python", "main.py"])

if __name__ == "__main__":
    select_credentials()
    key = ask_openai_key()
    folder = ask_folder_id()
    if key and folder:
        write_env(key)
        patch_folder_id(folder)
        run_app()
    else:
        messagebox.showerror("Fout", "API sleutel of folder-ID ontbreekt. Installatie afgebroken.")
