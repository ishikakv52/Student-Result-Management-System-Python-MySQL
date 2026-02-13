from tkinter import *
root=Tk()
root.geometry("500x900+200+200")
root.title("Result")

l1=Label(root,text="Enter Name : ",background="Gray",bd=10,relief=RIDGE)
l1.pack()
e1=Entry(root)
e1.pack()

l2=Label(root,text="Enter roll number : ",background="Gray",bd=10,relief=RIDGE)
l2.pack()
e2=Entry(root)
e2.pack()

l3=Label(root,text="Enter email : ",background="Gray",bd=10,relief=RIDGE)
l3.pack()
e3=Entry(root)
e3.pack()

l4=Label(root,text="Enter marks of subject 1",background="gray",bd=10,relief=RIDGE)
l4.pack()
e4=Entry(root)
e4.pack()

l5=Label(root,text="Enter marks of subject 2",background="gray",bd=10,relief=RIDGE)
l5.pack()
e5=Entry(root)
e5.pack()

l6=Label(root,text="Enter marks of subject 3",background="gray",bd=10,relief=RIDGE)
l6.pack()
e6=Entry(root)
e6.pack()

l7=Label(root,text="Enter marks of subject 4",background="gray",bd=10,relief=RIDGE)
l7.pack()
e7=Entry(root)
e7.pack()

l8=Label(root,text="Enter marks of subject 5",background="gray",bd=10,relief=RIDGE)
l8.pack()
e8=Entry(root)
e8.pack()
# (name,rollno,email,marks1,marks2,marks3,marks4,marks5,total,percentage)
def file_save():
    n=e1.get()
    r=e2.get()
    em=e3.get()
    a=e4.get()
    a1=float(a)
    b=e5.get()
    b1=float(b)
    c=e6.get()
    c1=float(c)
    d=e7.get()
    d1=float(d)
    e=e8.get()
    ef=float(e)
    if a1 < 0 or b1 < 0 or c1 < 0 or d1 < 0 or ef < 0:
            print("Marks cannot be negative")

    else:
        t=a1+b1+c1+d1+ef
        ts=str(t)
        per=t/5 
        ps=str(per)
        print("Percentage : ",per)
        file=n
        f=open(file+".txt","w")
        f.write("Name : "+n+"\nRoll no : "+r+"\nEmail : "+em+"\n-----------Marks----------"+"\nSubject 1 : "+a+"\nSubject 2 : "+b+"\nSubject 3 : "+c+"\nSubject 4 : "+d+"\nSubject 5 : "+e+"\nTotal : "+ts+"\nPercentage : "+ps)
        print("File generated successfully")
        f.close()

def sql_save():
        import mysql.connector
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jaat@2010",
            database="da"
        )

        cursor = con.cursor() 
        n=e1.get()
        r=e2.get()
        ri=int(r)
        em=e3.get()
        a=e4.get()
        a1=float(a)
        b=e5.get()
        b1=float(b)
        c=e6.get()
        c1=float(c)
        d=e7.get()
        d1=float(d)
        e=e8.get()
        ef=float(e)
        if a1 < 0 or b1 < 0 or c1 < 0 or d1 < 0 or ef < 0:
            print("Marks cannot be negative")

        else:
            t=a1+b1+c1+d1+ef
            per=t/5 

            sql='''INSERT INTO result(name,rollno,email,marks1,marks2,marks3,marks4,marks5,total,percentage)
            values
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''
            values=(n,ri,em,a1,b1,c1,d1,ef,t,per)
            cursor.execute(sql,values)
            con.commit()
            print("Data inserted")
            con.close()
fbt=Button(root,text="Save As File ",command=file_save)
fbt.pack()

sqlbt=Button(root,text="Save to records ",command=sql_save)
sqlbt.pack()

root.mainloop()
