from tkinter import *
import tkinter.font as font
import time
from PIL import ImageTk
import os
import time
from threading import Thread
from tkinter import filedialog
import cv2
from PIL import ImageFont, ImageDraw, Image
from tkinter import messagebox
from PIL import ImageGrab
import numpy as np

global lp
global exte
global st
global sc
global chch, out,nm,cco
global  frame_width, frame_height, frame_size,fps, fm
global p2
global kk 
global cc
global fca
global cap
global sm
global video
global imgtk
global cwb
global p
global o
global see
global ch
global uI2,x,y,w,h
global ln
global filename
global fln
global result
global res
global result2
global faces
global yn
check = 0
gui = Tk()
gui.title('Detector')
gui.geometry('500x700')
gui.geometry("+725+200")
gui.resizable(width=False, height=False)
wid = 500
hei = 700
canvas = Canvas(gui, bg = 'white', height = hei, width = wid)
canvas.pack()
header = PhotoImage(file='Graphics/header.png')
imgF = PhotoImage(file='Graphics/img1.png')
imgS = PhotoImage(file='Graphics/img2.png')
imgT = PhotoImage(file='Graphics/img3.png')
arr = PhotoImage(file='Graphics/arrow.png')
arr2 = PhotoImage(file='Graphics/arrow2.png')
krL = PhotoImage(file='Graphics/kr_l.png')
krL2 = PhotoImage(file='Graphics/kr_l2.png')
krL3 = PhotoImage(file='Graphics/kr_l3.png')
krD = PhotoImage(file = 'Graphics/kr_d.png')
krD2 = PhotoImage(file = 'Graphics/kr_d2.png')
krD3 = PhotoImage(file = 'Graphics/kr_d3.png')
getS = PhotoImage(file = 'Graphics/getS.png')
getS2 = PhotoImage(file = 'Graphics/getS2.png')
ph = PhotoImage(file = 'Graphics/photo.png')
vd = PhotoImage(file = 'Graphics/video.png')
wb = PhotoImage(file = 'Graphics/webcam.png')
phD = PhotoImage(file = 'Graphics/photoD.png')
vdD = PhotoImage(file = 'Graphics/videoD.png')
wbD = PhotoImage(file = 'Graphics/webcamD.png')
fl = PhotoImage(file = 'Graphics/file.png')
fl2 = PhotoImage(file = 'Graphics/file2.png')
bck = PhotoImage(file = 'Graphics/back.png')
bck2 = PhotoImage(file = 'Graphics/back2.png')
ext = PhotoImage(file = 'Graphics/exit.png')
ext2 = PhotoImage(file = 'Graphics/exit2.png')
sure = PhotoImage(file = 'Graphics/sure.png')
yes = PhotoImage(file = 'Graphics/yes.png')
yes2 = PhotoImage(file = 'Graphics/yes2.png')
no = PhotoImage(file = 'Graphics/no.png')
no2 = PhotoImage(file = 'Graphics/no2.png')
face = PhotoImage(file = 'Graphics/face.png')
face2 = PhotoImage(file = 'Graphics/face2.png')
eye = PhotoImage(file = 'Graphics/eye.png')
eye2 = PhotoImage(file = 'Graphics/eye2.png')
upperbody = PhotoImage(file = 'Graphics/upperbody.png')
upperbody2 = PhotoImage(file = 'Graphics/upperbody2.png')
lowerbody = PhotoImage(file = 'Graphics/lowerbody.png')
lowerbody2 = PhotoImage(file = 'Graphics/lowerbody2.png')
fullbody = PhotoImage(file = 'Graphics/fullbody.png')
fullbody2 = PhotoImage(file = 'Graphics/fullbody2.png')
plate = PhotoImage(file = 'Graphics/plate.png')
plate2 = PhotoImage(file = 'Graphics/plate2.png')
line = PhotoImage(file = 'Graphics/line.png')
white = PhotoImage(file = 'Graphics/white.png')
saveF = PhotoImage(file = 'Graphics/saveF.png')
saveF2 = PhotoImage(file = 'Graphics/saveF2.png')
saveH = PhotoImage(file = 'Graphics/saveH.png')
saveH2 = PhotoImage(file = 'Graphics/saveH2.png')
paste1 = PhotoImage(file = 'Graphics/paste.png')
paste2 = PhotoImage(file = 'Graphics/paste2.png')
cat = PhotoImage(file = 'Graphics/cat.png')
cat2 = PhotoImage(file = 'Graphics/cat2.png')
ware = PhotoImage(file = 'Graphics/ware.png')
ware2 = PhotoImage(file = 'Graphics/ware2.png')
mv = PhotoImage(file = 'Graphics/mv.png')
mv2 = PhotoImage(file = 'Graphics/mv2.png')
vdb = PhotoImage(file = 'Graphics/vbd.png')
vdb2 = PhotoImage(file = 'Graphics/vbd2.png')
im = PhotoImage(file = 'Graphics/im.png')
im2 = PhotoImage(file = 'Graphics/im2.png')
slot = PhotoImage(file = 'Graphics/slot.png')
fr1 = PhotoImage(file = 'Graphics/fr1.png')
fr2 = PhotoImage(file = 'Graphics/fr2.png')
kr1 = Button(gui, bd = '0', bg = 'white', image = krD)
pasteBtn = Button(gui, bd = '0', bg = 'white', image = paste1)
kr2 = Button(gui, bd = '0', bg = 'white', image = krD2)
kr3 = Button(gui, bd = '0', bg = 'white', image = krD3)
btn = Button(gui, bd = '0', bg = 'white', image = arr)
fc = Button(gui, bd = '0', bg = 'white', image = face)
ey = Button(gui, bd = '0', bg = 'white', image = eye)
upp = Button(gui, bd = '0', bg = 'white', image = upperbody)
low = Button(gui, bd = '0', bg = 'white', image = lowerbody)
full = Button(gui, bd = '0', bg = 'white', image = fullbody)
pt = Button(gui, bd = '0', bg = 'white', image = plate)
exitBtn = Button(gui, bd = '0', bg = 'white', image = ext)
gs = Button(gui, bd = '0', bg = 'white', image = getS)
ag = Button(gui, bd = '0', bg = 'white', image = yes)
ds = Button(gui, bd = '0', bg = 'white', image = no)
photo = Button(gui, bd = '0', bg = 'white', image = ph)
videol = Button(gui, bd = '0', bg = 'white', image = vd)
webcam = Button(gui, bd = '0', bg = 'white', image = wb)
chooseBtn = Button(gui, bd = '0', bg = 'white', image = fl)
backBtn = Button(gui, bd = '0', bg = 'white', image = bck)
saveFl = Button(gui, bd = '0', bg = 'white', image = saveF)
saveHi = Button(gui, bd = '0', bg = 'white', image = saveH)
catBtn = Button(gui, bd = '0', bg = 'white', image = cat)
wareBtn = Button(gui, bd = '0', bg = 'white', image = ware)
mvBtn = Button(gui, bd = '0', bg = 'white', image = mv)
vdbBtn = Button(gui, bd = '0', bg = 'white', image = vdb)
imBtn = Button(gui, bd = '0', bg = 'white', image = im)
frogBtn = Button(gui, bd = '0', bg = 'white', image = fr1)
img1 = canvas.create_image(100,190, anchor = NW, image = imgF)
krugL = canvas.create_image(170,530, anchor = NW, image = krL)
gs.place(x = 300, y =630)
kr1['image'] = krL
cap = cv2.VideoCapture(0)
fln = Label(gui, font=("Helvetica", 11, font.BOLD))

