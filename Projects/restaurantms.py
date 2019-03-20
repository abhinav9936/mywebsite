from tkinter import *
import random
import time

root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_Input=StringVar()
operator=""

TopFrame=Frame(root,width=1680,height=50, bg="red",relief=SUNKEN)
TopFrame.pack(side='top')

frame1=Frame(root,width=800,height=700,relief=SUNKEN)
frame1.pack(side='left')

frame2=Frame(root,width=300,height=700,relief=SUNKEN)
frame2.pack(side='right')
#heading
localtime=time.asctime(time.localtime(time.time()))
label1=Label(TopFrame,font=('arial',50,'bold'),text="Restaurant Managements Systems",fg="IndianRed3",bd=10,anchor='w')
label1.grid(row=0,column=0)
#time show
timelabel=Label(TopFrame,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
timelabel.grid(row=1,column=0)

txtDisplay=Entry(frame2,font=('aerial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='red',justify='right')
txtDisplay.grid(columnspan=4)

def btnClick(number):
    global operator
    operator=operator + str(number)
    text_Input.set(operator)

def clearclick():
    global operator
    operator=""
    text_Input.set(operator)

def equalclick():
    global operator
    value=str(eval(operator))
    text_Input.set(value)
    operator=value 

    
button7=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="7",bg="red",command=lambda: btnClick(7)).grid(row=2,column=0)
button8=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="8",bg="red",command=lambda: btnClick(8)).grid(row=2,column=1)
button9=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="9",bg="red",command=lambda: btnClick(9)).grid(row=2,column=2)
addition=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="+",bg="red",command=lambda: btnClick('+')).grid(row=2,column=3)
button6=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="6",bg="red",command=lambda: btnClick(6)).grid(row=3,column=0)
button5=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="5",bg="red",command=lambda: btnClick(5)).grid(row=3,column=1)
button4=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="4",bg="red",command=lambda: btnClick(4)).grid(row=3,column=2)
subtraction=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="-",bg="red",command=lambda: btnClick('-')).grid(row=3,column=3)
button3=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="3",bg="red",command=lambda: btnClick(3)).grid(row=4,column=0)
button2=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="2",bg="red",command=lambda: btnClick(2)).grid(row=4,column=1)
button1=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="1",bg="red",command=lambda: btnClick(1)).grid(row=4,column=2)
multiplication=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="*",bg="red",command=lambda: btnClick('*')).grid(row=4,column=3)
button0=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="0",bg="red",command=lambda: btnClick(0)).grid(row=5,column=0)
clear=Button(frame2,padx=16,pady=16,bd=8,fg="black",command=clearclick,font=('aerial',20,'bold'),text="C",bg="red").grid(row=5,column=1)
equal=Button(frame2,padx=16,pady=16,bd=8,command=equalclick,fg="black",font=('aerial',20,'bold'),text="=",bg="red").grid(row=5,column=2)
division=Button(frame2,padx=16,pady=16,bd=8,fg="black",font=('aerial',20,'bold'),text="/",bg="red",command=lambda: btnClick('/')).grid(row=5,column=3)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

rand=StringVar()
friesvar=StringVar()
burgvar=StringVar()
vegvar=StringVar()
nonvegvar=StringVar()
cheesevar=StringVar()
subtotal=StringVar()
service_charge=StringVar()
drinks=StringVar()
tax=StringVar()
cost=StringVar()
totalcost=StringVar()

referencelabel=Label(frame1,font=('aerial',16,'bold'),text="Reference",bd=16,anchor='w')
referencelabel.grid(row=0,column=0)

