import sqlite3
from tkinter import *
import datetime
from array import *
import tksheet

#hello
#import menucreate as M

date=datetime.date.today()
datesorted=date.strftime("%d-%m-%Y")

comic_sans_ms=("Comic Sans MS",13,"underline")
book_antiqua=("Book Antiqua",10,"bold")





def delete():
    try:    
        con=sqlite3.connect('My_Account')
        cur=con.cursor()
        delet=123
        cur.execute("delete from accounts where sqlbank=={}".format(delet))
        con.commit()
        con.close()
    except sqlite3.Error as err:
        print("Error - ",err)
    



def exits():
    exit(0)


#------------------------------------------------CREATE MENU-----------------------------------------------------#






#------------------------------------------------MENU---------------------------------------------------#

if __name__=="__main__":
        root=Tk()
        root.geometry("500x500")
        root.title("Budget App")
        root.configure(bg="#18181b")





def mainmenu(): 
    def clearmenu():
        lblmenu.destroy()
        btnnew.destroy()
        btninsert.destroy()
        btnupdate.destroy()
        btnsort.destroy()
        btndelete.destroy()
        btnexit.destroy()
        

    lblmenu=Label(root,text="Menu",bg="#18181b",fg="white",font=comic_sans_ms)
    #Buttons
    btnnew=Button(root,text="Create New Record",bg="#303036",fg="white",font=book_antiqua,width=20,command=lambda:[clearmenu(),menucreate()])
    btnupdate=Button(root,text="Update existing record",bg="#303036",fg="white",font=book_antiqua,width=20,command=lambda:[clearmenu(),menuupdate()])
    btninsert=Button(root,text="Insert Record",bg="#303036",fg="white",font=book_antiqua,width=20,command=lambda:[clearmenu(),menuinsert()])
    btndelete=Button(root,text="Delete Record",bg="#303036",fg="white",font=book_antiqua,width=20,command=delete)
    btnsort=Button(root,text="Sort Record",bg="#303036",fg="white",font=book_antiqua,width=20)
    btnexit=Button(root,text="Exit",bg="#303036",fg="white",font=book_antiqua,width=20,command=exits)


    #Lable Placements
    lblmenu.place(relx=0.5,rely=0.1,anchor=CENTER)    
    #Button Placements
    btnnew.place(relx=0.5,rely=0.25,anchor=CENTER)
    btnupdate.place(relx=0.5,rely=0.325,anchor=CENTER)
    btninsert.place(relx=0.5,rely=0.4,anchor=CENTER)
    btnsort.place(relx=0.5,rely=0.475,anchor=CENTER)
    btndelete.place(relx=0.5,rely=0.55,anchor=CENTER)
    btnexit.place(relx=0.5,rely=0.625,anchor=CENTER)
    


def menucreate():
    def clearcreate():
        lblass.destroy()
        tbass.destroy()
        lbltbname.destroy()
        tbname.destroy()
        btnsubmit.destroy()
        btnhome.destroy()
        lblmenucreate.destroy()
        

    lblmenucreate=Label(root,text="Create Your Account",fg="white",bg="#18181b",font=comic_sans_ms)
    lblass=Label(root,text="Enter how many assets :",fg="white",bg="#18181b")
    tbass=Entry(root)
    lbltbname=Label(root,text="Enter Your Name :",fg="white",bg="#18181b")
    tbname=Entry(root)
    
    def create():
        try:    
            con=sqlite3.connect('My_Account')
            cur=con.cursor()
            tblname=tbname.get()
            cur.execute("create table if not exists '{}'(date varchar(50) PRIMARY KEY NOT NULL,sqlbank int,sqlvault int,sqlwallet int,crypto int)".format(tblname))
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)

    btnsubmit=Button(root,text="Submit",bg="#303036",fg="white",font=book_antiqua,width=10,command=lambda:[create()])
    btnhome=Button(root,text="Home",bg="#303036",fg="white",font=book_antiqua,width=10,command=lambda:[clearcreate(),mainmenu()])

    #placemet
    lblmenucreate.place(relx=0.37,rely=0.07,anchor=CENTER)
    lblass.place(relx=0.2,rely=0.2,anchor=CENTER,width=150)
    tbass.place(relx=0.5,rely=0.2,anchor=CENTER,width=150)
    lbltbname.place(relx=0.2,rely=0.3,anchor=CENTER,width=150)
    tbname.place(relx=0.5,rely=0.3,anchor=CENTER,width=150)
    btnsubmit.place(relx=0.2,rely=0.4,anchor=CENTER,width=150)
    btnhome.place(relx=0.502,rely=0.4,anchor=CENTER,width=150)

    '''tblass=tbass.get()
    for i in range(tblass):'''