#for cleaning canvas
def clean():
   canvas.delete('all')
   chooseBtn.place(x = 1000, y = 1000)
   hd = canvas.create_image(0,0, anchor = NW, image = header)
   fc.place(x = 1000,y=1000)
   ey.place(x = 1000,y=1000)
   upp.place(x = 1000,y=1000)
   low.place(x = 1000,y=1000)
   full.place(x = 1000,y=1000)
   pt.place(x = 1000,y=1000)
   saveFl.place(x= 1000, y = 1000)
   saveHi.place(x= 1000, y = 1000)

#function for changing arrow when hovering over it
def on_enter(e):
   backBtn['image'] = bck2

def on_leave(e):
   backBtn['image'] = bck
backBtn.bind("<Enter>", on_enter)
backBtn.bind("<Leave>", on_leave)

test = 0
#start menu
def start():
    hd = canvas.create_image(0,0, anchor = NW, image = header)
    btn.place(x = 403, y =320 )
    kr1.place(x = 170, y = 530)
    kr2.place(x = 240, y = 530)
    kr3.place(x = 310, y = 530)

fimg = 1
#for changing fimg
def change(z):
   global fimg
   fimg = z

#switch images
def images():
    global fimg
    if fimg == 1 or fimg > 3:
       canvas.delete(imgT) 
       img1 = canvas.create_image(100,190, anchor = NW, image = imgF)
       kr1['image'] = krL
       kr3['image'] = krD3
       kr2['image'] = krD2
    elif fimg == 2:
       canvas.delete(imgF)
       img2 = canvas.create_image(100,190, anchor = NW, image = imgS)
       kr1['image'] = krD
       kr3['image'] = krD3
       kr2['image'] = krL2
    elif fimg == 3:
       canvas.delete(imgS)
       img3 = canvas.create_image(100,190, anchor = NW, image = imgT)
       kr2['image'] = krD2
       kr1['image'] = krD
       kr3['image'] = krL3
    if fimg > 3:
        fimg = 1

#command for dot1
def kr1C():
   global fimg
   y = 4
   change(y)
   images()

#command for dot2
def kr2C():
   global fimg
   c = 2
   change(c)
   images()

#command for dot3
def kr3C():
   global fimg
   v = 3
   change(v)
   images()

#thread for swithcing images
def threadNext():
   arrow2 = canvas.create_image(403,320, anchor = NW, image = arr2)
   time.sleep(0.2)
   btn.place(x = 403, y =320 )
th = Thread(target=threadNext)

#command for the switch button
def fbtn():
    global fimg
    global arr
    global th
    btn.place(x = 1000, y =1000 )
    if not th.is_alive():
      try:
         th.start()
      except RuntimeError:
         th = Thread(target=threadNext)
         th.start()
    fimg += 1
    print(fimg)
    images()
btn['command'] = fbtn

#thread for get started button
def threadGs():
   global test
   test += 1
   print('a' , test)
   gs2 = canvas.create_image(300,630, anchor = NW, image = getS2) 
   time.sleep(0.2)
   gs.place(x = 300, y = 630)
   btn.place(x = 1000, y = 1000)  
   clean()
   gs.place(x = 1000, y = 1000)
   choose()
thGs = Thread(target=threadGs)

#command for get started button
def fgs():
   global thGs
   gs.place(x = 1000, y =1000 )
   if not thGs.is_alive():
      try:
         thGs.start()
      except RuntimeError:
         thGs = Thread(target=threadGs)
         thGs.start()

#data type choose menu
def choose():
   global chch, p2,st,p
   chch = 0
   p2 = 0
   st = 0
   p = 0
   saveFl['command'] = saveFull
   exitBtn.place(x = 280, y = 620)
   photo.place(x = 85, y = 215)
   videol.place(x = 285, y = 375)
   ln = canvas.create_image(52, 363, anchor = NW, image = line)
   webcam.place(x = 85, y = 375)
   mvBtn.place(x = 285, y = 215)
   webcam['command'] = fWb
   mvBtn['command'] = fMv
   saveFl['command'] = saveFull
   if vdbBtn['state'] == 'disabled':
      vdbBtn["state"] = "active"
   else:
      pass
   kr1.place(x= 1000, y = 1000)
   kr2.place(x= 1000, y = 1000)
   kr3.place(x= 1000, y = 1000)
   backBtn['command'] = fback

#switching to data choosing menu
def fileM():
   exitBtn.place(x = 1000, y = 1000)
   photo.place(x = 1000,y = 1000)
   videol.place(x = 1000,y = 1000)
   webcam.place(x = 1000,y = 1000)
   mvBtn.place(x = 1000,y = 1000)
   clean()
   chooseBtn.place(x = 82, y = 300)
   pasteBtn.place(x = 280, y = 300)
   backBtn.place(x = 0, y = 100) 
   backBtn['command'] = fback

