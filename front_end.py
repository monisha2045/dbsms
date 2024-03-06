from tkinter import *
from tkinter import messagebox
from back_end import *
from PIL import ImageTk , Image
import cx_Oracle

window = Tk()
window.title("STUDENT INFORMATION SYSTEM")
window.geometry("800x600")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

connection = cx_Oracle.connect(user='system', password='monisha', dsn="localhost:1521/orcl")

def display_students():
    cur=connection.cursor()
    sql_query = "select * from students"
    cur.execute(sql_query)
    values = cur.fetchall()
    for value in values:
        yield value
    cur.close()

def display_teachers():
    cur = connection.cursor()
    sql="select * from teachers"
    cur.execute(sql)

    values = cur.fetchall()
    for value in values:
        yield value  
    cur.close()
    
def display_courses():
    cur = connection.cursor()
    cur.execute("select * from courses")
    for i in cur :
       yield i
    cur.close()
    
def display_grade_chart():
    cur = connection.cursor()
    cur.execute("select s.name ,g.avg_grade , t.avg_grade from SEM1 g join students s on s.digital_id = g.digital_id JOIN sem2 t on t.digital_id = g.digital_id ")
    for i in cur :
        yield i
    cur.close()

def display_activities():
    cur=connection.cursor()
    cur.execute("select * from extracurricularactivities")
    for i in cur :
        yield i      
    cur.close()  
    
def display_studentactivities():
    cur= connection.cursor()
    cur.execute("select s.name , e.activity_name from studentactivities sa join students s on s.digital_id = sa.student_id join extracurricularactivities e on e.activity_id = sa.activity_id")
    for i in cur:
        yield i
    cur.close()
    
def display_all_achievements():
    cur = connection.cursor()
    cur.execute("select e.activity_name , a.achievement_description from activityachievements a join extracurricularactivities e on e.activity_id = a.activity_id")
    for i in cur:
        yield i
    cur.close()
    
def show_classes():
    cur = connection.cursor()
    cur.execute("select t.name , t.qualification , t.phone ,c.class_name from classes c natural join teachers t ")
    for i in cur:
        yield i
    cur.close()

def sem1_results():
    cur = connection.cursor()
    cur.execute("select s.name , sem1.Mathematics1 ,sem1.Physics,sem1.ComputerScience  from sem1 natural join students s")
    for i in cur:
        yield i
    cur.close()
    
def sem2_results():
    cur = connection.cursor()
    cur.execute("select s.name , sem2.Mathematics2 ,sem2.EnglishLiterature,sem2.History from sem2 natural join students s")
    for i in cur:
        yield i
    cur.close()
    
def add_student(id_1,name,date,age,address,phone,gender,year):
    cur = connection.cursor()
    cur.execute("INSERT INTO students VALUES (:v8, :v7, TO_DATE(:v6, 'YYYY-MM-DD'), :v5, :v4, :v3, :v2, :v1)",
            {"v8": id_1, "v7": name, "v6": date, "v5": age, "v4": address, "v3": phone, "v2": gender, "v1": year})

    connection.commit()
    
def add_teacher(id1,name,quality,phone,gender):
    cur = connection.cursor()
    cur.execute("insert into teachers values (:v1,:v2,:v3,:v4,:v5)",
                {"v1":id1,"v2":name,"v3":quality,"v4":phone,"v5":gender})
    connection.commit()
    
def add_course(id1,name,credit):
    cur = connection.cursor()
    cur.execute("insert into courses values (:v1,:v2,:v3)",
                {"v1":id1,"v2":name,"v3":credit})
    connection.commit()
    
def enroll_course(e_id1,st_id2,c_id3):
    cur = connection.cursor()
    cur.execute("insert into enrollments values (:v1,:v2,:v3)",
                {"v1":e_id1,"v2":st_id2,"v3":c_id3})
    connection.commit()
    
def add_activity(id1,name,describe):
    cur = connection.cursor()
    cur.execute("insert into extracurricularactivities values (:v1,:v2,:v3)",
                {"v1":id1,"v2":name,"v3":describe})
    connection.commit()
    
def enroll_activity(ac_id1,st_id2):
    cur = connection.cursor()
    cur.execute("insert into studentactivities values( :v1 ,:v2)",
                {"v1":ac_id1,"v2":st_id2})
    connection.commit()
    
def add_class(id1,name,t_id):
    cur = connection.cursor()
    cur.execute("insert into classes values (:v1,:v2,:v3)",
                {"v1":id1,"v2":name,"v3":t_id})
    connection.commit()
    
def insert_sem1(id1,maths,phy,cs,avg):
    cur = connection.cursor()
    cur.execute("insert into sem1 values(:v1,:v2,:v3,:v4,:v5)",
                {"v1":id1,"v2":maths,"v3":phy,"v4":cs,"v5":avg})
    connection.commit()
    
def insert_sem2(id1,maths,el,his,avg):
    cur = connection.cursor()
    cur.execute("insert into sem2 values(:v1,:v2,:v3,:v4,:v5)",
                {"v1":id1,"v2":maths,"v3":el,"v4":his,"v5":avg})
    connection.commit()
    
def search_student(name) :
    cur = connection.cursor()
    cur.execute("select * from students where name=:var",var=name)
    try:
        t1.delete(1.0, END)
    except:
        pass 
    for i in cur:
        print(i)
        t1.insert(END, i + tuple("\n"))
        
def search_teacher(name):
    cur = connection.cursor()
    cur.execute("select * from teachers where name = :var",var=name)
    try:
        t2.delete(1.0, END)
    except:
        pass 
    for i in cur:
        print(i)
        t2.insert(END, i + tuple("\n"))
        
def search_grade(name):
    cur = connection.cursor()
    cur.execute("SELECT g.avg_grade , c.avg_grade FROM sem1 g JOIN sem2 c on c.digital_id = g.digital_id JOIN students s ON s.digital_id = c.digital_id WHERE s.name = :var" ,var = name)
    try:
        t4.delete(1.0, END)
    except:
        pass 
    for i in cur:
        print(i)
        t4.insert(END, i + tuple("\n"))
 
