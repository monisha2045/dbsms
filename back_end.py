import cx_Oracle


connection = cx_Oracle.connect(user='system', password='monisha', dsn="localhost:1521/orcl")
cur=connection.cursor()

# def display_students():
    
#     sql_query = "select * from students"
#     cur.execute(sql_query)
#     values = cur.fetchall()
#     for value in values:
#          print(value)

   
        
'''def display_teachers(cur):
    sql="select * from teachers"
    cur.execute(sql)

    values = cur.fetchall()
    for value in values:
        yield value  '''
        
# def search_student(name) :
#     cur.execute("select * from students where name=:var",var=name)
#     for i in cur:
#         yield i
    
# def search_teacher(name):
#     cur.execute("select * from teachers where name = :var",var=name)
#     for i in cur:
#        yield i
    
# def add_student(id_1,name,date,age,address,phone,gender,year):
    
#     cur.execute("INSERT INTO students VALUES (:v8, :v7, TO_DATE(:v6, 'YYYY-MM-DD'), :v5, :v4, :v3, :v2, :v1)",
#             {"v8": id_1, "v7": name, "v6": date, "v5": age, "v4": address, "v3": phone, "v2": gender, "v1": year})

#     connection.commit()
    
# def delete_student(name):
#     cur.execute("delete from students where name = :var",var=name)
#     connection.commit()
    
# def add_teacher(id1,name,quality,phone,gender):
#     cur.execute("insert into teachers values (:v1,:v2,:v3,:v4,:v5)",
#                 {"v1":id1,"v2":name,"v3":quality,"v4":phone,"v5":gender})
#     connection.commit()
    
# def delete_teacher(name):
#     cur.execute("delete from teachers where name = :var",var=name)
#     connection.commit()
    
# def add_course(id1,name,credit):
#     cur.execute("insert into courses values (:v1,:v2,:v3)",
#                 {"v1":id1,"v2":name,"v3":credit})
#     connection.commit()
    
# def display_courses():
#     cur.execute("select * from courses")
#     for i in cur :
#        yield i
        
# def delete_course(name):
#     cur.execute("delete from courses where course_name = :var",var = name)
#     connection.commit()
    
# def enroll_course(e_id1,st_id2,c_id3):
#     cur.execute("insert into enrollments values (:v1,:v2,:v3)",
#                 {"v1":e_id1,"v2":st_id2,"v3":c_id3})
#     connection.commit()
    
# def disenroll_course(st_id1,c_id2):
#     cur.execute("delete from enrollments where student_id = :var1 and course_id = :var2",
#                 {"var1" : st_id1,"var2":c_id2})
#     connection.commit()
    
# def display_grade_chart():
#     cur.execute("select s.name ,c.course_name ,g.grade from grades g join enrollments e on e.enrollment_id = g.enrollment_id join courses c on c.course_id = e.course_id join students s on s.digital_id = e.student_id ")
#     for i in cur :
#         yield i
        
# def search_grade(name):
#     cur.execute("SELECT g.grade , c.course_name FROM grades g JOIN enrollments e ON e.enrollment_id = g.enrollment_id JOIN courses c ON c.course_id = e.course_id JOIN students s ON s.digital_id = e.student_id WHERE s.name = :var " ,var = name)
#     for i in cur:
#         yield i
        
# def add_activity(id1,name,describe):
#     cur.execute("insert into extracurricularactivities values (:v1,:v2,:v3)",
#                 {"v1":id1,"v2":name,"v3":describe})
#     connection.commit()
    
# def display_activities():
#     cur.execute("select * from extracurricularactivities")
#     for i in cur :
#         yield i
        
# def delete_activity(name):
#     cur.execute("delete from extracurricularactivities where activity_name = :var",var = name)
#     connection.commit()
    
# def enroll_activity(ac_id1,st_id2):
#     cur.execute("insert into studentactivities values( :v1 ,:v2)",
#                 {"v1":ac_id1,"v2":st_id2})
#     connection.commit()
    
# def display_studentactivities():
#     cur.execute("select s.name , e.activity_name from studentactivities sa join students s on s.digital_id = sa.student_id join extracurricularactivities e on e.activity_id = sa.activity_id")
#     for i in cur:
#         yield i
        
