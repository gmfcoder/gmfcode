from tkinter import *

root=Tk()
root.title("Playfair\Wheatstone Cipher")
root.geometry("660x450")
root.resizable(False,False)
PlayfairImg=PhotoImage(file="wheatstone.gif")
Radval=IntVar()


def DivideList(Lst,GrpNum):
    for i in range(0,len(Lst),GrpNum):
        yield Lst[i:i+GrpNum]

def RadioSelect():
    if Enterbox.get()=="":
        Enterbox.insert(0,"Hide the gold in the tree stump")
    if Keybox.get()=="":
        Keybox.insert(0,"Playfair example")
    TextString,SpaceList=Textcreate(Enterbox.get(),[])
    KeyList=Keycreate(Keybox.get())
    PflabDisplay(KeyList)
    if Radval.get()==1:
        Encode(KeyList,TextString,SpaceList)
    else:
        Decode(KeyList,TextString,SpaceList)

def Encode(KeyLst,PlainTxt,SpaceLst):
    ResultLabel.configure(text="Encoded Text")
    EncTxt=""
    for txtpair in range(0,len(PlainTxt),2):
        for ind in range(0,5):
            if PlainTxt[txtpair] in KeyLst[ind]:
                Keyindy1=ind
                Keyindx1=KeyLst[ind].index(PlainTxt[txtpair])
            if PlainTxt[txtpair+1] in KeyLst[ind]:
                Keyindy2=ind
                Keyindx2=KeyLst[ind].index(PlainTxt[txtpair+1])

        #Playfair row rule
        if Keyindy1==Keyindy2:
            EncLet1=KeyLst[Keyindy1][(Keyindx1+1)%5]
            EncLet2=KeyLst[Keyindy2][(Keyindx2+1)%5]
            EncTxt+=EncLet1+EncLet2

            #playfair column rule
        elif Keyindx1==Keyindx2:
            EncLet1=KeyLst[(Keyindy1+1)%5][Keyindx1]
            EncLet2=KeyLst[(Keyindy2+1)%5][Keyindx2]
            EncTxt+=EncLet1+EncLet2

            #playfair box rule
        else:
            EncLet1=KeyLst[Keyindy1][Keyindx2]
            EncLet2=KeyLst[Keyindy2][Keyindx1]
            EncTxt+=EncLet1+EncLet2

    for item in SpaceLst:
        EncTxt=EncTxt[:item]+" "+EncTxt[item:]

    Resultbox.configure(text=EncTxt)

def Decode(KeyLst,PlainTxt,SpaceLst):
    ResultLabel.configure(text="Decoded Text")
    DecTxt=""
    for txtpair in range(0,len(PlainTxt),2):
        for ind in range(0,5):
            if PlainTxt[txtpair] in KeyLst[ind]:
                Keyindy1=ind
                Keyindx1=KeyLst[ind].index(PlainTxt[txtpair])
            if PlainTxt[txtpair+1] in KeyLst[ind]:
                Keyindy2=ind
                Keyindx2=KeyLst[ind].index(PlainTxt[txtpair+1])

        #Playfair row rule
        if Keyindy1==Keyindy2:
            EncLet1=KeyLst[Keyindy1][(Keyindx1-1)]
            EncLet2=KeyLst[Keyindy2][(Keyindx2-1)]
            DecTxt+=EncLet1+EncLet2

            #playfair column rule
        elif Keyindx1==Keyindx2:
            EncLet1=KeyLst[(Keyindy1-1)][Keyindx1]
            EncLet2=KeyLst[(Keyindy2-1)][Keyindx2]
            DecTxt+=EncLet1+EncLet2

            #playfair box rule
        else:
            EncLet1=KeyLst[Keyindy2][Keyindx1]
            EncLet2=KeyLst[Keyindy1][Keyindx2]
            DecTxt+=EncLet2+EncLet1

    print(DecTxt)

    for item in SpaceLst:
        DecTxt=DecTxt[:item]+" "+DecTxt[item:]

    Resultbox.configure(text=DecTxt)

def Keycreate(KeyStr):
    Key=[item for item in KeyStr.upper() if ord(item)>=65 and ord(item)<=91]
    Atoz=[chr(item) for item in range(65,91) if item !=74]
    KeyList=[]
    for item in Key:
        if item not in Atoz:
            continue
        else:
            KeyList.append(item)
            Atoz.remove(item)
    KeyList+=Atoz
    KeyList=list(DivideList(KeyList,5))
    return KeyList

def Textcreate(PlainStr,SpaceLst):
    TextStr=""
    PlainStr=PlainStr.upper()
    for item in range(0,len(PlainStr)):
        if ord(PlainStr[item])<65 or ord(PlainStr[item])>91:
            if ord(PlainStr[item])==32:
                SpaceLst.append(item)
            else:
                continue
        else:
            TextStr+=PlainStr[item]
    TextStr=TextStr.replace("J","I")
    for n in range(1,len(TextStr),2):
        if TextStr[n-1]==TextStr[n]:
            TextStr=TextStr[0:n]+"X"+TextStr[n:]
    if len(TextStr)%2!=0:
        TextStr+="X"

    return TextStr,SpaceLst

def PflabDisplay(KeyLst):
    PflabList=[]
    for row in range(0,5):
        for col in range(0,5):
            PflabList.append(Label(root,height=2,width=3,text=KeyLst[row][col],relief=SUNKEN))
            PflabList[-1].place(x=350+(30*col),y=220+(30*row))
    return

RBtn1=Radiobutton(root,text="To Encode",variable=Radval,value=1,command=RadioSelect)
RBtn2=Radiobutton(root,text="To Decode",variable=Radval,value=2,command=RadioSelect)
ImageLabel=Label(root,image=PlayfairImg,relief=SUNKEN)
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
