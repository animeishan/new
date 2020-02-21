from tkinter import *
import os
import tkinter.messagebox
from PIL import ImageTk, Image
class Employee():
    def __init__(self, name,  department, number, email, job, age):
        """This method initializes variables about the details of an employee with respect to each new object created."""
        self.name = name
        self.number = number
        self.department = department
        self.job = job
        self.email=email
        self.age=age
def viewemployeedetail():
    """This function allows the user to view the details of a existing employees."""
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Lookup Employee")
    screen1.geometry("400x355+700+300")
    global lookup_employee_name
    lookup_employee_name = StringVar()
    Label(screen1, text="Employee Name").pack()
    Label(screen1, text=" ").pack()
    employee_lookup_entry = Entry(screen1, textvariable=lookup_employee_name)
    employee_lookup_entry.pack()
    Label(screen1, text=" ").pack()
    Button(screen1, text="Search", width=30, height=1, command=searchemployeedetail, font=("Helvetica",10), bg="Red", activebackground="coral4",borderwidth=10).pack()
def addemployee():
    """This function allows the user to add the details of a new employee."""
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x500+700+300")
    global employee_name
    global employee_number
    global employee_department
    global employee_job
    global employee_email
    global employee_age
    employee_name = StringVar()
    employee_number = StringVar()
    employee_department = StringVar()
    employee_job = StringVar()
    employee_email=StringVar()
    employee_age=StringVar()
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Full Name").pack()
    employee_name_entry = Entry(screen1, textvariable=employee_name)
    employee_name_entry.pack()
    Label(screen1, text="Department").pack()
    employee_department_entry = Entry(screen1, textvariable=employee_department)
    employee_department_entry.pack()
    Label(screen1, text="Age").pack()
    employee_age_entry = Entry(screen1, textvariable=employee_age)
    employee_age_entry.pack()
    Label(screen1, text="Phone Number").pack()
    employee_number_entry = Entry(screen1, textvariable=employee_number)
    employee_number_entry.pack()
    Label(screen1, text="Email Address").pack()
    employee_email_entry = Entry(screen1, textvariable=employee_email)
    employee_email_entry.pack()
    Label(screen1, text="Job").pack()
    employee_job_entry = Entry(screen1, textvariable=employee_job)
    employee_job_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Done", width=30, height=1, command=add, font=("Arial",10), bg="Red", activebackground="coral4",borderwidth=10).pack()
    Label(screen1, text=" ").pack()
    Button(screen1,text="Reset",width=30, height=1,command=reset, font=("Arial",10), bg="Red", activebackground="coral4",borderwidth=10).pack()
    Label(screen1, text=" ").pack()
    Button(screen1, text="Exit", width=30, height=1,command=exit, font=("Arial",10), bg="Red", activebackground="coral4",borderwidth=10).pack()
def exit():
    """This function asks if you want to terminate screen1."""
    exit = tkinter.messagebox.askyesno("Employee system", "Do you want to exit this window?")
    if exit > 0:
        screen1.destroy()
        return
def reset():
    """This function resets all the values entered in the entry boxes."""
    employee_name.set("")
    employee_department.set("")
    employee_job.set("")
    employee_age.set("")
    employee_number.set("")
    employee_email.set("")
def writefile(mydict):
    """This function appends datas to the existing files."""
    f=open("employee.csv", "a+")
    line=mydict["name"]+","+mydict["email"]+","+mydict["department"] +","+mydict["number"]+","+mydict["job"]+","+mydict["age"]+"\n"
    f.write(line)
    f.close()
def add():
    emp_name = employee_name.get()
    emp_number = employee_number.get()
    emp_department = employee_department.get()
    emp_job = employee_job.get()
    emp_email=employee_email.get()
    emp_age = employee_age.get()
    if len(emp_name) != 0 and len(emp_age)!=0 and len(emp_department)!=0 and len(emp_email)!=0 and len(emp_job)!=0 and len(emp_number)!=0:
        employee = Employee(emp_name, emp_number, emp_department, emp_job,emp_email,emp_age)
        local_dict = {}
        local_dict["name"] = employee.name
        local_dict["number"] = employee.number
        local_dict["department"] = employee.department
        local_dict["job"] = employee.job
        local_dict["age"] = employee.age
        local_dict['email'] = employee.email
        writefile(local_dict)
        Label(screen1, text="You Have Been Sucessfully Added", fg="Red", font=("Arial", 15)).pack()
    else:
        Label(screen1, text="Employee Data Is Missing Cant Save", fg="Orange", font=("calibri", 11)).pack()
def delete_employee_screen():
    """This function checks if the username provided for deletion exists or not."""
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("This is where you can delete the Employees")
    screen3.geometry("400x355+700+300")
    global delete_employee_name
    delete_employee_name = StringVar()
    Label(screen3, text="enter name of employee to delete").pack()
    Label(screen3, text=" ").pack()
    employee_lookup_entry = Entry(screen3, textvariable=delete_employee_name)
    employee_lookup_entry.pack()
    Label(screen3, text=" ").pack()
    Button(screen3, text="Delete", width=30, height=1, command=delete_employee_by_name, font=("Helvetica",10), bg="Red", activebackground="coral3",borderwidth=10).pack()
