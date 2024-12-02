import mysql.connector as mysql
def enter_monday(code,name,sub):
   dm={}
   print(('-')*141)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR MONDAY",(' ')*49,"|")
   print(('-')*141)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("Enter class for I period:")
   t_2=input("Enter class for II period:")
   t_3=input("Enter class for III period:")
   t_4=input("Enter class for IV period:")
   t_5=input("Enter class for V period:")
   t_6=input("Enter class for VI period:")
   t_7=input("Enter class for VII period:")
   dm['code']=code
   dm['name']=name
   dm['sub']=sub
   dm['t1']=t_1
   dm['t2']=t_2
   dm['t3']=t_3
   dm['t4']=t_4
   dm['t5']=t_5
   dm['t6']=t_6
   dm['t7']=t_7
   return dm
def enter_tuesday(code,name,sub):
   dt={}
   print(('-')*141)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR TUESDAY",(' ')*48,"|")
   print(('-')*141)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("Enter class for I period:")
   t_2=input("Enter class for II period:")
   t_3=input("Enter class for III period:")
   t_4=input("Enter class for IV period:")
   t_5=input("Enter class for V period:")
   t_6=input("Enter class for VI period:")
   t_7=input("Enter class for VII period:")
   dt['code']=code
   dt['name']=name
   dt['sub']=sub
   dt['t1']=t_1
   dt['t2']=t_2
   dt['t3']=t_3
   dt['t4']=t_4
   dt['t5']=t_5
   dt['t6']=t_6
   dt['t7']=t_7
   return dt
def enter_wednesday(code,name,sub):
   dw={}
   print(('-')*141)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR WEDNESDAY",(' ')*45,"|")
   print(('-')*141)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("Enter class for I period:")
   t_2=input("Enter class for II period:")
   t_3=input("Enter class for III period:")
   t_4=input("Enter class for IV period:")
   t_5=input("Enter class for V period:")
   t_6=input("Enter class for VI period:")
   t_7=input("Enter class for VII period:")
   dw['code']=code
   dw['name']=name
   dw['sub']=sub
   dw['t1']=t_1
   dw['t2']=t_2
   dw['t3']=t_3
   dw['t4']=t_4
   dw['t5']=t_5
   dw['t6']=t_6
   dw['t7']=t_7
   return dw
def enter_thursday(code,name,sub):
   dth={}
   print(('-')*141)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR THURSDAY",(' ')*47,"|")
   print(('-')*141)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("Enter class for I period:")
   t_2=input("Enter class for II period:")
   t_3=input("Enter class for III period:")
   t_4=input("Enter class for IV period:")
   t_5=input("Enter class for V period:")
   t_6=input("Enter class for VI period:")
   t_7=input("Enter class for VII period:")
   dth['code']=code
   dth['name']=name
   dth['sub']=sub
   dth['t1']=t_1
   dth['t2']=t_2
   dth['t3']=t_3
   dth['t4']=t_4
   dth['t5']=t_5
   dth['t6']=t_6
   dth['t7']=t_7
   return dth
def enter_friday(code,name,sub):
   df={}
   print(('-')*141)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR FRIDAY",(' ')*49,"|")
   print(('-')*141)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("Enter class for I period:")
   t_2=input("Enter class for II period:")
   t_3=input("Enter class for III period:")
   t_4=input("Enter class for IV period:")
   t_5=input("Enter class for V period:")
   t_6=input("Enter class for VI period:")
   t_7=input("Enter class for VII period:")
   df['code']=code
   df['name']=name
   df['sub']=sub
   df['t1']=t_1
   df['t2']=t_2
   df['t3']=t_3
   df['t4']=t_4
   df['t5']=t_5
   df['t6']=t_6
   df['t7']=t_7
   return df
def enter_saturday(code,name,sub):
   ds={}
   print(('-')*141)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR SATURDAY",(' ')*47,"|")
   print(('-')*141)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("Enter class for I period:")
   t_2=input("Enter class for II period:")
   t_3=input("Enter class for III period:")
   t_4=input("Enter class for IV period:")
   t_5=input("Enter class for V period:")
   t_6=input("Enter class for VI period:")
   t_7=input("Enter class for VII period:")
   ds['code']=code
   ds['name']=name
   ds['sub']=sub
   ds['t1']=t_1
   ds['t2']=t_2
   ds['t3']=t_3
   ds['t4']=t_4
   ds['t5']=t_5
   ds['t6']=t_6
   ds['t7']=t_7
   return ds