# def find_enroll_activity(name):
#     cur.execute("select e.activity_name from studentactivities sa join students s on s.digital_id = sa.student_id join extracurricularactivities e on e.activity_id = sa.activity_id where s.name = :var",var = name)
#     for i in cur:
#         yield i
        
# def display_all_achievements():
#     cur.execute("select e.activity_name , a.achievement_description from activityachievements a join extracurricularactivities e on e.activity_id = a.activity_id")
#     for i in cur:
#         yield i

# def achievement(activity):
#     cur.execute("select a.achievement_description from activityachievements a join extracurricularactivities e on e.activity_id = a.activity_id where e.activity_name = :var",var= activity)
#     for i in cur:
#         yield i

# def show_classes():
#     cur.execute("select t.name , t.qualification , t.phone ,c.class_name from classes c natural join teachers t ")
#     for i in cur:
#         yield i

# def add_class(id1,name,t_id):
#     cur.execute("insert into classes values (:v1,:v2,:v3)",
#                 {"v1":id1,"v2":name,"v3":t_id})
#     connection.commit()
    
# def remove_class(name):
#     cur.execute("delete from classes where class_name = :var",var=name)
#     connection.commit()
    
        
# def class_handled(name):
#     cur.execute("select c.class_name from classes c join teachers t on t.teacher_id = c.teacher_id where t.name = :var",var = name)
#     for i in cur:
#         yield i
        
# def sem1_results():
#     cur.execute("select s.name , sem1.Mathematics1 ,sem1.Physics,sem1.ComputerScience  from sem1 natural join students s")
#     for i in cur:
#         yield i
        
# def insert_sem1(id1,maths,phy,cs,avg):
#     cur.execute("insert into sem1 values(:v1,:v2,:v3,:v4,:v5)",
#                 {"v1":id1,"v2":maths,"v3":phy,"v4":cs,"v5":avg})
#     connection.commit()

# def remove_result1(id1):
#     cur.execute("delete from sem1 where digital_id = :var",var=id1)
#     connection.commit()
    
        
# def result_sem1(name):
#     cur.execute("select sem1.Mathematics1,sem1.Physics,sem1.ComputerScience from sem1 natural join students where students.name = :var",var = name)
#     for i in cur:
#         yield i
        
# def sem2_results():
#     cur.execute("select s.name , sem2.Mathematics2 ,sem2.EnglishLiterature,sem2.History from sem2 natural join students s")
#     for i in cur:
#         yield i
        
# def insert_sem2(id1,maths,el,his,avg):
#     cur.execute("insert into sem2 values(:v1,:v2,:v3,:v4,:v5)",
#                 {"v1":id1,"v2":maths,"v3":el,"v4":his,"v5":avg})
#     connection.commit()

# def remove_result2(id1):
#     cur.execute("delete from sem2 where digital_id = :var",var=id1)
#     connection.commit()    

# def result_sem2(name):
#     cur.execute("select sem2.Mathematics2,sem2.EnglishLiterature,sem2.History from sem2 natural join students where students.name = :var",var = name)
#     for i in cur:
#         yield i
        

        


#search_student("Jhon Doe")
#add_student(8,"ragav","2005-04-20",19,"45 big road",123000,"Female",2026) 
# delete_student("ragav")
# display_students()
#add_teacher("6","Moni","Phd in ai",1098765,"Female")
#delete_teacher("Moni")
#display_teachers()
#add_course(7,"science",3)
#delete_course("science")
#enroll_course(6,4,1)
#disenroll_course(4,1)
#display_grade_chart()
#search_grade('Jane Smith')
#display_courses()
#add_activity(6,"disco","a rt of die")
#delete_activity("disco")
#display_activities()
#search_teacher("Dr. Smith")
#display_studentactivities()
#find_enroll_activity("Charlie Davis")
#display_all_achievements()
#achievement("Science Club")
#class_handled("Mr. Johnson")
#add_class(6,"moni",5)
#remove_class("moni")
#show_classes()
#result_sem1("John Doe")
#result_sem2("John Doe")
#insert_sem2(6,"A","A+","B","A+")
#remove_result2(6)
#sem2_results()
cur.close()
connection.close()    