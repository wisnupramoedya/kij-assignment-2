import os
import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
from tkdocviewer import *
from tkinter.filedialog import askopenfilename
from constants.file import *
from constants.mode import *
from services.verifying import Verifying

title_window = VERIFYING_APP
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

    btn_pri_key = tk.Button(frm_buttons, text="Open Public Key")
    btn_pri_key.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    sct_pri_key = scrolledtext.ScrolledText(
        frm_buttons, width=20, height=10, wrap='word', state='disabled')
    sct_pri_key.insert(1.0, BLANK_STRING)
    sct_pri_key.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    btn_sign = tk.Button(frm_buttons, text="Verify PDF")
    btn_sign.grid(row=3, column=0, sticky="ew", padx=5)

    lbl_result = tk.Label(frm_buttons, text="", wraplength=350)
    lbl_result.grid(row=4, column=0, sticky="w", padx=5, pady=5)

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

        window.title(f"{VERIFYING_APP} - {pdf_filepath}")

    def open_pri_key():
        """Open the public key for verifying in the PDF"""
        filepath = askopenfilename(
            filetypes=PUB_FILE_TYPE
        )
        if not filepath:
            return

        global pem_filepath
        pem_filepath = filepath

        with open(pem_filepath, "r") as file:
            sct_pri_key.configure(state='normal')
            sct_pri_key.insert(1.0, file.read())
            sct_pri_key.configure(state='disabled')

    def verify_file():
        """Verify the signatured file."""
        try:
            os.remove('digital_signature.txt')
            os.remove('original_file.pdf')
        except FileNotFoundError:
            pass

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

        verify_mode = Verifying.verify(path_file=pdf_filepath, path_key=pem_filepath)
        if verify_mode == SIGNATURE_NOT_FOUND:
            messagebox.showerror(
                "Error", f"File {os.path.basename(pdf_filepath)} does not have any signature")
        elif verify_mode == SIGNATURE_NOT_MATCH:
            messagebox.showerror(
                "Success", f"File {os.path.basename(pdf_filepath)} is not match with public key")
        elif verify_mode == SIGNATURE_MATCH:
            messagebox.showinfo(
                "Success", f"File {os.path.basename(pdf_filepath)}'s signature match with public key")

    btn_open.configure(command=open_file)
    btn_pri_key.configure(command=open_pri_key)
    btn_sign.configure(command=verify_file)

    window.mainloop()
