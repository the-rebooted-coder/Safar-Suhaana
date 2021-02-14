#______            ______             _    _               _____           _                 
#| ___ \           | ___ \           | |  (_)             /  ___|         | |                
#| |_/ /_   _ ___  | |_/ / ___   ___ | | ___ _ __   __ _  \ `--. _   _ ___| |_ ___ _ __ ___  
#| ___ \ | | / __| | ___ \/ _ \ / _ \| |/ / | '_ \ / _` |  `--. \ | | / __| __/ _ \ '_ ` _ \ 
#| |_/ / |_| \__ \ | |_/ / (_) | (_) |   <| | | | | (_| | /\__/ / |_| \__ \ ||  __/ | | | | |
#\____/ \__,_|___/ \____/ \___/ \___/|_|\_\_|_| |_|\__, | \____/ \__, |___/\__\___|_| |_| |_|
#                                                   __/ |         __/ |                      
#                                                  |___/         |___/                       
#______          _           _    ______                                                     
#| ___ \        (_)         | |   | ___ \        _                                           
#| |_/ / __ ___  _  ___  ___| |_  | |_/ /_   _  (_)                                          
#|  __/ '__/ _ \| |/ _ \/ __| __| | ___ \ | | |                                              
#| |  | | | (_) | |  __/ (__| |_  | |_/ / |_| |  _                                           
#\_|  |_|  \___/| |\___|\___|\__| \____/ \__, | (_)                                          
#              _/ |                       __/ |                                              
#             |__/                       |___/                                               
# _____                       _               _____                                          
#/  ___|                     | |             /  ___|                                         
#\ `--. _ __   __ _ _ __   __| | __ _ _ __   \ `--.  __ ___  _____ _ __   __ _               
# `--. \ '_ \ / _` | '_ \ / _` |/ _` | '_ \   `--. \/ _` \ \/ / _ \ '_ \ / _` |              
#/\__/ / |_) | (_| | | | | (_| | (_| | | | | /\__/ / (_| |>  <  __/ | | | (_| |              
#\____/| .__/ \__,_|_| |_|\__,_|\__,_|_| |_| \____/ \__,_/_/\_\___|_| |_|\__,_|              
#      | |                                                                                   
#      |_|

#______ _                                 __           ______ _____  ___ _________  ___ _____   _           __                                        _             
#| ___ \ |                               / _|          | ___ \  ___|/ _ \|  _  \  \/  ||  ___| | |         / _|                                      (_)            
#| |_/ / | ___  __ _ ___  ___   _ __ ___| |_ ___ _ __  | |_/ / |__ / /_\ \ | | | .  . || |__   | |__   ___| |_ ___  _ __ ___   _ __ _   _ _ __  _ __  _ _ __   __ _ 
#|  __/| |/ _ \/ _` / __|/ _ \ | '__/ _ \  _/ _ \ '__| |    /|  __||  _  | | | | |\/| ||  __|  | '_ \ / _ \  _/ _ \| '__/ _ \ | '__| | | | '_ \| '_ \| | '_ \ / _` |
#| |   | |  __/ (_| \__ \  __/ | | |  __/ ||  __/ |    | |\ \| |___| | | | |/ /| |  | || |___  | |_) |  __/ || (_) | | |  __/ | |  | |_| | | | | | | | | | | | (_| |
#\_|   |_|\___|\__,_|___/\___| |_|  \___|_| \___|_|    \_| \_\____/\_| |_/___/ \_|  |_/\____/  |_.__/ \___|_| \___/|_|  \___| |_|   \__,_|_| |_|_| |_|_|_| |_|\__, |
#                                                                                                                                                              __/ |
#                                                                                                                                                             |___/ 


from tkinter import *
from PIL import Image,ImageTk
import sqlite3
import tkinter.messagebox as messagebox
import pyglet
import random
pyglet.font.add_file('Safar Bold Italic.ttf')
pyglet.font.add_file('Safar Bold.ttf')
pyglet.font.add_file('Safar Regular.ttf')
pyglet.font.add_file('Safar Italics.ttf')
pyglet.font.add_file('Safar Bold Italic.ttf')

