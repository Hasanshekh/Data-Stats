# -*- coding: utf-8 -*-
"""Data Stats
    -by Paritosh Verma
"""

from tkinter import *
import numpy as np
import pandas as pd
from scipy.stats import stats
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
      
def open_file():
    global v
    global Dataset
    global text
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    Dataset=pd.read_csv(csv_file_path)
    if not csv_file_path:
        return
    txt_edit.delete(1.0, tk.END)
    with open(csv_file_path, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Data Stats - Paritosh Verma ")

def save_file():
    """Save the current file as a new file."""
    csv_file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not csv_file_path:
        return
    with open(csv_file_path, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Data Stats ")

def Quick():
    print("\nRows and Columns ---\n",Dataset.shape)
    print("\nPrint top 5 rows ---\n",Dataset.head)
    print("\nprint bottom 5 rows ---\n",Dataset.tail)
    print("\nDataset info ---")
    Dataset.info()
    print("\nDescribe ---\n",Dataset.describe())
    print("\nDatatypes ---\n",Dataset.dtypes)
    print("\nnull values ---\n",Dataset.isnull().sum()) #.sort_values(ascending=False).head(50))

def CLT():
    print("\nmean ---\n",Dataset.mean())
    print("\nmode ---\n",Dataset.mode())
    print("\nmedian ---\n",Dataset.median())

def SVS():
    print("\nStandard Deviation --- \n",Dataset.std())
    print("\nVariance --- \n",Dataset.var())
    print("\nSkewness --- \n",Dataset.skew())

def Correlation():
    f,ax = plt.subplots(figsize=(18, 18))
    sns.heatmap(Dataset.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
    plt.title('Correlation Map')
    plt.savefig('graph.png')
    plt.show()

window = tk.Tk()
v = tk.StringVar() 

window.title("Data Stats  - Paritosh Verma")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file)
btn_Quick = tk.Button(fr_buttons, text="Quick", command=Quick)
btn_CLT = tk.Button(fr_buttons, text="CLT", command=CLT)
btn_SVS = tk.Button(fr_buttons, text="SVS", command=SVS)
btn_Correlation = tk.Button(fr_buttons, text="Correlation", command=Correlation)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_Quick.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_CLT.grid(row=3, column=0, sticky="ew", padx=5)
btn_SVS.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_Correlation.grid(row=5, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()


