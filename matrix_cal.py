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
app.configure(bg="#f0f0f0") 
input_frame = tk.Frame(app, bg="#f0f0f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Matrix 1 Order (rows x columns):", bg="#f0f0f0").grid(row=0, column=0, columnspan=4, pady=5)
tk.Label(input_frame, text="Rows:", bg="#f0f0f0").grid(row=1, column=0)
rows1_entry = tk.Entry(input_frame, width=5)
rows1_entry.grid(row=1, column=1)
tk.Label(input_frame, text="Columns:", bg="#f0f0f0").grid(row=1, column=2)
cols1_entry = tk.Entry(input_frame, width=5)
cols1_entry.grid(row=1, column=3)

tk.Label(input_frame, text="Matrix 2 Order (rows x columns):", bg="#f0f0f0").grid(row=2, column=0, columnspan=4, pady=5)
tk.Label(input_frame, text="Rows:", bg="#f0f0f0").grid(row=3, column=0)
rows2_entry = tk.Entry(input_frame, width=5)
rows2_entry.grid(row=3, column=1)
tk.Label(input_frame, text="Columns:", bg="#f0f0f0").grid(row=3, column=2)
cols2_entry = tk.Entry(input_frame, width=5)
cols2_entry.grid(row=3, column=3)
