#Hotel Management Project

from tkinter import*
import tkinter as tk
from datetime import datetime
import time
import mysql.connector
import random

root=Tk()
root.title("Oberoi Hotels-Hotel Management")
root.geometry("1920x1080")

#Creating Databases
conn=mysql.connector.connect(host="localhost",user="root",passwd="Ravisha18")
obj=conn.cursor()
#obj.execute("create database hotel")
obj.execute("use hotel")
#obj.execute("create table table_booking (Table_No int(4),First_Name varchar(40),Last_Name varchar(40),Full_Name varchar(70), Date date, Time time, Email_ID varchar(60), Phone_No varchar(15),Restaurant varchar(40), Guest_NUmber int(2))")
#obj.execute("create table room_booking (Room_No int(4),First_Name varchar(40),Last_Name varchar(40),Full_Name varchar(70),Check-in date, Check-out date, Email_ID varchar(60), Phone_No varchar(15),Accomodation varchar(40), Number_Of_Rooms int(2))")
roomset=[101,102,103,104,105,106,107,108,109,110]
tableset=[1,2,3,4,5]

#Variables for Dining Booking
Fn=tk.StringVar()
Ln=tk.StringVar()
tareekh=tk.StringVar()
samay=tk.StringVar()
phone=tk.StringVar()
email=tk.StringVar()
bhojnalaya=tk.StringVar()
guestno=tk.StringVar()
restaurants_list=["Udaimahal","SuryaMahal and Chandni"]

#Variables for Room Booking
fn=tk.StringVar()
ln=tk.StringVar()
checkin=tk.StringVar()
checkout=tk.StringVar()

phoneno=tk.StringVar()
emailid=tk.StringVar()
accomodate=tk.StringVar()
accomodation_categories=["Premier Rooms","Luxury Suites","Twin Bedrooms"]

noofrooms=tk.StringVar()

#For Staff
SearchDate=tk.StringVar()

#Guest
def guest():
    root.title("Oberoi Hotels-Guest Home Page")
    root.geometry("1920x1080")

    def Rooms_Suites():
        root.title("Oberoi Hotels-Rooms & Suites")
        root.geometry("1920x1080")

        def RoomBooking():
            root.title("Oberoi Hotels-Book Your Room")
            root.geometry("1920x1080")

            BookYourRoom=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/RoomsBookingPage.png")
            BookYourRoomLabel=Label(image=BookYourRoom)
            BookYourRoomLabel.place(x=0,y=0)

#FormForBooking Room
            def on_enter(e):
                FName.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    Fname.insert(0,"First Name")

            FName=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=fn)
            FName.place(x=700,y=400,width=250)
            FName.insert(0,"First Name...")
            FName.bind("<FocusIn>",on_enter)
            FName.bind("<FocusOut>",on_leave)

            def on_enter(e):
                LName.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    LName.insert(0,"Last Name")

            LName=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=ln)
            LName.place(x=1175,y=400,width=250)
            LName.insert(0,"Last Name...")
            LName.bind("<FocusIn>",on_enter)
            LName.bind("<FocusOut>",on_leave)

            def on_enter(e):
                CheckInEntry.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    CheckInEntry.insert(0,"Check In")

            CheckInEntry=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=checkin)
            CheckInEntry.place(x=700,y=500,width=250)
            CheckInEntry.insert(0,"Check In")
            CheckInEntry.bind("<FocusIn>",on_enter)
            CheckInEntry.bind("<FocusOut>",on_leave)

            def on_enter(e):
                CheckOutEntry.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    CheckOutEntry.insert(0,"Check In")

            CheckOutEntry=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=checkout)
            CheckOutEntry.place(x=1175,y=500,width=250)
            CheckOutEntry.insert(0,"Check Out")
            CheckOutEntry.bind("<FocusIn>",on_enter)
            CheckOutEntry.bind("<FocusOut>",on_leave)

            def on_enter(e):
                NoOfRooms.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    NoOfRooms.insert(0,"Number Of Rooms")

            NoOfRooms=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=noofrooms)
            NoOfRooms.place(x=1175,y=600,width=350)
            NoOfRooms.insert(0,"Number Of Rooms")
            NoOfRooms.bind("<FocusIn>",on_enter)
            NoOfRooms.bind("<FocusOut>",on_leave)

            def on_enter(e):
                ContactNumber.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    ContactNumber.insert(0,"Contact Number")

            ContactNumber=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=phoneno)
            ContactNumber.place(x=1175,y=700,width=250)
            ContactNumber.insert(0,"Contact Number")
            ContactNumber.bind("<FocusIn>",on_enter)
            ContactNumber.bind("<FocusOut>",on_leave)

            def on_enter(e):
                EmailID.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    EmailID.insert(0,"Email ID")

            EmailID=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=emailid)
            EmailID.place(x=700,y=700,width=250)
            EmailID.insert(0,"Email ID")
            EmailID.bind("<FocusIn>",on_enter)
            EmailID.bind("<FocusOut>",on_leave)

            def on_enter(e):
                Accomodation.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    Accomodation.insert(0,"Accomodation")
            
            accomodate.set("Accomodation Type")
            Accomodation=OptionMenu(root,accomodate,*accomodation_categories)
            Accomodation.config(font=("Microsoft Yahei UI Light",20),bg="white",fg="black")
            Accomodation.place(x=700,y=600,width=350)
            Accomodation.bind("<FocusIn>",on_enter)
            Accomodation.bind("<FocusOut>",on_leave)

            ReserveButton=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/ReserveButton.png")
            ReserveButtonLabel=Button(image=ReserveButton,border=0,command=sendroom)
            ReserveButtonLabel.place(x=900,y=775)

            root.mainloop()

        RoomsSuites=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/RoomsSuites.png")
        RoomsSuitesLabel=Label(image=RoomsSuites)
        RoomsSuitesLabel.place(x=0,y=0)

