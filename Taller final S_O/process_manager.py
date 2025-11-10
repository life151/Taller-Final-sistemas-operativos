import psutil
import tkinter as tk
from tkinter import messagebox

def kill_process(pid_entry):
    try:
        pid=int(pid_entry.get())
        psutil.Process(pid).terminate()
        messagebox.showinfo("Exito", f"Proceso {pid} finalizado.")
    except Exception as e:
        
        messagebox.showerror("Error", str(e)) 
        
        
def launch():
    window = tk.Toplevel()
    window.title("Gestion de procesos")
        
    tk.Label(window, text="Procesos Activos").pack()
    text = tk.Text(window, height=15, width=60)
    text.pack()
        
    for proc in psutil.process_iter(['pid', 'name']):
        text.insert(tk.END, f"{proc.info['pid']} - {proc.info['name']}\n")

    tk.Label(window, text="PID a finalizar:").pack()
    pid_entry = tk.Entry(window)
    pid_entry.pack()
        
    tk.Button(window,text="finalizar Proceso", command =lambda: kill_process(pid_entry)).pack() 
        