exwarn = Label(gui,text = 'Ivalid extension', font=("Helvetica", 11, font.BOLD))
exwarn.config(width=29, bg = 'white', fg = '#f22416')
exwarn.pack()
#thread for clipboard button
def threadCl():
   global sm, p, p2, chch
   global yn, fln, fm,sc,ext
   webcam['state'] = 'disabled' 
   chooseBtn['state'] = 'disabled'
   if p == 2 and chch == 0:
      p2 = 1
   print('clip')
   if p == 2:
      canvas.create_image(275,300,anchor=NW, image = paste2)
      time.sleep(0.2)
      pasteBtn.place(x = 275, y = 300)
   elif p == 5 and p == 4:
      canvas.create_image(280,300,anchor=NW, image = paste2)
      time.sleep(0.2)
      pasteBtn.place(x = 280, y = 300)
   else:
      canvas.create_image(280,300,anchor=NW, image = paste2)
      time.sleep(0.2)
      pasteBtn.place(x = 280, y = 300)
   clipP = 'Output/'
   clipI = ImageGrab.grabclipboard() 
   warn.place(x = 1000, y = 1000)
   print(clipI)
   if type(clipI) == list:
      clipI2 = clipI[0]
      exte = os.path.splitext(clipI2)[-1].lower()
      print(p, p2)
      if p == 4 and exte == ".mp4" or p==2 and exte == ".mp4":
            clean()
            chooseBtn.place(x = 1000, y = 1000)
            pasteBtn.place(x = 1000, y = 1000)
            yn = clipI2
            try:
               fln.config(width=50, bg = 'white')
               fln.pack()
               fln.config(text = yn)
            except:
               pass
            if p == 2:
               clean()
               chooseBtn.place(x = 1000, y = 1000)
               pasteBtn.place(x = 1000, y = 1000)
               webcam.place(x = 1000, y = 1000)
               mvBtn.place(x = 1000, y = 1000)
               ff()
               try:
                  fln.config(width=50, bg = 'white')
                  fln.pack()
               except:
                  pass
            if p == 4:
               clean()
               chooseBtn.place(x = 1000, y = 1000)
               pasteBtn.place(x = 1000, y = 1000)
               webcam.place(x = 1000, y = 1000)
               mvBtn.place(x = 1000, y = 1000)
               wtd()
               try:
                  fln.config(width=50, bg = 'white')
                  fln.pack()
               except:
                  pass
            if p == 3:
               fln.config(text = 'Your Webcam')
            elif  p == 2 or p == 5:
               try:
                  fln.config(text = yn)
                  fln.place(x=20,y=250)
               except:
                  pass
               backBtn['command'] = askback
            elif p == 4 or  p ==1:
               try:
                  fln.config(text = yn)
                  fln.place(x=20,y=193)
               except:
                  pass
               backBtn['command'] = askback
               chooseBtn.place(x = 1000, y = 1000)
            else:
               print('sc ', sc)
               # if sc == 1:
               #    clean()
               #    chooseBtn.place(x = 1000,y = 1000)
               #    pasteBtn.place(x = 1000, y = 1000)
               #    sm = 1
               #    ff()
               # elif sc == 2:
               #    clean()
               #    chooseBtn.place(x = 1000,y = 1000)
               #    pasteBtn.place(x = 1000, y = 1000)
               #    sm = 1
               #    wtd()
      elif p == 1 and exte == ".png" or p == 2 and exte == ".png" :
            yn = clipI2
            print('scam')
            print(p)
            if p == 1:
               clean()
               chooseBtn.place(x = 1000,y = 1000)
               pasteBtn.place(x = 1000, y = 1000)
               wtd()
               print('one')
               sm = 1
               try:
                  fln.config(width=50, bg = 'white')
                  fln.pack()
               except:
                  pass
               chooseBtn.place(x = 1000, y = 1000)
            elif p == 2:
               print('two')
               clean()
               chooseBtn.place(x = 1000, y = 1000)
               pasteBtn.place(x = 1000, y = 1000)
               webcam.place(x = 1000, y = 1000)
               mvBtn.place(x = 1000, y = 1000)
               ff()
               try:
                  fln.config(width=50, bg = 'white')
                  fln.pack()
               except:
                  pass
               chooseBtn.place(x = 1000, y = 1000)
            if p == 3:
               fln.config(text = 'Your Webcam')
            elif p ==1 or p == 2:
               fln.config(text = yn)
               fln.place(x=20,y=250)
               clean()
               chooseBtn.place(x = 1000,y = 1000)
               pasteBtn.place(x = 1000, y = 1000)
               backBtn['command'] = askback
               chooseBtn.place(x = 1000, y = 1000)
            else:
               if p == 1:
                  clean()
                  chooseBtn.place(x = 1000,y = 1000)
                  pasteBtn.place(x = 1000, y = 1000)
                  wtd()
                  sm = 1
               else:
                  clean()
                  chooseBtn.place(x = 1000,y = 1000)
                  pasteBtn.place(x = 1000, y = 1000)
                  ff()
      else:
         if p == 2:
            chooseBtn.place(x = 95, y = 300)
            pasteBtn.place(x = 275, y = 300) 
         else:
            chooseBtn.place(x = 82, y = 300)
            pasteBtn.place(x = 280, y = 300) 
         exwarn.place(x = 118, y = 240)
         time.sleep(2)
         exwarn.place(x = 1000, y = 1000)
   elif clipI == None:
      if p == 2 and p2 == 0 or p == 2 and p2 == 1: 
         chooseBtn.place(x = 95, y = 300)
         pasteBtn.place(x = 275, y = 300)
         webcam.place(x = 180, y = 460)
      else:
         if p == 2:
            pasteBtn.place(x = 185, y = 300) 
         else:
           pasteBtn.place(x = 280, y = 300)
      chooseBtn['state'] = 'active'  
      webcam['state'] = 'active' 
   elif clipI.format == 'DIB':
      clipI.save(clipP+'paste.png', 'PNG')
      yn = 'Output/paste.png'
      print(yn)
      if p2 == 1:
         clean()
         chooseBtn.place(x = 1000,y = 1000)
         pasteBtn.place(x = 1000, y = 1000)
         webcam.place(x = 1000, y = 1000)
         mvBtn.place(x = 1000,y = 1000)
         ff()
         fln.config(width=50, bg = 'white')
         fln.pack()
         fln.place(x=20,y=250)
         if p == 3:
            fln.config(text = 'Your Webcam')
         elif p ==1 or p == 2:
            fln.config(text = yn)
         fln.place(x=20,y=250)
         backBtn['command'] = askback
         chooseBtn.place(x = 1000, y = 1000)
      else:
         clean()
         chooseBtn.place(x = 1000,y = 1000)
         pasteBtn.place(x = 1000, y = 1000)
         wtd()
         sm = 1
   else:
      if p2 == 1:
         chooseBtn.place(x = 30, y = 300)
         pasteBtn.place(x = 185, y = 300)
         webcam.place(x = 340, y = 300)
         pasteBtn.place(x = 185, y = 460)
      else:
         chooseBtn.place(x = 82, y = 300)
         pasteBtn.place(x = 280, y = 300)    
      chooseBtn['state'] = 'active'
      webcam['state'] = 'active'     
thCl = Thread(target =threadCl)

#command for clipboard button
def clip():
   global thCl,p
   pasteBtn.place(x= 1000, y =1000)
   if p == 2:
      pasteBtn.place(x = 275, y = 300)
   else:
      pasteBtn.place(x = 280, y = 300)
   if not thCl.is_alive():
      try:
         thCl.start()
      except RuntimeError:
         thCl = Thread(target =threadCl)
         thCl.start()

#thread for data choose button
def threadChoose():
   global o, p, p2
   global yn, fln,chch
   global photo, fm, exte
   pasteBtn['state'] = 'disabled'
   webcam['state'] = 'disabled' 
   print('ff',chch)
   exwarn.place(x = 1000, y = 1000)
   warn.place(x = 1000, y = 1000)
   if p == 2 and chch == 0:
      p2 = 1
   else:
      p2 = 0
   print('gg', p2)
   if p2 == 1 and p == 2:
      chooseD = canvas.create_image(95, 300, anchor = NW, image = fl2)
      time.sleep(0.2)
      chooseBtn.place(x = 95, y = 300)
   elif p == 5 and p == 4:
      chooseD = canvas.create_image(82, 300, anchor = NW, image = fl2)
      time.sleep(0.2)
      chooseBtn.place(x = 82, y = 300) 
   else:
      chooseD = canvas.create_image(82, 300, anchor = NW, image = fl2)
      time.sleep(0.2)
      chooseBtn.place(x =82, y = 300)
   gui.resizable(width=True, height=True)
   canvas.delete('all')
   hd = canvas.create_image(0,0, anchor = NW, image = header)
   if p == 4 and fm == 2:
      flt1 = "video", ".mp4"
   elif p == 2:
      flt1 =  'multiple', '.mp4 .png'
   else:
      flt1 = "image", ".png"
   filename = filedialog.askopenfilename(title = 'Choose', filetypes = [(flt1)] )
   print(filename)
   yn = filename
   print(yn, type(yn))
   if filename == '':
      pasteBtn['state'] = 'active'
      webcam['state'] = 'active'
      pass
   elif p2 == 1:
      backBtn['command'] = askback
      clean()
      chooseBtn.place(x = 1000,y = 1000)
      webcam.place(x = 1000, y = 1000)
      pasteBtn.place(x = 1000, y = 1000)
      mvBtn.place(x = 1000, y = 100)
      ff()
      fln.config(width=50, bg = 'white')
      fln.pack()
      fln.place(x=20,y=250)
      if p == 3:
         fln.config(text = 'Your Webcam')
      elif p ==1 or p == 2:
         fln.config(text = yn)
      fln.place(x=20,y=250)
   elif p == 5:
      backBtn['command'] = askback
      clean()
      chooseBtn.place(x = 1000,y = 1000)
      webcam.place(x = 1000, y = 1000)
      pasteBtn.place(x = 1000, y = 1000)
      mvBtn.place(x = 1000, y = 100)
      ff()
      try:
         fln.config(width=50, bg = 'white')
         fln.pack()
         fln.place(x=20,y=250)
      except:
         pass
      if p == 3:
         fln.config(text = 'Your Webcam')
      elif p ==1 or p == 2 or p == 5:
         try:
            fln.config(text = yn)
         except:
            pass
      try:
         fln.place(x=20,y=250)
      except:
         pass
   else:
      clean()
      chooseBtn.place(x = 1000,y = 1000)
      pasteBtn.place(x = 1000, y = 1000)
      wtd()