#Sending Data to SQL
        def sendroom():
               
               k=random.randint(0,9)
               l=roomset[k]
               roomset.remove(l)
               m=str(l)
               n="Rooms Booked Succesfully.Your Room Number is "
               o=n+m
               full=fn.get()+ln.get()
                               
               top= Toplevel(root)
               top.geometry("1000x200")
               top.title("Confirmation")
               Label(top, text=o, font=("Microsoft Yahei UI Light",20)).place(x=150,y=80)
               
               qry='insert into room_booking (Room_No,First_Name ,Last_Name ,Full_Name, Check_in , Check_out , Email_ID , Phone_No ,Accomodation, Number_Of_Rooms ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
               val=(l,fn.get(),ln.get(),full,checkin.get(),checkout.get(),emailid.get(),phoneno.get(),accomodate.get(),noofrooms.get())
               obj.execute(qry,val)
               obj.execute("commit")

        BookingLogo=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/BookNowLogo.png")
        BookingLogoLabel=Button(image=BookingLogo,border=0,command=RoomBooking)
        BookingLogoLabel.place(x=800,y=915)

        root.mainloop()
                            
#Dining
    def Dining():
        root.title("Oberoi Hotels-Dining")
        root.geometry("1920x1080")

        def DiningBooking():
            root.title("Oberoi Hotels-Book Your Table")
            root.geometry("1920x1080")

            BookYourTable=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/DiningBookingPage.png")
            BookYourTableLabel=Label(image=BookYourTable)
            BookYourTableLabel.place(x=0,y=0)

#FormForBookingTable
            def on_enter(e):
                FName.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    Fname.insert(0,"First Name")

            FName=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=Fn)
            FName.place(x=700,y=400,width=250)
            FName.insert(0,"First Name...")
            FName.bind("<FocusIn>",on_enter)
            FName.bind("<FocusOut>",on_leave)

            def on_enter(e):
                LName.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    LName.insert(0,"Last Name")

            LName=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=Ln)
            LName.place(x=1175,y=400,width=250)
            LName.insert(0,"Last Name...")
            LName.bind("<FocusIn>",on_enter)
            LName.bind("<FocusOut>",on_leave)

            def on_enter(e):
                Date.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    Date.insert(0,"Date")

            Date=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=tareekh)
            Date.place(x=700,y=500,width=250)
            Date.insert(0,"Date")
            Date.bind("<FocusIn>",on_enter)
            Date.bind("<FocusOut>",on_leave)

            def on_enter(e):
                Time.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    Time.insert(0,"Time")

            Time=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=samay)
            Time.place(x=1175,y=500,width=250)
            Time.insert(0,"Time")
            Time.bind("<FocusIn>",on_enter)
            Time.bind("<FocusOut>",on_leave)

            def on_enter(e):
                NoOfGuests.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    NoOfGuests.insert(0,"Number Of Guests")

            NoOfGuests=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=guestno)
            NoOfGuests.place(x=1175,y=600,width=350)
            NoOfGuests.insert(0,"Number Of Guests")
            NoOfGuests.bind("<FocusIn>",on_enter)
            NoOfGuests.bind("<FocusOut>",on_leave)

            def on_enter(e):
                ContactNumber.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    ContactNumber.insert(0,"Contact Number")

            ContactNumber=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=phone)
            ContactNumber.place(x=1175,y=700,width=250)
            ContactNumber.insert(0,"Contact Number")
            ContactNumber.bind("<FocusIn>",on_enter)
            ContactNumber.bind("<FocusOut>",on_leave)

            def on_enter(e):
                EmailID.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    EmailID.insert(0,"Email ID")

            EmailID=Entry(root,font=("Microsoft Yahei UI Light",20),bg="white",fg="black",textvariable=email)
            EmailID.place(x=700,y=700,width=250)
            EmailID.insert(0,"Email ID")
            EmailID.bind("<FocusIn>",on_enter)
            EmailID.bind("<FocusOut>",on_leave)

            def on_enter(e):
                Restaurant.delete(0,"end")
            def on_leave(e):
                if get()=='':
                    Restaurant.insert(0,"Restaurant")

            bhojnalaya.set("Restaurant Name")
            Restaurant=OptionMenu(root,bhojnalaya,*restaurants_list)
            Restaurant.config(font=("Microsoft Yahei UI Light",20),bg="white",fg="black")
            Restaurant.place(x=700,y=600,width=300)
            Restaurant.bind("<FocusIn>",on_enter)
            Restaurant.bind("<FocusOut>",on_leave)

            ReserveButton=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/ReserveButton.png")
            ReserveButtonLabel=Button(image=ReserveButton,border=0,command=sendtable)
            ReserveButtonLabel.place(x=900,y=775)

            root.mainloop()

        Diningbg=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/Dining.png")
        DiningLabel=Label(image=Diningbg)
        DiningLabel.place(x=0,y=0)

