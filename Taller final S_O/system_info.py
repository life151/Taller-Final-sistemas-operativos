import platform, shutil,getpass
import  tkinter as tk

def launch():
    window = tk.Toplevel()
    window.title("Informacion del Sistema")
    
    user = getpass.getuser()
    os_name=platform.system()
    os_version=platform.version()
    total, used, fre = shutil.disk_usage("/")
    
    tk.Label(window, text=f"Usuario: {user}").pack()
    tk.Label(window, text=f"Sistema Operativo: {os_name}").pack()
    tk.Label(window, text=f"Version : {os_version}").pack()
    tk.Label(window, text=f"Espacio libre en disco: {fre // (2**30)} GB").pack()
    