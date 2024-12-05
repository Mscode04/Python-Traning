import tkinter as tk
from tkinter import messagebox
import psycopg2


def register_student():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    age = entry_age.get()
    department = entry_department.get()
    phone_number = entry_phone_number.get()
    status = entry_status.get()

    try:
        connection = psycopg2.connect(database="student_db",user="postgres",host="localhost",port=5432,password="Msk@2009")

        cursor = connection.cursor()
        query = "INSERT INTO students (first_name, last_name, age, department, phone_number, status) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, age, department, phone_number, status)
        cursor.execute(query, values)
        print("uploaded")
        connection.commit()

        messagebox.showinfo("Success", "Student registered successfully!")
    except :
        messagebox.showerror("Database Error")
    finally:
        cursor.close()
        connection.close()


root = tk.Tk()
root.title("Student Form")

label_first_name = tk.Label(root, text="First Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=5)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.grid(row=1, column=0, padx=10, pady=5)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

label_department = tk.Label(root, text="Department:")
label_department.grid(row=3, column=0, padx=10, pady=5)
entry_department = tk.Entry(root)
entry_department.grid(row=3, column=1, padx=10, pady=5)

label_phone_number = tk.Label(root, text="Phone Number:")
label_phone_number.grid(row=4, column=0, padx=10, pady=5)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=4, column=1, padx=10, pady=5)

label_status = tk.Label(root, text="Status:")
label_status.grid(row=5, column=0, padx=10, pady=5)
entry_status = tk.Entry(root)
entry_status.grid(row=5, column=1, padx=10, pady=5)


submit_button = tk.Button(root, text="Register", command=register_student)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)

root.mainloop()