#Sending Data to SQL
        def sendtable():
               m=random.randint(0,4)
               l=tableset[m]
               tableset.remove(l)
               n=bhojnalaya.get()
               p=("Table Booked Succesfully.Your Table Number is ")
               q=(" in ")
               r=bhojnalaya.get()
               s=str(l)
               t=p+s+q+r
               full=Fn.get()+Ln.get()
             
               top= Toplevel(root)
               top.geometry("1000x200")
               top.title("Confirmation")
               Label(top, text=t, font=("Microsoft Yahei UI Light",20)).place(x=150,y=80)
               
               qry='insert into table_booking (Table_No,First_Name,Last_Name,Full_Name ,Date , Time , Email_ID ,Phone_No, Restaurant , Guest_NUmber ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
               val=(l,Fn.get(),Ln.get(),full,tareekh.get(),samay.get(),email.get(),phone.get(),bhojnalaya.get(),guestno.get())
               obj.execute(qry,val)
               obj.execute("commit")
                
        ReserveTableButton=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/ReserveATableButton.png")
        ReserveTableButtonLabel=Button(image=ReserveTableButton,border=0,command=DiningBooking)
        ReserveTableButtonLabel.place(x=800,y=900)

        root.mainloop()
        
#Guest Home Page
    Home=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/GuestHomePage.png")
    GuestHomePageLabel=Label(image=Home)
    GuestHomePageLabel.place(x=0,y=0)

    RoomsSuitesButton=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/RoomsSuitesButton.png")
    RoomsSuitesButtonLabel=Button(image=RoomsSuitesButton,border=0,command=Rooms_Suites)
    RoomsSuitesButtonLabel.place(x=450, y=825)

    DiningButton=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/DiningButton.png")
    DiningButtonLabel=Button(image=DiningButton,border=0,command=Dining)
    DiningButtonLabel.place(x=1050,y=825)
                   
    root.mainloop()

#TABLE CHECKING
        