def display(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   query="Select * from MONDAY"
   cursor.execute(query)
   val=cursor.fetchall()
   print("Teacher's code\t\tTeacher's name\t\tTeacher's sybject")
   for data in val:
      print(data[0],"\t\t\t",data[1],"\t\t",data[2])
def create(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   t_code=int(input("Enter teacher's code:"))
   t_name=input(("Enter teacher name:"))
   t_sub=input("Enter subject of teacher:")
   d1=enter_monday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS MONDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d2=enter_tuesday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS TUESDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d3=enter_wednesday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS WEDNESDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d4=enter_thursday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS THURSDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d5=enter_friday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS FRIDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d6=enter_saturday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS SATURDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   query="Insert into MONDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d1['code'],d1['name'],d1['sub'],d1['t1'],d1['t2'],d1['t3'],d1['t4'],d1['t5'],d1['t6'],d1['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into TUESDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d2['code'],d2['name'],d2['sub'],d2['t1'],d2['t2'],d2['t3'],d2['t4'],d2['t5'],d2['t6'],d2['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into WEDNESDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d3['code'],d3['name'],d3['sub'],d3['t1'],d3['t2'],d3['t3'],d3['t4'],d3['t5'],d3['t6'],d3['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into THURSDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d4['code'],d4['name'],d4['sub'],d4['t1'],d4['t2'],d4['t3'],d4['t4'],d4['t5'],d4['t6'],d4['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into FRIDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d5['code'],d5['name'],d5['sub'],d5['t1'],d5['t2'],d5['t3'],d5['t4'],d5['t5'],d5['t6'],d5['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into SATURDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d6['code'],d6['name'],d6['sub'],d6['t1'],d6['t2'],d6['t3'],d6['t4'],d6['t5'],d6['t6'],d6['t7'])
   cursor.execute(query)
   connection.commit()
   print("Your values have been inserted successfully.")
def search_data(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   display(a,b)
   code=int(input("Enter Teacher's code whose data you want to search:"))
   print("Which details you want to see?")
   print("1.PARTICULAR DAY")
   print("2.WHOLE TIME TABLE")
   ch=int(input("Enter your choice:"))
   query="Select * from MONDAY where T_CODE={}".format(code)
   cursor.execute(query)
   M=cursor.fetchall()
   query="Select * from TUESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   T=cursor.fetchall()
   query="Select * from WEDNESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   W=cursor.fetchall()
   query="Select * from THURSDAY where T_CODE={}".format(code)
   cursor.execute(query)
   Th=cursor.fetchall()
   query="Select * from FRIDAY where T_CODE={}".format(code)
   cursor.execute(query)
   F=cursor.fetchall()
   query="Select * from SATURDAY where T_CODE={}".format(code)
   cursor.execute(query)
   S=cursor.fetchall()
   if ch==1:
      ch1=1
      print("Enter 1 for Monday.")
      print("Enter 2 for Tuesday.")
      print("Enter 3 for Wednesday.")
      print("Enter 4 for Thursday.")
      print("Enter 5 for Friday.")
      print("Enter 6 for Saturday.")
      print("Enter 0 for exit.")
      while ch1!=0:
         ch1=input("Enter day:")
         if ch1==0:
            break
         elif ch1 in ['monday','Monday']:
            print("CODE : ",M[0][0])
            print("NAME : ",M[0][1])
            print("SUBJECT : ",M[0][2])
            print("I PERIOD : ",M[0][3])
            print("II PERIOD : ",M[0][4])
            print("III PERIOD : ",M[0][5])
            print("IV PERIOD : ",M[0][6])
            print("V PERIOD : ",M[0][7])
            print("VI PERIOD : ",M[0][8])
            print("VII PERIOD : ",M[0][9])
         elif ch1 in ['tuesday','Tuesday']:
            print("CODE : ",T[0][0])
            print("NAME : ",T[0][1])
            print("SUBJECT : ",T[0][2])
            print("I PERIOD : ",T[0][3])
            print("II PERIOD : ",T[0][4])
            print("III PERIOD : ",T[0][5])
            print("IV PERIOD : ",T[0][6])
            print("V PERIOD : ",T[0][7])
            print("VI PERIOD : ",T[0][8])
            print("VII PERIOD : ",T[0][9])
         elif ch1 in ['wednesday','Wednesday']:
            print("CODE : ",W[0][0])
            print("NAME : ",W[0][1])
            print("SUBJECT : ",W[0][2])
            print("I PERIOD : ",W[0][3])
            print("II PERIOD : ",W[0][4])
            print("III PERIOD : ",W[0][5])
            print("IV PERIOD : ",W[0][6])
            print("V PERIOD : ",W[0][7])
            print("VI PERIOD : ",W[0][8])
            print("VII PERIOD : ",W[0][9])
         elif ch1 in ['thursday','Thursday']:
            print("CODE : ",Th[0][0])
            print("NAME : ",Th[0][1])
            print("SUBJECT : ",Th[0][2])
            print("I PERIOD : ",Th[0][3])
            print("II PERIOD : ",Th[0][4])
            print("III PERIOD : ",Th[0][5])
            print("IV PERIOD : ",Th[0][6])
            print("V PERIOD : ",Th[0][7])
            print("VI PERIOD : ",Th[0][8])
            print("VII PERIOD : ",Th[0][9])
         elif ch1 in ['friday','Friday']:
            print("CODE : ",F[0][0])
            print("NAME : ",F[0][1])
            print("SUBJECT : ",F[0][2])
            print("I PERIOD : ",F[0][3])
            print("II PERIOD : ",F[0][4])
            print("III PERIOD : ",F[0][5])
            print("IV PERIOD : ",F[0][6])
            print("V PERIOD : ",F[0][7])
            print("VI PERIOD : ",F[0][8])
            print("VII PERIOD : ",F[0][9])
         elif ch1 in ['saturday','Saturday']:
            print("CODE : ",S[0][0])
            print("NAME : ",S[0][1])
            print("SUBJECT : ",S[0][2])
            print("I PERIOD : ",S[0][3])
            print("II PERIOD : ",S[0][4])
            print("III PERIOD : ",S[0][5])
            print("IV PERIOD : ",S[0][6])
            print("V PERIOD : ",S[0][7])
            print("VI PERIOD : ",S[0][8])
            print("VII PERIOD : ",S[0][9])
         else:
            print("Please enter valid choice.")
   if ch==2:
      print("TIME TABLE IS AS FOLLOWS:\n")
      print('-'*123)
      print("PERIODS\t\tI\t\tII\t\tIII\t\tIV\t\tV\t\tVI\t\tVII")
      print('-'*123)
      print("MONDAY",(' ')*6,M[0][3],(' ')*9,M[0][4],(' ')*11,M[0][5],(' ')*9,M[0][6],(' ')*9,M[0][7],(' ')*9,M[0][8],(' ')*9,M[0][9])
      print('-'*123)
      print("TUESDAY",(' ')*5,T[0][3],(' ')*9,T[0][4],(' ')*11,T[0][5],(' ')*9,T[0][6],(' ')*9,T[0][7],(' ')*9,T[0][8],(' ')*9,T[0][9])
      print('-'*123)
      print("WEDNESDAY",(' ')*3,W[0][3],(' ')*9,W[0][4],(' ')*11,W[0][5],(' ')*9,W[0][6],(' ')*9,W[0][7],(' ')*9,W[0][8],(' ')*9,W[0][9])
      print('-'*123)
      print("THURSDAY",(' ')*4,Th[0][3],(' ')*9,Th[0][4],(' ')*11,Th[0][5],(' ')*9,Th[0][6],(' ')*9,Th[0][7],(' ')*9,Th[0][8],(' ')*11,Th[0][9])
      print('-'*123)
      print("FRIDAY",(' ')*6,F[0][3],(' ')*9,F[0][4],(' ')*11,F[0][5],(' ')*9,F[0][6],(' ')*9,F[0][7],(' ')*9,F[0][8],(' ')*11,F[0][9])
      print('-'*123)
      print("SATURDAY",(' ')*4,S[0][3],(' ')*9,S[0][4],(' ')*10,S[0][5],(' ')*8,S[0][6],(' ')*9,S[0][7],(' ')*9,S[0][8],(' ')*9,S[0][9])
      print('-'*123,"\n")
def delete_data(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   display(a,b)
   code=int(input("Enter teacher's code whose data you want to delete:"))
   query="Delete from MONDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete from TUESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete * from WEDNESDAY where T_CODE={}".format(code) 
   cursor.execute(query)
   connection.commit()
   query="Delete * from THURSDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete * from FRIDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete * from SATURDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   print("RESPECTIVE TEACHER'S DATA HAS BEEN DELETED SUCCESSFULLY")
   connection.close()
def update_data(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   display(a,b)
   code=int(input("Enter teacher's code whose data you want to update:"))
   query="Select * from MONDAY where T_CODE={}".format(code)
   cursor.execute(query)
   M=cursor.fetchall()
   query="Select * from TUESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   T=cursor.fetchall()
   query="Select * from WEDNESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   W=cursor.fetchall()
   query="Select * from THURSDAY where T_CODE={}".format(code)
   cursor.execute(query)
   Th=cursor.fetchall()
   query="Select * from FRIDAY where T_CODE={}".format(code)
   cursor.execute(query)
   F=cursor.fetchall()
   query="Select * from SATURDAY where T_CODE={}".format(code)
   cursor.execute(query)
   S=cursor.fetchall()
   print("TIME TABLE IS AS FOLLOWS:\n")
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("PERIODS\t\tI\t\tII\t\tIII\t\tIV\t\tV\t\tVI\t\tVII")
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("MONDAY",(' ')*6,M[0][3],(' ')*9,M[0][4],(' ')*11,M[0][5],(' ')*9,M[0][6],(' ')*9,M[0][7],(' ')*9,M[0][8],(' ')*9,M[0][9])
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("TUESDAY",(' ')*5,T[0][3],(' ')*9,T[0][4],(' ')*11,T[0][5],(' ')*9,T[0][6],(' ')*9,T[0][7],(' ')*9,T[0][8],(' ')*9,T[0][9])
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("WEDNESDAY",(' ')*3,W[0][3],(' ')*9,W[0][4],(' ')*11,W[0][5],(' ')*9,W[0][6],(' ')*9,W[0][7],(' ')*9,W[0][8],(' ')*9,W[0][9])
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("THURSDAY",(' ')*4,Th[0][3],(' ')*9,Th[0][4],(' ')*11,Th[0][5],(' ')*9,Th[0][6],(' ')*9,Th[0][7],(' ')*9,Th[0][8],(' ')*11,Th[0][9])
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("FRIDAY",(' ')*6,F[0][3],(' ')*9,F[0][4],(' ')*11,F[0][5],(' ')*9,F[0][6],(' ')*9,F[0][7],(' ')*9,F[0][8],(' ')*11,F[0][9])
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("SATURDAY",(' ')*4,S[0][3],(' ')*9,S[0][4],(' ')*10,S[0][5],(' ')*8,S[0][6],(' ')*9,S[0][7],(' ')*9,S[0][8],(' ')*9,S[0][9])
   print("---------------------------------------------------------------------------------------------------------------------------")
   ch=1
   while ch!=0:
      print("\n",(' ')*58,"WHICH DAY DATA YOU WANT TO UPDATE?\n")
      print((' ')*55,('-')*44)
      print((' ')*55,"|",(' ')*12,"1.MONDAY",(' ')*18,"|")
      print((' ')*55,"|",(' ')*12,"2.TUESDAY",(' ')*17,"|")
      print((' ')*55,"|",(' ')*12,"3.WEDNESDAY",(' ')*15,"|")
      print((' ')*55,"|",(' ')*12,"4.THURSDAY",(' ')*16,"|")
      print((' ')*55,"|",(' ')*12,"5.FRIDAY",(' ')*18,"|")
      print((' ')*55,"|",(' ')*12,"6.SATURDAY",(' ')*16,"|")
      print((' ')*55,"|",(' ')*12,"0.EXIT",(' ')*20,"|")
      print((' ')*55,('-')*44)
      ch=int(input("\nEnter Your Choice : "))
      if ch==0:
         connection.close()
         break
      elif ch==1:
         c=1
         while c!=0:
            print("\n",(' ')*58,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('-')*44)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17)
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16)
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15)
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16)
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17)
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16)
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15)
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21)
            print((' ')*55,('-')*44)
            c=int(input("Enter your choice:"))
            if c==0:
               break
            elif c==1:
               val=input("Enter value to be changed with : ")
               query="Update monday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==2:
               val=input("Enter value to be changed with : ")
               query="Update monday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==3:
               val=input("Enter value to be changed with : ")
               query="Update monday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==4:
               val=input("Enter value to be changed with : ")
               query="Update monday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==5:
               val=input("Enter value to be changed with : ")
               query="Update monday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==6:
               val=input("Enter value to be changed with : ")
               query="Update monday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==7:
               val=input("Enter value to be changed with : ")
               query="Update monday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            else:
               print("Enter a Valid choice.")
      elif ch==2:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('-')*44)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('-')*44)
            if c==0:
               break
            elif c==1:
               val=input("Enter value to be changed with : ")
               query="Update tuesday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               print("\nValue Updated Successfully.\n")
               connection.commit()
            elif c==2:
               val=input("Enter value to be changed with : ")
               query="Update tuesday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==3:
               val=input("Enter value to be changed with : ")
               query="Update tuesday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==4:
               val=input("Enter value to be changed with : ")
               query="Update tuesday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==5:
               val=input("Enter value to be changed with : ")
               query="Update tuesday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==6:
               val=input("Enter value to be changed with : ")
               query="Update tuesday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==7:
               val=input("Enter value to be changed with : ")
               query="Update tuesday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            else:
               print("Enter a Valid choice.")
      elif ch==3:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('-')*44)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('-')*44)
            if c==0:
               break
            elif c==1:
               val=input("Enter value to be changed with : ")
               query="Update wednesday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==2:
               val=input("Enter value to be changed with : ")
               query="Update wednesday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==3:
               val=input("Enter value to be changed with : ")
               query="Update wednesday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==4:
               val=input("Enter value to be changed with : ")
               query="Update wednesday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==5:
               val=input("Enter value to be changed with : ")
               query="Update wednesday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==6:
               val=input("Enter value to be changed with : ")
               query="Update wednesday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==7:
               val=input("Enter value to be changed with : ")
               query="Update wednesday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            else:
               print("Enter a Valid choice.")
      elif ch==4:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('-')*44)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('-')*44)
            if c==0:
               break
            elif c==1:
               val=input("Enter value to be changed with : ")
               query="Update thursday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==2:
               val=input("Enter value to be changed with : ")
               query="Update thursday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==3:
               val=input("Enter value to be changed with : ")
               query="Update thursday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==4:
               val=input("Enter value to be changed with : ")
               query="Update thursday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==5:
               val=input("Enter value to be changed with : ")
               query="Update thursday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==6:
               val=input("Enter value to be changed with : ")
               query="Update thursday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==7:
               val=input("Enter value to be changed with : ")
               query="Update thursday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            else:
               print("Enter a Valid choice.")
      elif ch==5:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('-')*44)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('-')*44)
            if c==0:
               break
            elif c==1:
               val=input("Enter value to be changed with : ")
               query="Update friday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==2:
               val=input("Enter value to be changed with : ")
               query="Update friday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==3:
               val=input("Enter value to be changed with : ")
               query="Update friday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==4:
               val=input("Enter value to be changed with : ")
               query="Update friday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==5:
               val=input("Enter value to be changed with : ")
               query="Update friday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==6:
               val=input("Enter value to be changed with : ")
               query="Update friday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==7:
               val=input("Enter value to be changed with : ")
               query="Update friday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            else:
                print("Enter a Valid choice.")
      elif ch==6:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('-')*44)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('-')*44)
            if c==0:
               break
            elif c==1:
               val=input("Enter value to be changed with : ")
               query="Update saturday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==2:
               val=input("Enter value to be changed with : ")
               query="Update saturday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==3:
               val=input("Enter value to be changed with : ")
               query="Update saturday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==4:
               val=input("Enter value to be changed with : ")
               query="Update saturday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==5:
               val=input("Enter value to be changed with : ")
               query="Update saturday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==6:
               val=input("Enter value to be changed with : ")
               query="Update saturday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            elif c==7:
               val=input("Enter value to be changed with : ")
               query="Update saturday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\nValue Updated Successfully.\n")
            else:
               print("Enter a Valid choice.")
      else:
         print("\nEnter a Valid choice.\n")
