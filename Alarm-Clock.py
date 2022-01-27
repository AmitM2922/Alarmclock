from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    
    
display=Tk()
display.geometry("450x250+550+250")
display.title("Alarm Clock By Amit Mulmule")
display.config(bg='aliceblue',relief=SOLID,border=6)

hour=StringVar()
sec=StringVar()
min=StringVar()

label_alarm=Label(display,text=" Alarm Clock By Amit Mulmule",font=("Helevetica",11,"bold"))
label_alarm.pack()

labelhr=Label(display,text="Hr",font=("Helevetica",11,"bold"),bg='lightyellow',fg='red').place(x=120,y=28)
labelmin=Label(display,text="Min",font=("arial",11,"bold"),bg='lightyellow',fg='red').place(x=190,y=28)
labelsec=Label(display,text="Sec",font=("arial",11,"bold"),fg='red',bg='lightyellow').place(x=260,y=28)

hbox=Entry(display,textvariable=hour,width=5,bg='pink',relief=SOLID,fg='darkred',font=("arial",15,"bold")).place(x=110,y=50)
mbox=Entry(display,textvariable=min,width=5,bg='pink',relief=SOLID,fg='darkred',font=("arial",15,"bold")).place(x=180,y=50)
sbox=Entry(display,textvariable=sec,width=5,bg='pink',relief=SOLID,fg='darkred',font=("arial",15,"bold")).place(x=250,y=50)

button=Button(display,text="Set Alarm",font=("arial",12,"bold"),fg='silver',bg='darkred',activebackground='yellow',border=5,command=actual_time)
button.pack(pady=65)

labelnote=Label(display,text="Note:Enter Time in Only 24 Hr Format",font=("arial",12,"bold"),bg='lightgray',fg='red')
labelnote.pack()


display.mainloop()