thC = Thread(target =threadChoose)

#for creating a label with filename
def lbl():
   global fln, p, yn
   try:
      fln.config(width=50, bg = 'white')
      fln.pack()
      fln.place(x=20,y=193)
   except:
      pass
   if p == 3:
      try:
         fln.config(text = 'Your Webcam')
      except:
         pass
   elif p ==1 or p == 4:
      try:
         fln.config(text = yn)
      except:
         pass

#function for switching to detecting menu
def wtd():
   global sureAbove, filename, p,sc, lp
   fc.place(x = 40,y=230)
   ey.place(x = 180,y=230)
   upp.place(x = 320,y=230)
   low.place(x = 40,y=400)
   full.place(x = 180,y=400)
   pt.place(x = 320,y=400)
   chooseBtn.place(x = 1000, y = 1000)
   pasteBtn.place(x = 1000, y = 1000)
   sureAbove = canvas.create_image(1000, 1000, anchor='nw', image=sure)
   lbl()
   sc = 0
   ln = canvas.create_image(47, 380, anchor = NW, image = line)
   if p == 1:
      backBtn['command'] = askback
   elif p == 3:
      backBtn['command'] = fback

#command for data choose button
def fchoose():
   global thC
   chooseBtn.place(x = 1000, y = 1000)
   if not thC.is_alive():
      try:
         thC.start()
      except RuntimeError:
         thC = Thread(target = threadChoose)
         thC.start()

#thread for photo button
def threadPh():
   global o,p,fm
   global test,cap
   exwarn.place(x = 1000, y = 1000)
   cap = cv2.VideoCapture(0)
   warn.place(x=1000,y=1000)
   test+=1
   o = 0
   p = 1
   fm = 1
   photoD = canvas.create_image(85,215, anchor = NW, image = phD)
   time.sleep(0.2)
   photo.place(x = 85, y = 215)
   fileM()
thPh = Thread(target=threadPh)

#command for photo button
def fPh():
   global thPh
   photo.place(x = 1000, y = 1000)
   if not thPh.is_alive():
      try:
         thPh.start()
      except RuntimeError:
         thPh = Thread(target=threadPh)
         thPh.start()

#thread for video button
def threadMv():
   global o,p,fm, p2, sc,cco
   global test,cap,cc, chch
   cap = cv2.VideoCapture(0)
   warn.place(x=1000,y=1000)
   exwarn.place(x = 1000, y = 1000)
   test+=1
   fm = 2
   if p ==2:
      p = 5
   else:
      p = 4
   o = 0
   cc = 0
   chch = 1
   saveFl['command'] = saveFull2
   mvD = canvas.create_image(285,215, anchor = NW, image = mv2)
   time.sleep(0.2)
   mvBtn.place(x = 285, y = 215)
   fileM()
thMv = Thread(target=threadMv)

#command for video button
def fMv():
   global thMv
   mvBtn.place(x = 1000, y = 1000)
   if not thMv.is_alive():
      try:
         thMv.start()
      except RuntimeError:
         thMv = Thread(target=threadMv)
         thMv.start()

#thread for video button2
def threadMv2():
   global o,p,fm,p2, chch
   global test,cap,cc,sc
   exwarn.place(x = 1000, y = 1000)
   sc = 2
   fm = 2
   chch = 1
   if p ==2:
      p = 5
   else:
      p = 4
   cap = cv2.VideoCapture(0)
   warn.place(x=1000,y=1000)
   mvD = canvas.create_image(185,460, anchor = NW, image = mv2)
   time.sleep(0.2)
   mvBtn.place(x = 185, y = 460)
   fileM()
thMv2 = Thread(target=threadMv2)

#command for video button2
def fMv2():
   global thMv2
   mvBtn.place(x = 1000, y = 1000)
   if not thMv2.is_alive():
      try:
         thMv2.start()
      except RuntimeError:
         thMv2 = Thread(target=threadMv2)
         thMv2.start()

#func for spawning new buttons
def ff():
   global fln, p2
   print(p2)
   frogBtn.place(x = 180, y = 450)
   catBtn.place(x = 80, y = 300)
   wareBtn.place(x = 285, y = 300)

#thread for cat button
def threadCa():
   global o,p, p2,fm,ext
   global test,cap,cco,yn,lp
   cco = 0
   cap = cv2.VideoCapture(0)
   print(p)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      catBtn.place(x = 80, y = 300)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      catBtn.place(x = 1000, y = 1000)
      faceD = canvas.create_image(80,300, anchor = NW, image = cat2)
      time.sleep(0.2)
      catBtn.place(x = 80, y = 300)
      warn.place(x=1000,y=1000)
      clean()
      print('ch',p)
      try:
         exte = os.path.splitext(yn)[-1].lower()
      except:
         exte = ''
      if exte == '.png':
         saveFl['command'] = saveFull
      elif exte == '.mp4':
         saveFl['command'] = saveFull2
      if exte == '.png':
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
         catR()
         print('norm')
      elif exte == '':
         print('webcam')
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
         bf()
         catWb()
      elif exte == '.mp4':
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
         bf()
         catVd()
thCa = Thread(target=threadCa)

#command for cat button
def fCa():
   global thCa
   catBtn.place(x = 1000, y = 1000)
   catBtn.place(x = 80, y = 300)
   if not thCa.is_alive():
      try:
         thCa.start()
      except RuntimeError:
         thCa = Thread(target=threadCa)
         thCa.start()

#thread for frog button
def threadFr():
   global o,p, p2,fm,ext
   global test,cap,cco,yn,lp
   cco = 0
   cap = cv2.VideoCapture(0)
   print(p)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      frogBtn.place(x = 180, y = 450)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      frogBtn.place(x = 1000, y = 1000)
      faceD = canvas.create_image(180,450, anchor = NW, image = fr2)
      time.sleep(0.2)
      frogBtn.place(x = 180, y = 450)
      warn.place(x=1000,y=1000)
      clean()
      print('ch',p)
      try:
         exte = os.path.splitext(yn)[-1].lower()
      except:
         exte = ''
      if exte == '.png':
         saveFl['command'] = saveFull
      elif exte == '.mp4':
         saveFl['command'] = saveFull2
      if exte == '.png':
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
         frogR()
         print('norm')
      elif exte == '':
         print('webcam')
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
         bf()
         frogWb()
      elif exte == '.mp4':
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
         bf()
         frogVd()
thFr = Thread(target=threadFr)

#command for frog button
def fFr():
   global thFr
   frogBtn.place(x = 1000, y = 1000)
   frogBtn.place(x = 180, y = 450)
   if not thFr.is_alive():
      try:
         thFr.start()
      except RuntimeError:
         thFr = Thread(target=threadFr)
         thFr.start()

#thread for ware button
def threadWr():
   global o,p, p2,fm,sc,yn
   global test,cap, cco, exte, lp
   cco = 2
   cap = cv2.VideoCapture(0)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      wareBtn.place(x = 285, y = 300)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      wareBtn.place(x = 1000, y = 1000)
      faceD = canvas.create_image(285,300, anchor = NW, image = ware2)
      time.sleep(0.2)
      wareBtn.place(x = 285, y = 300)
      print('ch',p)
      try:
         exte = os.path.splitext(yn)[-1].lower()
      except:
         exte = ''
      if exte == '.png':
         saveFl['command'] = saveFull
      elif exte == '.mp4':
         saveFl['command'] = saveFull2
      if exte == '.png':
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
         wareR()
         print('norm')
      elif exte == '':
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)   
         print('webcam')
         bf()
         coWb()
      elif exte == '.mp4':
         fln.place(x = 1000, y = 1000)
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x = 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)   
         bf()
         coVd()
