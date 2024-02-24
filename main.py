from copy_checker_ai_checker import copy_checker_ai_checker
from tkinter import *
from tkinter import filedialog
import messagebox
from mail_life import mail_life_checker


def callback():
    name = filedialog.askopenfilename()
    file_path_text.config(text=name)


def check_insert():
    mail_life = mail_life_checker(Enter_system_id_text.get())
    life = mail_life.life
    gmail = mail_life.gmail
    if len(Enter_system_id_text.get()) > 3 and len(Enter_gmail_text.get()) > 3 and len(file_path_text.cget("text")) > 4:
        with open(file_path_text.cget("text"), encoding="utf-8", errors="ignore") as file:
            text = "".join(file.read().split("\n"))
            if life > 0:
                if copy_checker_ai_checker(text).send_check():
                    with open(
                            f"C:/Users/HP/Documents/Programming/Python/plagiarism project/data/{Enter_system_id_text.get()}.txt",
                            mode="w", errors="ignore") as file_to_be_stored:
                        file_to_be_stored.write(text)
                else:
                    messagebox.showwarning(title="Plagiarism detected",
                                           message=f"The assignment that you are submitting is not original\nYou have {life} remaining")
                    mail_life.decrease_life()
            else:
                messagebox.showwarning(title="Error", message="You can no longer submit your assignment")
    else:
        messagebox.showwarning(title="Warning", message="Data submitted was incorrect")


window = Tk()
window.title("Document copy checker")
window.geometry("500x500")

Enter_system_id = Label(text="Enter your system id")
Enter_system_id.grid(row=0, column=0, padx=(50, 20), pady=(50, 20))

Enter_system_id_text = Entry(width=40)
Enter_system_id_text.grid(row=0, column=1, padx=(0, 20), pady=(50, 20))

Enter_gmail_label = Label(text="Enter your gmail:")
Enter_gmail_label.grid(row=1, column=0, padx=(40, 0))

Enter_gmail_text = Entry(width=40)
Enter_gmail_text.grid(row=1, column=1, padx=(0, 20))

file_button = Button(text="File path", command=callback, width=10)
file_button.grid(row=2, column=0, padx=(40, 0), pady=(20, 0))

file_path_text = Label(text="", wraplength=250)
file_path_text.grid(row=2, column=1, padx=(0, 20), pady=(20, 0))

submit = Button(text="Submit", command=check_insert)
submit.grid(row=3, column=0, columnspan=2, padx=(30, 0))

window.mainloop()
