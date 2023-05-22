from win10toast import ToastNotifier
import requests as reqlib
import os, json, time
from tkinter import *
import tkinter
verurl = "http://setup.roblox.com/version.txt"
verst = reqlib.get(url=verurl).text
toast = ToastNotifier()
try:
    f = open("settings.json", "r")
except:
    print("Create a settings.json file, please look to docs")
    time.sleep(10)
    
settsjson = f.read()
print(settsjson)
f.close()
settsdict = json.loads(settsjson)
locals().update(settsdict)
if username == "":
    print("Set your appdata username in settings.json")
toast.show_toast(
    "Roblox Version Notifier Started!",
    f"The Newest version is {verst}",
    duration = secstart,
    icon_path = icon,
    threaded = True,
)
while 1:
    while time.sleep(check):
        nver = reqlib.get(url=verurl).text
        if nver is not verst:
            if auto == True:
                toast.show_toast(
                "New Roblox Update!",
                f"New roblox update came out: {ver}, updating.",
                duration = secs,
                icon_path = icon,
                threaded = True,
                )
                root = Tk()
                root.title("ROBLOX Player")
                root.geometry("362x130")
                root.iconbitmap("assets/Roblox.ico")
                image = tkinter.PhotoImage(file="assets/updateapp.png")
                tkinter.Label(root, image=image).pack()
                root.resizable(False, False)
                root.update()
                time.sleep(5)
                os.system(f"C:/Users/{username}/AppData/Local/Roblox/Versions/{verst}/RobloxPlayerLauncher.exe")
            else:
               toast.show_toast(
                "New Roblox Update!",
                f"New roblox update came out: {ver}.",
                duration = secs,
                icon_path = icon,
                threaded = True,
                ) 
            