thWr = Thread(target=threadWr)

#command for contour button
def fWr():
   global thWr
   wareBtn.place(x = 1000, y = 1000)
   wareBtn.place(x = 285, y = 300)
   if not thWr.is_alive():
      try:
         thWr.start()
      except RuntimeError:
         thWr = Thread(target=threadWr)
         thWr.start()
         
#thread for video
def threadVd():
   global o,p, fm,cc,sc
   backBtn['command'] = fback
   webcam['command'] = fWb2
   mvBtn['command'] = fMv2
   saveFl['command'] = saveFull2
   mvBtn['command'] = fMv2
   warn.place(x=1000,y=1000)
   exwarn.place(x = 1000, y = 1000)
   p = 2
   fm = 2
   cc = 0
   sc = 1
   videoD = canvas.create_image(285,375, anchor = NW, image = vdD)
   time.sleep(0.2)
   videol.place(x = 285, y = 375)
   clean()
   exitBtn.place(x = 1000, y = 1000)
   photo.place(x = 1000,y = 1000)
   videol.place(x = 1000,y = 1000)
   webcam.place(x = 1000,y = 1000)
   mvBtn.place(x = 1000,y = 1000)
   clean()
   chooseBtn.place(x = 95, y = 300)
   pasteBtn.place(x = 275, y = 300)
   webcam.place(x= 180, y = 460)
   backBtn.place(x = 0, y = 100) 
thVd = Thread(target=threadVd)

#command for video button
def fVd():
   global thVd
   videol.place(x = 1000, y = 1000)
   if not thVd.is_alive():
      try:
         thVd.start()
      except RuntimeError:
         thVd = Thread(target=threadVd)
         thVd.start()

warn = Label(gui,text = 'Your web camera is not available', font=("Helvetica", 11, font.BOLD))
warn.config(width=29, bg = 'white', fg = '#f22416')
warn.pack()
#thread for webcam
def threadWb():
   global cwb, p,cap,fca,cc, p2
   cap = cv2.VideoCapture(0)
   exwarn.place(x = 1000, y = 1000)
   if cap is None or not cap.isOpened():
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      saveFl['command'] = saveFull2
      cc = 0
      p = 3
      webcam.place(x = 1000, y = 1000)
      webcamD = canvas.create_image(85,375, anchor = NW, image = wbD)
      time.sleep(0.2)
      webcam.place(x = 85, y = 375)
      clean()
      photo.place(x = 1000,y = 1000)
      videol.place(x = 1000,y = 1000)
      webcam.place(x = 1000,y = 1000)
      mvBtn.place(x = 1000,y = 1000)
      backBtn.place(x = 0, y = 100) 
      backBtn['command'] = fback
      wtd()
      fln.config(width=50, bg = 'white')
      fln.pack()
      fln.config(text = 'Your Webcam')
      fln.place(x=20,y=200)
thWb = Thread(target=threadWb)

#command for webcam button
def fWb():
   global thWb
   if not thWb.is_alive():
      try:
         thWb.start()
      except RuntimeError:
         thWb = Thread(target=threadWb)
         thWb.start()


#thread for webcam2
def threadWb2():
   global cwb, p,cap,fca,cc, p2
   cap = cv2.VideoCapture(0)
   exwarn.place(x = 1000, y = 1000)
   if cap is None or not cap.isOpened():
      warn.place(x=118,y=240)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      p2 = 2
      cc = 0
      webcam.place(x = 1000, y = 1000)
      p = 2
      webcamD = canvas.create_image(180,460, anchor = NW, image = wbD)
      time.sleep(0.2)
      webcam.place(x = 180, y = 460)
      clean()
      pasteBtn.place(x = 1000,y = 1000)
      chooseBtn.place(x = 1000,y = 1000)
      webcam.place(x = 1000,y = 1000)
      mvBtn.place(x = 1000,y = 1000)
      backBtn.place(x = 0, y = 100) 
      backBtn['command'] = fback
      ff()
      fln.config(width=50, bg = 'white')
      fln.pack()
      fln.config(text = 'Your Webcam')
      fln.place(x=20,y=250)
thWb2 = Thread(target=threadWb2)

#command for webcam button2
def fWb2():
   global thWb2
   if not thWb2.is_alive():
      try:
         thWb2.start()
      except RuntimeError:
         thWb2 = Thread(target=threadWb2)
         thWb2.start()

#func for changing back button command
def bf():
   global p
   backBtn.place(x = 0, y = 100) 
   backBtn['command'] = fback

#func for video label
def vl():
   global video,cc
   cc = 0
   video = Label(gui)
   video.config(width = int(wid/2+160), height = int(hei/2))
   video.pack()
   video.place(relx = 0.5, rely = 0.55, anchor = CENTER)

#command for back button
def fback():
   global p,fln , kk,cc,video,chch,cap,out,st,lp
   pasteBtn['state'] = 'active'
   chooseBtn['state'] = 'active'
   webcam['state'] = 'active'
   warn.place(x = 1000, y = 1000)
   try:
      video.place(anchor="nw", x=0, y=0, width=0, height=0)
      print('forgotten')
   except:
      pass
   exwarn.place(x = 1000, y = 1000)
   cc = 1
   st = 1
   chch = 0
   lp = 1
   imBtn.place(x = 1000, y = 1000)
   vdbBtn.place(x = 1000, y = 1000)
   chooseBtn.place(x= 1000, y = 1000)
   pasteBtn.place(x= 1000, y = 1000)
   clean()
   choose()
   st = 0
   print(p)
   catBtn.place(x = 1000, y = 1000)
   wareBtn.place(x = 1000, y = 1000)
   frogBtn.place(x = 1000, y = 1000)
   try:
      os.remove('Output/output.avi')
   except:
      pass
   if p == 2:
      catBtn.place(x= 1000, y = 1000)
      wareBtn.place(x= 1000, y = 1000)
      frogBtn.place(x = 1000, y = 1000)
   try:      
      cap.release()
      out.release()
      os.remove('Output/res.png')
   except:
      print('no')
   backBtn.place(x = 1000, y = 1000)
   if p == 3 or p == 4 or p == 2:
      print('okk')
      imBtn.place(x = 1000, y = 1000)
      vdbBtn.place(x = 1000, y = 1000)
      try:
         imBtn.place(x = 1000, y = 1000)
         vdbBtn.place(x = 1000, y = 1000)
      except:
         pass
   try:
      fln.place(x=1000,y=1000)
   except:
      pass
   p = 0
   
#thread for exit button
def threadExit():
   exitD = canvas.create_image(280,620, anchor = NW, image = ext2)
   time.sleep(0.2)
   exitBtn.place(x = 280, y = 620)
   close()
thEx = Thread(target = threadExit)

#command for exit button
def fext():
   global thEx
   exitBtn.place(x = 1000, y = 1000)
   if not thEx.is_alive():
      try:
         thEx.start()
      except RuntimeError:
         thEx = Thread(target=threadExit)
         thEx.start()

#thread for yes button2
def threadAg2():
   global fln
   time.sleep(0.2)
   ag.place(x =100, y = 290)
   chooseBtn.place(x= 1000, y = 1000)
   clean()
   choose()
   backBtn.place(x = 1000, y = 1000)
   fc.place(x = 1000,y=1000)
   ey.place(x = 1000,y=1000)
   upp.place(x = 1000,y=1000)
   low.place(x = 1000,y=1000)
   full.place(x = 1000,y=1000)
   pt.place(x = 1000,y=1000)
   ag.place(x =1000, y = 1000)
   ds.place(x =1000, y = 1000)
thAg2 = Thread(target=threadAg2)

