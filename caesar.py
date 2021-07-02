from tkinter import *

root=Tk()
root.title("Caesar Cipher")
root.geometry("600x250")
root.resizable(False,False)

Radval=IntVar()
shift=2

def Select():
    if Radval.get()==1:
        Encode()
    else:
        Decode()

def Encode():
    ResultLabel.configure(text="Encoded Text")
    EncStr=""
    uptext=(Enterbox.get()).upper()
    for char in uptext:
        if ord(char)>64 and ord(char)<91:
            Encchar=(ord(char)-64)%26
            EncStr+=chr(Encchar+(64+shift))
        else:
            EncStr+=char
    Resultbox.configure(text=EncStr)
    return

def Decode():
    ResultLabel.configure(text="Decoded Text")
    DecStr=""
    uptext=(Enterbox.get()).upper()
    for char in uptext:
        if ord(char)>64 and ord(char)<91:
            Decchar=(ord(char)-64)%26
            DecStr+=chr(Decchar+(64-shift))
        else:
            DecStr+=char
    Resultbox.configure(text=DecStr)
    return


RBtn1=Radiobutton(root,text="Encode",variable=Radval,value=1,command=Select)
RBtn2=Radiobutton(root,text="Decode",variable=Radval,value=2,command=Select)
EnterLabel=Label(root,text="Original Text",relief=RAISED)
Enterbox=Entry(root,width=76,relief=SUNKEN)
ResultLabel=Label(root,text="            ",relief=RAISED)
Resultbox=Label(root,width=65,relief=SUNKEN)

RBtn1.place(x=50,y=150)
RBtn2.place(x=50,y=180)
EnterLabel.place(x=10,y=20)
Enterbox.place(x=100,y=20)
ResultLabel.place(x=10,y=50)
Resultbox.place(x=100,y=50)





root.mainloop()
