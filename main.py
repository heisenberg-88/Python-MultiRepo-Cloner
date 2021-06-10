from os import name, stat
from tkinter.constants import DISABLED, END, RIGHT, Y
from tkinter.font import names
from github import Github
import tkinter as gui
import threading
from tkinter import StringVar, messagebox
from tkinter import filedialog

root=gui.Tk()
root.configure(background='black')
root.title("Github-TraningData-Collector-for-pythonTransformers")
root.geometry('700x700')

## initial strings for access token & folder to save cloned repo
access_token_string=""
folder_for_cloning=""

## First Label above the access token entry widget , token_var is saving String variable from entry widget
token_var=gui.StringVar()
token_label = gui.Label(root, text = 'Github-Access-Token', font=('calibre',10, 'bold'))
token_label.configure(background='black',foreground='white')
token_label.pack()

## Entry Widget to enter gh access token
token_entry = gui.Entry(root,textvariable = token_var, font=('calibre',10,'normal'))
token_entry.config(show="*")
token_entry.pack(ipadx=200)

## Output Text Widget for showing logs of repo names
output = gui.Text(root, height = 20, width = 85, background = "blue")

## Label above number of queries entry widget
querynumlooplabel=gui.Label(root,text="Enter number of queries:",font=('calibre',10, 'bold'))
querynumlooplabel.configure(background='black',foreground='white')
querynumlooplabel.pack()

## Entry widget to enter number of queries , query_num_loop is saving int variable from Entry widget
query_num_loop=gui.IntVar()
querynumber_entry=gui.Entry(root,textvariable=query_num_loop,font=('calibre',10, 'normal'))
querynumber_entry.pack()

## Entry widget for Query time span 
query_span_tosearch=gui.Label(root,text="Enter time span of query ( yyyy-mm-dd..yyyy-mm-dd ) i.e. Start Date..End Date",font=('calibre',10, 'bold'))
query_span_tosearch.configure(background='black',foreground='white')
query_span_tosearch.pack()

## query_span_var saves String variable from entry widget
query_span_var=StringVar()
query_span_entry=gui.Entry(root,textvariable=query_span_var,font=('calibre',10,'normal'))
query_span_entry.pack(padx=100)

## Label above cloned repo saving folder selector button
directory_clone_label=gui.Label(root,text="Folder for saving cloned repos",font=('calibre',10, 'bold'))
directory_clone_label.configure(background='black',foreground='white')
directory_clone_label.pack()

## Text widget to show Directory path selected from button
directory_text_show=gui.Text(root,height=1,width=75,background='yellow',foreground='red')




## main function that creates github token object and shows repo names in output widget
def getaccess():
    access_token_string=token_var.get()

    ghtoken=Github(str(access_token_string))

    output.tag_config('warning', background="yellow", foreground="red")
    output.insert('1.0',f"{ghtoken.get_user()}\n",'warning')
    
    query=f"language:python created:{query_span_var.get()}"
    result=ghtoken.search_repositories(query)
    
    ## the for loop below will only run query_num_loop times
    i=0
    for file in result:
        if(i==query_num_loop.get()):
            break
        output.insert('1.0',f"{file.name}  cloneurl: {file.clone_url} \n")
        output.pack()
        i=i+1

    ## state=disable disables write acces to the output window
    output.config(state=DISABLED)
    output.pack()





## making thread for smooth UI interface while background code running
def threadcreation():
    t=threading.Thread(target=getaccess)
    t.start()




## warning message box and conditional statements 
def showWarning():
    if(token_var.get()==""):
        messagebox.showwarning('ERROR !!',"Please Enter valid github access token")
    elif(query_num_loop.get()>0):
        messagebox.showwarning('WAIT !!!',"Script is running ,logs will be shown automatically in BLUE LogBox")
    else:
        messagebox.showwarning('ERROR!!!' , "Close the program & Enter number of queries greater than 0")
    



## directory selecting function
def askingDIR():
    folder_for_cloning=filedialog.askdirectory()
    directory_text_show.insert("1.0",str(folder_for_cloning))
    directory_text_show.config(state=DISABLED)
    directory_text_show.pack()




## directory selection button is declared here
dirButton=gui.Button(root,height=1,width=20,text="Select Directory",command=askingDIR)
dirButton.configure(activebackground="yellow")
dirButton.pack()
    


## Creating multiple command list for single button btnRead
commandsList=lambda:[showWarning(),threadcreation()]


## Creating Button for Read access token , uses getaccess function and show warning functiom       
btnRead=gui.Button(root, height=1, width=15, text="Read Access Token", command=commandsList )
btnRead.configure(activebackground="yellow")
btnRead.pack(pady=6)


## Exit button to exit the window
exitButton=gui.Button(root,height=1,width=10,text="Exit",command=lambda: root.destroy())
exitButton.pack(pady=5)

root.mainloop()

