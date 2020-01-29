import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
# root.minsize(400,400)
# root.configure(background="#330033")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

listofsongs = []
realnames = []

# root=Tk()
root.minsize(300,300)


# label_1=Label(root,text="age")
# label_2=Label(root,text="name")

# entry_1=Entry(root)
# entry_2=Entry(root)

# label_1.grid(row=8,sticky=E)
# label_2.grid(row=9,sticky=E)

# entry_1.grid(row=8,column=1)
# entry_2.grid(row=9,column=1)

# root.mainloop()


# name = input("enter your name: ")

# age = int(input("enter your age: "))

# song = input("what is your favorite genre?? : ")

# print(" hello " +name+ " your age is " +str(age)+ " and your favourite genre is " +song+ " thanks for downloading the app. if you have any questions about the app please email us")

# print("all rights reserved /n by dominic nyambane")


# song label (but not yet still working)
v = StringVar()
songlabel = Label(root,textvariable=v,width=35,background="violet",) 

index =0

# buttons functions(next, prev, stop, replay and label update when a song is playing)



def updatelabel():
    
    global index
    global songname
    v.set(realnames[index])
    return songname

def next(event):
    print("next music")
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    #return songname



def prev(event):
    print("previous music")
    global index
    index-= 1
    pygame.mixer.music.load(listofsongs[index])

    pygame.mixer.music.play()
    Updatelabel()
    #return songname


def stop(event):
    print("pause")
    pygame.mixer.music.stop()
    v.set("")
    #return songname


def replay(event):
    print("ewplay")
    pygame.mixer.music.replay()


def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    return songname




# prompt the user to choose directory section


def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            # print("select")

           # realdir = os.path.realpath(files)
           # audio = ID3(realdir)
           # realnames.append(audio['TIT2'].text[0])

           listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()




# layout colouring 


label = Label(root,text = 'feel the beat',background="#990026")
label.pack(fill=X,)

two = Label(root,background="#330066")
two.pack(fill=Y,side=LEFT)

three = Label(root,background="#330066")
three.pack(fill=Y,side=RIGHT)

four = Label(root,background="#330066")
four.pack(fill=Y,side=LEFT)

five = Label(root,background="#330066")
five.pack(fill=Y,side=RIGHT)

six = Label(root,background="#330066")
six.pack(fill=X,side=BOTTOM)

seven = Label(root,background="#330066")
seven.pack(fill=X,side=BOTTOM)

eight = Label(root,background="#330066")
eight.pack(fill=X,side=TOP)

nine = Label(root,background="#003300")
nine.pack(fill=X,side=BOTTOM)

ten = Label(root,background="#003300")
ten.pack(fill=X,side=TOP)

eleven = Label(root,background="#003300")
eleven.pack(fill=Y,side=LEFT)

twelve = Label(root,background="#003300")
twelve.pack(fill=Y,side=RIGHT)



# label_image.configure(background="blue")
# label.pack()

# label_image.config(bg="black")

listbox = Listbox(root,background="grey")
listbox.pack()

listofsongs.reverse()


for items in listofsongs:
    listbox.insert(0,items)

listofsongs.reverse()
# buttons section 


nextbutton = Button(root,text = 'next',bg="orange",fg="red")
nextbutton.pack(side=LEFT)

previousbutton = Button(root,text = 'prev', background="orange",fg="red")
previousbutton.pack(side=RIGHT)

stopbutton = Button(root,text = 'stop', background="orange",fg="red")
stopbutton.pack(side=LEFT)

replaybutton = Button(root,text = 'replay', background="orange",fg="red")
replaybutton.pack(side=RIGHT)

songlabel.pack(fill=Y,side=BOTTOM,)


nextbutton.bind("<Button-1>",next)
previousbutton.bind("<Button-1>",prev)
# stopbutton.bind("<Button-l>",stop)
# replaybutton.bind("<Button>",replay)



root.mainloop()
