import tkinter as tk 
from tkinter import messagebox

def open_file_explorer():
    import file_explorer
    file_explorer.launch()
    
def open_process_manager():
    import process_manager
    process_manager.launch()
    
def open_shell():
    import shell # type: ignore
    shell.launch()  
    
def open_system_info():
    import system_info
    system_info.launch()    
    
            
root =tk.Tk()
root.title("mini sistema operativo")
root.geometry("300x200")    

tk.Label(root, text="mini sistema operativo", font=("Arial", 16)).pack(pady=10) 

tk.Button(root, text="Explorador de Archivos", command=open_file_explorer).pack(fill='x', padx=20, pady=5)
tk.Button(root, text="Administrador de procesos", command=open_process_manager).pack(fill="x", padx=20, pady=5)
tk.Button(root, text="Shell", command=open_shell).pack(fill="x", padx=20, pady=5)
tk.Button(root, text="Informacion del sistema", command=open_system_info).pack(fill="x", padx=20, pady=5)   

root.mainloop()


