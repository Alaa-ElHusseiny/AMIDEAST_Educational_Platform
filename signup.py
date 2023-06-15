from tkinter import*
from tkinter import messagebox
import ast
    

Sinup=Tk()
Sinup.geometry("1039x587+150+50")
Sinup.resizable(False,False)
Sinup.iconbitmap("G:\\python\\professional\\neural.ico")
Sinup.title("My graduation project")
lI=PhotoImage(file="G:\\python\\professional\\try1.png")
Li=Label(Sinup,image=lI,borderwidth=0,bd=0,highlightthickness=0)
Li.pack()





def SignUp():
    Username=user.get()
    Password=password.get()
    Confirm=confirm.get()
    if (Password==Confirm):
        try:
            file=open("datasheet.txt","r+")
            d=file.read()
            r=ast.literal_eval(d)
            dict2={Username:Password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open("datasheet.txt","w")
            w=file.write(str(r))
            messagebox.showinfo("sign up","signed up successfuly")

        except:
            file=open("datasheet.txt","w")
            pp=str({Username:Password})
            file.write(pp)
            file.close
    #else:
    #    messagebox.showerror("Invalid sign up","both passwords should match.")






l=PhotoImage(file="G:\\python\\professional\\llll.png")
L=Button(Sinup,image=l,borderwidth=0,highlightthickness=0)
L.place(x=728,y=0)
s=PhotoImage(file="G:\\python\\professional\\s.png")
S=Button(Sinup,image=s,borderwidth=0,highlightthickness=0)
S.place(x=885,y=0)
a=PhotoImage(file="G:\\python\\professional\\A.png")
A=Button(Sinup,image=a,borderwidth=0,highlightthickness=0)
A.place(x=570,y=0)
h=PhotoImage(file="G:\\python\\professional\\h.png")
H=Button(Sinup,image=h,borderwidth=0,highlightthickness=0)
H.place(x=408,y=0)

def loginH(e):
    lH=PhotoImage(file="G:\\python\\professional\\lh.png")
    L["image"]=lH
    L.image=lH
    L.place(x=728,y=0)
def loginN(l):
    l=PhotoImage(file="G:\\python\\professional\\llll.png")
    L["image"]=l
    L.image=l
    L.place(x=728,y=0)
def AboutH(e):
    aH=PhotoImage(file="G:\\python\\professional\\Ah.png")
    A["image"]=aH
    A.image=aH
    A.place(x=570,y=0)
def AboutN(l):
    a=PhotoImage(file="G:\\python\\professional\\A.png")
    A["image"]=a
    A.image=a
    A.place(x=570,y=0)
def signupH(e):
    SH=PhotoImage(file="G:\\python\\professional\\sh.png")
    S["image"]=SH
    S.image=SH
    S.place(x=885,y=0)
def signupN(l):
    s=PhotoImage(file="G:\\python\\professional\\s.png")
    S["image"]=s
    S.image=s
    S.place(x=885,y=0)
def homeH(e):
    hH=PhotoImage(file="G:\\python\\professional\\hh.png")
    H["image"]=hH
    H.image=hH
    H.place(x=408,y=0)
def homeN(l):
    h=PhotoImage(file="G:\\python\\professional\\h.png")
    H["image"]=h
    H.image=h
    H.place(x=408,y=0)


L.bind("<Enter>",loginH)
L.bind("<Leave>",loginN)
S.bind("<Enter>",signupH)
S.bind("<Leave>",signupN)
A.bind("<Enter>",AboutH)
A.bind("<Leave>",AboutN)
H.bind("<Enter>",homeH)
H.bind("<Leave>",homeN)
##################################################################################################################################################
#Sign up Frame
#################
signupF=Frame(Sinup,bg="#4472C4",width=400,height=420)
signupF.place(x=325,y=140)
LSign=Label(signupF,text="Sign up",fg="black",bg="#4472C4",font=("Calibri",24,"bold"),bd=0,highlightbackground="#05051A")
LSign.place(x=148,y=35)
LSign=Label(signupF,text="join us now!!",fg="#FF8A10",bg="#4472C4",font=("arial black",16,"bold"),bd=0,highlightbackground="#05051A")
LSign.place(x=120,y=72)
##################################################################################################################################################
def enterusersignup(e):
    if(user.get()=="Username"):
        user.delete(0,"end")
def leaveusersignup(e):
    if(user.get()==""):
        user.insert(0,"Username")

user=Entry(signupF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
user.insert(0,"Username")
user.place(x=40,y=130)
user.bind("<FocusIn>",enterusersignup)
user.bind("<FocusOut>",leaveusersignup)

l1=Frame(signupF,height=2,bg="black",width=300)
l1.place(x=40,y=161)
####################################################################################################################################################
def enterPassword(e):
    if(password.get()=="Password"):
        password.config(show="*")
        password.delete(0,"end")
def leavePassword(e):
    if(password.get()==""):
        password.insert(0,"Password")
        password.config(show="")

password=Entry(signupF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
password.insert(0,"Password")
password.place(x=40,y=195)
password.bind("<FocusIn>",enterPassword)
password.bind("<FocusOut>",leavePassword)

l1=Frame(signupF,height=2,bg="black",width=300)
l1.place(x=40,y=226)
####################################################################################################################################################
def enterConfirm(e):
    if(confirm.get()=="Confirm Password"):
        confirm.config(show="*")
        confirm.delete(0,"end")
        
def leaveConfirm(e):
    if(confirm.get()==""):
        confirm.insert(0,"Confirm Password")
        confirm.config(show="")

confirm=Entry(signupF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
confirm.insert(0,"Confirm Password")
confirm.place(x=40,y=260)
confirm.bind("<FocusIn>",enterConfirm)
confirm.bind("<FocusOut>",leaveConfirm)

l1=Frame(signupF,height=2,bg="black",width=300)
l1.place(x=40,y=291)
####################################################################################################################################################

def signinH(e):
    B1["font"]=("Calibri",14,"bold","underline")

def signinN(e):
    B1["font"]=("Calibri",14,"bold")

def hidePass():
    eyeP["image"]=hide
    password.config(show="*")
    eyeP.config(command=showP)

def hideCon():
    eyeC["image"]=hide
    confirm.config(show="*")
    eyeC.config(command=showC)


def showP():
    eyeP["image"]=unhide
    password.config(show="")
    eyeP.config(command=hidePass)

def showC():
    eyeC["image"]=unhide
    confirm.config(show="")
    eyeC.config(command=hideCon)

B2=Button(signupF,text="Sign up",fg="white",bg="#05051A",font=("Calibri",18,"bold"),command=SignUp,width=22,activebackground="#05051A",activeforeground="#FF8A10")
B2.place(x=40,y=325)
Label(signupF,text="I have an account?",bg="#4472C4",fg="black",font=("Calibri",12,"bold")).place(x=80,y=385)
B1=Button(signupF,text="Sign in",bg="#4472C4",fg="#FF8A10",font=("Calibri",14,"bold"),border=0,activebackground="#4472C4")
B1.place(x=220,y=380)
B1.bind("<Enter>",signinH)
B1.bind("<Leave>",signinN)
unhide=PhotoImage(file="G:\\python\\professional\\unhide.png")
hide=PhotoImage(file="G:\\python\\professional\\hide.png")
eyeC=Button(signupF,image=unhide,border=0,borderwidth=0,bd=0,highlightthickness=0,activebackground="#4472C4",command=showC)
eyeC.place(x=299,y=253)
eyeP=Button(signupF,image=unhide,border=0,borderwidth=0,bd=0,highlightthickness=0,activebackground="#4472C4",command=showP)
eyeP.place(x=299,y=188)
####################################################################################################################################################
Sinup.mainloop()