#command for yes button2
def agree2():
   global thAg2, fln
   ag.place(x =1000, y = 1000)
   if not thAg2.is_alive():
      try:
         thAg2.start()
      except RuntimeError:
         thAg2 = Thread(target=threadAg2)
         thAg2.start()

#thread for no button3
def threadDs3():
   global uI
   agr = canvas.create_image(270,290, anchor = NW, image = no2)
   time.sleep(0.2)
   ds.place(x =270, y = 290)
   clean()
   ag.place(x =1000, y = 1000)
   ds.place(x =1000, y = 1000)
thDs3 = Thread(target=threadDs3)

#thread for face button
def threadFc():
   global p, fln, lp
   cap = cv2.VideoCapture(0)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      fc.place(x = 40,y=230)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      fc.place(x = 1000, y = 1000)
      faceD = canvas.create_image(40,230, anchor = NW, image = face2)
      time.sleep(0.2)
      warn.place(x=1000,y=1000)
      fln.place(x=1000,y=1000)
      clean()
      print('ch',p)
      if p == 1:
         saveHi['command'] = saveHigh
         faceR()
         print('norm')
      elif p == 3:
         saveHi['command'] = saveHigh
         print('webcam')
         bf()
         faceWb()
      elif p == 4:
         bf()
         faceVd()
thFc = Thread(target=threadFc)

#command for face button
def fFc():
   global thFc
   fc.place(x = 1000, y = 1000)
   fc.place(x = 40,y=230)
   if not thFc.is_alive():
      try:
         thFc.start()
      except RuntimeError:
         thFc = Thread(target=threadFc)
         thFc.start()

#thread for eye button
def threadEy():
   global p, fln, lp
   cap = cv2.VideoCapture(0)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      ey.place(x = 180,y=230)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      ey.place(x = 1000, y = 1000)
      eyeD = canvas.create_image(180,230, anchor = NW, image = eye2)
      time.sleep(0.2)
      warn.place(x = 1000, y = 1000)
      fln.place(x=1000,y=1000)
      clean()
      if p == 1:
         eyeRec()
         saveHi['command'] = saveHigh
         eyeRec()
      elif p == 3:
         saveHi['command'] = saveHigh
         bf()
         eyeWb()
      elif p == 4:
         bf()
         eyeVd()
thEy = Thread(target=threadEy)

#command for eye button
def fEy():
   global thEy
   ey.place(x = 1000, y = 1000)
   ey.place(x = 180,y=230)
   if not thEy.is_alive():
      try:
         thEy.start()
      except RuntimeError:
         thEy = Thread(target=threadEy)
         thEy.start()

#thread for upperbody button
def threadUp():
   global p, fln, lp
   cap = cv2.VideoCapture(0)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      upp.place(x = 320,y=230)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      upp.place(x = 1000,y=1000)
      upper = canvas.create_image(320,230, anchor = NW, image = upperbody2)
      time.sleep(0.2)
      warn.place(x = 1000, y =1000)
      fln.place(x=1000,y=1000)
      clean()
      if p == 1:
         saveHi['command'] = saveHigh
         uppRec()
      elif p == 3:
         saveHi['command'] = saveHigh
         bf()
         uppWb()
      elif p == 4:
         bf()
         uppVd()
thUp = Thread(target=threadUp)

#command for upperbody button
def fUp():
   global thUp
   upp.place(x = 1000, y = 1000)
   upp.place(x = 320,y=230)
   if not thUp.is_alive():
      try:
         thUp.start()
      except RuntimeError:
         thUp = Thread(target=threadUp)
         thUp.start()

#thread for lowerbody button
def threadLw():
   global p, fln, lp
   cap = cv2.VideoCapture(0)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      low.place(x = 40,y=400)         
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      low.place(x = 1000,y=1000)
      lowerD = canvas.create_image(40,400, anchor = NW, image = lowerbody2)
      time.sleep(0.2)
      warn.place(x = 1000, y = 1000)
      fln.place(x=1000,y=1000)
      clean()
      if p == 1:
         saveHi['command'] = saveHigh
         lowRec()
      elif p == 3:
         saveHi['command'] = saveHigh
         bf()
         lowWb()
      elif p == 4:
         bf()
         lowVd()
thLw = Thread(target=threadLw)

#command for lowerbody button
def fLw():
   global thLw
   low.place(x = 1000, y = 1000)
   low.place(x = 40,y=400)
   if not thLw.is_alive():
      try:
         thLw.start()
      except RuntimeError:
         thLw = Thread(target=threadLw)
         thLw.start()

#thread for fullbody button
def threadFl():
   global p, fln, lp
   cap = cv2.VideoCapture(0) 
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      full.place(x = 180,y=400)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      full.place(x = 1000,y=1000)
      fullD = canvas.create_image(180,400, anchor = NW, image = fullbody2)
      time.sleep(0.2)
      warn.place(x = 1000, y = 1000)
      fln.place(x=1000,y=1000)
      clean()
      bf()
      if p == 1:
         saveHi['command'] = saveHigh
         fulRec()
      elif p == 3:
         saveHi['command'] = saveHigh
         fulWb()
      elif p == 4:
         bf()
         fulVd()
thFl = Thread(target=threadFl)

#command for fullbody button
def fFl():
   global thFl
   full.place(x = 1000, y = 1000)
   full.place(x = 180,y=400)
   if not thFl.is_alive():
      try:
         thFl.start()
      except RuntimeError:
         thFl = Thread(target = threadFl)
         thFl.start()

#thread for smile button
def threadSm():
   global p, fln, lp
   cap = cv2.VideoCapture(0)
   if cap is None and p == 3 or not cap.isOpened() and p == 3:
      pt.place(x = 320,y=400)
      warn.place(x=118,y=160)
      time.sleep(2)
      warn.place(x=1000,y=1000)
   else:
      lp = 1
      pt.place(x = 1000,y=1000)
      plateD = canvas.create_image(320,400, anchor = NW, image = plate2)
      time.sleep(0.2)
      warn.place(x = 1000, y = 1000)
      fln.place(x=1000,y=1000)
      clean()
      if p == 1:
         saveHi['command'] = saveHigh
         plRec()
      elif p == 3:
         saveHi['command'] = saveHigh
         bf()
         plWb()
      elif p == 4:
         bf()
         plVd()
thSm = Thread(target=threadSm)

#command for smile button
def fSm():
   global thSm
   pt.place(x = 1000, y = 1000)
   pt.place(x = 320,y=400)
   if not thSm.is_alive():
      try:
         thSm.start()
      except RuntimeError:
         thSm = Thread(target = threadSm)
         thSm.start()
  
         
photo['command'] = fPh
videol['command'] = fVd
webcam['command'] = fWb
gs['command'] = fgs
chooseBtn['command'] = fchoose
exitBtn['command'] = fext
fc['command'] = fFc
ey['command'] = fEy
upp['command'] = fUp
low['command'] = fLw
full['command'] = fFl
pt['command'] = fSm
kr1['command'] = kr1C
kr2['command'] = kr2C
kr3['command'] = kr3C
pasteBtn['command'] = clip
catBtn['command'] = fCa
wareBtn['command'] = fWr
frogBtn['command'] = fFr
mvBtn['command'] = fMv

