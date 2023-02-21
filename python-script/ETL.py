import mysql.connector
import pandas as pd
import sys

try:
      people = pd.read_excel('DEM_Challenge_Section1_DATASET.xlsx', sheet_name='DATA')
      print("Was able to load the excel file")
except Exception as e:
      print('could not open DEM_Challenge_Section1_DATASET.xlsx:' + str(e))
      #sys.exit()

connection = mysql.connector.connect(
      user='root', password='root', host="mysql", port="3306", database='db')
print("DB Connected")

cursor = connection.cursor()

for row in people.itertuples():

    cursor.execute("""
                INSERT INTO People (FirstName, LastName, Email, Gender, IPAddress)
                VALUES ( %s, %s, %s, %s, %s)
                """,
                
                (row.first_name,
                row.last_name,
                row.email,
                row.gender,
                row.ip_address
                ))
connection.commit()

#cursor.execute('Select * FROM People')
#people = cursor.fetchall()
connection.close()

print("ETL is complete. All the data from the excel file has been loaded into mysql db successfully.")

#print(people)

