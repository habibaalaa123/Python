from tkinter import *
from tkinter import filedialog, ttk
from pygame import mixer
import os
root=Tk()
root.title('Music player ')
root.geometry("900x400+290+85")
root.configure(bg= "#0f1a2b")
root.resizable(False, False)
logo=PhotoImage(file="index-media-cover-art-play-button-overlay-5.png")
label=Label(root, image=logo, bg="#212121"). place(x=100,y=50,width=150,height=150)
mixer.init()
playlist=Listbox()
def Open_Folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)
def Play():
    music_name=playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

play_button=Button(root, text="Play",width=15, height=2,font=("arial",10,"bold"), command=Play(),bg="#7FB3D5").place(x=120,y=250)
stop_button=Button(master=root, text="Stop",width=15, height=2,font=("arial",10,"bold"), command=mixer.music.stop(),bg="#7FB3D5").place(x=30,y=300)
pause_button=Button(master=root, text="Pause",width=15, height=2,font=("arial",10,"bold"), command=mixer.music.pause(),bg="#7FB3D5").place(x=200,y=300)
folder_button=Button(root, text="Open Folder", width=15, height=2,font=("arial",10,"bold"),bg="#7FB3D5",command=Open_Folder()).place(x=330,y=50)
frame=Frame(root,bd=2, relief=RIDGE)
frame.place(x=330,y=100, width=560, height=250)
scroll=Scrollbar(frame)
playlist=Listbox(frame,font=100,bg="#333333", fg="grey", selectbackground="lightblue",cursor="hand2",yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop() 