s_root = Tk()
Label(s_root, text="Hello")
s_root.geometry('600x490')
s_root.overrideredirect(True)
load_bg = Image.open("root4_bg.png")
image_bg = ImageTk.PhotoImage(load_bg)
img = Label(s_root, image=image_bg)
img.image = image_bg
img.place(x=0, y=0)
Label(s_root, text="Bus Booking System", font=('Product Sans Bold', 30)).pack(pady=25)
Label(s_root, text="Developed as a part of courses: \n Advanced Programming Lab & DBMS Lab", font=('Product Sans', 20,'italic')).pack(pady=25)
Label(s_root, text="Created and Maintained by Spandan Saxena \n Enr: 191B265 \n", font=('Product Sans', 20)).pack(pady=25)
Label(s_root, text="Project Supervisors: \n Dr. Mahesh Kumar and Mr. Nileshkumar R. Patel", font=('Product Sans', 15,'bold')).pack(pady=25)
s_root.after(4000, s_root.destroy)
s_root.mainloop()

def fun():
    root=Tk()
    root.geometry('567x510')
    root.configure(background='#F3F3F3')
    root.title('Safar Suhaana 191B265 Spandan Saxena')
    head_frame=Frame(root,bg="#913f92",borderwidth=5)
    head_frame.pack()
    img=Image.open("init_bg.png")
    photo=ImageTk.PhotoImage(img)
    photo_label=Label(root,image=photo)
    photo_label.pack()
    f1=Frame(root,bg='#F1DAD7',borderwidth=5)
    f1.place(x=0, y=0)
    #Add bus
    def sec():#add bus function
        root.destroy()
        root1=Tk()
        root1.geometry('500x550')
        head_label2=Label(root1,text="Bus Booking System", fg='#fff',bg="#1a1a1a",font=("bold","20"))
        head_label2.config(anchor="center")
        head_label2.grid(row=0,column=4)
        #maintaining background
        load_bg = Image.open('root1_bg.png')
        image_bg = ImageTk.PhotoImage(load_bg)
        img = Label(root1, image=image_bg)
        img.image = image_bg
        img.place(x=0, y=0)
        #setting data
        fullname=Label(root1,text="Driver's Name",font=('Product Sans',11)).place(x=100,y=10)
        contact=Label(root1,text="Contact Number",font=('Product Sans',11)).place(x=100,y=45)
        adress=Label(root1,text="Bus Stop Add",font=('Product Sans',11)).place(x=100,y=80)
        #assigning variables
        namevar=StringVar()
        contactvar=IntVar()
        adressvar=StringVar()
        #taking input
        nameentry=Entry(root1,textvariable=namevar).place(x=230,y=10)
        contactentry=Entry(root1,textvariable=contactvar).place(x=230,y=45)
        adressentry=Entry(root1,textvariable=adressvar).place(x=230,y=80)
        #add detail function
        def add_detail():
            name1=namevar.get()
            if not name1:
                    messagebox.showinfo("Driver Name Error","Please Enter the Name of Driver")
            else:
                operator=Label(root1,text="Operator Name",font=('Product Sans',11)).place(x=100,y=150)
                bustype=Label(root1,text="Bus Type",font=('Product Sans',11)).place(x=100,y=185)
                from1=Label(root1,text="Source City",font=('Product Sans',11)).place(x=100,y=220)
                to=Label(root1,text="Destination City",font=('Product Sans',11)).place(x=100,y=255)
                date=Label(root1,text="Date (DD-MM-YYYY)",font=('Product Sans',11)).place(x=100,y=290)
                deptime=Label(root1,text="Departure (24hrs)",font=('Product Sans',11)).place(x=100,y=325)
                arrtime=Label(root1,text="Arrival (24hrs)",font=('Product Sans',11)).place(x=100,y=360)
                fare=Label(root1,text="Fare (INR)",font=('Product Sans',11)).place(x=100,y=395)
                seat=Label(root1,text="Available Seats",font=('Product Sans',11)).place(x=100,y=430)
                def save():
                    name1=namevar.get()
                    from1=fromvar.get()
                    to1=tovar.get()
                    dep1=depvar.get()
                    arr1=arrvar.get()
                    fare1=farevar.get()
                    seat1=seatvar.get()
                    if not from1:
                        messagebox.showinfo("Source City Error","Please Enter the Source City")
                    elif not to1:
                        messagebox.showinfo("Destination City Error","Please Enter the Destination City")
                    elif from1==to1:
                        messagebox.showinfo("Trip Error","Source and Destination Cities can't be Same")
                    elif not dep1:
                        messagebox.showinfo("Departure Time Error","Please Enter the Departure Time")
                    elif not arr1:
                        messagebox.showinfo("Arrival Time Error","Please Enter the Arrival Time")
                    elif not fare1:
                        messagebox.showinfo("Fare Error","Please Enter the Fare of Travel")
                    elif not seat1:
                        messagebox.showinfo("Seats Error","Please Enter the Number of Seats Offered")
                    else:
                        con=sqlite3.Connection('spandan_db')
                        cur=con.cursor()
                        cur.execute("""CREATE TABLE IF NOT EXISTS travel1(name text,from1 text,to1 text,date text,arr text,fare INTEGER,seat INTEGER)""")
                        con.commit()
                        cur.execute("INSERT INTO travel1 VALUES (?,?,?,?,?,?,?)",(name1,from1,to1,dep1,arr1,fare1,seat1))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Bus Details Saved Succesfully!")
                        root1.destroy()
                        fun()
            #making variable
                operatorvar=StringVar()
                bustypevar=StringVar()
                fromvar=StringVar()
                tovar=StringVar()
                datevar=StringVar()
                depvar=StringVar()
                arrvar=StringVar()
                farevar=IntVar()
                seatvar=IntVar()
                #taking input
                operatorentry=Entry(root1,textvariable=operatorvar).place(x=230,y=150)
                busentry=Entry(root1,textvariable=bustypevar).place(x=230,y=185)
                fromentry=Entry(root1,textvariable=fromvar).place(x=230,y=220)
                toentry=Entry(root1,textvariable=tovar).place(x=230,y=255)
                dateentry=Entry(root1,textvariable=datevar).place(x=245,y=290)
                depentry=Entry(root1,textvariable=depvar).place(x=230,y=325)
                arrentry=Entry(root1,textvariable=arrvar).place(x=230,y=360)
                fareentry=Entry(root1,textvariable=farevar).place(x=230,y=395)
                seatentry=Entry(root1,textvariable=seatvar).place(x=230,y=430)
                Button(text="Save Bus",width=10,bg="black",font=('Product Sans',11,),fg="#fff",command=save).place(x=200,y=458)
        Button(text="Continue",width=10,bg="black",font=('Product Sans',11,),fg="#fff",command=add_detail).place(x=200,y=110)

        root1.mainloop()
    b1=Button(root,text="Add Bus",padx=3,pady=3,bg='#CDB5CD',borderwidth=6,font=('Product Sans', 14),command=sec)
    b1.place(x=250, y=360)
    # b1.bind('<Button-1>',sec)
    #Search bus fun
    def search_bus():
        root.destroy()
        root2=Tk()
        root2.title('Book Now')
        root2.geometry('500x550')
        head_label3=Label(root2,text="Bus Booking System",bg="#1a1a1a", fg='#fff',font=("bold","20"))
        head_label3.config(anchor="center")
        head_label3.grid(row=0,column=4)
        #bg
        load_bg = Image.open('root2_bg.png')
        image_bg = ImageTk.PhotoImage(load_bg)
        img = Label(root2, image=image_bg)
        img.image = image_bg
        img.place(x=0, y=0)
        from1=Label(root2,text="Source City",font=('Product Sans',11)).place(x=130, y=180)
        to=Label(root2,text="Destination City",font=('Product Sans',11)).place(x=130, y=210)
        date=Label(root2,text="Date of Travel",font=('Product Sans',11)).place(x=130, y=240)
        dformat=Label(root2,text="Enter Date in DD-MM-YYYY",font=('Product Sans',11,'bold')).place(x=160, y=270)

        fromvar=StringVar()
        tovar=StringVar()
        datevar=StringVar()

        fromentry=Entry(root2,textvariable=fromvar).place(x=240, y=180)
        toentry=Entry(root2,textvariable=tovar).place(x=240, y=210)
        dateentry=Entry(root2,textvariable=datevar).place(x=240, y=240)
        def home():
            root2.destroy()
            fun()
        Button(text="Go Back",bg="black",font=('Product Sans',11),fg="#fff",command=home).place(x=224, y=335)
        def search():
            con=sqlite3.Connection('spandan_db')
            cur=con.cursor()
            root2.destroy()
            root3=Tk()
            root3.geometry('600x390')
            load_bg = Image.open('root3_bg.png')
            image_bg = ImageTk.PhotoImage(load_bg)
            img = Label(root3, image=image_bg)
            img.image = image_bg
            img.place(x=0, y=0)

            customer_name=StringVar()
            customer_number=StringVar()
            customer_age=StringVar()
            
            name=Label(root3,text="Operator |",font=('Product Sans',11),padx=-5).grid(row=2,column=0)
            from2=Label(root3,text="Source |",font=('Product Sans',11),padx=5).grid(row=2,column=1)
            to=Label(root3,text="Destination |",font=('Product Sans',11),padx=5).grid(row=2,column=2)
            dep=Label(root3,text="Dep |",font=('Product Sans',11),padx=5).grid(row=2,column=3)
            arr=Label(root3,text="Arr |",font=('Product Sans',11),padx=5).grid(row=2,column=4)
            fare=Label(root3,text="Fare |",font=('Product Sans',11),padx=5).grid(row=2,column=5)
            seat=Label(root3,text="Available Seats",font=('Product Sans',11),padx=5).grid(row=2,column=6)
            
            cust_name=Label(root3,text="Customer Name",font=('Product Sans',11,'bold')).place(x=20, y=150)
            cust_name_entry=Entry(root3,textvariable=customer_name).place(x=20, y=180)

            cust_no=Label(root3,text="Mobile Number",font=('Product Sans',11,'bold')).place(x=150, y=150)
            cust_no_entry=Entry(root3,textvariable=customer_number).place(x=150, y=180)

            cust_age=Label(root3,text="Age",font=('Product Sans',11,'bold')).place(x=280, y=150)
            cust_age_entry=Entry(root3,textvariable=customer_age).place(x=280, y=180)


            cust_gen=Label(root3,text="Gender",font=('Product Sans',11,'bold')).place(x=410, y=150)

            cust_gen_entry = StringVar(root3)
            cust_gen_entry.set("Select")

            w = OptionMenu(root3, cust_gen_entry, "Male", "Female", "Not to Disclose")

            w.place(x=410,y=180)
            
            def book():
                n = random.randint(1,8)
                seat = str(n)
                pnr = random.randint(1000,3000)
                ticket = str(pnr)
                customer_set=customer_name.get()
                mobile_set=customer_number.get()
                age_set=customer_age.get()
                if not customer_set:
                    messagebox.showinfo("Error","Please Enter the name for which ticket is being booked!")
                elif not mobile_set:
                    messagebox.showinfo("Error","Please Enter the Mobile Number of the traveller!")
                elif not age_set:
                    messagebox.showinfo("Error","Please Enter the age of traveller!")
                else:
                    seatvar=IntVar()
                    seatv=seatvar.get
                    con=sqlite3.Connection('spandan_db')
                    cur=con.cursor()
                    cur.execute("UPDATE travel1 SET seat = seat - 1",(seatv,))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Reciept","<--------------------->\n"+"Booking for "+customer_set+"\nSeat Number: " +seat+ "\nTicket No: "+ ticket + "\nMobile Number: "+mobile_set+"\nAge: "+age_set+"\nBooking Status: Confirmed\n"+"\nPay the amount while boarding the bus\nMultiple Buses can be booked together also!\n" + "<--------------------->")
                    root3.destroy()
                    fun()
            Button(text="Book Now",font=('Product Sans',11,'bold'),bg="black",fg="#FFFFFF",command=book).place(x=260,y=292)
            fromv=fromvar.get()
            cur.execute("SELECT * FROM travel1 WHERE from1=(?)",(fromv,))
            store=cur.fetchall()
            con.close()
            print(store)
            num=3
            for i in store:
                print(i)
                n=1
                v=IntVar()
                name2=Label(root3,text=i[0]).grid(row=num)
                from2=Label(root3,text=i[1]).grid(row=num,column=1)
                to=Label(root3,text=i[2]).grid(row=num,column=2)
                dep=Label(root3,text=i[3]).grid(row=num,column=3)
                arr=Label(root3,text=i[4]).grid(row=num,column=4)
                fare=Label(root3,text=i[5]).grid(row=num,column=5)
                seat=Label(root3,text=i[6]).grid(row=num,column=6)
                radio=Radiobutton(root3,variable=v,value=n).grid(row=num,column=7)
                n+1
                num=num+1

            
        Button(text="Search",bg="black",font=('Product Sans', 11),fg="#B0E0E6",command=search).place(x=230, y=300)
        
    b2=Button(root,bg="#FFBD59",text="Search and Book",font=('Product Sans', 14),borderwidth=6,padx=4,pady=4,command=search_bus)
    b2.place(x=215, y=285)
    def delete():
        con=sqlite3.Connection('spandan_db')
        cur=con.cursor()
        cur.execute("DELETE FROM travel1")
        con.commit()
        messagebox.showinfo("Database","Database spandan_db cleared")
    b3=Button(root,bg='#FF5757', font=('Product Sans', 14, 'bold'),text="Clear Entire Database",borderwidth=6,padx=4,pady=4,command=delete)
    b3.place(x=185, y=430)
    root.mainloop()
fun()
