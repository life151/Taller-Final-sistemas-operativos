import os
import tkinter as tk
from tkinter import messagebox

current_path = os.getcwd()

def refresh_list(listbox):
    listbox.delete(0, tk.END)
    items = os.listdir(current_path)
    if not items:
        listbox.insert(tk.END, "carpeta vacia")
    else:
        for item in items:
            listbox.insert(tk.END, item)    
            
def go_up(listbox):
    global current_path
    current_path = os.path.dirname(current_path)
    refresh_list(listbox)
    
    
def launch():
    global current_path    
    window = tk.Toplevel()
    window.title("Explorador de archivos") 
    
    lista = tk.Listbox(window, width=50)
    lista.pack()
    
    refresh_list(lista)
    
    tk.Button(window, text="Refrescar", command=lambda: refresh_list(lista)).pack()
    tk.Button(window, text="Subir Nivel",command=lambda: go_up(lista)).pack()
    
    
    
