from tkinter import *
import time
import pyautogui
from pynput.mouse import Button, Controller

clickerL = 0
clickerR = 0

window = Tk()
window.title('AUTOMATIONEN--PYTHON')
c = Canvas(window, relief = FLAT, width=400, height=200, bg='white')
c.pack(side = TOP, anchor = NW, padx = 10, pady = 10)

def pressed(event):

    pos = c.coords(w)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        time.sleep(5)
        c.itemconfig(w,fill="gray")
        pyautogui.keyDown('w')

    pos = c.coords(a)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        time.sleep(5)
        c.itemconfig(a,fill="gray")
        pyautogui.keyDown('a')

    pos = c.coords(s)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        time.sleep(5)
        c.itemconfig(s,fill="gray")
        pyautogui.keyDown('s')

    pos = c.coords(d)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        time.sleep(5)
        c.itemconfig(d,fill="gray")
        pyautogui.keyDown('d')

def release(event):

    pos = c.coords(w)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        c.itemconfig(w,fill="white")
        pyautogui.keyUp('w')

    pos = c.coords(a)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        c.itemconfig(a,fill="white")
        pyautogui.keyUp('a')

    pos = c.coords(s)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        c.itemconfig(s,fill="white")
        pyautogui.keyUp('s')

    pos = c.coords(d)
    if event.x > pos[0] and event.x < pos[2] and event.y > pos[1] and event.y < pos[3]:
        c.itemconfig(d,fill="white")
        pyautogui.keyUp('d')       

def click(event):
    global clickerL, clickerR
    if event.keysym == 'q':
        clickerL = 1
        clickerR = 0
        c.itemconfig(autoclicker,fill="gray")
        c.itemconfig(autoclicker2,fill="white")
    elif event.keysym == 'e':
        clickerR = 1
        clickerL = 0
        c.itemconfig(autoclicker2,fill="gray")
        c.itemconfig(autoclicker,fill="white")
    else:
        clickerL = 0
        clickerR = 0
        c.itemconfig(autoclicker,fill="white")
        c.itemconfig(autoclicker2,fill="white")

        

w = c.create_rectangle(60,10,110,60,outline="black",width=5)
a = c.create_rectangle(10,60,60,110,outline="black",width=5)
s = c.create_rectangle(60,60,110,110,outline="black",width=5)
d = c.create_rectangle(110,60,160,110,outline="black",width=5)

ww = c.create_text(85,35,text="W")
aa = c.create_text(35,85,text="A")
ss = c.create_text(85,85,text="S")
dd = c.create_text(135,85,text="D")

info1 = c.create_text(95,130,text="Linke Maustaste = aktivieren")
info2 = c.create_text(90,145,text="(danach 5 Sekunden Pause)")
info3 = c.create_text(105,170,text="Rechte Maustaste = deaktivieren")

c.bind_all("<Button-1>", pressed)
c.bind_all("<Button-2>", release)

autoclicker = c.create_rectangle(240,35,300,85,outline="black",width=5)
autoclicker2 = c.create_rectangle(300,35,360,85,outline="black",width=5)

autoclickerr = c.create_text(270,60,text="Maus-L\n100Cps")
autoclickerr2 = c.create_text(330,60,text="Maus-L\n2Cps")

info4 = c.create_text(300,100,text="'q' = Maus-L 100Cps")
info5 = c.create_text(300,115,text="'e' = Maus-L 2Cps")
info6 = c.create_text(300,130,text="(andere Taste = deaktivieren)")

c.bind_all("<Key>", click)


while True:
    window.update() 
    if clickerL == 1:
        Controller().click(Button.left)
        time.sleep(0.01)
    elif clickerR == 1:
        Controller().click(Button.left)
        time.sleep(0.6)