import mysql.connector as mysql
def enter_monday(code,name,sub):
   dm={}
   print(('-')*144)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR MONDAY",(' ')*49,"|")
   print(('-')*144)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("⏺ Enter class for I period:")
   t_2=input("⏺ Enter class for II period:")
   t_3=input("⏺ Enter class for III period:")
   t_4=input("⏺ Enter class for IV period:")
   t_5=input("⏺ Enter class for V period:")
   t_6=input("⏺ Enter class for VI period:")
   t_7=input("⏺ Enter class for VII period:")
   dm['code']=code
   dm['name']=name
   dm['sub']=sub
   dm['t1']=t_1
   dm['t2']=t_2
   dm['t3']=t_3
   dm['t4']=t_4
   dm['t5']=t_5
   dm['t6']=t_6
   dm['t7']=t_7
   return dm
def enter_tuesday(code,name,sub):
   dt={}
   print(('-')*144)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR TUESDAY",(' ')*48,"|")
   print(('-')*144)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("⏺ Enter class for I period:")
   t_2=input("⏺ Enter class for II period:")
   t_3=input("⏺ Enter class for III period:")
   t_4=input("⏺ Enter class for IV period:")
   t_5=input("⏺ Enter class for V period:")
   t_6=input("⏺ Enter class for VI period:")
   t_7=input("⏺ Enter class for VII period:")
   dt['code']=code
   dt['name']=name
   dt['sub']=sub
   dt['t1']=t_1
   dt['t2']=t_2
   dt['t3']=t_3
   dt['t4']=t_4
   dt['t5']=t_5
   dt['t6']=t_6
   dt['t7']=t_7
   return dt