def stafftable():
    root.title("Oberoi Hotels-Staff Home Page")
    root.geometry("1920x1080")
    
    TableOccupancyHomePage=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/TableOccupancyHomePage.png")
    TableOccupancyHomePageLabel=Label(image=TableOccupancyHomePage)
    TableOccupancyHomePageLabel.place(x=0,y=0)

    l1 = Label(root, text = "Restaurant Name")
    l1.config(font =("Microsoft Yahei UI Light", 20))
    l1.place(x=150,y=300,width=300)
    
    r1 = Label(root, text = "Udaimahal")
    r1.config(font =("Microsoft Yahei UI Light", 20))
    r1.place(x=150,y=350,width=300)
    r2 = Label(root, text = "Udaimahal")
    r2.config(font =("Microsoft Yahei UI Light", 20))
    r2.place(x=150,y=400,width=300)
    r3 = Label(root, text = "Udaimahal")
    r3.config(font =("Microsoft Yahei UI Light", 20))
    r3.place(x=150,y=450,width=300)
    r4 = Label(root, text = "Udaimahal")
    r4.config(font =("Microsoft Yahei UI Light", 20))
    r4.place(x=150,y=500,width=300)
    r5 = Label(root, text = "Udaimahal")
    r5.config(font =("Microsoft Yahei UI Light", 20))
    r5.place(x=150,y=550,width=300)
    r6 = Label(root, text = "Suryamahal&Chandni")
    r6.config(font =("Microsoft Yahei UI Light", 20))
    r6.place(x=150,y=600,width=300)
    r7 = Label(root, text = "Suryamahal&Chandni")
    r7.config(font =("Microsoft Yahei UI Light", 20))
    r7.place(x=150,y=650,width=300)
    r8 = Label(root, text = "Suryamahal&Chandni")
    r8.config(font =("Microsoft Yahei UI Light", 20))
    r8.place(x=150,y=700,width=300)
    r9 = Label(root, text = "Suryamahal&Chandni")
    r9.config(font =("Microsoft Yahei UI Light", 20))
    r9.place(x=150,y=750,width=300)
    r10 = Label(root, text = "Suryamahal&Chandni")
    r10.config(font =("Microsoft Yahei UI Light", 20))
    r10.place(x=150,y=800,width=300)

    l2 = Label(root, text = "Table Number")
    l2.config(font =("Microsoft Yahei UI Light", 20))
    l2.place(x=475,y=300,width=200)

    r1 = Label(root, text = "1")
    r1.config(font =("Microsoft Yahei UI Light", 20))
    r1.place(x=475,y=350,width=200)
    r2 = Label(root, text = "2")
    r2.config(font =("Microsoft Yahei UI Light", 20))
    r2.place(x=475,y=400,width=200)
    r3 = Label(root, text = "3")
    r3.config(font =("Microsoft Yahei UI Light", 20))
    r3.place(x=475,y=450,width=200)
    r4 = Label(root, text = "4")
    r4.config(font =("Microsoft Yahei UI Light", 20))
    r4.place(x=475,y=500,width=200)
    r5 = Label(root, text = "5")
    r5.config(font =("Microsoft Yahei UI Light", 20))
    r5.place(x=475,y=550,width=200)
    r6 = Label(root, text = "1")
    r6.config(font =("Microsoft Yahei UI Light", 20))
    r6.place(x=475,y=600,width=200)
    r7 = Label(root, text = "2")
    r7.config(font =("Microsoft Yahei UI Light", 20))
    r7.place(x=475,y=650,width=200)
    r8 = Label(root, text = "3")
    r8.config(font =("Microsoft Yahei UI Light", 20))
    r8.place(x=475,y=700,width=200)
    r9 = Label(root, text = "4")
    r9.config(font =("Microsoft Yahei UI Light", 20))
    r9.place(x=475,y=750,width=200)
    r10 = Label(root, text = "5")
    r10.config(font =("Microsoft Yahei UI Light", 20))
    r10.place(x=475,y=800,width=200)
    
    l3 = Label(root, text = "Name")
    l3.config(font =("Microsoft Yahei UI Light", 20,))
    l3.place(x=700,y=300,width=250)

    queryname=(" select Full_Name from table_booking where Table_No=%s and Restaurant=%s")
    valu1=["1","Udaimahal"]
    valu2=["2","Udaimahal"]
    valu3=["3","Udaimahal"]
    valu4=["4","Udaimahal"]
    valu5=["5","Udaimahal"]
    valsc1=["1","SuryaMahal and Chandni"]
    valsc2=["2","SuryaMahal and Chandni"]
    valsc3=["3","SuryaMahal and Chandni"]
    valsc4=["4","SuryaMahal and Chandni"]
    valsc5=["5","SuryaMahal and Chandni"]
           
    obj.execute(queryname,valu1)
    for i in obj:
        k1=i
        
        r1 = Label(root, text = k1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=700,y=350,width=250)
    
    obj.execute(queryname,valu2)
    for i in obj:
        k2=i
        r2 = Label(root, text = k2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=700,y=400,width=250)

    obj.execute(queryname,valu3)
    for i in obj:
        k3=i
        r3 = Label(root, text = k3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=700,y=450,width=250)

    obj.execute(queryname,valu4)
    for i in obj:
        k4=i
        r4 = Label(root, text = k4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=700,y=500,width=250)

    obj.execute(queryname,valu5)
    for i in obj:
        k5=i
        r5 = Label(root, text = k5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=700,y=550,width=250)
        
    obj.execute(queryname,valsc1)
    for i in obj:
        k6=i
        r6 = Label(root, text = k6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=700,y=600,width=250)

    obj.execute(queryname,valsc2)
    for i in obj:
        k7=i
        r7 = Label(root, text = k7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=700,y=650,width=250)

    obj.execute(queryname,valsc3)
    for i in obj:
        k8=i
        r8 = Label(root, text = k8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=700,y=700,width=250)

    obj.execute(queryname,valsc4)
    for i in obj:
        k9=i
        r9 = Label(root, text = k9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=700,y=750,width=250)

    obj.execute(queryname,valsc5)
    for i in obj:
        k10=i
        r10 = Label(root, text = k10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=700,y=800,width=250)
    
    l4 = Label(root, text = "Time")
    l4.config(font =("Microsoft Yahei UI Light", 20))
    l4.place(x=975,y=300,width=200)

    querytime=("select Time from table_booking where Table_No=%s and Restaurant=%s")
    
    obj.execute(querytime,valud1)
    for i in obj:
        b1=i

        r1 = Label(root, text = b1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=975,y=350,width=200)

    obj.execute(querytime,valud2)
    for i in obj:
        b2=i
        r2 = Label(root, text = b2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=975,y=400,width=200)
    
    obj.execute(querytime,valud3)
    for i in obj:
        b3=i
        r3 = Label(root, text = b3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=975,y=450,width=200)

    obj.execute(querytime,valud4)
    for i in obj:
        b4=i
    
        r4 = Label(root, text = b4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=975,y=500,width=200)

    obj.execute(querytime,valud5)
    for i in obj:
        b5=i 
        r5 = Label(root, text = b5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=975,y=550,width=200)

    obj.execute(querytime,valsnc1)
    for i in obj:
        b6=i
        r6 = Label(root, text = b6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=975,y=600,width=200)

    obj.execute(querytime,valsnc2)
    for i in obj:
        b7=i
        r7 = Label(root, text = b7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=975,y=650,width=200)

    obj.execute(querytime,valsnc3)
    for i in obj:
        b8=i

        r8 = Label(root, text = b8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=975,y=700,width=200)   

    obj.execute(querytime,valsnc4)
    for i in obj:
        b9=i
        r9 = Label(root, text = b9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=975,y=750,width=200)

    obj.execute(querytime,valsnc5)
    for i in obj:
        b10=i
        r10 = Label(root, text = b10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=975,y=800,width=200)

    l5 = Label(root, text = "No. of Guests")
    l5.config(font =("Microsoft Yahei UI Light",20))
    l5.place(x=1200,y=300,width=200)

    querynoofguest=("select Guest_NUmber from table_booking where Table_No=%s and Restaurant=%s")
    
    valud1=["1","Udaimahal"]
    valud2=["2","Udaimahal"]
    valud3=["3","Udaimahal"]
    valud4=["4","Udaimahal"]
    valud5=["5","Udaimahal"]
    valsnc1=["1","SuryaMahal and Chandni"]
    valsnc2=["2","SuryaMahal and Chandni"]
    valsnc3=["3","SuryaMahal and Chandni"]
    valsnc4=["4","SuryaMahal and Chandni"]
    valsnc5=["5","SuryaMahal and Chandni"]           

    obj.execute(querynoofguest,valud1)
    for i in obj:
        bmw1=i
        r1 = Label(root, text = bmw1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=1200,y=350,width=200)
    
    obj.execute(querynoofguest,valud2)
    for i in obj:
        bmw2=i
        r2 = Label(root, text = bmw2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=1200,y=400,width=200)

    obj.execute(querynoofguest,valud3)
    for i in obj:
        bmw3=i
        r3 = Label(root, text = bmw3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=1200,y=450,width=200)

    obj.execute(querynoofguest,valud4)
    for i in obj:
        bmw4=i
        r4 = Label(root, text = bmw4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=1200,y=500,width=200)

    obj.execute(querynoofguest,valud5)
    for i in obj:
        bmw5=i 
        r5 = Label(root, text = bmw5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=1200,y=550,width=200)
        
    obj.execute(querynoofguest,valsnc1)
    for i in obj:
        bmw6=i
        r6 = Label(root, text = bmw6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=1200,y=600,width=200)

    obj.execute(querynoofguest,valsnc2)
    for i in obj:
        bmw7=i
        r7 = Label(root, text = bmw7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=1200,y=650,width=200)

    obj.execute(querynoofguest,valsnc3)
    for i in obj:
        bmw8=i
        r8 = Label(root, text = bmw8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=1200,y=700,width=200)

    obj.execute(querynoofguest,valsnc4)
    for i in obj:
        bmw9=i
        r9 = Label(root, text = bmw9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=1200,y=750,width=200)

    obj.execute(querynoofguest,valsnc5)
    for i in obj:
        bmw10=i
        r10 = Label(root, text = bmw10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=1200,y=800,width=200)

    l7 = Label(root, text = "Date")
    l7.config(font =("Microsoft Yahei UI Light", 20))
    l7.place(x=1425,y=300,width=200)

    querydiwas=("select Date from table_booking where Table_No=%s and Restaurant=%s")

    valud1=["1","Udaimahal"]
    valud2=["2","Udaimahal"]
    valud3=["3","Udaimahal"]
    valud4=["4","Udaimahal"]
    valud5=["5","Udaimahal"]
    valsnc1=["1","SuryaMahal and Chandni"]
    valsnc2=["2","SuryaMahal and Chandni"]
    valsnc3=["3","SuryaMahal and Chandni"]
    valsnc4=["4","SuryaMahal and Chandni"]
    valsnc5=["5","SuryaMahal and Chandni"]           

    obj.execute(querydiwas,valud1)
    for i in obj:
        bomw1=i
        r1 = Label(root, text = bomw1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=1425,y=350,width=200)
    
    obj.execute(querydiwas,valud2)
    for i in obj:
        bomw2=i
        r2 = Label(root, text = bomw2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=1425,y=400,width=200)

    obj.execute(querydiwas,valud3)
    for i in obj:
        bomw3=i
        r3 = Label(root, text = bomw3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=1425,y=450,width=200)

    obj.execute(querydiwas,valud4)
    for i in obj:
        bomw4=i
        r4 = Label(root, text = bomw4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=1425,y=500,width=200)

    obj.execute(querydiwas,valud5)
    for i in obj:
        bomw5=i 
        r5 = Label(root, text = bomw5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=1425,y=550,width=200)
        
    obj.execute(querydiwas,valsnc1)
    for i in obj:
        bomw6=i
        r6 = Label(root, text = bomw6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=1425,y=600,width=200)

    obj.execute(querydiwas,valsnc2)
    for i in obj:
        bomw7=i
        r7 = Label(root, text = bomw7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=1425,y=650,width=200)

    obj.execute(querydiwas,valsnc3)
    for i in obj:
        bomw8=i
        r8 = Label(root, text = bomw8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=1425,y=700,width=200)

    obj.execute(querydiwas,valsnc4)
    for i in obj:
        bomw9=i
        r9 = Label(root, text = bomw9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=1425,y=750,width=200)

    obj.execute(querydiwas,valsnc5)
    for i in obj:
        bomw10=i
        r10 = Label(root, text = bomw10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=1425,y=800,width=200)

    l8 = Label(root, text = "Phone")
    l8.config(font =("Microsoft Yahei UI Light", 20))
    l8.place(x=1650,y=300,width=200)

    queryphone=("select Phone_No from table_booking where Table_No=%s and Restaurant=%s")

    valud1=["1","Udaimahal"]
    valud2=["2","Udaimahal"]
    valud3=["3","Udaimahal"]
    valud4=["4","Udaimahal"]
    valud5=["5","Udaimahal"]
    valsnc1=["1","SuryaMahal and Chandni"]
    valsnc2=["2","SuryaMahal and Chandni"]
    valsnc3=["3","SuryaMahal and Chandni"]
    valsnc4=["4","SuryaMahal and Chandni"]
    valsnc5=["5","SuryaMahal and Chandni"]

    obj.execute(queryphone,valud1)
    for i in obj:
        bw1=i
        r1 = Label(root, text = bw1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=1650,y=350,width=200)
    
    obj.execute(queryphone,valud2)
    for i in obj:
        bw2=i
        r2 = Label(root, text = bw2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=1650,y=400,width=200)

    obj.execute(queryphone,valud3)
    for i in obj:
        bw3=i
        r3 = Label(root, text = bw3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=1650,y=450,width=200)

    obj.execute(queryphone,valud4)
    for i in obj:
        bw4=i
        r4 = Label(root, text = bw4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=1650,y=500,width=200)

    obj.execute(queryphone,valud5)
    for i in obj:
        bw5=i 
        r5 = Label(root, text = bw5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=1650,y=550,width=200)
        
    obj.execute(queryphone,valsnc1)
    for i in obj:
        bw6=i
        r6 = Label(root, text = bw6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=1650,y=600,width=200)

    obj.execute(queryphone,valsnc2)
    for i in obj:
        bw7=i
        r7 = Label(root, text = bw7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=1650,y=650,width=200)

    obj.execute(queryphone,valsnc3)
    for i in obj:
        bw8=i
        r8 = Label(root, text = bw8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=1650,y=700,width=200)

    obj.execute(queryphone,valsnc4)
    for i in obj:
        bw9=i
        r9 = Label(root, text = bw9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=1650,y=750,width=200)

    obj.execute(queryphone,valsnc5)
    for i in obj:
        bw10=i
        r10 = Label(root, text = bw10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=1650,y=800,width=200)

    root.mainloop()

