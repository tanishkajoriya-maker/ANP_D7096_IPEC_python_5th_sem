##to import mysql.connector module
import mysql.connector

#to establish connection with mysql
dataconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tanishka@123",
    database="studentmanagement"
)

print("Connected to the database successfully!")

#to create a cursor object
cursor = dataconnection.cursor()

#-----------------------------------------------
# Example: Delete student with ID 'std101'
delete_query = "DELETE FROM student WHERE student_id = %s"
delete_value = ("std101",)

cursor.execute(delete_query, delete_value)

# Commit the changes
dataconnection.commit()

# Check if row deleted
if cursor.rowcount > 0:
    print("Data deleted successfully!")
else:
    print("No matching record found to delete.")

# Close connection
cursor.close()
dataconnection.close()