def find_enroll_activity(name):
    cur = connection.cursor()
    cur.execute("select e.activity_name from studentactivities sa join students s on s.digital_id = sa.student_id join extracurricularactivities e on e.activity_id = sa.activity_id where s.name = :var",var = name)
    try:
        t5.delete(1.0, END)
    except:
        pass 
    for i in cur:
        print(i)
        t5.insert(END, i + tuple("\n")) 
        
def achievement(activity):
    cur = connection.cursor()
    cur.execute("select a.achievement_description from activityachievements a join extracurricularactivities e on e.activity_id = a.activity_id where e.activity_name = :var",var= activity)
    try:
        t6.delete(1.0, END)
    except:
        pass
    for i in cur:
        print(i)
        t6.insert(END, i + tuple("\n"))
        
def class_handled(name):
    cur = connection.cursor()
    cur.execute("select c.class_name from classes c join teachers t on t.teacher_id = c.teacher_id where t.name = :var",var = name)
    try:
        t7.delete(1.0, END)
    except:
        pass
    for i in cur:
        print(i)
        t7.insert(END, i + tuple("\n"))
        
def result_sem1(name):
    cur = connection.cursor()
    cur.execute("select sem1.Mathematics1,sem1.Physics,sem1.ComputerScience from sem1 natural join students where students.name = :var",var = name)
    try:
        t8.delete(1.0, END)
    except:
        pass 
    for i in cur:
        print(i)
        t8.insert(END, i + tuple("\n"))
        
def result_sem2(name):
    cur = connection.cursor()
    cur.execute("select sem2.Mathematics2,sem2.EnglishLiterature,sem2.History from sem2 natural join students where students.name = :var",var = name)
    try:
        t9.delete(1.0, END)
    except:
        pass
    for i in cur:
        print(i)
        t9.insert(END, i + tuple("\n"))
        
def delete_student(name):
    cur = connection.cursor()
    cur.execute("delete from students where name = :var",var=name)
    connection.commit()
    
def delete_teacher(name):
    cur = connection.cursor()
    cur.execute("delete from teachers where name = :var",var=name)
    connection.commit()
    
def delete_course(name):
    cur = connection.cursor()
    cur.execute("delete from courses where course_name = :var",var = name)
    connection.commit()
    
def remove_result1(id1):
    cur = connection.cursor()
    cur.execute("delete from sem1 where digital_id = :var",var=id1)
    connection.commit()
        
def frame_changer(f):
    f.tkraise()
    
def insert_into_t3(func):
    try:
        t3.delete(1.0, END)
    except:
        pass
    for i in func():
        print(i)
        t3.insert(END, i + tuple("\n"))
      
def disenroll_course(st_id1,c_id2):
    cur = connection.cursor()
    cur.execute("delete from enrollments where student_id = :var1 and course_id = :var2",
                {"var1" : st_id1,"var2":c_id2})
    connection.commit() 
    
def delete_activity(name):
    cur = connection.cursor()
    cur.execute("delete from extracurricularactivities where activity_name = :var",var = name)
    connection.commit()
    
def remove_class(name):
    cur = connection.cursor()
    cur.execute("delete from classes where class_name = :var",var=name)
    connection.commit() 
    
def remove_result2(id1):
    cur = connection.cursor()
    cur.execute("delete from sem2 where digital_id = :var",var=id1)
    connection.commit()  

        
#INSERT STUDENT        
def submit1():
    try:
        id1 = label480.get()
        name = label410.get() 
        date = label420.get()
        age = label430.get()
        city = label440.get()
        phone = label450.get()
        gender = label460.get()
        year = label470.get()
        add_student(id1,name,date,age,city,phone,gender,year)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
   
#INSERT TEACHER
def submit2():
    try:
        id1 = l410.get()
        name = l420.get()
        qualify = l430.get()
        phone = l440.get()
        gender = l450.get()
        add_teacher(id1,name,qualify,phone,gender)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
    
#INSERT COURSE
def submit3():
    try:
        id1 = la410.get()
        name = la420.get()
        credit = la430.get()
        add_course(id1,name,credit)
    except cx_Oracle.Error as e:
        messagebox.showerror('error', e)
        
#ENROLL COURSE
def submit4():
    try:
        id1 = lab410.get()
        st_id = lab420.get()
        c_id = lab430.get()
        enroll_course(id1,st_id,c_id)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
#ADD ACTIVITY
def submit5():
    try:
        id1 = labe410.get()
        name = labe420.get()
        describe = labe430.get()
        add_activity(id1,name,describe)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
# ENROLL ACTIVITY
def submit6():
    try:
        id1 = e410.get()
        id2 = e420.get()
        enroll_activity(id1,id2)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
#ADD CLASS
def submit7():
    try:
        id1 = c410.get()
        name = c420.get()
        t_id = c430.get()
        add_class(id1,name,t_id)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
# ADD SEM 1 RESULTS
def submit8():
    try:
        id1 = r410.get()
        maths1 = r420.get()
        phy = r430.get()
        cs = r440.get()
        avg = r450.get()
        insert_sem1(id1,maths1,phy,cs,avg)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
#ADD SEM 2 RESULTS
def submit9():
    try:
        id1 = rr410.get()
        maths2 = rr420.get()
        el = rr430.get()
        his = rr440.get()
        avg = rr450.get()
        insert_sem2(id1,maths2,el,his,avg)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
