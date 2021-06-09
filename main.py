from github import Github
import tkinter as gui


root=gui.Tk()
root.title("Github-TraningData-Collector-for-pythonTransformers")
root.geometry('700x450')

access_token_string="invalid"

##Below code is for fetching the github access token from gui
token_var=gui.StringVar()
token_label = gui.Label(root, text = 'Github-Access-Token', font=('calibre',10, 'bold'))
token_label.pack()

token_entry = gui.Entry(root,textvariable = token_var, font=('calibre',10,'normal'))
token_entry.config(show="*")
token_entry.pack(ipadx=200)



def getaccess():
    access_token_string=token_var.get()
    print(access_token_string)

    ghtoken=Github(str(access_token_string))

    print(ghtoken.get_user())

    query="language:python"
    result=ghtoken.search_repositories(query)
    print(result.totalCount)

    for file in result:
        print(file.name)



btnRead=gui.Button(root, height=1, width=10, text="Read", command=getaccess)
btnRead.pack()

root.mainloop()

