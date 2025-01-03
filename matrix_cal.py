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
def create_matrix_input():
    global matrix1_entries, matrix2_entries

    for widget in matrix1_frame.winfo_children():
        widget.destroy()
    for widget in matrix2_frame.winfo_children():
        widget.destroy()

    rows1 = int(rows1_entry.get())
    cols1 = int(cols1_entry.get())
    rows2 = int(rows2_entry.get())
    cols2 = int(cols2_entry.get())

    if cols1 != rows2:
        messagebox.showerror("Error", "Number of columns in Matrix 1 must be equal to number of rows in Matrix 2")
        return

    matrix1_entries = create_matrix_entries(matrix1_frame, rows1, cols1)
    matrix2_entries = create_matrix_entries(matrix2_frame, rows2, cols2)

app = tk.Tk()
app.title("Matrix Multiplication Calculator")
app.geometry("600x600")
app.configure(bg="#f0f0f0")  # Set background color
