import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
import mysql.connector
import tkinter.filedialog as fd
from tkinter.filedialog import askopenfilename


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tuition_booking_system"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS STUDENT_INFORMATION (NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, SUBJECT TEXT)"
)


def reset_fields():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, subject_strvar

    name_strvar.set('')
    email_strvar.set('')
    contact_strvar.set('')
    gender_strvar.set('')
    dob.set_date(datetime.datetime.now().date())
    subject_strvar.set('')


def reset_form():
    global tree
    tree.delete(*tree.get_children())
    reset_fields()


def display_records():
    tree.delete(*tree.get_children())

    mycursor.execute('SELECT * FROM STUDENT_INFORMATION')
    data = mycursor.fetchall()

    for records in data:
        tree.insert('', END, values=records)


def open_file():
    file_path = fd.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
                # Insert the file contents into a text widget or any other appropriate widget
                text_widget.insert('1.0', file_contents)
        except Exception as e:
            mb.showerror('Error!', str(e))

def save_database():
    directory = askdirectory()
    if directory:
        try:
            file_path = directory + "/tuition_booking_system.db"
            conn = sqlite3.connect(file_path)
            with open("tuition_booking_system.sql", "w") as file:
                for line in conn.iterdump():
                    file.write('%s\n' % line)
            mb.showinfo('Success', 'Database saved successfully!')
        except Exception as e:
            mb.showerror('Error!', str(e))

def add_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, subject_strvar

    name = name_strvar.get()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    DOB = dob.get_date()
    subject = subject_strvar.get()

    if not name or not email or not contact or not gender or not DOB or not subject:
        mb.showerror('Error!', "Please fill all the missing fields!!")
    else:
        try:
            mycursor.execute(
                'INSERT INTO STUDENT_INFORMATION (NAME, EMAIL, PHONE_NO, GENDER, DOB, SUBJECT) VALUES (%s,%s,%s,%s,%s,%s)',
                (name, email, contact, gender, DOB, subject)
            )
            mydb.commit()
            mb.showinfo('Record added', f"Record of {name} was successfully added")
            reset_fields()
            display_records()
        except Exception as e:
            mb.showerror('Error!', str(e))


def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        tree.delete(current_item)

        mycursor.execute('DELETE FROM STUDENT_INFORMATION WHERE NAME=%s', (selection[0],))
        mydb.commit()

        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

        display_records()




def update_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, subject_strvar

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    old_name = selection[0]

    new_name = name_strvar.get()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    dob_value = dob.get_date()
    subject = subject_strvar.get()

    if not new_name or not email or not contact or not gender or not dob_value or not subject:
        mb.showerror('Error!', "Please fill all the missing fields!!")
    else:
        try:
            mycursor.execute(
                'UPDATE STUDENT_INFORMATION SET NAME=%s, EMAIL=%s, PHONE_NO=%s, GENDER=%s, DOB=%s, SUBJECT=%s WHERE NAME=%s',
                (new_name, email, contact, gender, dob_value, subject, old_name)
            )
            mydb.commit()
            mb.showinfo('Record updated', f"Record of {old_name} was successfully updated to {new_name}")
            reset_fields()
            display_records()
        except Exception as e:
            mb.showerror('Error!', str(e))


main = Tk()
main.title('DataFlair School Management System')
main.geometry('1000x600')
main.resizable(0, 0)

headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

lf_bg = 'SkyBlue'
cf_bg = 'lightpink'

name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
subject_strvar = StringVar()

Label(main, text="SCHOOL MANAGEMENT SYSTEM", font=headlabelfont, bg='Skyblue').pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)

center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.05)
Label(left_frame, text="Subject", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.18)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.31)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.7)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.44)
Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.57)

Entry(left_frame, width=19, textvariable=subject_strvar, font=entryfont).place(x=20, rely=0.23)
Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.1)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=20, rely=0.36)
Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=20, rely=0.49)


OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=45, rely=0.75, relwidth=0.5)

dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=20, rely=0.63)

Button(left_frame, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(relx=0.025,
                                                                                                     rely=0.85)

Button(center_frame, text='Delete Record', font=labelfont, command=remove_record, width=15, bg="skyblue").place(relx=0.1, rely=0.25)
Button(center_frame, text='Update Record', font=labelfont, command=update_record, width=15, bg="skyblue").place(relx=0.1, rely=0.35)
Button(center_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15, bg="skyblue").place(relx=0.1, rely=0.45)
Button(center_frame, text='Reset Form', font=labelfont, command=reset_form, width=15, bg="skyblue").place(relx=0.1, rely=0.55)

# Add a button to open the file
Button(center_frame, text='Open File', font=labelfont, command=open_file, width=15, bg="skyblue").place(relx=0.1, rely=0.15)
Button(center_frame, text='Save Database', font=labelfont, command=save_database, width=15, bg="skyblue").place(relx=0.1, rely=0.65)


tree_frame = Frame(right_frame)
tree_frame.pack(fill=BOTH, expand=1)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

tree['columns'] = ("Name", "Email", "Contact", "Gender", "DOB", "Subject")

tree.column("#0", width=0, stretch=NO)
tree.column("Name", anchor=CENTER, width=120)
tree.column("Email", anchor=CENTER, width=180)
tree.column("Contact", anchor=CENTER, width=120)
tree.column("Gender", anchor=CENTER, width=100)
tree.column("DOB", anchor=CENTER, width=100)
tree.column("Subject", anchor=CENTER, width=120)

tree.heading("#0", text="", anchor=CENTER)
tree.heading("Name", text="Name", anchor=CENTER)
tree.heading("Email", text="Email", anchor=CENTER)
tree.heading("Contact", text="Contact", anchor=CENTER)
tree.heading("Gender", text="Gender", anchor=CENTER)
tree.heading("DOB", text="DOB", anchor=CENTER)
tree.heading("Subject", text="Subject", anchor=CENTER)

tree.pack(fill=BOTH, expand=1)

tree_scroll.config(command=tree.yview)

mydb = sqlite3.connect("tuition_booking_system.db")


display_records()

main.mainloop()
