import customtkinter
from customtkinter import *
import os

root = customtkinter.CTk()
root.config(bg="Black")
root.title("Convert")
root.attributes("-alpha", 0.9)

def center_window():
    window_height = 250
    window_width = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
center_window()
def main(event):
    folder_location = entry.get()
    files_format = format.get()

    label.configure(text="Done!")
    import covertor

    covertor.main(folder_location, files_format)
    
    entry.delete(0, END)
    format.delete(0, END)

label = CTkLabel(root, text="Convert Folder contents format", font=("Acme", 20), bg_color="black", text_color="white")
label.pack(pady=10)

entry = CTkEntry(root, width=240, height=30, bg_color="black", placeholder_text="Folder Location EG: C:\\\\Users")
entry.pack(pady=20)
entry.tk_focusFollowsMouse()

format = CTkEntry(root, width=240, height=30, bg_color="black", placeholder_text="File format EG: mp3, mp4, png")
format.pack(pady=20)
format.tk_focusFollowsMouse()

reminder_label = CTkLabel(root, text="NB:This Process Converts every single file", font=("Pristina", 20), bg_color="black", text_color="white")#
reminder_label.pack(pady=20)


root.bind('<Return>', main)
root.mainloop()