def enter_wednesday(code,name,sub):
   dw={}
   print(('-')*144)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR WEDNESDAY",(' ')*45,"|")
   print(('-')*144)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("⏺ Enter class for I period:")
   t_2=input("⏺ Enter class for II period:")
   t_3=input("⏺ Enter class for III period:")
   t_4=input("⏺ Enter class for IV period:")
   t_5=input("⏺ Enter class for V period:")
   t_6=input("⏺ Enter class for VI period:")
   t_7=input("⏺ Enter class for VII period:")
   dw['code']=code
   dw['name']=name
   dw['sub']=sub
   dw['t1']=t_1
   dw['t2']=t_2
   dw['t3']=t_3
   dw['t4']=t_4
   dw['t5']=t_5
   dw['t6']=t_6
   dw['t7']=t_7
   return dw
def enter_thursday(code,name,sub):
   dth={}
   print(('-')*144)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR THURSDAY",(' ')*47,"|")
   print(('-')*144)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("⏺ Enter class for I period:")
   t_2=input("⏺ Enter class for II period:")
   t_3=input("⏺ Enter class for III period:")
   t_4=input("⏺ Enter class for IV period:")
   t_5=input("⏺ Enter class for V period:")
   t_6=input("⏺ Enter class for VI period:")
   t_7=input("⏺ Enter class for VII period:")
   dth['code']=code
   dth['name']=name
   dth['sub']=sub
   dth['t1']=t_1
   dth['t2']=t_2
   dth['t3']=t_3
   dth['t4']=t_4
   dth['t5']=t_5
   dth['t6']=t_6
   dth['t7']=t_7
   return dth