def exitusernotfounddelete():
    """This function terminates the 'Delete Section' window."""
    delete_screen.destroy()
def delete_employee_by_name():
    """This function allows the user to enter the name of the employee whose details he wants to delete."""
    delete_employee = delete_employee_name.get()
    mydict = load_data()
    global delete_screen
    delete_screen = Toplevel(screen3)
    delete_screen.title("Delete Section")
    delete_screen.geometry("400x355+700+300")
    if len(delete_employee) == 0:
        Label(delete_screen, text="Enter a Name.").pack()
        Label(delete_screen, text=" ").pack()
        Button(delete_screen, text="Return", command=exitusernotfounddelete, height=2, width=20,font=("Helvetica",10), bg="Red", activebackground="coral3",borderwidth=10).pack()
    elif delete_employee in mydict:
        del mydict[delete_employee]
        Label(delete_screen, text="Employee deleted successfully").pack()
    else:
        Label(delete_screen, text="Employee by the given name was not found.").pack()
        Label(delete_screen, text=" ").pack()
        Button(delete_screen, text="Return", command=exitusernotfounddelete, height=2, width=20, font=("Helvetica", 10),bg="Red", activebackground="coral3", borderwidth=10).pack()
    write_file(mydict)
def write_file(mydict):
    f = open("employee.csv", "w+")
    for k in mydict:
        line = mydict[k]["name"] + "," + mydict[k]["email"] + "," + mydict[k]["department"] + "," + mydict[k]["number"] + "," + \
               mydict[k]["job"] + "," + mydict[k]["age"] + "\n"
        f.write(line)
    f.close()
def searchemployeedetail():
    search_name = lookup_employee_name.get()
    mydict = load_data()
    global search_screen
    search_screen = Toplevel(screen1)
    search_screen.title("Searched Results")
    screen1.geometry("400x355+700+300")
    if len(search_name) == 0:
        Label(search_screen, text="Enter a Name").pack()
    elif search_name in mydict:
        Label(search_screen, text=mydict[search_name]).pack()
        print(mydict[search_name])
    else:
        Label(search_screen, text="Employee Unavailable").pack()
def load_data():
   p=open("employee.csv", "r")
   mydict={}
   for line in p:
       if len(m)==6:
           local_dict={}
           local_dict["name"]=m[0]
           local_dict["email"]=m[1]
           local_dict["department"]=m[2]
           local_dict["number"]=m[3]
           local_dict["job"]=m[4]
           local_dict["age"]=m[5]
           mydict[m[0]]=local_dict
   p.close()
   return mydict
def exitmainscreen():
    "This function terminates the 'Home Page' window when the 'Exit' button is pressed in it."
    employee_main_screen.destroy()
def deletescreen2():
    """This function terminates the 'Sign In Page' window and presents a window 'Main Window' which provides vaarious option for the user."""
    screen3.destroy()
    global employee_main_screen
    employee_main_screen = Tk()
    employee_main_screen.geometry("900x650+500+200")
    employee_main_screen.title("Main Window")
    Label(employee_main_screen, font=('arial', 30, 'bold'), text="Employee Management System ", bd=10, fg="red").pack()
    Label(employee_main_screen, text="").pack()
    Button(employee_main_screen, text="View Employee Details", height="2", width="30", command=viewemployeedetail, bg="Red2", activebackground="coral3",borderwidth=10).pack()
    Label(employee_main_screen, text="").pack()
    Button(employee_main_screen, text="Add Employee", height="2", width="30",command=addemployee, bg="Red", activebackground="coral3",borderwidth=10).pack()
    Label(employee_main_screen, text="").pack()
    Button(employee_main_screen, text="Delete Employee", height="2", width="30",command=delete_employee_screen, bg="Red", activebackground="coral3",borderwidth=10).pack()
    Label(employee_main_screen, text="").pack()
    Button(employee_main_screen, text="Sign Out", height="1", width="20",command=exitmainscreen, bg="Red", activebackground="coral3",borderwidth=10).pack()
    employee_main_screen.mainloop()
###Login Page
def delete3():
    """This function terminates the 'Incorrect Password' window."""
    screen4.destroy()
def delete4():
    """This function terminates the 'User not available' window."""
    screen5.destroy()
def user_login_sucess():
    """This function opens a new window 'Success' if the Sign In entries exists."""
    global screen3
    screen2.destroy()
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("400x355+700+300")
    Label(screen3, text="Sign In Success", font=("Helvetica", 15)).pack()
    Label(screen3,text=" ").pack()
    Label(screen3, text=" ").pack()
    Label(screen3, text=" ").pack()
    Button(screen3, text="Next", command=deletescreen2, width=20, height=2, font=("Helvetica"), bg="Red", activebackground="coral3",borderwidth=10).pack()
