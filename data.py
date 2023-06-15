from tkinter import*
import os
import random
root = Tk()
root.geometry("500x500+400+120")
um=PhotoImage(file="photos\\trymain2.png")


def Usermain():
    global usermain
    usermain=Toplevel(root)
    usermain.geometry("1039x587+150+50")
    usermain.resizable(False,False)
    usermain.iconbitmap("photos\\neural.ico")
    usermain.title("My graduation project")
    UM=Label(usermain,image=um)
    UM.pack()
    Bm1=Button(usermain,text="Story generator",command=StorygeneratorW)
    Bm1.place(x=200,y=300)


def StorygeneratorW():
    global Storygenerator_window
    Storygenerator_window=Toplevel(usermain)
    Storygenerator_window.geometry("1039x587+150+50")
    Storygenerator_window.resizable(False,False)
    Storygenerator_window.iconbitmap("photos\\neural.ico")
    Storygenerator_window.title("My graduation project")
    UM=Label(Storygenerator_window,image=um)
    UM.pack()
    StoryButton=Button(Storygenerator_window,text="generate a story",command=storytextwindow,bg="#FF8A10",fg="white",font=("tajawal",18,"bold"))
    StoryButton.place(x=200,y=500)


def storytextwindow():
    stories=os.listdir("Stories")
    randomStoryfile=random.choice(stories)
    print(randomStoryfile)
    f=open("Stories\\"+randomStoryfile,"r")
    randomStory=str(f.read())
    print(randomStory)
    f.close()
    fL=open("Labels\\"+randomStoryfile+"Label.txt","r")
    randomStoryLabel=str(fL.read())
    print(randomStoryLabel)
    f.close()
    SF=Frame(Storygenerator_window,width=750,height=300,bg="#011A31")
    SF.place(x=50,y=150)
        
    L1=Label(SF,text=randomStory,fg="white",font=("tajawal",14,"bold"),bg="#011A31",wraplength=700,anchor="se")
    L1.place(x=10,y=60)
    L2=Label(SF,text=randomStoryLabel,fg="white",font=("tajawal",18,"bold"),bg="#011A31")
    L2.place(x=200,y=20)


B=Button(root,text="Next page",command=Usermain)
B.place(x=200,y=100)

root.mainloop()