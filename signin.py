from tkinter import*
root=Tk()
root.geometry("1039x587+150+50")
root.resizable(False,False)
root.iconbitmap("photos\\neural.ico")
root.title("My graduation project")
BI=PhotoImage(file="photos\\homefinal2.png")
bi=Label(root,image=BI)
bi.pack()
SI=PhotoImage(file="photos\\homefinal3.png")


root.mainloop()