def password_unrecognised():
    """This function displays a message if the entered password during sign in is incorrect."""
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Incorrect Password")
    screen4.geometry("400x355+700+300")
    Label(screen4, text="Incorrect Password").pack()
    Label(screen4, text=" ").pack()
    Button(screen4, text="Return", command=delete3, bg="Red", activebackground="coral3",borderwidth=10).pack()
def user_doesnotexist():
    """This function displays a message if the entered username does not exist."""
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User not available")
    screen5.geometry("400x355+700+300")
    Label(screen5, text="User Does Not Exist", font=("Helvetica", 10)).pack()
    Label(screen5, text=" ").pack()
    Button(screen5, text="Return", command=delete4, bg="Red", activebackground="coral3",borderwidth=10).pack()
def register_employee():
    """This function creates a new file and writes the registered details into it."""
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    enter_username_entry.delete(0, END)
    enter_password_entry.delete(0, END)
    Label(screen1, text="Your entries has been successfully registered. ", bg="Red", font=("Helvetica", 10)).pack()
def signin_verify():
    """This function checks whether the entered username already exists or not."""
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_data = os.listdir()
    if username1 in list_of_data:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            user_login_sucess()
        else:
            password_unrecognised()
    else:
        user_doesnotexist()
def exitsigninpage():
    """This function quits the 'Sign In Page' of the program when the 'Exit' button is pressed in the 'Sign In' window."""
    screen2.destroy()
#Sign In Page:
def signin1():
    """This function presents a page where an existing user can sign in to the program with his username and password and it runs when 'Sign In' button is pressed in the 'Home Page' window."""
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Sign In Page")
    screen2.geometry("400x355+700+300")
    Label(screen2, text="Sign In Details:", bg="Red", width=150, height=3, font=("Helvetica", 15)).pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username:", font=("Helvetica", 10)).pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password:", font=("Helvetica", 10)).pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show="*")
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Sign In", width=20, height=1, command=signin_verify, font=("Helvetica", 10), bg="Red", activebackground="coral3",borderwidth=10).pack()
    Label(screen2, text=" ").pack()
    Button(screen2, text="Exit", height=1, width=20, command=exitsigninpage, font=("Helvetica",10), bg="Red", activebackground="coral3",borderwidth=10).pack()
def exitregisterpage():
    """This function quits the 'Register Page' of the program when the 'Exit' button is pressed in the 'Register Page' window."""
    screen1.destroy()
#Register Page:
def register1():
    """This function presents a page where a new user can register his username and password and it runs when 'Register' button is presssed in the 'Home Page' window."""
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register Page")
    screen1.geometry("400x355+700+300")
    global username
    global password
    global enter_username_entry
    global enter_password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text="Register Details", bg="Red", width=150, height=3, font=("Helvetica", 15)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username", font=("Helvetica", 10)).pack()
    enter_username_entry = Entry(screen1, textvariable=username)
    enter_username_entry.pack()
    Label(screen1, text="New Password", font=("Helvetica", 10)).pack()
    enter_password_entry = Entry(screen1, textvariable=password, show="*")
    enter_password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=20, height=1, command=register_employee, font=("Helvetica", 10), bg="Red", activebackground="coral3",borderwidth=10).pack()
    Label(screen1, text=" ").pack()
    Button(screen1, text="Exit", height=1, width=20, command=exitregisterpage, font=("Helvetica", 10), bg="Red", activebackground="coral3",borderwidth=10).pack()
def exithomepage():
    """This function quits the 'Home Page' of the program when the 'Exit' button is pressed in the 'Home Page' window."""
    screen.destroy()
#Home Page:
def homepage():
        """This function presents the home page of the program where the user can choose either to register, sign in or exit the program."""
        global screen
        screen = Tk()
        screen.geometry("400x430+700+300")
        screen.title("Home Page")
        canvas = Canvas(screen, width=300, height=160)
        background_image = ImageTk.PhotoImage(Image.open("abc.jpg"))
        # canvas.create_image(0, 0, anchor=NW, image=background_image)
        background_label = Label(screen, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        canvas.pack()

        Label(text=" Employee Management System", bg="Red2", width="150", height="3", font=("Helvetica", 15)).pack()
        Label(text="").pack()
        Button(text="Register", height="3", width="40", command=register1, font=("Helvetica", 10), bg="Red", activebackground="coral3",borderwidth=10).pack()
        Label(text="").pack()
        Button(text="Sign In", height="3", width="40", command=signin1, font=("Helvetica", 10), bg="Red", activebackground="coral3",borderwidth=10).pack()
        Label(text="").pack()
        Button(text="Exit", height=2, width=20, command=exithomepage, font=("Helvetica",10), bg="Red", activebackground="coral3",borderwidth=10).pack()
        screen.mainloop()


homepage()