def enter_friday(code,name,sub):
   df={}
   print(('-')*144)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR FRIDAY",(' ')*49,"|")
   print(('-')*144)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("⏺ Enter class for I period:")
   t_2=input("⏺ Enter class for II period:")
   t_3=input("⏺ Enter class for III period:")
   t_4=input("⏺ Enter class for IV period:")
   t_5=input("⏺ Enter class for V period:")
   t_6=input("⏺ Enter class for VI period:")
   t_7=input("⏺ Enter class for VII period:")
   df['code']=code
   df['name']=name
   df['sub']=sub
   df['t1']=t_1
   df['t2']=t_2
   df['t3']=t_3
   df['t4']=t_4
   df['t5']=t_5
   df['t6']=t_6
   df['t7']=t_7
   return df
def enter_saturday(code,name,sub):
   ds={}
   print(('-')*144)
   print("|",(' ')*58,"PLEASE ENTER DETAILS FOR SATURDAY",(' ')*47,"|")
   print(('-')*144)
   print()
   print((' ')*50,"----Enter Null if you don't want to insert any value----")
   t_1=input("⏺ Enter class for I period:")
   t_2=input("⏺ Enter class for II period:")
   t_3=input("⏺ Enter class for III period:")
   t_4=input("⏺ Enter class for IV period:")
   t_5=input("⏺ Enter class for V period:")
   t_6=input("⏺ Enter class for VI period:")
   t_7=input("⏺ Enter class for VII period:")
   ds['code']=code
   ds['name']=name
   ds['sub']=sub
   ds['t1']=t_1
   ds['t2']=t_2
   ds['t3']=t_3
   ds['t4']=t_4
   ds['t5']=t_5
   ds['t6']=t_6
   ds['t7']=t_7
   return ds
