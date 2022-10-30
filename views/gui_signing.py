import shutil
import os
import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
from tkdocviewer import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from constants.file import BLANK_STRING, PDF_FILE_TYPE, PEM_FILE_TYPE, SIGNING_APP


title_window = SIGNING_APP
pdf_filepath = BLANK_STRING
pem_filepath = BLANK_STRING


def gui_on():
    window = tk.Tk()
    window.title(title_window)

    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    frm_buttons.grid(row=0, column=0, sticky="ns")

    btn_open = tk.Button(frm_buttons, text="Open PDF File")
    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    btn_pub_key = tk.Button(frm_buttons, text="Open Public Key")
    btn_pub_key.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    sct_pub_key = scrolledtext.ScrolledText(
        frm_buttons, width=20, height=10, wrap='word', state='disabled')
    sct_pub_key.insert(1.0, BLANK_STRING)
    sct_pub_key.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    btn_sign = tk.Button(frm_buttons, text="Sign PDF")
    btn_sign.grid(row=3, column=0, sticky="ew", padx=5)

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
        """Open the public key for signing in the PDF"""
        filepath = askopenfilename(
            filetypes=PEM_FILE_TYPE
        )
        if not filepath:
            return

        global pem_filepath
        pem_filepath = filepath

        with open(pem_filepath, "r") as file:
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

        global pem_filepath
        if not pem_filepath:
            messagebox.showwarning(
                "Warning", f"Public key should be inputted!")
            return

        filepath = asksaveasfilename(
            filetypes=PDF_FILE_TYPE,
        )
        if not filepath:
            return

        ## Enter logic of signing here ##

        shutil.copyfile(pdf_filepath, filepath)

        messagebox.showinfo(
            "Success", f"File {os.path.basename(pdf_filepath)} is successfully signed with {os.path.basename(pem_filepath)}")

    btn_open.configure(command=open_file)
    btn_pub_key.configure(command=open_pub_key)
    btn_sign.configure(command=save_file)

    window.mainloop()