def menuupdate():
    tables=[]
    buttons=[]
    def cleardisplay():
        btnhome.destroy()
        sheet.destroy()
        '''for tab in tables:
            tab.destroy()
        for but in buttons:
            but.destroy()'''

    try:
        con=sqlite3.connect("My_Account")
        cur=con.cursor()
        data=[]
        for row in cur.execute("select name from sqlite_master Where type='table'"):
            data.append(row)
            print(row)
        con.close()
    except sqlite3.Error as err:
        print("Error..... :",err)


    sheet = tksheet.Sheet(root)
    sheet.grid()
    total_rows=len(data)

    sheet.set_sheet_data([[f"{ri+c}" for c in range(2)] for ri in range(total_rows)])
    sheet.enable_bindings(("single_select","row_select","column_width_resize","rc_select"))








    
    '''mystr = StringVar()
    
    
    
    mi=0

    for i in range(total_rows):
        mystr.set(data[1])
        mi+=1
        
            
        table=Entry(root,textvariable=mystr,width=20,fg='white',bg='grey',font=('Areal',16),state=DISABLED)
        button=Button(root,text="Open")

        button.grid(row=i, column=4)            
        table.grid(row=i)
        table.insert(END, data[i])
            
        tables.append(table)
        print(mi)
        buttons.append(button)'''


    btnhome=Button(root,text="Home",bg="#303036",fg="white",font=book_antiqua,width=10,command=lambda:[cleardisplay(),mainmenu()])
    btnhome.place(relx=0.2,rely=0.65,anchor=CENTER,width=170)












def menuinsert():
    def clearinsert():
        lblmenuinsert.destroy()
        lblbank1.destroy()
        sqlbank1.destroy()
        lblvault1.destroy()
        sqlvault1.destroy()
        lblwallet1.destroy()
        sqlwallet1.destroy()
        lblcrypto1.destroy()
        sqlcrypto1.destroy()
        btnsubmit.destroy()
        btnhome.destroy()
    
    def clearinput():
        sqlbank1.delete(0,END)
        sqlvault1.delete(0,END)
        sqlwallet1.delete(0,END)
        sqlcrypto1.delete(0,END)


    lblmenuinsert=Label(root,text="Insert Data into Records: ",bg="black",fg="white",font=comic_sans_ms)
    lblbank1=Label(root,text="Enter your current bank balance : ",fg="white",bg="#18181b")
    sqlbank1=Entry(root)
    lblvault1=Label(root,text="Enter your current vault balance :",fg="white",bg="#18181b")
    sqlvault1=Entry(root)
    lblwallet1=Label(root,text="Enter your current wallet balance :",fg="white",bg="#18181b")
    sqlwallet1=Entry(root)
    lblcrypto1=Label(root,text="Enter your current crypto balance :",fg="white",bg="#18181b")
    sqlcrypto1=Entry(root)

    btnsubmit=Button(root,text="Submit",bg="#303036",fg="white",font=book_antiqua,width=10,command=lambda:[insert(),clearinput()])
    btnhome=Button(root,text="Home",bg="#303036",fg="white",font=book_antiqua,width=10,command=lambda:[clearinsert(),mainmenu()])

    lblmenuinsert.place(relx=0.37,rely=0.07,anchor=CENTER)
    lblbank1.place(relx=0.2,rely=0.2,anchor=CENTER,width=190)
    sqlbank1.place(relx=0.5,rely=0.2,anchor=CENTER,width=120)
    lblvault1.place(relx=0.2,rely=0.3,anchor=CENTER,width=190)
    sqlvault1.place(relx=0.5,rely=0.3,anchor=CENTER,width=120)
    lblwallet1.place(relx=0.2,rely=0.4,anchor=CENTER,width=190)
    sqlwallet1.place(relx=0.5,rely=0.4,anchor=CENTER,width=120)
    lblcrypto1.place(relx=0.2,rely=0.5,anchor=CENTER,width=190)
    sqlcrypto1.place(relx=0.5,rely=0.5,anchor=CENTER,width=120)

    btnsubmit.place(relx=0.2,rely=0.6,anchor=CENTER,width=170)
    btnhome.place(relx=0.5,rely=0.6,anchor=CENTER,width=170)

    def insert():
        try:    
            con=sqlite3.connect('My_Account')
            cur=con.cursor()
            #cur.execute("create table if not exists accounts(date varchar(50) NOT NULL,sqlbank int,sqlvault int,sqlwallet int,crypto int)")
            bank1=sqlbank1.get()
            vault1=sqlvault1.get()
            wallet1=sqlwallet1.get()
            crypto1=sqlcrypto1.get()
            cur.execute("SHOW TABLES shan1")
            con.commit()
            con.close()
        except sqlite3.Error as err:
            print("Error - ",err)

def menudisplayall():
    def cleardisplay():
        btnhome.destroy()

    btnhome=Button(root,text="Home",bg="#303036",fg="white",font=book_antiqua,width=10,command=lambda:[cleardisplay(),mainmenu()])
    btnhome.place(relx=0.5,rely=0.6,anchor=CENTER,width=170)
    dis=input("enter tb name: ")
    
    
    try:    
        con=sqlite3.connect('My_Account')
        cur=con.cursor()
        for row in cur.execute("Select * from '{}'".format(dis)):
            print(row)
        con.close()
    except sqlite3.Error as err:
        print("Error - ",err)
    

mainmenu()
root.mainloop()