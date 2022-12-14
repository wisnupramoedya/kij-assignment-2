import os
import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
from tkdocviewer import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from constants.file import *
from services.signing import Signing
from services.generate import Generate

title_window = SIGNING_APP
pdf_filepath = BLANK_STRING
pub_filepath = BLANK_STRING


def gui_on():
    window = tk.Tk()
    window.title(title_window)

    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    frm_buttons.grid(row=0, column=0, sticky="ns")

    btn_open = tk.Button(frm_buttons, text="Open PDF File")
    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    btn_pub_key = tk.Button(frm_buttons, text="Open Private Key")
    btn_pub_key.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    sct_pub_key = scrolledtext.ScrolledText(
        frm_buttons, width=20, height=10, wrap='word', state='disabled')
    sct_pub_key.insert(1.0, BLANK_STRING)
    sct_pub_key.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    btn_sign = tk.Button(frm_buttons, text="Sign PDF")
    btn_sign.grid(row=3, column=0, sticky="ew", padx=5)

    label = tk.Label(frm_buttons, text='Don\'t have keypair? \nGenerate keypair \nusing button below')
    label.config(font=("Courier", 8))
    label.grid(row=4, column=0, sticky="ew", padx=5, pady=(30, 0))
    btn_generate_key = tk.Button(frm_buttons, text="Generate Keypair")
    btn_generate_key.grid(row=5, column=0, sticky="ew", padx=5)

    pdfview = DocViewer(window)
    pdfview.grid(row=0, column=1, sticky="nsew")

    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=PDF_FILE_TYPE
        )
        if not filepath:
            return

        global pdf_filepath
        pdf_filepath = filepath
        pdfview.display_file(pdf_filepath)

        window.title(f"{SIGNING_APP} - {pdf_filepath}")

    def open_pub_key():
        """Open the private key for signing in the PDF"""
        filepath = askopenfilename(
            filetypes=PEM_FILE_TYPE
        )
        if not filepath:
            return

        global pub_filepath
        pub_filepath = filepath

        with open(pub_filepath, "r") as file:
            sct_pub_key.configure(state='normal')
            sct_pub_key.insert(1.0, file.read())
            sct_pub_key.configure(state='disabled')

    def save_file():
        """Save the current file as a new file."""
        global pdf_filepath
        if not pdf_filepath:
            messagebox.showwarning(
                "Warning", f"{PDF_FILE_TYPE[0][0]} should be inputted!")
            return

        global pub_filepath
        if not pub_filepath:
            messagebox.showwarning(
                "Warning", f"Blank private key. Pair key will be generated in folder testcase automatically!")
            pub_filepath = Generate.generate_keypair()

        filepath = asksaveasfilename(
            filetypes=PDF_FILE_TYPE,
        )
        if not filepath:
            return

        if not filepath.endswith(PDF_FILE_EXTENSION):
            filepath += PDF_FILE_EXTENSION

        sign_mode = Signing.sign(pdf_filepath, filepath, pub_filepath)
        if sign_mode:
            messagebox.showinfo(
                "Success",
                f"File {os.path.basename(pdf_filepath)} is successfully signed with {os.path.basename(pub_filepath)}")
        else:
            messagebox.showwarning(
                "Warning", f"File {os.path.basename(pdf_filepath)} has been signed before!")

    def generate_keypair():
        path = Generate.generate_keypair()
        path = path.split('_privkey.')
        if path:
            messagebox.showinfo(
                "Success",
                f"Keypair is successfully generated at {path[0]}_privkey.pem and {path[0]}_pubkey.pub")

    btn_open.configure(command=open_file)
    btn_pub_key.configure(command=open_pub_key)
    btn_sign.configure(command=save_file)
    btn_generate_key.configure(command=generate_keypair)

    window.mainloop()