def display(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   query="Select * from MONDAY"
   cursor.execute(query)
   val=cursor.fetchall()
   print("\n⏺⏺ Below is the information of the teachers which include their code, their name and the subject they teach. ⏺⏺\n")
   print(('🖱')*55,"\n")
   print("Teacher's code\t\tTeacher's name\t\tTeacher's subject")
   for data in val:
      print(data[0],"\t\t\t",data[1],"\t\t",data[2])
   print("\n")
   print(('🖱')*55)
def create(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   t_code=int(input("⏺ Enter teacher's code:"))
   t_name=input(("⏺ Enter teacher name:"))
   t_sub=input("⏺ Enter subject of teacher:")
   d1=enter_monday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS MONDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d2=enter_tuesday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS TUESDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d3=enter_wednesday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS WEDNESDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d4=enter_thursday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS THURSDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d5=enter_friday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS FRIDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   d6=enter_saturday(t_code,t_name,t_sub)
   createTable ="CREATE TABLE IF NOT EXISTS SATURDAY(T_CODE INT,T_NAME VARCHAR(30),T_SUB VARCHAR(30),I VARCHAR(30),II VARCHAR(30),III VARCHAR(30),IV VARCHAR(30),V VARCHAR(30),VI VARCHAR(30),VII VARCHAR(30))"
   cursor.execute(createTable)
   query="Insert into MONDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d1['code'],d1['name'],d1['sub'],d1['t1'],d1['t2'],d1['t3'],d1['t4'],d1['t5'],d1['t6'],d1['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into TUESDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d2['code'],d2['name'],d2['sub'],d2['t1'],d2['t2'],d2['t3'],d2['t4'],d2['t5'],d2['t6'],d2['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into WEDNESDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d3['code'],d3['name'],d3['sub'],d3['t1'],d3['t2'],d3['t3'],d3['t4'],d3['t5'],d3['t6'],d3['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into THURSDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d4['code'],d4['name'],d4['sub'],d4['t1'],d4['t2'],d4['t3'],d4['t4'],d4['t5'],d4['t6'],d4['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into FRIDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d5['code'],d5['name'],d5['sub'],d5['t1'],d5['t2'],d5['t3'],d5['t4'],d5['t5'],d5['t6'],d5['t7'])
   cursor.execute(query)
   connection.commit()
   query="Insert into SATURDAY(T_CODE,T_NAME,T_SUB,I,II,III,IV,V,VI,VII) values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(d6['code'],d6['name'],d6['sub'],d6['t1'],d6['t2'],d6['t3'],d6['t4'],d6['t5'],d6['t6'],d6['t7'])
   cursor.execute(query)
   connection.commit()
   print("\n😃 Your values have been inserted successfully. 😃")
def search_data(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   display(a,b)
   code=int(input("\n⏺ Enter Teacher's code whose data you want to search:"))
   print("\n⏺ Which details you want to see?\n")
   print(('🕹')*20)
   
   print("\n1.PARTICULAR DAY")
   print("2.WHOLE TIME TABLE\n")
   print(('🕹')*20)
   print("\n")
   ch=int(input("⏺ Enter your choice:"))
   query="Select * from MONDAY where T_CODE={}".format(code)
   cursor.execute(query)
   M=cursor.fetchall()
   query="Select * from TUESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   T=cursor.fetchall()
   query="Select * from WEDNESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   W=cursor.fetchall()
   query="Select * from THURSDAY where T_CODE={}".format(code)
   cursor.execute(query)
   Th=cursor.fetchall()
   query="Select * from FRIDAY where T_CODE={}".format(code)
   cursor.execute(query)
   F=cursor.fetchall()
   query="Select * from SATURDAY where T_CODE={}".format(code)
   cursor.execute(query)
   S=cursor.fetchall()
   if ch==1:
      ch1=1
      print("\nEnter 1 for Monday.")
      print("Enter 2 for Tuesday.")
      print("Enter 3 for Wednesday.")
      print("Enter 4 for Thursday.")
      print("Enter 5 for Friday.")
      print("Enter 6 for Saturday.")
      print("Enter 0 for exit\n.")
      while ch1!=0:
         ch1=int(input("\nEnter your choice:"))
         if ch1==str(0):
            break
         elif ch1==1:
            print(('💿')*25)
            print("CODE        : ",M[0][0])
            print("NAME        : ",M[0][1])
            print("SUBJECT     : ",M[0][2])
            print("I PERIOD    : ",M[0][3])
            print("II PERIOD   : ",M[0][4])
            print("III PERIOD  : ",M[0][5])
            print("IV PERIOD   : ",M[0][6])
            print("V PERIOD    : ",M[0][7])
            print("VI PERIOD   : ",M[0][8])
            print("VII PERIOD  : ",M[0][9])
            print(('💿')*25)
         elif ch1==2:
            print(('💿')*25)
            print("CODE        : ",T[0][0])
            print("NAME        : ",T[0][1])
            print("SUBJECT     : ",T[0][2])
            print("I PERIOD    : ",T[0][3])
            print("II PERIOD   : ",T[0][4])
            print("III PERIOD  : ",T[0][5])
            print("IV PERIOD   : ",T[0][6])
            print("V PERIOD    : ",T[0][7])
            print("VI PERIOD   : ",T[0][8])
            print("VII PERIOD  : ",T[0][9])
            print(('💿')*25)
         elif ch1==3:
            print(('💿')*25)
            print("CODE        : ",W[0][0])
            print("NAME        : ",W[0][1])
            print("SUBJECT     : ",W[0][2])
            print("I PERIOD    : ",W[0][3])
            print("II PERIOD   : ",W[0][4])
            print("III PERIOD  : ",W[0][5])
            print("IV PERIOD   : ",W[0][6])
            print("V PERIOD    : ",W[0][7])
            print("VI PERIOD   : ",W[0][8])
            print("VII PERIOD  : ",W[0][9])
            print(('💿')*25)
         elif ch1==4:
            print(('💿')*25)
            print("CODE        : ",Th[0][0])
            print("NAME        : ",Th[0][1])
            print("SUBJECT     : ",Th[0][2])
            print("I PERIOD    : ",Th[0][3])
            print("II PERIOD   : ",Th[0][4])
            print("III PERIOD  : ",Th[0][5])
            print("IV PERIOD   : ",Th[0][6])
            print("V PERIOD    : ",Th[0][7])
            print("VI PERIOD   : ",Th[0][8])
            print("VII PERIOD  : ",Th[0][9])
            print(('💿')*25)
         elif ch1==5:
            print(('💿')*25)
            print("CODE        : ",F[0][0])
            print("NAME        : ",F[0][1])
            print("SUBJECT     : ",F[0][2])
            print("I PERIOD    : ",F[0][3])
            print("II PERIOD   : ",F[0][4])
            print("III PERIOD  : ",F[0][5])
            print("IV PERIOD   : ",F[0][6])
            print("V PERIOD    : ",F[0][7])
            print("VI PERIOD   : ",F[0][8])
            print("VII PERIOD  : ",F[0][9])
            print(('💿')*25)
         elif ch1==6:
            print(('💿')*25)
            print("CODE        : ",S[0][0])
            print("NAME        : ",S[0][1])
            print("SUBJECT     : ",S[0][2])
            print("I PERIOD    : ",S[0][3])
            print("II PERIOD   : ",S[0][4])
            print("III PERIOD  : ",S[0][5])
            print("IV PERIOD   : ",S[0][6])
            print("V PERIOD    : ",S[0][7])
            print("VI PERIOD   : ",S[0][8])
            print("VII PERIOD  : ",S[0][9])
            print(('💿')*25)
         else:
            print("Please enter valid choice.")
   if ch==2:
      print("⏺ TIME TABLE IS AS FOLLOWS:\n")
      print('-'*123)
      print("PERIODS\t\tI\t\tII\t\tIII\t\tIV\t\tV\t\tVI\t\tVII")
      print('-'*123)
      print("MONDAY",(' ')*5,M[0][3],(' ')*9,M[0][4],(' ')*11,M[0][5],(' ')*9,M[0][6],(' ')*9,M[0][7],(' ')*9,M[0][8],(' ')*9,M[0][9])
      print('-'*123)
      print("TUESDAY",(' ')*5,T[0][3],(' ')*9,T[0][4],(' ')*11,T[0][5],(' ')*9,T[0][6],(' ')*9,T[0][7],(' ')*9,T[0][8],(' ')*9,T[0][9])
      print('-'*123)
      print("WEDNESDAY",(' ')*3,W[0][3],(' ')*9,W[0][4],(' ')*11,W[0][5],(' ')*9,W[0][6],(' ')*9,W[0][7],(' ')*9,W[0][8],(' ')*9,W[0][9])
      print('-'*123)
      print("THURSDAY",(' ')*4,Th[0][3],(' ')*9,Th[0][4],(' ')*11,Th[0][5],(' ')*9,Th[0][6],(' ')*9,Th[0][7],(' ')*9,Th[0][8],(' ')*11,Th[0][9])
      print('-'*123)
      print("FRIDAY",(' ')*6,F[0][3],(' ')*9,F[0][4],(' ')*11,F[0][5],(' ')*9,F[0][6],(' ')*9,F[0][7],(' ')*9,F[0][8],(' ')*11,F[0][9])
      print('-'*123)
      print("SATURDAY",(' ')*4,S[0][3],(' ')*9,S[0][4],(' ')*10,S[0][5],(' ')*8,S[0][6],(' ')*9,S[0][7],(' ')*9,S[0][8],(' ')*9,S[0][9])
      print('-'*123,"\n")
def delete_data(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   display(a,b)
   code=int(input("Enter teacher's code whose data you want to delete:"))
   query="Delete from MONDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete from TUESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete from WEDNESDAY where T_CODE={}".format(code) 
   cursor.execute(query)
   connection.commit()
   query="Delete from THURSDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete from FRIDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   query="Delete from SATURDAY where T_CODE={}".format(code)
   cursor.execute(query)
   connection.commit()
   print(('💿')*50)
   print("\n😃 RESPECTIVE TEACHER'S DATA HAS BEEN DELETED SUCCESSFULLY 😃\n")
   print(('💿')*50)
   connection.close()
def update_data(a,b):
   connection=mysql.connect(host="localhost",user=a,passwd=b,database="TIMETABLE")
   cursor=connection.cursor(buffered=True)
   display(a,b)
   code=int(input("\n⏺️ Enter teacher's code whose data you want to update:"))
   query="Select * from MONDAY where T_CODE={}".format(code)
   cursor.execute(query)
   M=cursor.fetchall()
   query="Select * from TUESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   T=cursor.fetchall()
   query="Select * from WEDNESDAY where T_CODE={}".format(code)
   cursor.execute(query)
   W=cursor.fetchall()
   query="Select * from THURSDAY where T_CODE={}".format(code)
   cursor.execute(query)
   Th=cursor.fetchall()
   query="Select * from FRIDAY where T_CODE={}".format(code)
   cursor.execute(query)
   F=cursor.fetchall()
   query="Select * from SATURDAY where T_CODE={}".format(code)
   cursor.execute(query)
   S=cursor.fetchall()
   print("⏺ TIME TABLE IS AS FOLLOWS:\n")
   print('-'*123)
   print("PERIODS\t\tI\t\tII\t\tIII\t\tIV\t\tV\t\tVI\t\tVII")
   print('-'*123)
   print("MONDAY",(' ')*6,M[0][3],(' ')*9,M[0][4],(' ')*11,M[0][5],(' ')*9,M[0][6],(' ')*9,M[0][7],(' ')*9,M[0][8],(' ')*9,M[0][9])
   print('-'*123)
   print("TUESDAY",(' ')*5,T[0][3],(' ')*9,T[0][4],(' ')*11,T[0][5],(' ')*9,T[0][6],(' ')*9,T[0][7],(' ')*9,T[0][8],(' ')*9,T[0][9])
   print('-'*123)
   print("WEDNESDAY",(' ')*3,W[0][3],(' ')*9,W[0][4],(' ')*11,W[0][5],(' ')*9,W[0][6],(' ')*9,W[0][7],(' ')*9,W[0][8],(' ')*9,W[0][9])
   print('-'*123)
   print("THURSDAY",(' ')*4,Th[0][3],(' ')*9,Th[0][4],(' ')*11,Th[0][5],(' ')*9,Th[0][6],(' ')*9,Th[0][7],(' ')*9,Th[0][8],(' ')*11,Th[0][9])
   print('-'*123)
   print("FRIDAY",(' ')*6,F[0][3],(' ')*9,F[0][4],(' ')*11,F[0][5],(' ')*9,F[0][6],(' ')*9,F[0][7],(' ')*9,F[0][8],(' ')*11,F[0][9])
   print('-'*123)
   print("SATURDAY",(' ')*4,S[0][3],(' ')*9,S[0][4],(' ')*10,S[0][5],(' ')*8,S[0][6],(' ')*9,S[0][7],(' ')*9,S[0][8],(' ')*9,S[0][9])
   print('-'*123,"\n")
   ch=1
   while ch!=0:
      print("\n",(' ')*58,"WHICH DAY DATA YOU WANT TO UPDATE?\n")
      print((' ')*55,('🖥')*25)
      print((' ')*55,"|",(' ')*12,"1.MONDAY",(' ')*18,"|")
      print((' ')*55,"|",(' ')*12,"2.TUESDAY",(' ')*17,"|")
      print((' ')*55,"|",(' ')*12,"3.WEDNESDAY",(' ')*15,"|")
      print((' ')*55,"|",(' ')*12,"4.THURSDAY",(' ')*16,"|")
      print((' ')*55,"|",(' ')*12,"5.FRIDAY",(' ')*18,"|")
      print((' ')*55,"|",(' ')*12,"6.SATURDAY",(' ')*16,"|")
      print((' ')*55,"|",(' ')*12,"0.EXIT",(' ')*20,"|")
      print((' ')*55,('🖥')*25)
      print("\n⏺⏺ ENTER NULL IN CASE YOU WANT TO ASSIGN ARRANGEMENT. ⏺⏺")
      print("\n⏺⏺ PRESS 0 IN CASE YOU DO NOT WANT TO UPDATE FURTHER. ⏺⏺")
      ch=int(input("\nEnter Your Choice : "))
      if ch==0:
         connection.close()
         break
      elif ch==1:
         c=1
         while c!=0:
            print("\n",(' ')*58,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('🖥')*25)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('🖥')*25)
            c=int(input("\n⏺️ Enter your choice:"))
            if c==0:
               break
            elif c==1:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update monday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==2:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update monday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==3:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update monday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==4:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update monday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==5:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update monday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==6:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update monday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==7:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update monday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            else:
               print("⏺️ Enter a Valid choice.")
      elif ch==2:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('🖥')*25)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('🖥')*25)
            c=int(input("\n⏺️ Enter your choice:"))
            if c==0:
               break
            elif c==1:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update tuesday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               print("\n😃 Value Updated Successfully. 😃\n")
               connection.commit()
            elif c==2:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update tuesday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==3:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update tuesday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==4:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update tuesday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==5:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update tuesday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==6:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update tuesday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==7:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update tuesday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            else:
               print("⏺️ Enter a Valid choice.")
      elif ch==3:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('🖥')*25)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('🖥')*25)
            c=int(input("\n⏺️ Enter your choice:"))
            if c==0:
               break
            elif c==1:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update wednesday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==2:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update wednesday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==3:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update wednesday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==4:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update wednesday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==5:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update wednesday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==6:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update wednesday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==7:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update wednesday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            else:
               print("⏺️ Enter a Valid choice.")
      elif ch==4:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('🖥')*25)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('🖥')*25)
            c=int(input("\n⏺️ Enter your choice:"))
            if c==0:
               break
            elif c==1:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update thursday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==2:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update thursday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==3:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update thursday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==4:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update thursday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==5:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update thursday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==6:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update thursday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==7:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update thursday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            else:
               print("⏺️ Enter a Valid choice.")
      elif ch==5:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('🖥')*25)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('🖥')*25)
            c=int(input("\n⏺️ Enter your choice:"))
            if c==0:
               break
            elif c==1:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update friday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==2:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update friday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==3:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update friday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==4:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update friday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==5:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update friday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==6:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update friday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==7:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update friday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            else:
                print("⏺️ Enter a Valid choice.")
      elif ch==6:
         c=1
         while c!=0:
            print("\n",(' ')*55,"WHICH PERIOD DATA TOU WANT TO UPDATE?\n")
            print((' ')*55,('🖥')*25)
            print((' ')*55,"|",(' ')*11,"1.I PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"2.II PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"3.III PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"4.IV PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"5.V PERIOD",(' ')*17,"|")
            print((' ')*55,"|",(' ')*11,"6.VI PERIOD",(' ')*16,"|")
            print((' ')*55,"|",(' ')*11,"7.VII PERIOD",(' ')*15,"|")
            print((' ')*55,"|",(' ')*11,"0.EXIT",(' ')*21,"|")
            print((' ')*55,('🖥')*25)
            c=int(input("\n⏺️ Enter your choice:"))
            if c==0:
               break
            elif c==1:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update saturday set I='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==2:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update saturday set II='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==3:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update saturday set III='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==4:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update saturday set IV='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==5:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update saturday set V='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==6:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update saturday set VI='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            elif c==7:
               val=input("⏺️ Enter value to be changed with : ")
               query="Update saturday set VII='{}' where T_CODE={}".format(val,code)
               cursor.execute(query)
               connection.commit()
               print("\n😃 Value Updated Successfully. 😃\n")
            else:
               print("⏺️ Enter a Valid choice.")
      else:
         print("\n⏺️ Enter a Valid choice.\n")
