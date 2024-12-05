import psycopg2
connection = psycopg2.connect(database="student_db",user="postgres",host="localhost",port=5432,password="Msk@2009")
cursor = connection.cursor()


cursor.execute("DELETE FROM STUDENTS WHERE STATUS='FAIL'")
connection.commit()
cursor.close()
connection.close()

print("done")
