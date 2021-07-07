from tkinter import *

root=Tk()
root.title("Vigenere Cipher")
root.geometry("660x400")
root.resizable(False,False)
CaesarImg=PhotoImage(file="vigenere.gif")
Radval=IntVar()
Startchar=64
Endchar=91

def RadioSelect():
    if Enterbox.get()=="":
        Enterbox.insert(0,"The undecipherble cipher")
    if Keybox.get()=="":
        Keybox.insert(0,"Keyword")
    Keylist=[((ord(let.upper()))-Startchar) for let in Keybox.get()]
    if Radval.get()==1:
        Encode(Startchar,Endchar,Keylist)
    else:
        Decode(Startchar,Endchar,Keylist)

def Encode(Startchr,Endchr,Keylst):
    ResultLabel.configure(text="Encoded Text")
    EncStr=""
    Keynum=0
    Keylen=len(Keylst)
    uptext=(Enterbox.get()).upper()
    for char in uptext:
        if ord(char)>=Startchr and ord(char)<=Endchr:
            EncChar=((ord(char)-Startchr+(Keylst[Keynum%Keylen]-1))%26)+1
            EncStr+=chr(EncChar+Startchr)
            Keynum+=1
        else:
            EncStr+=char
    Resultbox.configure(text=EncStr)

def Decode(Startchr,Endchr,Keylst):
    ResultLabel.configure(text="Decoded Text")
    DecStr=""
    Keynum=0
    Keylen=len(Keylst)
    uptext=(Enterbox.get()).upper()
    for char in uptext:
        if ord(char)>=Startchr and ord(char)<=Endchr:
            DecChar=((ord(char)-Startchr+(25-(Keylst[Keynum%Keylen])))%26)+1
            DecStr+=chr(DecChar+Startchr)
            Keynum+=1
        else:
            DecStr+=char
    return Resultbox.configure(text=DecStr)

RBtn1=Radiobutton(root,text="To Encode",variable=Radval,value=1,command=RadioSelect)
RBtn2=Radiobutton(root,text="To Decode",variable=Radval,value=2,command=RadioSelect)
ImageLabel=Label(root,image=CaesarImg,relief=SUNKEN)
EnterLabel=Label(root,text="Original Text",relief=SUNKEN)
Enterbox=Entry(root,width=90,relief=SUNKEN)
KeyLabel=Label(root,text="Keyword",relief=SUNKEN)
Keybox=Entry(root,width=90, relief=SUNKEN)
ResultLabel=Label(root,text="             ",relief=SUNKEN)
Resultbox=Label(root,width=77,relief=SUNKEN,anchor=W)

RBtn1.place(x=250,y=150)
RBtn2.place(x=450,y=150)
ImageLabel.place(x=10,y=120)
EnterLabel.place(x=10,y=20)
Enterbox.place(x=100,y=20)
KeyLabel.place(x=10,y=50)
Keybox.place(x=100,y=50)
ResultLabel.place(x=10,y=80)
Resultbox.place(x=100,y=80)





root.mainloop()