def MYSQLconnection():
   userName = input("\n⏺️ ENTER MYSQL SERVER'S USERNAME : ")
   password = input("\n⏺️ ENTER MYSQL SERVER'S PASSWORD : ")
   myConnection=mysql.connect(host="localhost",user=userName,passwd=password )
   if myConnection:
       print("\n😃 CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED ! 😃\n")
       cursor=myConnection.cursor()
       cursor.execute("CREATE DATABASE IF NOT EXISTS TIMETABLE")
       cursor.execute("COMMIT")
       cursor.close()
       return userName,password
   else:
       return 0,1
def main():
   a,b=MYSQLconnection()
   if a!=0:
      while True:
         print("\n")
         print((' ')*55,('🖥')*26)
         print((' ')*55,"|",(' ')*6,"1--->ENTER TEACHER DETAILS",(' ')*7,"|")
         print((' ')*55,"|",(' ')*6,"2--->TEACHER INFORMATION",(' ')*9,"|")
         print((' ')*55,"|",(' ')*6,"3--->SEE TIMETABLE",(' ')*15,"|")
         print((' ')*55,"|",(' ')*6,"4--->DELETE TEACHER DETAILS",(' ')*6,"|")
         print((' ')*55,"|",(' ')*6,"5--->ASSIGN CLASS TO A TEACHER",(' ')*3,"|")
         print((' ')*55,"|",(' ')*6,"0--->EXIT",(' ')*24,"|")
         print((' ')*55,('🖥')*26)
         print("\n") 
         choice = int(input("⏺️ Enter Your Choice:"))
         if choice==1:
            create(a,b)
         elif choice==2:
            display(a,b)
         elif choice==3:
            search_data(a,b)
         elif choice==4:
            delete_data(a,b)
         elif choice==5:
            update_data(a,b)
         elif choice==0:
            print("\n🙏🏻 THANKS FOR YOUR PRECIOUS TIME. 🙏🏻\n")
            break
         else:
            print(" Sorry, May Be You Are Giving Me Wrong Input. Please Try Again!!  ")
   else:
      print("\nERROR ESTABLISHING MYSQL CONNECTION !")
main()
