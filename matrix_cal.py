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
def get_matrix_from_entries(entries):
    return [[int(entry.get()) for entry in row] for row in entries]

def multiply_matrices():
    try:
        matrix1 = get_matrix_from_entries(matrix1_entries)
        matrix2 = get_matrix_from_entries(matrix2_entries)

        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in Matrix 1 must be equal to number of rows in Matrix 2")

        result = [[sum(a * b for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]

        result_str = '\n'.join([' '.join(map(str, row)) for row in result])
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, result_str)
    except Exception as e:
        messagebox.showerror("Error", str(e))
