from tkinter import *
import pymysql

window=Tk()
window.title("Sign up")
window.configure(background="light blue")
window.geometry("600x480")
fNvar=StringVar()
lNvar=StringVar()
aNvar=StringVar()
bNvar=StringVar()
cNvar=StringVar()
dNvar=StringVar()
eNvar=StringVar()
gNvar=StringVar()
hNvar=StringVar()
iNvar=StringVar()
jNvar=StringVar()
kNvar=StringVar()
mNvar=StringVar()

def storeDataInTextFile(data):
    with open("studenttxt.txt", "a") as fObj:
        fObj.write(data + '\n')
    print("Text inserted")

def printData():
    fNam=fNvar.get()
    lNam=lNvar.get()
    aNam=aNvar.get()
    bNam=bNvar.get()
    cNam=cNvar.get()
    dNam=dNvar.get()
    eNam=eNvar.get()
    gNam=gNvar.get()
    hNam=hNvar.get()
    iNam=iNvar.get()
    jNam=jNvar.get()
    kNam=kNvar.get()
    mNam=mNvar.get()
    mysql_data = (fNam, lNam, aNam, bNam, cNam, dNam, eNam, gNam, hNam, iNam, jNam, kNam, mNam)
    userd = (f"Date: {fNam}\n"
            f"Name: {lNam}\n"
            f"Mobile no: {aNam}\n"
            f"Alternate no: {bNam}\n"
            f"Email id: {cNam}\n"
            f"Address: {dNam}\n"
            f"Course interested: {eNam}\n"
            f"How you came to know about us: {gNam}\n"
            f"Are you experienced or fresher: {hNam}\n"
            f"Contact person from besant technologies: {iNam}\n"
            f"Counselor: {jNam}\n"
            f"Fees: {kNam}\n"
            f"Comment: {mNam}\n")
    
    return userd,mysql_data

def sqlbase(data):
    
    connection=pymysql.connect(host="127.0.0.1",user="root",password='',database='employeee')
    cursor=connection.cursor()

    addRecord='''INSERT INTO empldata (
            Date, Name, Mobile_no, Alternate_no, Email_id, Address, 
            Course, How_you_came_to_know_about_us, 
            Are_you_Experienced_or_a_fresher, Contact_person_from_besant_technologies, 
            Counselor, Fees, Comment
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(addRecord,data)
    connection.commit()
    print("Table created successfully")
    connection.close()
    
def storeData():
    userd,mysql_data=printData()
    storeDataInTextFile(userd)
    sqlbase(mysql_data)
def signUp():
    fLbl=Label(window,text="Date",bg="light blue").grid(row=0,column=0,sticky=W)
    lLbl=Label(window,text="Name",bg="light blue").grid(row=1,column=0,sticky=W)
    aLbl=Label(window,text="Mobile no:",bg="light blue").grid(row=2,column=0,sticky=W)
    bLbl=Label(window,text="Alternate no",bg="light blue").grid(row=3,column=0,sticky=W)
    cLbl=Label(window,text="Email id:",bg="light blue").grid(row=4,column=0,sticky=W)
    dLbl=Label(window,text="Address:",bg="light blue").grid(row=5,column=0,sticky=W)
    eLbl=Label(window,text="Course interested:",bg="light blue").grid(row=6,column=0,sticky=W)
    gLbl=Label(window,text="How you came to know about us:",bg="light blue").grid(row=7,column=0,sticky=W)
    hLbl=Label(window,text="Are you experienced or fresher:",bg="light blue").grid(row=8,column=0,sticky=W)
    iLbl=Label(window,text="Contact person from besant technologies:",bg="light blue").grid(row=9,column=0,sticky=W)
    jLbl=Label(window,text="Counselor:",bg="light blue").grid(row=10,column=0,sticky=W)
    kLbl=Label(window,text="Fees:",bg="light blue").grid(row=11,column=0,sticky=W)
    mLbl=Label(window,text="Comment:",bg="light blue").grid(row=12,column=0,sticky=W)
    fName=Entry(window,textvariable=fNvar)
    lName=Entry(window,textvariable=lNvar)
    aName=Entry(window,textvariable=aNvar)
    bName=Entry(window,textvariable=bNvar)
    cName=Entry(window,textvariable=cNvar)
    dName=Entry(window,textvariable=dNvar)
    eName=Entry(window,textvariable=eNvar)
    gName=Entry(window,textvariable=gNvar)
    hName=Entry(window,textvariable=hNvar)
    iName=Entry(window,textvariable=iNvar)
    jName=Entry(window,textvariable=jNvar)
    kName=Entry(window,textvariable=kNvar)
    mName=Entry(window,textvariable=mNvar)
    fName.grid(row=0,column=1,ipadx=80)
    lName.grid(row=1,column=1,ipadx=80)
    aName.grid(row=2,column=1,ipadx=80)
    bName.grid(row=3,column=1,ipadx=80)
    cName.grid(row=4,column=1,ipadx=80)
    dName.grid(row=5,column=1,ipadx=80)
    eName.grid(row=6,column=1,ipadx=80)
    gName.grid(row=7,column=1,ipadx=80)
    hName.grid(row=8,column=1,ipadx=80)
    iName.grid(row=9,column=1,ipadx=80)
    jName.grid(row=10,column=1,ipadx=80)
    kName.grid(row=11,column=1,ipadx=80)
    mName.grid(row=12,column=1,ipadx=80)
    fNvar.set(" ")
    lNvar.set(" ")
    Button(window,text="submit",bg="green",fg="blue",command=storeData).grid(row=13,column=1,sticky=W)
    Button(window,text="quit",bg="red",fg="blue",command=storeData).grid(row=13,column=2)
    window.mainloop()
signUp()

"""
import pymysql
connection=pymysql.connect(host="127.0.0.1",user="root",password='',database='employeee')
cursor=connection.cursor()

cQuery='''create table empldata(Date varchar(20),
                                Name char(20),
                                Mobile_no varchar(20),
                                Alternate_no varchar(20),
                                Email_id varchar(20),
                                Address varchar(50),
                                Course char(50),
                                How_you_came_to_know_about_us char(50),
                                Are_you_Experienced_or_a_fresher char(50),
                                Contact_person_from_besant_technologies char(50),
                                Counselor char(50),
                                Fees char(50),
                                Comment char(50))'''
cursor.execute(cQuery)
connection.commit()
print("Table created successfully")
connection.close()
"""
"""
import pymysql
connection=pymysql.connect(host="127.0.0.1",user="root",password='',database='employee')
cursor=connection.cursor()
"""
#input from the user to add data
"""
en=input("Enter the name:")
ei=input("Enter the id:")
es=input("Enter the sal:")
ed=input("Enter the desi:")
ee=input("Enter the experience:")
addRecord='''insert into empdata(ename,eid,esalary,edesign,eexpe)
values('%s','%s','%s','%s','%s')'''%(en,ei,es,ed,ee)
"""
#update data
"""
updateval='''update empdata
                set ename="khabib",esalary=30000
                WHERE eid=43'''
"""

#delete data
"""
delval='''Delete from empdata Where ename="jhon"'''
"""
#insert data
"""

cQuery='''Insert into empdata(ename,eid,esalary,edesign,eexpe)
            values("jhon",123,200000,"general",1)'''
"""

"""
retrieve="Select *  from empdata"
cursor.execute(retrieve)
records= cursor.fetchall()
print("*************************")
for record in records:
    print(record)
print("*************************")
print("Read successfull")
"""
"""
cursor.execute(delval)
connection.commit()
print("Table created successfully")
connection.close()

"""

























