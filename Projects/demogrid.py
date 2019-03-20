#MADE BY ABHINAV KUMAR
#AN interface to find filename , path and modification time
import tkinter
import os
from datetime import datetime
print(tkinter.TkVersion)
print(tkinter.TclVersion)
mainwindow=tkinter.Tk()
mainwindow.title("Grid Demo")
mainwindow.geometry('640x480-8-200')
mainwindow.minsize(height=640,width=480)
mainwindow['padx']=8

label=tkinter.Label(mainwindow,text="Demo Grid")
label.grid(row=0,column=0,columnspan=3)

mainwindow.columnconfigure(0,weight=100)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=1000)
mainwindow.columnconfigure(3,weight=600)
mainwindow.columnconfigure(4,weight=1000)
mainwindow.rowconfigure(0,weight=1)
mainwindow.rowconfigure(1,weight=10)
mainwindow.rowconfigure(2,weight=1)
mainwindow.rowconfigure(3,weight=3)
mainwindow.rowconfigure(4,weight=3)

filelist=tkinter.Listbox(mainwindow)
filelist.grid(row=1,column=0,sticky='nsew',rowspan=2)
filelist.config(border=2,relief='sunken')
for zone in os.listdir('/Windows/System32'):
    filelist.insert(tkinter.END,zone)

listScroll=tkinter.Scrollbar(mainwindow,orient=tkinter.VERTICAL,command=filelist.yview)
listScroll.grid(row=1,column=1,sticky='nsw',rowspan=2)
filelist['yscrollcommand']=listScroll.set
filelist.selection_set(first=0)

optionFrame=tkinter.LabelFrame(mainwindow,text="File Details")
optionFrame.grid(row=1,column=2,sticky='ne')
rbValue=tkinter.IntVar()
rbValue.set(3)

resultLabel=tkinter.Label(mainwindow,text="Result")
resultLabel.grid(row=2,column=2,sticky='nw')
result=tkinter.Entry(mainwindow,font=('default',10))
result.grid(row=2,column=2,sticky='sw')
#resultScroll=tkinter.Scrollbar(mainwindow,orient=tkinter.HORIZONTAL,command=result.xview)
#resultScroll.grid(row=3,column=2,sticky='sw',rowspan=2)
#result['xscrollcommand']=resultScroll.set

def filename():
    result.delete(0,'end')
    fileselected=filelist.get(filelist.curselection())
    result.insert(0,fileselected)
def pathinfo():
    result.delete(0,'end')
    fileselected=filelist.get(filelist.curselection())
    result.insert(0,"C:/Windows/System32/")
    result.insert('end',fileselected)
def modificationtime():
    result.delete(0,'end')
    fileselected=filelist.get(filelist.curselection())
    mod_time=os.stat("C:/Windows/System32/"+fileselected).st_mtime
    result.insert(0,datetime.fromtimestamp(mod_time))
    
radio1=tkinter.Radiobutton(optionFrame,text="Filename",value=1,variable=rbValue,command=filename)
radio2=tkinter.Radiobutton(optionFrame,text="Path",value=2,variable=rbValue,command=pathinfo)
radio3=tkinter.Radiobutton(optionFrame,text="Timestamp",value=3,variable=rbValue,command=modificationtime)
radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')



timeFrame=tkinter.LabelFrame(mainwindow,text='Time')
timeFrame.grid(row=3,column=0,sticky='new')

hourSpinner=tkinter.Spinbox(timeFrame,width=2,values=tuple(range(0,24)))
minuteSpinner=tkinter.Spinbox(timeFrame,width=2,from_=0,to=59)
secondSpinner=tkinter.Spinbox(timeFrame,width=2,from_=0,to=59) 
hourSpinner.grid(row=0,column=0)
tkinter.Label(timeFrame,text=':').grid(row=0,column=1)
minuteSpinner.grid(row=0,column=2)
tkinter.Label(timeFrame,text=':').grid(row=0,column=3)
secondSpinner.grid(row=0,column=4)
timeFrame['padx']=36

dateFrame=tkinter.Frame(mainwindow)
dateFrame.grid(row=4,column=0,sticky="new")

dayLabel=tkinter.Label(dateFrame,text="Day")
monthLabel=tkinter.Label(dateFrame,text="Month")
yearLabel=tkinter.Label(dateFrame,text="Year")
dayLabel.grid(row=0,column=0,sticky='w')
monthLabel.grid(row=0,column=1,sticky='w')
yearLabel.grid(row=0,column=2,sticky='w')

daySpin=tkinter.Spinbox(dateFrame,width=5,from_=1,to=31)
monthSpin=tkinter.Spinbox(dateFrame,width=5,values=('Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'))
yearSpin=tkinter.Spinbox(dateFrame,width=5,from_=2000,to=2099)
daySpin.grid(row=0,column=0,sticky='w')
monthSpin.grid(row=0,column=1,sticky='w')
yearSpin.grid(row=0,column=2,sticky='w')

okButton=tkinter.Button(mainwindow,text="OK")
cancelButton=tkinter.Button(mainwindow,text="Cancel",command=mainwindow.destroy )
okButton.grid(row=4,column=3,sticky='e')
cancelButton.grid(row=4,column=4,sticky='w')
mainwindow.mainloop()
print(rbValue.get())
