import tkinter as tk
from tkinter import messagebox

def create_matrix_entries(matrix_frame, rows, cols):
    entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries
