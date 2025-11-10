import subprocess
import tkinter as tk

def run_command(entry, output):
    cmd = entry.get()
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output.delete(1.0, tk.END)
        output.insert(tk.END,result.stdout + result.stderr )
    except Exception as e:
        output.insert(tk.END,str(e))
        
def launch():
    window = tk.Toplevel()
    window.title("shell Educativa")
    
    tk.Label(window,text="comando:").pack()
    entry = tk.Entry(window, width=50)
    entry.pack()
    
    output= tk.Text(window, height=15, width=60)  
    output.pack()
    
    tk.Button (window, text="Ejecutar", command=lambda: run_command(entry, output)).pack()
        