textreference=Entry(frame1,font=('aerial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,
                    bg='red',justify='right')
textreference.grid(row=0,column=1)

fries=Label(frame1,font=('aerial',16,'bold'),text="French Fries",bd=16,anchor='w')
fries.grid(row=1,column=0)

textfries=Entry(frame1,font=('aerial',16,'bold'),textvariable=friesvar,bd=10,insertwidth=4,
                    bg='red',justify='right')
textfries.grid(row=1,column=1)

burgerlabel=Label(frame1,font=('aerial',16,'bold'),text="Big Burger",bd=16,anchor='w')
burgerlabel.grid(row=2,column=0)

textburger=Entry(frame1,font=('aerial',16,'bold'),textvariable=burgvar,bd=10,insertwidth=4,
                    bg='red',justify='right')
textburger.grid(row=2,column=1)

veglabel=Label(frame1,font=('aerial',16,'bold'),text="Vegetairan Meal",bd=16,anchor='w')
veglabel.grid(row=3,column=0)

textveg=Entry(frame1,font=('aerial',16,'bold'),textvariable=vegvar,bd=10,insertwidth=4,
                    bg='red',justify='right')
textveg.grid(row=3,column=1)

nonveglabel=Label(frame1,font=('aerial',16,'bold'),text="Non-Vegetairan Meal",bd=16,anchor='w')
nonveglabel.grid(row=4,column=0)

textnonveg=Entry(frame1,font=('aerial',16,'bold'),textvariable=nonvegvar,bd=10,insertwidth=4,
                    bg='red',justify='right')
textnonveg.grid(row=4,column=1)

cheeselabel=Label(frame1,font=('aerial',16,'bold'),text="Cheese Meal",bd=16,anchor='w')
cheeselabel.grid(row=5,column=0)

textcheese=Entry(frame1,font=('aerial',16,'bold'),textvariable=cheesevar,bd=10,insertwidth=4,
                    bg='red',justify='right')
textcheese.grid(row=5,column=1)
#-------------------------------------------------------------------------
drinkslabel=Label(frame1,font=('aerial',16,'bold'),text="Cold Drinks",bd=16,anchor='w')
drinkslabel.grid(row=0,column=2)
drinksreference=Entry(frame1,font=('aerial',16,'bold'),textvariable=drinks,bd=10,insertwidth=4,
                    bg='red',justify='right')
drinksreference.grid(row=0,column=3)

costlabel=Label(frame1,font=('aerial',16,'bold'),text="Cost of Meal",bd=16,anchor='w')
costlabel.grid(row=1,column=2)
costfries=Entry(frame1,font=('aerial',16,'bold'),textvariable=cost,bd=10,insertwidth=4,
                    bg='red',justify='right')
costfries.grid(row=1,column=3)

servicelabel=Label(frame1,font=('aerial',16,'bold'),text="Service Charges",bd=16,anchor='w')
servicelabel.grid(row=2,column=2)
textservice=Entry(frame1,font=('aerial',16,'bold'),textvariable=service_charge,bd=10,insertwidth=4,
                    bg='red',justify='right')
textservice.grid(row=2,column=3)

taxlabel=Label(frame1,font=('aerial',16,'bold'),text="State Tax",bd=16,anchor='w')
taxlabel.grid(row=3,column=2)
texttax=Entry(frame1,font=('aerial',16,'bold'),textvariable=tax,bd=10,insertwidth=4,
                    bg='red',justify='right')
texttax.grid(row=3,column=3)

sublabel=Label(frame1,font=('aerial',16,'bold'),text="Sub Total",bd=16,anchor='w')
sublabel.grid(row=4,column=2)
textsub=Entry(frame1,font=('aerial',16,'bold'),textvariable=subtotal,bd=10,insertwidth=4,
                    bg='red',justify='right')
textsub.grid(row=4,column=3)

totallabel=Label(frame1,font=('aerial',16,'bold'),text="Total Cost",bd=16,anchor='w')
totallabel.grid(row=5,column=2)
texttotal=Entry(frame1,font=('aerial',16,'bold'),textvariable=totalcost,bd=10,insertwidth=4,
                    bg='red',justify='right')
texttotal.grid(row=5,column=3)
#------------------------------------------------------------------
l1=Label(frame1,font=('aerial',12),text="French Fries-Rs 99.0",bd=6,anchor='w')
l1.grid(row=0,column=4)

l2=Label(frame1,font=('aerial',12),text="Cold Drinks-Rs 25.0",bd=6,anchor='w')
l2.grid(row=1,column=4)

l3=Label(frame1,font=('aerial',12),text="Non-Veg Meal-Rs 250.0",bd=6,anchor='w')
l3.grid(row=2,column=4)

l4=Label(frame1,font=('aerial',12),text="Veg Meal-Rs 200.0",bd=6,anchor='w')
l4.grid(row=3,column=4)

l5=Label(frame1,font=('aerial',12),text="Burgar-Rs 65.0",bd=6,anchor='w')
l5.grid(row=4,column=4)

l6=Label(frame1,font=('aerial',12),text="Cheese Meal-Rs 225.0",bd=6,anchor='w')
l6.grid(row=5,column=4)

l7=Label(TopFrame,font=('aerial',10),text="We welcome you to our Restaurant.Hope you enjoy!!",justify='center')
l7.grid(row=2,column=0)

l8=Label(frame1,font=('aerial',12),text="Service Charges-9%",bd=6,anchor='w')
l8.grid(row=6,column=4)

l9=Label(frame1,font=('aerial',12),text="Tax-9%",bd=6,anchor='w')
l9.grid(row=7,column=4)
#------------------------------------------------------------------
#Down Buttons
def totalclick():
    x=random.randint(12000,50000)
    randomRef=str(x)
    rand.set(randomRef)
    cof=float(friesvar.get())*99.0
    cod=float(drinks.get())*25.0
    con=float(nonvegvar.get())*250
    cov=float(vegvar.get())*200
    cob=float(burgvar.get())*65
    coc=float(cheesevar.get())*225
    cost.set("Rs."+str(cof+cod+con+cov+cob+coc))
    tax.set("Rs."+str((cof+cod+con+cov+cob+coc)*0.09))
    subtotal.set("Rs."+str((cof+cod+con+cov+cob+coc)*0.09+(cof+cod+con+cov+cob+coc)))
    service_charge.set("Rs."+str((cof+cod+con+cov+cob+coc)*0.09))
    totalcost.set("Rs."+str((cof+cod+con+cov+cob+coc)*0.18+(cof+cod+con+cov+cob+coc)))
    if(rand.get()!=""):
        l10=Label(TopFrame,font=('aerial',8),text="Your Reference id is"+str(rand.get())+".You will need this to get bill at the counter",bd=2,anchor='w')
        l10.grid(row=3,column=0)

    

    

def exitclick():
    root.destroy()

def resetclick():
    rand.set("")
    friesvar.set("")
    burgvar.set("")
    vegvar.set("")
    nonvegvar.set("")
    cheesevar.set("")
    subtotal.set("")
    service_charge.set("")
    drinks.set("")
    tax.set("")
    cost.set("")
    totalcost.set("")
    

    
buttontotal=Button(frame1,padx=16,pady=8,bd=16,fg='Black',font=('aerial',16,'bold'),width=10,
                   text="Total",bg="red",command=totalclick).grid(row=7,column=1)
buttonReset=Button(frame1,padx=16,pady=8,bd=16,fg='Black',font=('aerial',16,'bold'),width=10,
                   text="Reset",bg="red",command=resetclick).grid(row=7,column=2)
buttonexit=Button(frame1,padx=16,pady=8,bd=16,fg='Black',font=('aerial',16,'bold'),width=10,
                   text="Exit",bg="red",command=exitclick).grid(row=7,column=3)




root.mainloop()
