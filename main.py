from os import name
from tkinter.constants import DISABLED, END, RIGHT, Y
from tkinter.font import names
from github import Github
import tkinter as gui
import threading


root=gui.Tk()
root.configure(background='black')
root.title("Github-TraningData-Collector-for-pythonTransformers")
root.geometry('700x450')

access_token_string="invalid"



##Below code is for fetching the github access token from gui
token_var=gui.StringVar()
token_label = gui.Label(root, text = 'Github-Access-Token', font=('calibre',10, 'bold'))
token_label.configure(background='black',foreground='white')
token_label.pack()

token_entry = gui.Entry(root,textvariable = token_var, font=('calibre',10,'normal'))
token_entry.config(show="*")
token_entry.pack(ipadx=200)

output = gui.Text(root, height = 20, width = 85, background = "blue")


def getaccess():
    access_token_string=token_var.get()
    print(access_token_string)

    ghtoken=Github(str(access_token_string))


    # output.insert(END,f"{ghtoken.get_user()}\n")
    query="language:python"
    result=ghtoken.search_repositories(query)

    # output.insert(END,f"{result.totalCount}")
    
    for file in result:
        output.insert('1.0',f"{file.name}\n")
        output.config(state=DISABLED)
        output.pack()
        
## making thread for smooth UI interface while background code running
def threadcreation():
    t=threading.Thread(target=getaccess)
    t.start()
        
btnRead=gui.Button(root, height=1, width=20, text="Read Access Token", command=threadcreation )
btnRead.configure(activebackground="yellow")
btnRead.pack(pady=5)


root.mainloop()

