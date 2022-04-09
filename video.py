# This class handle all video related task
import cv2 as cv
import os
import sys



class Video:
    def __init__(self):
        self.dirname="./"
        self.cv=cv
        self.total=0
        self.length=0
        self.time=0
        self.fps=0
        self.cap=0
    def gettotal(self):
        return self.total
    def getcap(self):
        return self.cap
    def setcap(self,cap):
        self.cap=cap
    def getfps(self):
        return self.fps
    def setfps(self,fps):
        self.fps=fps
    def getlength(self):
        return self.length
    def setlength(self,data):
        self.length=data
        self.settime(self.length//self.fps)
    def settime(self,time):
        self.time=time
    def gettime(self):
        return self.time
    
    #function for making path and directory in same folder 
    def makeFileconfigure(self,path):
        
        allDATA=path.split('/')
        dirname='/'
       

        for x in allDATA[:-1]:
            dirname=os.path.join(dirname,x)
       
        name=allDATA[-1].split('.')[0]
        name+="VideoFrames"

        dirname=os.path.join(dirname,name)
        
        self.dirname=dirname
        print(self.dirname)
    #function for setup all value 
    def saveFrame(self,path):
        try:
            self.makeFileconfigure(path)
            self.createDir(self.dirname)
            self.workDone=False
            self.cap = self.cv.VideoCapture(path)
            self.setfps(self.cap.get(cv.CAP_PROP_FPS))
            self.total=int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))
            self.setlength(self.total)
        except:
            print("Error Occure in opening file")
       
    #function for processing of frame and saving it into folder
    def procFrame(self,cap,lable,timeLeb):
        idx=0
        count=0
        size=self.gettotal()//self.getlength()
        length=self.getlength()
        
        while True:
            ret,Frame= cap.read()
            
            if not ret:
                self.cap.release()
                return True
                break
            else:
                
                cv.imwrite(f"{self.dirname}/{count}.png",Frame)
                percent= (idx/self.gettotal())*100
                length-=1
                timeLeb.config(text=f"Total left: {length/self.getfps():.2f}s +")
                lable.config(text=f"{percent:.2f} % done")
                lable.update()
                print(f"addQuesworking{idx} {percent:.2f} %")
                
                idx+=size
                cap.set(cv.CAP_PROP_POS_FRAMES, idx)
                count+=1
                
    #function for creating directory at given path             
    def createDir(self,path):
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                print("created Path : "+path)
        except OSError:
            print(f"ERROR: Creating directrory with name{path}")
    
        


