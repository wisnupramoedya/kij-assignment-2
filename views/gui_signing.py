import shutil
import tkinter as tk
from tkdocviewer import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

file_extension = ".pdf"
filetype = [("PDF Files", f"*{file_extension}")]

title_window = "Signature App"
pdf_filepath = ""


def gui_on():
    window = tk.Tk()
    window.title(title_window)

    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    frm_buttons.grid(row=0, column=0, sticky="ns")

    btn_open = tk.Button(frm_buttons, text="Open PDF File")
    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    lbl_private_key = tk.Label(frm_buttons, text="Enter Private Key:")
    ent_private_key = tk.Entry(frm_buttons, width=50)
    lbl_private_key.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    ent_private_key.grid(row=2, column=0, padx=5, pady=5)

    btn_sign = tk.Button(frm_buttons, text="Verify PDF")
    btn_sign.grid(row=3, column=0, sticky="ew", padx=5)

    pdfview = DocViewer(window)
    pdfview.grid(row=0, column=1, sticky="nsew")

    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=filetype
        )
        if not filepath:
            return

        pdfview.display_file(filepath)
        global pdf_filepath
        pdf_filepath = filepath
        # with open(filepath, mode="r", encoding="utf-8") as input_file:
        #     text = input_file.read()
        #     txt_edit.insert(tk.END, text)
        window.title(f"{title_window} - {pdf_filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=filetype,
        )
        if not filepath:
            return

        global pdf_filepath
        shutil.copyfile(pdf_filepath, filepath)

        window.title(f"{title_window} - {filepath}")

    btn_open.configure(command=open_file)
    btn_sign.configure(command=save_file)

    window.mainloop()
