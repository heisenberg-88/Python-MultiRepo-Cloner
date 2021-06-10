from os import name
from tkinter.constants import DISABLED, END, RIGHT, Y
from tkinter.font import names
from github import Github
import tkinter as gui
import threading
import time
from tkinter import messagebox

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

query_num_loop=gui.IntVar()
querynumber_entry=gui.Entry(root,textvariable=query_num_loop,font=('calibre',10, 'normal'))
querynumber_entry.pack()

def getaccess():
    access_token_string=token_var.get()
    print(access_token_string)

    ghtoken=Github(str(access_token_string))

    output.tag_config('warning', background="yellow", foreground="red")
    time.sleep(5.0)

    output.insert(END,f"{ghtoken.get_user()}\n",'warning')
    query="language:python"
    result=ghtoken.search_repositories(query)
    
    i=0
    for file in result:
        if(i==query_num_loop.get()):
            break
        output.insert('1.0',f"{file.name}\n")
        output.pack()
        i=i+1

    output.config(state=DISABLED)
    output.pack()
       
## making thread for smooth UI interface while background code running
def threadcreation():
    t=threading.Thread(target=getaccess)
    t.start()

def showWarning():
    messagebox.showwarning('WAIT !!!',"Script is running ,logs will be shown automatically in BLUE LogBox")

commandsList=lambda:[showWarning(),threadcreation()]
        
btnRead=gui.Button(root, height=1, width=20, text="Read Access Token", command=commandsList )
btnRead.configure(activebackground="yellow")
btnRead.pack(pady=5)


exitButton=gui.Button(root,height=1,width=20,text="Exit",command=lambda: root.destroy())
exitButton.pack()

root.mainloop()

