import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Nirbhay15Tiwari@#")
ch='y'
while ch=='y' or ch=='Y':
    mycursor=con.cursor()
    print("1.insert record")
    print("2.modify record")
    print("3.delete record")
    print("4.show all records")
    print("5.exit")
    mycursor.execute('use 12csql')
    def add_record():
        sno=int(input("enter serial no. :"))
        name=input("student name :")
        admn=int(input("admission no. of student :"))
        lclass=input("class of student :")
        book_name=input("book issued by the student :")
        author_name=input("author of the book issued :")
        book_id=input("id of book :")
        date_of_issue=input("date when book is issued :")
        cmd="insert into library1(sno,name,admn,lclass,book_name,author_name,book_id,date_of_issue) values({},'{}',{},'{}','{}','{}','{}','{}')".format(sno,name,admn,lclass,book_name,author_name,book_id,date_of_issue)
        mycursor.execute(cmd)
        con.commit()
    def modify_record():
        sno=int(input("enter serial no. :"))
        cmd="select * from library1 where sno={}".format(sno)
        mycursor.execute(cmd)
        row=mycursor.fetchone()
        if row is None:
            print("error:no record with given serial no. ")
            return
        else:
            print("the current values are :")
            print("name =",row[1])
            print("admn =",row[2])
            print("class =",row[3])
            print("book_name =",row[4])
            print("author_name =",row[5])
            print("book_id =",row[6])
            print("date_of_issue =",row[7])
            print("enter new values :")
            sno=int(input("enter serial no. :"))
            name=input("student name :")
            admn=int(input("admission no. of student :"))
            lclass=input("class of student :")
            book_name=input("book issued by the student :")
            author_name=input("author of the book issued :")
            book_id=input("id of book :")
            date_of_issue=input("date when book is issued :")
            cmd="update library1 set name='{}',admn={},lclass='{}',book_name='{}',author_name='{}',book_id='{}',date_of_issue='{}' where sno={}".format(name,admn,lclass,book_name,author_name,book_id,date_of_issue,sno)
        mycursor.execute(cmd)
        con.commit()
    def delete_record():
        name=input("enter name:")
        cmd="select * from library1 where name='{}'".format(name)
        mycursor.execute(cmd)
        row=mycursor.fetchone()
        if row is None:
            print("error: no record with given serial no. ")
        else:
            print("the current values are :")
            print("name =",row[1])
            print("admn =",row[2])
            print("class =",row[3])
            print("book_name =",row[4])
            print("author_name =",row[5])
            print("book_id =",row[6])
            print("date_of_issue =",row[7])
        q=input('do you want to delete this data???')
        if q=="y" or q=="Y":
            cmd="delete from library1 where name='{}'".format(name)
            mycursor.execute(cmd)
            con.commit()
    def show_all_record():
        mycursor.execute("select * from library1")
        print("sno \tname \tadmn \tclass \tbook_name \t \tauthor_name \t \tbook_id \t\tdate_of_issue")
        for row in mycursor.fetchall():
            print(row[0],row[1],row[2],row[3],row[4],'\t',row[5],'\t ',row[6],'\t ',row[7],sep="\t")
    choice=int(input("what you want to do(1-5):"))
    if choice==1:
        add_record()
    if choice==2:
        modify_record()
    if choice==3:
        delete_record()
    elif choice==4:
        show_all_record()
    else:
        con.close()
    ch=input('do you want to continue??(y/n)')

        


