import sqlite3 as sql
con=sql.connect('database1.sqlite3')
con.execute(''' create table employee3(employee_id int,first_name varchar2(255),last_name varchar2(255),email varchar2(255),job_id int,salary int,commission_pct int,manager_id int,department_id varchar2(255))''')
con.execute(''' insert into employee3 values(476,'nani','don','donnani@gmail.com',8214364588,40000,76,56,'csea')''')
con.execute(''' insert into employee3 values(487,'raja','shaik','rajashaik213@gmail.com',9144158756,3000,78,300,'csea')''')
con.execute(''' insert into employee3 values(812,'vamsi','kondeti','vamsikondeti12@gmail.com',9246418769,120000,59,120,'csec')''')
con.execute(''' insert into employee3 values(817,'nasreen','parveen','nasreenparveen1@gmail.com',9246814310,12985,45,12,'cseb')''')
con.commit()
query1=con.execute(''' select * from employee3 ''')
for i in query1:
    print(i)