#face recognition function
def faceR():
   global ln,uI2,x,y,w,h,faces,ch,yn
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
   ch = faces
   for (x,y,w,h) in faces:
      cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,320,0), 2)
      cv2.putText(uI2, "Face", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   ln = len(faces)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   print('faces', faces)
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break

#eye recognition function
def eyeRec():
   global ln,uI2,x,y,w,h,faces,ch
   eye_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_eye.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   eye = eye_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
   ch = eye
   for (x,y,w,h) in eye:
      cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
      cv2.putText(uI2, "Eye", (x+1, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break

#upperbody recognition function
def uppRec():
   global ln,uI2,x,y,w,h,faces,ch
   upp_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_upperbody.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   upp = upp_cascade_db.detectMultiScale(uI2_gray, 1.2,3)
   ch = upp
   for (x,y,w,h) in upp:
      cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
      cv2.putText(uI2, "Upperbody", (x, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break

#lowerbody recognition function
def lowRec():
   global ln,uI2,x,y,w,h,faces,ch
   low_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_lowerbody.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   low = low_cascade_db.detectMultiScale(uI2_gray, 1.2,3)
   ch = low
   for (x,y,w,h) in low:
      cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
      cv2.putText(uI2, "Lowerbody", (x, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break

#fullbody recognition function
def fulRec():
   global ln,uI2,x,y,w,h,faces,ch
   ful_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_fullbody.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   bodies = ful_cascade_db.detectMultiScale(uI2_gray, 1.2,3)
   ch = bodies
   for (x,y,w,h) in bodies:
      cv2.rectangle(uI2,(x,y),(x+w,y+h),(0,255,0),2)
      cv2.putText(uI2, "Fullbody", (x, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break

#platerecognition function
def plRec():
   global ln,uI2,x,y,w,h,faces,ch
   pl_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_russian_plate_number.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   plate = pl_cascade_db.detectMultiScale(uI2_gray, 1.2,3)
   ch = plate
   for (x,y,w,h) in plate:
      cv2.rectangle(uI2,(x,y),(x+w,y+h),(0,255,0),2)
      cv2.putText(uI2, "Plate Number", (x+-6, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break

#cat recognition function
def catR():
   global ln,uI2,x,y,w,h,faces,ch
   cat_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalcatface.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   cat = cat_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
   ch = cat
   for (x,y,w,h) in cat:
      cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
      cv2.putText(uI2, "Cat", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break
   print('catR')

#contour recognition function
def wareR():
   uI2 = cv2.imread(yn)
   gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   blur = cv2.blur(gray, (10,10))
   ret, thresh = cv2.threshold(blur, 1, 255, cv2.THRESH_OTSU)
   contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   cv2.drawContours(uI2, contours, -1, (0,255,0), 3)
   cv2.imwrite('Output/res.png',uI2)
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break

#frog recognition function
def frogR():
   global ln,uI2,x,y,w,h,faces,ch
   cat_cascade_db = cv2.CascadeClassifier('frog.xml')
   uI2 = cv2.imread(yn)
   uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
   cat = cat_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
   ch = cat
   for (x,y,w,h) in cat:
      cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
      cv2.putText(uI2, "Frog", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
   cv2.imwrite('Output/res.png',uI2)
   print(os.getcwd())
   while True:
      if os.path.isfile('Output/res.png') == True:
         print('show')
         showI()
         break


#show func
def showI():
   global result
   global res
   global result2
   result = Image.open('Output/res.png')
   result2 = result.resize((wid-45,hei-280))
   res = ImageTk.PhotoImage(result2)
   canvas.create_image(wid/2,hei/2 + 50,anchor = CENTER, image = res)
   print('canvas')
   rS()

#func for removing save buttons
def rS():
   global p, cco
   try:
      if p == 2 and cco ==2 or p == 4 and cco ==2:
         saveFl.place(x= 150, y = 630)
         saveHi.place(x= 1000, y = 1000)
      else:
         saveFl.place(x= 20, y = 630)
         saveHi.place(x= 270, y = 630)
   except:
      saveFl.place(x= 20, y = 630)
      saveHi.place(x= 270, y = 630)


#func for face recognition on webcam
def faceWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out,st
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Face", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for eye recognition on webcam
def eyeWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_eye.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))   
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Eye", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for upperbody recognition on webcam
def uppWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_upperbody.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))  
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Upperbody", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for lowerbody recognition on webcam
def lowWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_lowerbody.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Lowerbody", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for fullbody recognition on webcam
def fulWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_fullbody.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Fullbody", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for plate recognition on webcam
def plWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_russian_plate_number.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))   
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Plate", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for cat recognition on webcam
def catWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalcatface.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Cat", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for contour recognition on webcam
def coWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      check, uI2 = cap.read()
      gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      ret, tresh = cv2.threshold(gray, 127, 255, 0)
      contours, hierarchy = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      cv2.drawContours(uI2,contours, -1, (0,255,0), 3)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for frog recognition on webcam
def frogWb():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier('frog.xml')
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
      faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
      ch = faces
      for (x,y,w,h) in faces:
         cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
         cv2.putText(uI2, "Frog", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
      out.write(uI2)
      cv2.imwrite('Output/res.png',uI2)
      result = Image.open('Output/res.png')
      fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
      imageg = Image.fromarray(fw)
      imgtk = ImageTk.PhotoImage(image=imageg)
      video.config(image = imgtk)
      video.image = imgtk
      gui.update()

#func for face recognition on video
def faceVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
         ch = faces
         for (x,y,w,h) in faces:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Face", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()

#func for eye recognition on video
def eyeVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_eye.xml')
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
         ch = faces
         for (x,y,w,h) in faces:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Eye", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()      

   #func for upperbody recognition on video
def uppVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_upperbody.xml')
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
         ch = faces
         for (x,y,w,h) in faces:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Upperbody", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()

#func for lowerbody recognition on video
def lowVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, frame_width, frame_height, frame_size,fps
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   low_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_lowerbody.xml')
   vl()
   rS()
   while (cap.isOpened()):
      ret, uI2 = cap.read()
      if ret:
         gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         low = low_cascade_db.detectMultiScale(gray, 1.1,19)
         ch = low
         for (x,y,w,h) in low:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Lowerbody", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()

#func for fullbody recognition on video
def fulVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_fullbody.xml')
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
         ch = faces
         for (x,y,w,h) in faces:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Fullbody", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()

#func for plate recognition on video
def plVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_russian_plate_number.xml')
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
         ch = faces
         for (x,y,w,h) in faces:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Plate", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()

#func for cat recognition on video
def catVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalcatface.xml')
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
         ch = faces
         for (x,y,w,h) in faces:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Cat", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()

#func for frog recognition on video
def frogVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   face_cascade_db = cv2.CascadeClassifier('frog.xml')
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         uI2_gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         faces = face_cascade_db.detectMultiScale(uI2_gray, 1.1,19)
         ch = faces
         for (x,y,w,h) in faces:
            cv2.rectangle(uI2, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(uI2, "Frog", (x+3, y-6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()

#func for contour recognition on video
def coVd():
   global ln,uI2,x,y,w,h,faces,ch, imgtk, video,cap, fca, result, cc, out
   exitBtn.place(x = 1000, y =1000)
   cap = cv2.VideoCapture(yn)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('Output/output.avi', fourcc, 20.0, (300,300))
   fca = cap
   vl()
   rS()
   while cc<1 or (cap.isOpened()):
      succes, uI2 = cap.read()
      if succes:
         gray = cv2.cvtColor(uI2, cv2.COLOR_BGR2GRAY)
         ret, tresh = cv2.threshold(gray, 127, 255, 0)
         contours, hierarchy = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
         cv2.drawContours(uI2,contours, -1, (0,255,0), 3)
         vidout=cv2.resize(uI2,(300,300))
         out.write(vidout)
         cv2.imwrite('Output/res.png',uI2)
         result = Image.open('Output/res.png')
         fw = cv2.cvtColor(uI2, cv2.COLOR_BGR2RGB)
         imageg = Image.fromarray(fw)
         imgtk = ImageTk.PhotoImage(image=imageg)
         video.config(image = imgtk)
         video.image = imgtk
         gui.update()
   cap.release()


#thread for saving full photo
def threadSf():
   global p
   print('save')
   if p == 4 or p == 3:
      imd = canvas.create_image(270,630, anchor = NW, image = im2)
   elif p == 2 and cco == 2:
      sfD = canvas.create_image(150,630, anchor = NW, image = saveF2)
   elif p == 2 and cco == 0:
      sfD = canvas.create_image(20,630, anchor = NW, image = saveF2)
   else:
      sfD = canvas.create_image(20,630, anchor = NW, image = saveF2)
   time.sleep(0.2)
   if p == 4 or p==3:
      imBtn.place(x= 270, y = 630)
   elif p == 2 and cco == 2:
      saveFl.place(x = 150, y = 630)
   elif p == 2 and cco == 0:
      saveFl.place(x = 20, y = 630)
   else:
      saveFl.place(x = 20, y = 630)
   wts = filedialog.asksaveasfilename(title=u'Save file', filetypes=[("PNG", ".png")])
   if wts != '':
      result.save(str(wts) + '.png', 'PNG')
   if p == 4 or p == 3:
      saveFl.place(x = 20, y = 630)
      saveHi.place(x = 270, y = 630)
   elif p == 2:
      if cco == 2:
         saveFl.place(x = 150, y = 630)
         saveHi.place(x = 1000, y = 1000)
      elif cco == 0:
         saveFl.place(x = 20, y = 630)
         saveHi.place(x = 270, y = 630)
   else:
      pass
   vdbBtn.place(x = 1000, y = 1000)
   imBtn.place(x = 1000, y = 1000)
thSf = Thread(target= threadSf)

#command for saving full photo
def saveFull():
   global thSf,p
   if p == 4:
      imBtn.place(x = 1000, y =1000 )
   else:
      saveFl.place(x = 1000, y =1000 )
   if not thSf.is_alive():
      try:
         thSf.start()
      except RuntimeError:
         thSf = Thread(target=threadSf)
         thSf.start()



#thread for saving full video
def threadSv():
   print('save')
   global p, nm, cc, cco,out,cap,ext
   vbdF = canvas.create_image(20,630, anchor = NW, image = vdb2)
   time.sleep(0.2)
   vdbBtn.place(x= 20, y = 630)
   nm = 1
   cc = 1
   try:
      wts = filedialog.asksaveasfilename(title=u'Save file', filetypes=[("AVI", ".avi")])
      print(wts)
      if wts == '':
         print('err')
         try:
            os.remove('Output/output.avi')
         except:
            pass
      else:
         cap.release()
         out.release()
         print('d')
         os.rename(r'Output/output.avi',wts+'.avi')
         print('ok')
         vdbBtn["state"] = "disabled"
   except:
      pass
   vdbBtn.place(x = 1000, y = 1000)
   imBtn.place(x = 1000, y = 1000)
   if p == 2 and cco == 2:
      saveFl.place(x = 150, y = 630)
      saveHi.place(x = 1000, y = 1000)
   else:
     saveFl.place(x = 20, y = 630)
     saveHi.place(x = 270, y = 630) 
   canvas.delete(vbdF)
thSv = Thread(target= threadSv)

#command for saving full video
def saveFullv():
   global thSv
   vdbBtn.place(x = 1000, y =1000 )
   if not thSv.is_alive():
      try:
         thSv.start()
      except RuntimeError:
         thSv = Thread(target=threadSv)
         thSv.start()
imBtn['command'] = saveFull
vdbBtn['command'] = saveFullv

#thread for saving full photo2
def threadSf2():
   saveFl.place(x = 1000, y = 1000)
   saveHi.place(x = 1000, y = 1000)
   vdbBtn.place(x = 20, y = 630)
   imBtn.place(x = 270, y = 630)
thSf2 = Thread(target= threadSf2)

#command for saving full photo2
def saveFull2():
   global thSf2
   saveFl.place(x = 1000, y =1000 )
   if not thSf2.is_alive():
      try:
         thSf2.start()
      except RuntimeError:
         thSf2 = Thread(target=threadSf2)
         thSf2.start()

#thread for saving highlited photo
def threadSh():
   global ln
   global uI2,x,y,w,h,ch,p
   shD = canvas.create_image(270,630, anchor = NW, image = saveH2)
   time.sleep(0.2)
   saveHi.place(x= 270, y = 630)
   canvas.delete(shD)
   i = 0
   try:
      wts = filedialog.asksaveasfilename(title=u'Save file', filetypes=[("PNG", ".png")])
      for (x, y, w, h) in ch:
         roi_color = uI2[y:y + h, x:x + w]
         if i >=1:
            cv2.imwrite(str(wts)+str(i+1) + '.png', roi_color)
         else:
            cv2.imwrite(str(wts) + '.png', roi_color)
         i+=1
   except:
      pass
thSh = Thread(target= threadSh)

#command for saving highlited photo
def saveHigh():
   global thSh,p
   saveHi.place(x = 1000, y =1000 )
   if not thSh.is_alive():
      try:
         thSh.start()
      except RuntimeError:
         thSh = Thread(target=threadSh)
         thSh.start()
saveFl['command'] = saveFull
saveHi['command'] = saveHigh

#func for changing variable
def pl():
   global cc
   cc =1

#func for back
def askback():
   global p,sm, video,cap,cc,fln,chch,st
   if messagebox.askyesno("Back", "Are you sure?"):
      pasteBtn['state'] = 'active'
      chooseBtn['state'] = 'active'
      webcam['state'] = 'active'
      warn.place(x = 1000, y = 1000)
      exwarn.place(x = 1000, y = 1000)
      cc = 1
      st = 1
      catBtn.place(x = 1000, y = 1000)
      wareBtn.place(x = 1000, y = 1000)
      frogBtn.place(x = 1000, y = 1000)   
      chch = 0
      saveHi.place(x = 1000, y = 1000)
      saveFl.place(x = 1000, y = 1000)
      imBtn.place(x = 1000, y = 1000)
      vdbBtn.place(x = 1000, y = 1000)
      try:
         video.place(anchor="nw", x=0, y=0, width=0, height=0)
      except:
         pass
      try:
         os.remove('Output/output.avi')
      except:
         pass
      try:
         os.remove('Output/res.png')
      except:
         pass
      try:
         os.remove('Output/paste.png')
      except:
         pass
      try:
         fln.place(x = 1000, y = 1000)
      except:
         pass
      if p == 2:
         try:
            fln.place(x = 1000, y = 1000)
         except:
            pass
         catBtn.place(x= 1000, y = 1000)
         wareBtn.place(x= 1000, y = 1000)
         frogBtn.place(x = 1000, y = 1000)
      if  os.path.isfile('Output/res.png') == True:
         pl()
         try:
            fln.place(x = 1000, y = 1000)
            os.remove('Output/paste.png')
            cap.release()
            os.remove('Output/res.png')
         except:
            pass
         agree2() 
      else:
         agree2()

#func for closing
def close():
   global sm,p,cc,chch,st
   if messagebox.askokcancel("Quit", "Do you want to quit?"):
      st = 1
      try:
         os.remove('Output/output.avi')
      except:
         pass
      try:
         os.remove('Output/paste.png')
      except:
         pass
      imBtn.place(x = 1000, y = 1000)
      vdbBtn.place(x = 1000, y = 1000)
      if os.path.isfile('Output/res.png') == True:
         pl()
         cc = 1
         try:
            os.remove('Output/paste.png')
         except:
            pass
         try:
            cap.release()
            out.release()
         except:
            pass
         try:
            os.remove('Output/res.png')
         except:
            pass
         gui.quit()
      else:
        gui.quit()
gui.protocol("WM_DELETE_WINDOW", close)
start() 


gui.mainloop()