# This class manage all window activites(widget)
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from video import Video
import random
import os
class Window(Video):
    def __init__(self,root):
        Video.__init__(self)
        self.root= root
        self.root.title("InfyU LABS")
        self.root.geometry("1000x700+200+10")
        self.root.resizable(0,0)
        
        #This main frame
        self.frame= Frame(self.root,bg="#1261A0")
        self.frame.place(x=0,y=0,width=1000,height=700)

        butn1=Button(self.frame,text="Upload Video",font=("Helvetica", "16"),command=self.uploadVideo)
        butn1.place(x=300,y=600)
        butn1=Button(self.frame,text="Close App",font=("Helvetica", "16"),command=self.closeApp)
        butn1.place(x=500,y=600)
        picLable=Label(self.frame,background='white',text="Videos Frames",font=("Helvetica", "16"))
        picLable.place(x=400,y=10)

        self.videoFrame()
        self.showSinglePic("./img/submit.jpeg")

    def closeApp(self):
        self.root.destroy()
    # For making Frame to show pic after processing   
    def videoFrame(self):
        self.framLable=Label(self.frame)
        self.framLable.place(x=20,y=50,width=960,height=540)
    #this is called by button uploadVideos    
    def uploadVideo(self):
        fileName=filedialog.askopenfile( initialdir="~/Videos",title="Select A Video File",filetypes=[('Videos File',['.mp4','.mkv'])])

        self.saveFrame(fileName.name)
        self.framLable.destroy()
        self.infoShow()
    # Function for showing random image after completion    
    def showRanImg(self,dir):
        self.videoFrame()
        fileNames=os.listdir(path=dir)
        while True:
            randFile=random.choice(fileNames)
            path=os.path.join(dir,randFile)
            self.showSinglePic(path)
    # Function for showing one pic inside video frame     
    def showSinglePic(self,path):
        image = Image.open(path)
        image= image.resize((960,540),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(image=image)
        self.framLable.config(image=self.img)
        self.framLable.after(1000)
        self.framLable.update()
    # function for showing information inside info Frame this will execute after upload button clicked
    def infoShow(self):
        self.infoFrame = Frame(self.frame)
        self.lengthLeb = Label(self.infoFrame,text=f"Total Number Of Frame: {self.getlength()}",font=("Helvetica", "16"))
        self.lengthLeb.place(x=80,y=200)
        self.timeLeb= Label(self.infoFrame,text=f"Total Time to upload: {self.gettime()} s +",font=("Helvetica", "16"))
        self.timeLeb.place(x=550,y=200)
        print(self.length)
        self.decFrom = Button(self.infoFrame,text=f"Decrease Number Of Frame",command=self.decNumFrame)
        self.decFrom.place(x=170,y=280)
        
        self.btnstart=Button(self.infoFrame,text="Start",command=self.startPorc)
        self.btnstart.place(x=600,y=280)
        self.infoFrame.place(x=20,y=50,width=960,height=540)
    #This function call when start button will click
    def startPorc(self):
        self.btnstart.destroy()
        self.decFrom.destroy()
        self.precentDone=Label(self.infoFrame,text="percentage",font=("Helvetica", "16"),background="green")
        self.precentDone.place(x=400,y=180)
        
        if(self.procFrame(self.cap,self.precentDone,self.timeLeb)):
            self.infoFrame.destroy()
            self.showRanImg(self.dirname)

    # This function call when Decrease Frame button will clicked 
    def decNumFrame(self):
        self.frameForInput=Frame(self.infoFrame)
        Label(self.frameForInput,text="How Many Frame You want:").pack()
        self.numOfFrame=Entry(self.frameForInput)
        self.numOfFrame.pack()
        Button(self.frameForInput,text="OK",command=self.changNumFrame).pack()
        self.frameForInput.place(x=400,y=130)
    # this function updating number of frames   
    def changNumFrame(self):
        
        try:
            data=int(self.numOfFrame.get())
            if data>=1:
                if(data<self.gettotal()):
                    self.setlength(data)
                    self.frameForInput.destroy()

                    self.lengthLeb.config(text=f"Total Number Of Frame: {self.getlength()}")
                    self.timeLeb.config(text=f"Total Time Take : {self.gettime()}s + ")
                else:
                    self.lengthLeb.config(text=f"Total Number Of Frame: {self.getlength()}")
                    self.timeLeb.config(text=f"Value Greater Then Expected")
            self.root.update()
               
        except  :
            Label(self.frameForInput,text="Please Enter Number Only")

    
        


        
