import tkinter as tk
from tkinter import messagebox
import socket

def scan_port():
    host = entry_ip.get()
    port = int(entry_port.get())

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            result = s.connect_ex((host, port))
            if result == 0:
                messagebox.showinfo("Port Scanner", f"Port {port} is open on {host}")
            else:
                messagebox.showinfo("Port Scanner", f"Port {port} is closed on {host}")
    except Exception as e:
        messagebox.showerror("Port Scanner", f"An error occurred: {e}")
root = tk.Tk()
root.title("Port Scanner")
root.geometry("300x150")
root.resizable(False, False)
root.configure(bg="#f0f0f0")
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)
label_ip = tk.Label(input_frame, text="Enter IP Address:", bg="#f0f0f0")
label_ip.grid(row=0, column=0, padx=5, pady=5)
entry_ip = tk.Entry(input_frame)
entry_ip.grid(row=0, column=1, padx=5, pady=5)
label_port = tk.Label(input_frame, text="Enter Port Number:", bg="#f0f0f0")
label_port.grid(row=1, column=0, padx=5, pady=5)
entry_port = tk.Entry(input_frame)
entry_port.grid(row=1, column=1, padx=5, pady=5)
button_scan = tk.Button(button_frame, text="Scan", command=scan_port, bg="#4caf50", fg="white")
button_scan.pack(pady=5, ipadx=10, ipady=5)
root.mainloop()