#ROOM CHECKING

def staffroom():
    root.title("Oberoi Hotels-Staff Home Page")
    root.geometry("1920x1080")

    RoomOccupancyHomePage=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/RoomOccupancyHomePage.png")
    RoomOccupancyHomePageLabel=Label(image=RoomOccupancyHomePage)
    RoomOccupancyHomePageLabel.place(x=0,y=0)

    l1 = Label(root, text = "Room Number")
    l1.config(font =("Microsoft Yahei UI Light", 20))
    l1.place(x=150,y=300,width=300)
    
    r1 = Label(root, text = "101")
    r1.config(font =("Microsoft Yahei UI Light", 20))
    r1.place(x=150,y=350,width=300)
    r2 = Label(root, text = "102")
    r2.config(font =("Microsoft Yahei UI Light", 20))
    r2.place(x=150,y=400,width=300)
    r3 = Label(root, text = "103")
    r3.config(font =("Microsoft Yahei UI Light", 20))
    r3.place(x=150,y=450,width=300)
    r4 = Label(root, text = "104")
    r4.config(font =("Microsoft Yahei UI Light", 20))
    r4.place(x=150,y=500,width=300)
    r5 = Label(root, text = "105")
    r5.config(font =("Microsoft Yahei UI Light", 20))
    r5.place(x=150,y=550,width=300)
    r6 = Label(root, text = "106")
    r6.config(font =("Microsoft Yahei UI Light", 20))
    r6.place(x=150,y=600,width=300)
    r7 = Label(root, text = "107")
    r7.config(font =("Microsoft Yahei UI Light", 20))
    r7.place(x=150,y=650,width=300)
    r8 = Label(root, text = "108")
    r8.config(font =("Microsoft Yahei UI Light", 20))
    r8.place(x=150,y=700,width=300)
    r9 = Label(root, text = "109")
    r9.config(font =("Microsoft Yahei UI Light", 20))
    r9.place(x=150,y=750,width=300)
    r10 = Label(root, text = "110")
    r10.config(font =("Microsoft Yahei UI Light", 20))
    r10.place(x=150,y=800,width=300)

    l2 = Label(root, text = "Accomodation")
    l2.config(font =("Microsoft Yahei UI Light", 20))
    l2.place(x=475,y=300,width=200)

    queryaccomodation=("select Accomodation from room_booking where Room_No=%s")

    val1=["101"]
    val2=["102"]
    val3=["103"]
    val4=["104"]
    val5=["105"]
    val6=["106"]
    val7=["107"]
    val8=["108"]
    val9=["109"]
    val10=["110"]

    obj.execute(queryaccomodation,val1)
    for i in obj:
        k1=i
        r1 = Label(root, text = k1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=475,y=350,width=200)

    obj.execute(queryaccomodation,val2)
    for i in obj:
        k2=i    
        r2 = Label(root, text = k2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=475,y=400,width=200)

    obj.execute(queryaccomodation,val3)  
    for i in obj:
        k3=i    
        r3 = Label(root, text = k3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=475,y=450,width=200)

    obj.execute(queryaccomodation,val4)    
    for i in obj:
        k4=i
        r4 = Label(root, text = k4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=475,y=500,width=200)
        
    obj.execute(queryaccomodation,val5)
    for i in obj:
        k5=i    
        r5 = Label(root, text = k5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=475,y=550,width=200)
        
    obj.execute(queryaccomodation,val6)
    for i in obj:
        k6=i
        r6 = Label(root, text = k6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=475,y=600,width=200)
        
    obj.execute(queryaccomodation,val7)
    for i in obj:
        k7=i
        r7 = Label(root, text = k7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=475,y=650,width=200)

    obj.execute(queryaccomodation,val8)
    for i in obj:
        k8=i
        r8 = Label(root, text = k8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=475,y=700,width=200)

    obj.execute(queryaccomodation,val9)
    for i in obj:
        k9=i
        r9 = Label(root, text = k9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=475,y=750,width=200)

    obj.execute(queryaccomodation,val10)
    for i in obj:
        k10=i
        r10 = Label(root, text = k10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=475,y=800,width=200)
    
    l3 = Label(root, text = "Occupant Name")
    l3.config(font =("Microsoft Yahei UI Light", 20,))
    l3.place(x=700,y=300,width=250)

    queryname=(" select Full_Name from room_booking where Room_No=%s")
    
    obj.execute(queryname,val1)
    for i in obj:
        k1=i        
        r1 = Label(root, text = k1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=700,y=350,width=250)
    
    obj.execute(queryname,val2)
    for i in obj:
        k2=i
        r2 = Label(root, text = k2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=700,y=400,width=250)

    obj.execute(queryname,val3)
    for i in obj:
        k3=i
        r3 = Label(root, text = k3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=700,y=450,width=250)

    obj.execute(queryname,val4)
    for i in obj:
        k4=i
        r4 = Label(root, text = k4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=700,y=500,width=250)

    obj.execute(queryname,val5)
    for i in obj:
        k5=i
        r5 = Label(root, text = k5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=700,y=550,width=250)
        
    obj.execute(queryname,val6)
    for i in obj:
        k6=i
        r6 = Label(root, text = k6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=700,y=600,width=250)

    obj.execute(queryname,val7)
    for i in obj:
        k7=i
        r7 = Label(root, text = k7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=700,y=650,width=250)

    obj.execute(queryname,val8)
    for i in obj:
        k8=i
        r8 = Label(root, text = k8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=700,y=700,width=250)

    obj.execute(queryname,val9)
    for i in obj:
        k9=i
        r9 = Label(root, text = k9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=700,y=750,width=250)

    obj.execute(queryname,val10)
    for i in obj:
        k10=i
        r10 = Label(root, text = k10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=700,y=800,width=250)
    
    l4 = Label(root, text = "Check-In")
    l4.config(font =("Microsoft Yahei UI Light", 20))
    l4.place(x=975,y=300,width=200)

    querycheckin=("select Check_in from room_booking where Room_No=%s")

    obj.execute(querycheckin,val1)
    for i in obj:
        b1=i
        r1 = Label(root, text = b1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=975,y=350,width=200)

    obj.execute(querycheckin,val2)
    for i in obj:
        b2=i
    
        r2 = Label(root, text = b2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=975,y=400,width=200)    

    obj.execute(querycheckin,val3)
    for i in obj:
        b3=i
        r3 = Label(root, text = b3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=975,y=450,width=200)

    obj.execute(querycheckin,val4)
    for i in obj:
        b4=i
        r4 = Label(root, text = b4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=975,y=500,width=200)

    obj.execute(querycheckin,val5)
    for i in obj:
        b5=i 
        r5 = Label(root, text = b5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=975,y=550,width=200)

    obj.execute(querycheckin,val6)
    for i in obj:
        b6=i
        r6 = Label(root, text = b6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=975,y=600,width=200)

    obj.execute(querycheckin,val7)
    for i in obj:
        b7=i
        r7 = Label(root, text = b7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=975,y=650,width=200)

    obj.execute(querycheckin,val8)
    for i in obj:
        b8=i
        r8 = Label(root, text = b8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=975,y=700,width=200)
   
    obj.execute(querycheckin,val9)
    for i in obj:
        b9=i
        r9 = Label(root, text = b9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=975,y=750,width=200)

    obj.execute(querycheckin,val10)
    for i in obj:
        b10=i
        r10 = Label(root, text = b10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=975,y=800,width=200)

    l5 = Label(root, text = "Check-Out")
    l5.config(font =("Microsoft Yahei UI Light",20))
    l5.place(x=1200,y=300,width=200)

    querycheckout=("select Check_out from room_booking where Room_No=%s")
           
    obj.execute(querycheckout,val1)
    for i in obj:
        bmw1=i
        r1 = Label(root, text = bmw1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=1200,y=350,width=200)
    
    obj.execute(querycheckout,val2)
    for i in obj:
        bmw2=i
        r2 = Label(root, text = bmw2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=1200,y=400,width=200)

    obj.execute(querycheckout,val3)
    for i in obj:
        bmw3=i
        r3 = Label(root, text = bmw3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=1200,y=450,width=200)

    obj.execute(querycheckout,val4)
    for i in obj:
        bmw4=i
        r4 = Label(root, text = bmw4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=1200,y=500,width=200)

    obj.execute(querycheckout,val5)
    for i in obj:
        bmw5=i 
        r5 = Label(root, text = bmw5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=1200,y=550,width=200)
        
    obj.execute(querycheckout,val6)
    for i in obj:
        bmw6=i
        r6 = Label(root, text = bmw6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=1200,y=600,width=200)

    obj.execute(querycheckout,val7)
    for i in obj:
        bmw7=i
        r7 = Label(root, text = bmw7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=1200,y=650,width=200)

    obj.execute(querycheckout,val8)
    for i in obj:
        bmw8=i
        r8 = Label(root, text = bmw8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=1200,y=700,width=200)

    obj.execute(querycheckout,val9)
    for i in obj:
        bmw9=i
        r9 = Label(root, text = bmw9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=1200,y=750,width=200)

    obj.execute(querycheckout,val10)
    for i in obj:
        bmw10=i
        r10 = Label(root, text = bmw10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=1200,y=800,width=200)

    l7 = Label(root, text = "No. of Rooms")
    l7.config(font =("Microsoft Yahei UI Light", 20))
    l7.place(x=1425,y=300,width=200)

    querynoofrooms=("select Number_Of_Rooms from room_booking where Room_No=%s")           

    obj.execute(querynoofrooms,val1)
    for i in obj:
        bomw1=i
        r1 = Label(root, text = bomw1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=1425,y=350,width=200)
    
    obj.execute(querynoofrooms,val2)
    for i in obj:
        bomw2=i
        r2 = Label(root, text = bomw2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=1425,y=400,width=200)

    obj.execute(querynoofrooms,val3)
    for i in obj:
        bomw3=i
        r3 = Label(root, text = bomw3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=1425,y=450,width=200)

    obj.execute(querynoofrooms,val4)
    for i in obj:
        bomw4=i
        r4 = Label(root, text = bomw4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=1425,y=500,width=200)

    obj.execute(querynoofrooms,val5)
    for i in obj:
        bomw5=i 
        r5 = Label(root, text = bomw5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=1425,y=550,width=200)
        
    obj.execute(querynoofrooms,val6)
    for i in obj:
        bomw6=i
        r6 = Label(root, text = bomw6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=1425,y=600,width=200)

    obj.execute(querynoofrooms,val7)
    for i in obj:
        bomw7=i
        r7 = Label(root, text = bomw7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=1425,y=650,width=200)

    obj.execute(querynoofrooms,val8)
    for i in obj:
        bomw8=i
        r8 = Label(root, text = bomw8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=1425,y=700,width=200)

    obj.execute(querynoofrooms,val9)
    for i in obj:
        bomw9=i
        r9 = Label(root, text = bomw9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=1425,y=750,width=200)

    obj.execute(querynoofrooms,val10)
    for i in obj:
        bomw10=i
        r10 = Label(root, text = bomw10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=1425,y=800,width=200)

    l8 = Label(root, text = "Phone")
    l8.config(font =("Microsoft Yahei UI Light", 20))
    l8.place(x=1650,y=300,width=200)

    queryphone=("select Phone_No from room_booking where Room_No=%s")

    obj.execute(queryphone,val1)
    for i in obj:
        bw1=i
        r1 = Label(root, text = bw1)
        r1.config(font =("Microsoft Yahei UI Light", 20))
        r1.place(x=1650,y=350,width=200)
    
    obj.execute(queryphone,val2)
    for i in obj:
        bw2=i
        r2 = Label(root, text = bw2)
        r2.config(font =("Microsoft Yahei UI Light", 20))
        r2.place(x=1650,y=400,width=200)

    obj.execute(queryphone,val3)
    for i in obj:
        bw3=i
        r3 = Label(root, text = bw3)
        r3.config(font =("Microsoft Yahei UI Light", 20))
        r3.place(x=1650,y=450,width=200)

    obj.execute(queryphone,val4)
    for i in obj:
        bw4=i
        r4 = Label(root, text = bw4)
        r4.config(font =("Microsoft Yahei UI Light", 20))
        r4.place(x=1650,y=500,width=200)

    obj.execute(queryphone,val5)
    for i in obj:
        bw5=i 
        r5 = Label(root, text = bw5)
        r5.config(font =("Microsoft Yahei UI Light", 20))
        r5.place(x=1650,y=550,width=200)
        
    obj.execute(queryphone,val6)
    for i in obj:
        bw6=i
        r6 = Label(root, text = bw6)
        r6.config(font =("Microsoft Yahei UI Light", 20))
        r6.place(x=1650,y=600,width=200)

    obj.execute(queryphone,val7)
    for i in obj:
        bw7=i
        r7 = Label(root, text = bw7)
        r7.config(font =("Microsoft Yahei UI Light", 20))
        r7.place(x=1650,y=650,width=200)

    obj.execute(queryphone,val8)
    for i in obj:
        bw8=i
        r8 = Label(root, text = bw8)
        r8.config(font =("Microsoft Yahei UI Light", 20))
        r8.place(x=1650,y=700,width=200)

    obj.execute(queryphone,val9)
    for i in obj:
        bw9=i
        r9 = Label(root, text = bw9)
        r9.config(font =("Microsoft Yahei UI Light", 20))
        r9.place(x=1650,y=750,width=200)

    obj.execute(queryphone,val10)
    for i in obj:
        bw10=i
        r10 = Label(root, text = bw10)
        r10.config(font =("Microsoft Yahei UI Light", 20))
        r10.place(x=1650,y=800,width=200)

    root.mainloop()    

#LandingPage

bg=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/Landing_Page.png")
LandingLabel=Label(image=bg)
LandingLabel.place(x=0,y=0)

GuestLogo=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/GuestLogo.png")
GuestLogoLabel=Button(image=GuestLogo,border=0,command=guest)
GuestLogoLabel.place(x=625, y=750)

RoomOccupancyLogo=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/RoomOCcupancy.png")
RoomOccupancyLabel=Button(image=RoomOccupancyLogo,border=0,command=staffroom)
RoomOccupancyLabel.place(x=875, y=750)

TableOccupancyLogo=PhotoImage(file="C:/1-DATA STORAGE/Ravisha/RAVISHA/Class XII/Computer Science/Hotel Management Project/Images/TableOccupancy.png")
TableOccupancyLabel=Button(image=TableOccupancyLogo,border=0,command=stafftable)
TableOccupancyLabel.place(x=1125, y=750)

root.mainloop()





