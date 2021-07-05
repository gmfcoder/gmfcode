from tkinter import *

root=Tk()
root.title("Caesar Cipher")
root.geometry("660x400")
root.resizable(False,False)
CaesarImg=PhotoImage(file="caesar1.gif")
Radval=IntVar()
Shiftval=IntVar()
Startchar=64
Endchar=91

def RadioSelect():
    Shift=Shiftval.get()
    if Radval.get()==1:
        Encode(Startchar,Endchar,Shift)
    else:
        Decode(Startchar,Endchar,Shift)

def Encode(Startchr,Endchr,Shft):
    ResultLabel.configure(text="Encoded Text")
    EncStr=""
    uptext=(Enterbox.get()).upper()
    for char in uptext:
        if ord(char)>=Startchr and ord(char)<=Endchr:
            EncChar=((ord(char)-Startchr+(Shft-1))%26)+1
            EncStr+=chr(EncChar+Startchr)
        else:
            EncStr+=char
    Resultbox.configure(text=EncStr)

def Decode(Startchr,Endchr,Shft):
    ResultLabel.configure(text="Decoded Text")
    DecStr=""
    uptext=(Enterbox.get()).upper()
    for char in uptext:
        if ord(char)>=Startchr and ord(char)<=Endchr:
            DecChar=((ord(char)-Startchr+(25-Shft))%26)+1
            DecStr+=chr(DecChar+Startchr)
        else:
            DecStr+=char
    return Resultbox.configure(text=DecStr)

RBtn1=Radiobutton(root,text="To Encode",variable=Radval,value=1,command=RadioSelect)
RBtn2=Radiobutton(root,text="To Decode",variable=Radval,value=2,command=RadioSelect)
ShiftScale=Scale(root,from_=1, to=25,label="Shift Value",orient=HORIZONTAL,length=300,tickinterval=4,variable=Shiftval)
ImageLabel=Label(root,image=CaesarImg,relief=SUNKEN)
EnterLabel=Label(root,text="Original Text",relief=SUNKEN)
Enterbox=Entry(root,width=90,relief=SUNKEN)
ResultLabel=Label(root,text="             ",relief=SUNKEN)
Resultbox=Label(root,width=77,relief=SUNKEN,anchor=W)

RBtn1.place(x=250,y=150)
RBtn2.place(x=450,y=150)
ShiftScale.place(x=250,y=250)
ImageLabel.place(x=10,y=80)
EnterLabel.place(x=10,y=20)
Enterbox.place(x=100,y=20)
ResultLabel.place(x=10,y=50)
Resultbox.place(x=100,y=50)





root.mainloop()
