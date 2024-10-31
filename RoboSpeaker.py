# -------------------------- Text to Voice ------------------------>>>




# WITHOUT UI/UX
# import os
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1. Created by Divv")
#     while True:
#         x = input("Enter what you want me to Speak: ")
#         if x=="q":
#             os.system("say 'bye bye friend'")
#             break
#         command = f"say {x}"
#         os.system(command)





# WITH UI/UX
import os
import tkinter as tk

from tkinter import messagebox
def speak():
    text = entry.get()
    if text.lower() == 'q':
        os.system("say 'bye bye friend'")
        root.quit()  # Closes the app
    elif text.strip() == "":
        messagebox.showwarning("RoboSpeaker", "Please enter some text.")
    else:
        command = f"say '{text}'"
        os.system(command)
        messagebox.showinfo("RoboSpeaker", f"Speaking: {text}")
        entry.delete(0, tk.END)  

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()


def on_enter(e):
    speak_button.config(bg="#00b894", fg="white")

def on_leave(e):
    speak_button.config(bg="#55efc4", fg="#2d3436")


root = tk.Tk()
root.title("RoboSpeaker 1.1")
root.geometry("480x320")
root.config(bg="#2d3436")  

title_font = ("Arial", 24, "bold")
button_font = ("Arial", 14, "bold")
entry_font = ("Arial", 16)

header_frame = tk.Frame(root, bg="#00cec9", height=100)
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="RoboSpeaker 1.1", font=title_font, fg="white", bg="#00cec9")
title_label.pack(pady=20)

main_frame = tk.Frame(root, bg="#2d3436")
main_frame.pack(pady=20)

entry = tk.Entry(main_frame, width=30, font=entry_font, bg="#dfe6e9", fg="#2d3436", bd=0, relief="solid", justify="center")
entry.pack(pady=10, ipady=10)


speak_button = tk.Button(main_frame, text="Speak", font=button_font, bg="#55efc4", fg="#2d3436", width=10, bd=0, cursor="hand2", activebackground="#00b894", activeforeground="white", relief="flat")
speak_button.pack(pady=10, ipady=5)
speak_button.bind("<Enter>", on_enter)  

speak_button.config(command=speak)

exit_label = tk.Label(main_frame, text="Enter 'q' to exit", font=("Arial", 10), bg="#2d3436", fg="#dfe6e9")
exit_label.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
