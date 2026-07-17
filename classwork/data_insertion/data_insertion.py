#to import mysql.connecter module
import mysql.connector
#to establish connection with mysql
dataconnection = mysql.connector.connect(host = "localhost", user = "root", password = "Tanishka@123", database = "studentmanagement")
#---------------------------------------------------------------------------------
print("Connected to the database successfully!")
#--------------------------------------------------
#to create a cursor object
cursor = dataconnection.cursor()
#-------------------------------------------------------
#write down the desire query
sql_query = "insert into student values (%s%s,%s,%s)"
#---------------------------------------------------------
stdid = "std101"
stdname = "Anil"
standard = "10th"
age = 15
#---------------------------------------------------------
#to commit changes 
dataconnection.commit()
#---------------------------------------------------------
#to check data inserted or not
if(cursor.rowcount > 0):
    print("Data inserted successfully!")
else:
    print("unable to insert data!")
#------------------------------------------------------------