#search by name in student
def submit10():
    try:
        name =label510.get()
        search_student(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
# search by name in teacher
def submit11():
    try:
        name =l510.get()
        search_teacher(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
#search grade by name
def submit12():
    try:
        name =la510.get()
        search_grade(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e) 
        
# search by name
def submit13():
    try:
        name =lab510.get()
        find_enroll_activity(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
#SEARCH BY ACTIVITY
def submit14():
    try:
        name =labe510.get()
        achievement(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
#SEARCH BY TEACHER NAME
def submit15():
    try:
        name =x510.get()
        class_handled(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
# search by name
def submit16():
    try:
        name =y510.get()
        result_sem1(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
# search by name
def submit17():
    try:
        name =z510.get()
        result_sem2(name)
    except cx_Oracle.Error as e :
        messagebox.showerror('error',e)
        
# remove student
def submit18():
    try:
        name = d510.get()
        delete_student(name)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
# remove teacher
def submit19():
    try:
        name = f510.get()
        delete_teacher(name)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
# remove course
def submit20():
    try:
        name = h510.get()
        delete_course(name)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)

# DISENROLL COURSE
def submit21():
    try:
        st_id = j510.get()
        c_id = k510.get()
        disenroll_course(st_id,c_id)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
# delete activity
def submit22():
    try:
        name = m510.get()
        delete_activity(name)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
# remove class
def submit23():
    try:
        name = n510.get()
        remove_class(name)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
# remove sem1 result
def submit24():
    try:
        id1 = o510.get()
        remove_result1(id1)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)
        
# remove sem2 result
def submit25():
    try:
        id1 = o510.get()
        remove_result2(id1)
    except cx_Oracle.Error as e:
        messagebox.showerror('error',e)

        
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window) 
# Define frame3 before referencing it
frame4 = Frame(window)
frame41 = Frame(window)
frame42 = Frame(window)
frame43 = Frame(window)
frame44 = Frame(window)
frame45 = Frame(window)
frame46 = Frame(window)
frame47 = Frame(window)
frame48 = Frame(window)
frame49 = Frame(window)
frame5 = Frame(window)
frame51 = Frame(window)
frame52 = Frame(window)
frame53 = Frame(window)
frame54 = Frame(window)
frame55 = Frame(window)
frame56 = Frame(window)
frame57 = Frame(window)
frame58 = Frame(window)
frame6 = Frame(window)
frame61 = Frame(window)
frame62 = Frame(window)
frame63 = Frame(window)
frame64 = Frame(window)
frame65 = Frame(window)
frame66 = Frame(window)
frame67 = Frame(window)
frame68 = Frame(window)

f1img = ImageTk.PhotoImage(Image.open("E:\it lab\SEM 3\Database Technology\Lab\sis\student.jpg"))
cavsimg=Label(frame1,image=f1img)
cavsimg.place(x=0,y=0)

frame1.grid(row=0, column=0, sticky='nsew')

label1 = Label(frame1, text="WELCOME TO STUDENT INFORMATION SYSTEM", font=("Quiche Sans", 18))
label1.place(relx=0.2,rely=0.9)

start_button = Button(frame1, text="START!", font=("Quiche Sans", 12), command=lambda: frame_changer(frame2))
start_button.place(relx=0.5,rely=0.2,anchor="center")

frame2.grid(row=0, column=0, sticky='nsew')
frame3.grid(row=0, column=0, sticky='nsew')  # Corrected column value
frame4.grid(row=0, column=0, sticky='nsew')
frame41.grid(row=0, column=0, sticky='nsew')
frame42.grid(row=0, column=0, sticky='nsew')
frame43.grid(row=0, column=0, sticky='nsew')
frame44.grid(row=0, column=0, sticky='nsew')
frame45.grid(row=0, column=0, sticky='nsew')
frame46.grid(row=0, column=0, sticky='nsew')
frame47.grid(row=0, column=0, sticky='nsew')
frame48.grid(row=0, column=0, sticky='nsew')
frame49.grid(row=0, column=0, sticky='nsew')
frame5.grid(row=0, column=0, sticky='nsew')
frame51.grid(row=0, column=0, sticky='nsew')
frame52.grid(row=0, column=0, sticky='nsew')
frame53.grid(row=0, column=0, sticky='nsew')
frame54.grid(row=0, column=0, sticky='nsew')
frame55.grid(row=0, column=0, sticky='nsew')
frame56.grid(row=0, column=0, sticky='nsew')
frame57.grid(row=0, column=0, sticky='nsew')
frame58.grid(row=0, column=0, sticky='nsew')
frame6.grid(row=0, column=0, sticky='nsew')
frame61.grid(row=0, column=0, sticky='nsew')
frame62.grid(row=0, column=0, sticky='nsew')
frame63.grid(row=0, column=0, sticky='nsew')
frame64.grid(row=0, column=0, sticky='nsew')
frame65.grid(row=0, column=0, sticky='nsew')
frame66.grid(row=0, column=0, sticky='nsew')
frame67.grid(row=0, column=0, sticky='nsew')
frame68.grid(row=0, column=0, sticky='nsew')

f2img = ImageTk.PhotoImage(Image.open("E:\it lab\SEM 3\Database Technology\Lab\sis\WhatsApp Image 2023-12-20 at 21.44.08_6a95249b.jpg"))
cavsimg2=Label(frame2,image=f2img)
cavsimg2.place(x=0,y=0)
f3img = ImageTk.PhotoImage(Image.open("E:\it lab\SEM 3\Database Technology\Lab\sis\WhatsApp Image 2023-12-20 at 21.44.08_0fef5ca7.jpg"))
cavsimg3=Label(frame3,image=f3img)
cavsimg3.place(x=0,y=0)
f4img = ImageTk.PhotoImage(Image.open("E:\it lab\SEM 3\Database Technology\Lab\sis\WhatsApp Image 2023-12-20 at 21.44.08_0fef5ca7.jpg"))
cavsimg4=Label(frame4,image=f4img)
cavsimg4.place(x=0,y=0)
cavsimg41=Label(frame41,image=f4img)
cavsimg41.place(x=0,y=0)
cavsimg42=Label(frame42,image=f4img)
cavsimg42.place(x=0,y=0)
cavsimg43=Label(frame43,image=f4img)
cavsimg43.place(x=0,y=0)
cavsimg44=Label(frame44,image=f4img)
cavsimg44.place(x=0,y=0)
cavsimg45=Label(frame45,image=f4img)
cavsimg45.place(x=0,y=0)
cavsimg46=Label(frame46,image=f4img)
cavsimg46.place(x=0,y=0)
cavsimg47=Label(frame47,image=f4img)
cavsimg47.place(x=0,y=0)
cavsimg48=Label(frame48,image=f4img)
cavsimg48.place(x=0,y=0)
cavsimg49=Label(frame49,image=f4img)
cavsimg49.place(x=0,y=0)
f5img = ImageTk.PhotoImage(Image.open("E:\it lab\SEM 3\Database Technology\Lab\sis\WhatsApp Image 2023-12-20 at 21.44.07_2aec12f4.jpg"))
cavsimg5=Label(frame5,image=f5img)
cavsimg5.place(x=0,y=0)
cavsimg51=Label(frame51,image=f5img)
cavsimg51.place(x=0,y=0)
cavsimg52=Label(frame52,image=f5img)
cavsimg52.place(x=0,y=0)
cavsimg53=Label(frame53,image=f5img)
cavsimg53.place(x=0,y=0)
cavsimg54=Label(frame54,image=f5img)
cavsimg54.place(x=0,y=0)
cavsimg55=Label(frame55,image=f5img)
cavsimg55.place(x=0,y=0)
cavsimg56=Label(frame56,image=f5img)
cavsimg56.place(x=0,y=0)
cavsimg57=Label(frame57,image=f5img)
cavsimg57.place(x=0,y=0)
cavsimg58=Label(frame58,image=f5img)
cavsimg58.place(x=0,y=0)
f6img = ImageTk.PhotoImage(Image.open("E:\it lab\SEM 3\Database Technology\Lab\sis\WhatsApp Image 2023-12-20 at 21.44.07_2aec12f4.jpg"))
cavsimg6=Label(frame6,image=f6img)
cavsimg6.place(x=0,y=0)
cavsimg61=Label(frame61,image=f6img)
cavsimg61.place(x=0,y=0)
cavsimg62=Label(frame62,image=f6img)
cavsimg62.place(x=0,y=0)
cavsimg63=Label(frame63,image=f6img)
cavsimg63.place(x=0,y=0)
cavsimg64=Label(frame64,image=f6img)
cavsimg64.place(x=0,y=0)
cavsimg65=Label(frame65,image=f6img)
cavsimg65.place(x=0,y=0)
cavsimg66=Label(frame66,image=f6img)
cavsimg66.place(x=0,y=0)
cavsimg67=Label(frame67,image=f6img)
cavsimg67.place(x=0,y=0)
cavsimg68=Label(frame68,image=f6img)
cavsimg68.place(x=0,y=0)

label2 = Label(frame2, text="CHOOSE THE FUNCTIONS ABOVE!", font=("Quiche Sans", 18))
label2.place(relx=0.4,rely=0.9)

t_button1 = Button(frame2, text="DISPLAY", font=("Quiche Sans", 12), command=lambda: frame_changer(frame3))
t_button1.place(relx=0.2,rely=0.2)
t_button2 = Button(frame2, text="SEARCH", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
t_button2.place(relx=0.8,rely=0.2)
t_button3 = Button(frame2, text="INSERT", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
t_button3.place(relx=0.2,rely=0.4)  # Adjusted column value
t_button4 = Button(frame2, text="REMOVE", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
t_button4.place(relx=0.8,rely=0.4)  # Adjusted column value

label3 = Label(frame3, text="CHOOSE THE BUTTON TO SEE !", font=("Quiche Sans", 18))
label3.place(relx=0.4)

# display 
b1=Button(frame3, text="STUDENTS", font=("Quiche Sans", 10), command=lambda: insert_into_t3(display_students)).place(relx=0.25,rely=0.2)
b2=Button(frame3, text="TEACHERS", font=("Quiche Sans", 10), command=lambda:insert_into_t3(display_teachers)).place(relx=0.4,rely=0.2)
b3=Button(frame3, text="COURSES", font=("Quiche Sans", 10), command=lambda:insert_into_t3(display_courses)).place(relx=0.6,rely=0.2)
b4=Button(frame3, text="GRADE_CHART", font=("Quiche Sans", 10), command=lambda:insert_into_t3(display_grade_chart)).place(relx=0.8,rely=0.2)
b5=Button(frame3, text=" ENROLACTIVITY", font=("Quiche Sans", 10), command=lambda:insert_into_t3(display_studentactivities)).place(relx=0.25,rely=0.4)
b6=Button(frame3, text="ACHIEVEMENTS", font=("Quiche Sans", 10), command=lambda:insert_into_t3(display_all_achievements)).place(relx=0.4,rely=0.4)
b7=Button(frame3, text="CLASSES", font=("Quiche Sans", 10), command=lambda:insert_into_t3(show_classes)).place(relx=0.6,rely=0.4)
b8=Button(frame3, text="SEM 1 RESULTS", font=("Quiche Sans", 10), command=lambda:insert_into_t3(sem1_results)).place(relx=0.8,rely=0.4)
b9=Button(frame3, text="SEM 2 RESULTS", font=("Quiche Sans", 10), command=lambda:insert_into_t3(sem2_results)).place(relx=0.10,rely=0.4)
b10=Button(frame3, text="ACTIVITIES", font=("Quiche Sans", 10), command=lambda:insert_into_t3(display_activities)).place(relx=0.10,rely=0.2)
t3=Text(frame3,height=20,width=150)
t3.place(relx=0.10,rely=0.5)

label4 = Label(frame4, text="CHOOSE THE BUTTON TO SEE !", font=("Quiche Sans", 18))
label4.place(relx=0.4)


#INSERT STUDENT
label4 = Label(frame41, text="FILL THE DETAILS OF THE STUDENT!", font=("Quiche Sans", 18))
label4.place(relx=0.2,rely = 0.1)
label41 = Label(frame41, text="NAME :", font=("Quiche Sans", 12))
label41.place(relx=0.2,rely=0.2)
label410 = Entry(frame41)
label410.place(relx=0.4,rely=0.2)
label42 = Label(frame41, text="DOB :", font=("Quiche Sans", 12))
label42.place(relx=0.2,rely=0.3)
label420 = Entry(frame41)
label420.place(relx=0.4,rely=0.3)
label43 = Label(frame41, text="AGE :", font=("Quiche Sans", 12))
label43.place(relx=0.2,rely=0.4)
label430 = Entry(frame41)
label430.place(relx=0.4,rely=0.4)
label44 = Label(frame41, text="CITY :", font=("Quiche Sans", 12))
label44.place(relx=0.2,rely=0.5)
label440 = Entry(frame41)
label440.place(relx=0.4,rely=0.5)
label45 = Label(frame41, text="PHONE :", font=("Quiche Sans", 12))
label45.place(relx=0.2,rely=0.6)
label450 = Entry(frame41)
label450.place(relx=0.4,rely=0.6)
label46 = Label(frame41, text="GENDER :", font=("Quiche Sans", 12))
label46.place(relx=0.2,rely=0.7)
label460 = Entry(frame41)
label460.place(relx=0.4,rely=0.7)
label47 = Label(frame41, text="YEAR OF ADMISSION :", font=("Quiche Sans", 12))
label47.place(relx=0.2,rely=0.8)
label470 = Entry(frame41)
label470.place(relx=0.4,rely=0.8)
label48 = Label(frame41, text="ID :", font=("Quiche Sans", 12))
label48.place(relx=0.2,rely=0.9)
label480 = Entry(frame41)
label480.place(relx=0.4,rely=0.9)

# INSERT TEACHER
l4 = Label(frame42, text="FILL THE DETAILS OF THE TEACHER!", font=("Quiche Sans", 18))
l4.place(relx=0.2,rely = 0.1)
l41 = Label(frame42, text="ID :", font=("Quiche Sans", 12))
l41.place(relx=0.2,rely=0.2)
l410 = Entry(frame42)
l410.place(relx=0.4,rely=0.2)
l42 = Label(frame42, text="NAME :", font=("Quiche Sans", 12))
l42.place(relx=0.2,rely=0.3)
l420 = Entry(frame42)
l420.place(relx=0.4,rely=0.3)
l43 = Label(frame42, text="QUALIFICATION :", font=("Quiche Sans", 12))
l43.place(relx=0.2,rely=0.4)
l430 = Entry(frame42)
l430.place(relx=0.4,rely=0.4)
l44 = Label(frame42, text="PHONE :", font=("Quiche Sans", 12))
l44.place(relx=0.2,rely=0.5)
l440 = Entry(frame42)
l440.place(relx=0.4,rely=0.5)
l45 = Label(frame42, text="GENDER :", font=("Quiche Sans", 12))
l45.place(relx=0.2,rely=0.6)
l450 = Entry(frame42)
l450.place(relx=0.4,rely=0.6)

#insert course
la4 = Label(frame43, text="FILL THE DETAILS OF THE COURSE!", font=("Quiche Sans", 18))
la4.place(relx=0.2,rely = 0.1)
la41 = Label(frame43, text="ID :", font=("Quiche Sans", 12))
la41.place(relx=0.2,rely=0.2)
la410 = Entry(frame43)
la410.place(relx=0.4,rely=0.2)
la42 = Label(frame43, text="NAME :", font=("Quiche Sans", 12))
la42.place(relx=0.2,rely=0.3)
la420 = Entry(frame43)
la420.place(relx=0.4,rely=0.3)
la43 = Label(frame43, text="CREDIT :", font=("Quiche Sans", 12))
la43.place(relx=0.2,rely=0.4)
la430 = Entry(frame43)
la430.place(relx=0.4,rely=0.4)

#enroll course
lab4 = Label(frame44, text="FILL THE DETAILS OF THE ENROLLMENT OF COURSE!", font=("Quiche Sans", 18))
lab4.place(relx=0.2,rely = 0.1)
lab41 = Label(frame44, text="ID :", font=("Quiche Sans", 12))
lab41.place(relx=0.2,rely=0.2)
lab410 = Entry(frame44)
lab410.place(relx=0.4,rely=0.2)
lab42 = Label(frame44, text="STUDENT ID :", font=("Quiche Sans", 12))
lab42.place(relx=0.2,rely=0.3)
lab420 = Entry(frame44)
lab420.place(relx=0.4,rely=0.3)
lab43 = Label(frame44, text="COURSE ID :", font=("Quiche Sans", 12))
lab43.place(relx=0.2,rely=0.4)
lab430 = Entry(frame44)
lab430.place(relx=0.4,rely=0.4)

#add activity
labe4 = Label(frame45, text="FILL THE DETAILS OF THE ACTIVITY", font=("Quiche Sans", 18))
labe4.place(relx=0.2,rely = 0.1)
labe41 = Label(frame45, text="ID :", font=("Quiche Sans", 12))
labe41.place(relx=0.2,rely=0.2)
labe410 = Entry(frame45)
labe410.place(relx=0.4,rely=0.2)
labe42 = Label(frame45, text="NAME :", font=("Quiche Sans", 12))
labe42.place(relx=0.2,rely=0.3)
labe420 = Entry(frame45)
labe420.place(relx=0.4,rely=0.3)
labe43 = Label(frame45, text="DESCRIBE :", font=("Quiche Sans", 12))
labe43.place(relx=0.2,rely=0.4)
labe430 = Entry(frame45)
labe430.place(relx=0.4,rely=0.4)

#enroll activity
e4 = Label(frame46, text="FILL THE DETAILS OF THE ENROLLMENT OF THE ACTIVITY", font=("Quiche Sans", 18))
e4.place(relx=0.1,rely = 0.1)
e41 = Label(frame46, text="ACTIVITY ID :", font=("Quiche Sans", 12))
e41.place(relx=0.2,rely=0.3)
e410 = Entry(frame46)
e410.place(relx=0.4,rely=0.3)
e42 = Label(frame46, text="STUDENT ID :", font=("Quiche Sans", 12))
e42.place(relx=0.2,rely=0.4)
e420 = Entry(frame46)
e420.place(relx=0.4,rely=0.4)

#add class
c4 = Label(frame47, text="FILL THE DETAILS OF THE CLASS", font=("Quiche Sans", 18))
c4.place(relx=0.2,rely = 0.1)
c41 = Label(frame47, text="ID :", font=("Quiche Sans", 12))
c41.place(relx=0.2,rely=0.2)
c410 = Entry(frame47)
c410.place(relx=0.4,rely=0.2)
c42 = Label(frame47, text="NAME :", font=("Quiche Sans", 12))
c42.place(relx=0.2,rely=0.3)
c420 = Entry(frame47)
c420.place(relx=0.4,rely=0.3)
c43 = Label(frame47, text="TEACHER ID :", font=("Quiche Sans", 12))
c43.place(relx=0.2,rely=0.4)
c430 = Entry(frame47)
c430.place(relx=0.4,rely=0.4)

#add sem results1
r4 = Label(frame48, text="UPDATE THE GRADES FOR SEM 1!", font=("Quiche Sans", 18))
r4.place(relx=0.2,rely = 0.1)
r41 = Label(frame48, text=" STUDENT ID :", font=("Quiche Sans", 12))
r41.place(relx=0.2,rely=0.2)
r410 = Entry(frame48)
r410.place(relx=0.4,rely=0.2)
r42 = Label(frame48, text="MATHS 1 :", font=("Quiche Sans", 12))
r42.place(relx=0.2,rely=0.3)
r420 = Entry(frame48)
r420.place(relx=0.4,rely=0.3)
r43 = Label(frame48, text="PHYSICS :", font=("Quiche Sans", 12))
r43.place(relx=0.2,rely=0.4)
r430 = Entry(frame48)
r430.place(relx=0.4,rely=0.4)
r44 = Label(frame48, text="COMPUTERSCIENCE :", font=("Quiche Sans", 10))
r44.place(relx=0.2,rely=0.5)
r440 = Entry(frame48)
r440.place(relx=0.4,rely=0.5)
r45 = Label(frame48, text="AVERAGE GRADE:", font=("Quiche Sans", 12))
r45.place(relx=0.2,rely=0.6)
r450 = Entry(frame48)
r450.place(relx=0.4,rely=0.6)

#add sem 2 results
rr4 = Label(frame49, text="UPDATE THE GRADES FOR SEM 2!", font=("Quiche Sans", 18))
rr4.place(relx=0.2,rely = 0.1)
rr41 = Label(frame49, text=" STUDENT ID :", font=("Quiche Sans", 12))
rr41.place(relx=0.2,rely=0.2)
rr410 = Entry(frame49)
rr410.place(relx=0.4,rely=0.2)
rr42 = Label(frame49, text="MATHS 2 :", font=("Quiche Sans", 12))
rr42.place(relx=0.2,rely=0.3)
rr420 = Entry(frame49)
rr420.place(relx=0.4,rely=0.3)
rr43 = Label(frame49, text="ENGLISHLITERATURE :", font=("Quiche Sans", 10))
rr43.place(relx=0.2,rely=0.4)
rr430 = Entry(frame49)
rr430.place(relx=0.4,rely=0.4)
rr44 = Label(frame49, text="HISTORY:", font=("Quiche Sans", 12))
rr44.place(relx=0.2,rely=0.5)
rr440 = Entry(frame49)
rr440.place(relx=0.4,rely=0.5)
rr45 = Label(frame49, text="AVERAGE GRADE:", font=("Quiche Sans", 12))
rr45.place(relx=0.2,rely=0.6)
rr450 = Entry(frame49)
rr450.place(relx=0.4,rely=0.6)

b1=Button(frame4, text="STUDENT", font=("Quiche Sans", 12), command=lambda: frame_changer(frame41)).place(relx=0.1,rely=0.2)
b2=Button(frame4, text="TEACHER", font=("Quiche Sans", 12), command=lambda:frame_changer(frame42)).place(relx=0.3,rely=0.2)
b3=Button(frame4, text="COURSE", font=("Quiche Sans", 12), command=lambda:frame_changer(frame43)).place(relx=0.5,rely=0.2)
b4=Button(frame4, text="ENROLL COURSE", font=("Quiche Sans", 12), command=lambda:frame_changer(frame44)).place(relx=0.7,rely=0.2)
b5=Button(frame4, text="ACTIVITY", font=("Quiche Sans", 12), command=lambda:frame_changer(frame45)).place(relx=0.1,rely=0.4)
b6=Button(frame4, text="ENROLL ACTIVITY", font=("Quiche Sans", 12), command=lambda:frame_changer(frame46)).place(relx=0.3,rely=0.4)
b7=Button(frame4, text=" ADD CLASS", font=("Quiche Sans", 12), command=lambda:frame_changer(frame47)).place(relx=0.5,rely=0.4)
b8=Button(frame4, text="ADD RESULT SEM1", font=("Quiche Sans", 12), command=lambda:frame_changer(frame48)).place(relx=0.7,rely=0.4)
b9=Button(frame4, text="ADD RESULT SEM2", font=("Quiche Sans", 12), command=lambda:frame_changer(frame49)).place(relx=0.5,rely=0.6,anchor="center")

label22 = Label(frame5, text="CHOOSE THE FUNCTIONS ABOVE!", font=("Quiche Sans", 18))
label22.place(relx=0.4,rely=0.9)

#search in student
label51 = Label(frame51, text="NAME :", font=("Quiche Sans", 12))
label51.place(relx=0.25,rely=0.3)
label510 = Entry(frame51)
label510.place(relx=0.65,rely=0.3)
t1=Text(frame51,height=30,width=150)
t1.place(relx=0.10,rely=0.5)

#search in teacher
l51 = Label(frame52, text="NAME :", font=("Quiche Sans", 12))
l51.place(relx=0.25,rely=0.3)
l510 = Entry(frame52)
l510.place(relx=0.65,rely=0.3)
t2=Text(frame52,height=30,width=150)
t2.place(relx=0.10,rely=0.5)

#search grade
la51 = Label(frame53, text="STUDENT NAME :", font=("Quiche Sans", 12))
la51.place(relx=0.25,rely=0.3)
la510 = Entry(frame53)
la510.place(relx=0.65,rely=0.3)
t4=Text(frame53,height=30,width=150)
t4.place(relx=0.10,rely=0.5)

#search enroll activity
lab51 = Label(frame54, text="STUDENT NAME :", font=("Quiche Sans", 12))
lab51.place(relx=0.25,rely=0.3)
lab510 = Entry(frame54)
lab510.place(relx=0.65,rely=0.3)
t5=Text(frame54,height=30,width=150)
t5.place(relx=0.10,rely=0.5)

#SEARCH ACHIEVIEMENT
labe51 = Label(frame55, text="ACTIVITY NAME :", font=("Quiche Sans", 12))
labe51.place(relx=0.25,rely=0.3)
labe510 = Entry(frame55)
labe510.place(relx=0.65,rely=0.3)
t6=Text(frame55,height=30,width=150)
t6.place(relx=0.10,rely=0.5)

#search class handle 
x51 = Label(frame56, text="TEACHER NAME :", font=("Quiche Sans", 12))
x51.place(relx=0.25,rely=0.3)
x510 = Entry(frame56)
x510.place(relx=0.65,rely=0.3)
t7=Text(frame56,height=30,width=150)
t7.place(relx=0.10,rely=0.5)

#search resut sem1
y51 = Label(frame57, text="STUDENT NAME :", font=("Quiche Sans", 12))
y51.place(relx=0.25,rely=0.3)
y510 = Entry(frame57)
y510.place(relx=0.65,rely=0.3)
t8=Text(frame57,height=30,width=150)
t8.place(relx=0.10,rely=0.5)

#search resut sem2
z51 = Label(frame58, text="STUDENT NAME :", font=("Quiche Sans", 12))
z51.place(relx=0.25,rely=0.3)
z510 = Entry(frame58)
z510.place(relx=0.65,rely=0.3)
t9=Text(frame58,height=30,width=150)
t9.place(relx=0.10,rely=0.5)


b11=Button(frame5, text="STUDENT", font=("Quiche Sans", 12), command=lambda: frame_changer(frame51)).place(relx=0.1,rely=0.2)
b21=Button(frame5, text="TEACHER", font=("Quiche Sans", 12), command=lambda:frame_changer(frame52)).place(relx=0.3,rely=0.2)
b31=Button(frame5, text="GRADE", font=("Quiche Sans", 12), command=lambda:frame_changer(frame53)).place(relx=0.5,rely=0.2)
b41=Button(frame5, text="ACTIVITY", font=("Quiche Sans", 12), command=lambda:frame_changer(frame54)).place(relx=0.7,rely=0.2)
b51=Button(frame5, text="ACHIEVEMENT", font=("Quiche Sans", 12), command=lambda:frame_changer(frame55)).place(relx=0.1,rely=0.4)
b61=Button(frame5, text="CLASS HANDLED", font=("Quiche Sans", 12), command=lambda:frame_changer(frame56)).place(relx=0.3,rely=0.4)
b71=Button(frame5, text=" SEM 1 RESULT", font=("Quiche Sans", 12), command=lambda:frame_changer(frame57)).place(relx=0.5,rely=0.4)
b81=Button(frame5, text="SEM 2 RESULT", font=("Quiche Sans", 12), command=lambda:frame_changer(frame58)).place(relx=0.7,rely=0.4)

label23 = Label(frame6, text="CHOOSE THE FUNCTIONS ABOVE!", font=("Quiche Sans", 18))
label23.place(relx=0.4,rely=0.9)

# remove by name
d51 = Label(frame61, text="NAME :", font=("Quiche Sans", 12))
d51.place(relx=0.3,rely=0.4)
d510 = Entry(frame61)
d510.place(relx=0.6,rely=0.4,height=25)


# remove by name
f51 = Label(frame62, text="NAME :", font=("Quiche Sans", 12))
f51.place(relx=0.3,rely=0.4)
f510 = Entry(frame62)
f510.place(relx=0.6,rely=0.4,height=25)

# remove course
h51 = Label(frame63, text="NAME :", font=("Quiche Sans", 12))
h51.place(relx=0.3,rely=0.4)
h510 = Entry(frame63)
h510.place(relx=0.6,rely=0.4,height=25)

# disenroll
j51 = Label(frame64, text="STUDENT ID :", font=("Quiche Sans", 12))
j51.place(relx=0.3,rely=0.3)
j510 = Entry(frame64)
j510.place(relx=0.6,rely=0.3,height=25)
k51 = Label(frame64, text="COURSE ID :", font=("Quiche Sans", 12))
k51.place(relx=0.3,rely=0.4)
k510 = Entry(frame64)
k510.place(relx=0.6,rely=0.4,height=25)

# delete activity
m51 = Label(frame65, text="NAME :", font=("Quiche Sans", 12))
m51.place(relx=0.3,rely=0.4)
m510 = Entry(frame65)
m510.place(relx=0.6,rely=0.4,height=25)

# remove class
n51 = Label(frame66, text="NAME :", font=("Quiche Sans", 12))
n51.place(relx=0.3,rely=0.4)
n510 = Entry(frame66)
n510.place(relx=0.6,rely=0.4,height=25)

# remove sem1 result
o51 = Label(frame67, text="STUDENT ID :", font=("Quiche Sans", 12))
o51.place(relx=0.3,rely=0.4)
o510 = Entry(frame67)
o510.place(relx=0.6,rely=0.4,height=25)

# remove sem2 result
p51 = Label(frame68, text="STUDENT ID :", font=("Quiche Sans", 12))
p51.place(relx=0.3,rely=0.4)
p510 = Entry(frame68)
p510.place(relx=0.6,rely=0.4,height=25)


b12=Button(frame6, text=" REMOVE STUDENT", font=("Quiche Sans", 10), command=lambda: frame_changer(frame61)).place(relx=0.1,rely=0.2)
b22=Button(frame6, text="REMOVE TEACHER", font=("Quiche Sans", 10), command=lambda:frame_changer(frame62)).place(relx=0.3,rely=0.2)
b32=Button(frame6, text="DELETE COURSE", font=("Quiche Sans", 10), command=lambda:frame_changer(frame63)).place(relx=0.5,rely=0.2)
b42=Button(frame6, text="DISENROLL", font=("Quiche Sans", 10), command=lambda:frame_changer(frame64)).place(relx=0.7,rely=0.2)
b52=Button(frame6, text="DELETE ACTIVITY", font=("Quiche Sans", 10), command=lambda:frame_changer(frame65)).place(relx=0.1,rely=0.4)
b62=Button(frame6, text="REMOVE CLASS", font=("Quiche Sans", 10), command=lambda:frame_changer(frame66)).place(relx=0.3,rely=0.4)
b72=Button(frame6, text=" REMOVE SEM1", font=("Quiche Sans", 10), command=lambda:frame_changer(frame67)).place(relx=0.5,rely=0.4)
b82=Button(frame6, text="REMOVE SEM2", font=("Quiche Sans", 10), command=lambda:frame_changer(frame68)).place(relx=0.7,rely=0.4)


back_button = Button(frame2, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame1))
back_button.place(relx=0.50,rely=0.100)
back_button1 = Button(frame3, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame2))
back_button1.place(relx=0.5,rely=0.100)  # Adjusted row and column values
back_button2= Button(frame4, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame2))
back_button2.place(relx=0.5,rely=0.100 , anchor="center")
back_button3 = Button(frame41, text="SUBMIT", font=("Quiche Sans", 12), command=lambda: submit1())
back_button3.place(relx=0.7,rely=0.50, anchor="center")
back_button4 = Button(frame41, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button4.place(relx=0.7,rely=0.60, anchor="center")
back_button5 = Button(frame42, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit2())
back_button5.place(relx=0.7,rely=0.50, anchor="center")
back_button6 = Button(frame42, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button6.place(relx=0.7,rely=0.60, anchor="center")
back_button7 = Button(frame43, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit3())
back_button7.place(relx=0.5,rely=0.5, anchor="center")
back_button8 = Button(frame43, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button8.place(relx=0.5,rely=0.6, anchor="center")
back_button9 = Button(frame44, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit4())
back_button9.place(relx=0.5,rely=0.5, anchor="center")
back_button11 = Button(frame44, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button11.place(relx=0.5,rely=0.6, anchor="center")
back_button12 = Button(frame45, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit5())
back_button12.place(relx=0.5,rely=0.5, anchor="center")
back_button13 = Button(frame45, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button13.place(relx=0.5,rely=0.6, anchor="center")
back_button14 = Button(frame46, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit6())
back_button14.place(relx=0.5,rely=0.5, anchor="center")
back_button15 = Button(frame46, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button15.place(relx=0.5,rely=0.6, anchor="center")
back_button16 = Button(frame47, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit7())
back_button16.place(relx=0.5,rely=0.5, anchor="center")
back_button17 = Button(frame47, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button17.place(relx=0.5,rely=0.6, anchor="center")
back_button18 = Button(frame48, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit8())
back_button18.place(relx=0.7,rely=0.4, anchor="center")
back_button19 = Button(frame48, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button19.place(relx=0.7,rely=0.5, anchor="center")
back_button21 = Button(frame49, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit9())
back_button21.place(relx=0.7,rely=0.4, anchor="center")
back_button22 = Button(frame49, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame4))
back_button22.place(relx=0.7,rely=0.5, anchor="center")
back_button23= Button(frame5, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame2))
back_button23.place(relx=0.5,rely=0.1, anchor="center")
back_button24= Button(frame51, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit10())
back_button24.place(relx=0.3,rely=0.4, anchor="center")
back_button25 = Button(frame51, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button25.place(relx=0.7,rely=0.4, anchor="center")
back_button26 = Button(frame52, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit11())
back_button26.place(relx=0.3,rely=0.4, anchor="center")
back_button27 = Button(frame52, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button27.place(relx=0.7,rely=0.4, anchor="center")
back_button28 = Button(frame53, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit12())
back_button28.place(relx=0.3,rely=0.4, anchor="center")
back_button29 = Button(frame53, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button29.place(relx=0.7,rely=0.4, anchor="center")
back_button30 = Button(frame54, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit13())
back_button30.place(relx=0.3,rely=0.4, anchor="center")
back_button31 = Button(frame54, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button31.place(relx=0.7,rely=0.4, anchor="center")
back_button32 = Button(frame55, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit14())
back_button32.place(relx=0.3,rely=0.4, anchor="center")
back_button33 = Button(frame55, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button33.place(relx=0.7,rely=0.4, anchor="center")
back_button34 = Button(frame56, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit15())
back_button34.place(relx=0.3,rely=0.4, anchor="center")
back_button35 = Button(frame56, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button35.place(relx=0.7,rely=0.4, anchor="center")
back_button36 = Button(frame57, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit16())
back_button36.place(relx=0.3,rely=0.4, anchor="center")
back_button37= Button(frame57, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button37.place(relx=0.7,rely=0.4, anchor="center")
back_button38 = Button(frame58, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit17())
back_button38.place(relx=0.3,rely=0.4, anchor="center")
back_button39 = Button(frame58, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame5))
back_button39.place(relx=0.7,rely=0.4, anchor="center")
back_button40= Button(frame6, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame2))
back_button40.place(relx=0.5,rely=0.1, anchor="center")
back_button41 = Button(frame61, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit18())
back_button41.place(relx=0.35,rely=0.5, anchor="center")
back_button42 = Button(frame61, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button42.place(relx=0.65,rely=0.5, anchor="center")
back_button43 = Button(frame62, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit19())
back_button43.place(relx=0.35,rely=0.5, anchor="center")
back_button44 = Button(frame62, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button44.place(relx=0.65,rely=0.5, anchor="center")
back_button45 = Button(frame63, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit20())
back_button45.place(relx=0.35,rely=0.5, anchor="center")
back_button46 = Button(frame63, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button46.place(relx=0.65,rely=0.5, anchor="center")
back_button47 = Button(frame64, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit21())
back_button47.place(relx=0.35,rely=0.5, anchor="center")
back_button48 = Button(frame64, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button48.place(relx=0.65,rely=0.5, anchor="center")
back_button49 = Button(frame65, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit22())
back_button49.place(relx=0.35,rely=0.5, anchor="center")
back_button50 = Button(frame65, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button50.place(relx=0.65,rely=0.5, anchor="center")
back_button51 = Button(frame66, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit23())
back_button51.place(relx=0.35,rely=0.5, anchor="center")
back_button52 = Button(frame66, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button52.place(relx=0.65,rely=0.5, anchor="center")
back_button53 = Button(frame67, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit24())
back_button53.place(relx=0.35,rely=0.5, anchor="center")
back_button54 = Button(frame67, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button54.place(relx=0.65,rely=0.5, anchor="center")
back_button55 = Button(frame68, text="SUBMIT", font=("Quiche Sans", 12), command=lambda:submit25())
back_button55.place(relx=0.35,rely=0.5, anchor="center")
back_button56 = Button(frame68, text="Back", font=("Quiche Sans", 12), command=lambda: frame_changer(frame6))
back_button56.place(relx=0.65,rely=0.5, anchor="center")
# Initially, show the first frame
frame1.tkraise()

window.mainloop()
