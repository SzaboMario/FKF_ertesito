from datetime import datetime as dt
from plyer import notification
from tkinter import messagebox

def Universal_noti(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None, 
        timeout=20,  
    )


def Console_log(message):
    with open("Log.txt", "a", encoding = "utf-8") as file:
        file.writelines(f"{dt.now()}: {message}")