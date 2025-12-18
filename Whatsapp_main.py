import tkinter as tk
from tkinter import messagebox
import pywhatkit
from datetime import datetime, timedelta

# ---------- Functions ----------
def send_message():
    mobile = entry_mobile.get().strip()
    message = text_message.get("1.0", tk.END).strip()

    if not mobile.startswith("+"):
        messagebox.showerror("Error", "Enter mobile number with country code (+91...)")
        return

    if not message:
        messagebox.showerror("Error", "Message cannot be empty")
        return

    status_label.config(text="Opening WhatsApp Web...", fg="#075E54")
    root.update()

    time = datetime.now() + timedelta(minutes=3)

    try:
        pywhatkit.sendwhatmsg(
            mobile,
            message,
            time.hour,
            time.minute
        )
        status_label.config(
            text="Message scheduled successfully ✔",
            fg="green"
        )
    except Exception as e:
        status_label.config(text="Failed to send message ❌", fg="red")
        messagebox.showerror("Error", str(e))


def clear_fields():
    entry_mobile.delete(0, tk.END)
    text_message.delete("1.0", tk.END)
    status_label.config(text="")


# ---------- UI ----------
root = tk.Tk()
root.title("PyWhatsApp Web Sender")
root.geometry("450x450")
root.resizable(False, False)
root.configure(bg="#ECE5DD")

# Header
header = tk.Frame(root, bg="#075E54", height=60)
header.pack(fill="x")

tk.Label(
    header,
    text="PyWhatsApp Web Sender",
    bg="#075E54",
    fg="white",
    font=("Segoe UI", 18, "bold")
).pack(pady=12)

# Main Frame
main = tk.Frame(root, bg="#ECE5DD")
main.pack(pady=20)

tk.Label(
    main,
    text="Mobile Number",
    bg="#ECE5DD",
    font=("Segoe UI", 10, "bold")
).grid(row=0, column=0, sticky="w")

entry_mobile = tk.Entry(
    main,
    width=35,
    font=("Segoe UI", 10)
)
entry_mobile.grid(row=1, column=0, pady=5)

tk.Label(
    main,
    text="Message",
    bg="#ECE5DD",
    font=("Segoe UI", 10, "bold")
).grid(row=2, column=0, sticky="w", pady=(10, 0))

text_message = tk.Text(
    main,
    width=35,
    height=5,
    font=("Segoe UI", 10),
    wrap="word"
)
text_message.grid(row=3, column=0, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#ECE5DD")
btn_frame.pack(pady=10)

send_btn = tk.Button(
    btn_frame,
    text="Send Message",
    command=send_message,
    bg="#25D366",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15,
    relief="flat"
)
send_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    command=clear_fields,
    bg="#DDDDDD",
    fg="black",
    font=("Segoe UI", 11),
    width=10,
    relief="flat"
)
clear_btn.grid(row=0, column=1)

# Status Bar
status_label = tk.Label(
    root,
    text="",
    bg="#ECE5DD",
    font=("Segoe UI", 9)
)
status_label.pack(side="bottom", pady=5)

root.mainloop()
