import tkinter as tk
from tkinter import messagebox
import pywhatkit
from datetime import datetime, timedelta

def send_message():
    mobile = entry_mobile.get()
    message = text_message.get("1.0", tk.END).strip()

    if not mobile or not message:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Schedule message 3 minutes later
    time = datetime.now() + timedelta(minutes=3)

    try:
        pywhatkit.sendwhatmsg(
            mobile,
            message,
            time.hour,
            time.minute
        )
        messagebox.showinfo(
            "Success",
            "WhatsApp Web will open.\nMessage will be sent in 3 minutes."
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- UI ----------------
root = tk.Tk()
root.title("WhatsApp Message Sender")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="WhatsApp Message Sender", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Mobile Number (+91...)").pack()
entry_mobile = tk.Entry(root, width=30)
entry_mobile.pack(pady=5)

tk.Label(root, text="Message").pack()
text_message = tk.Text(root, height=5, width=30)
text_message.pack(pady=5)

tk.Button(
    root,
    text="Send Message",
    command=send_message,
    bg="green",
    fg="white",
    font=("Arial", 12)
).pack(pady=15)

root.mainloop()
