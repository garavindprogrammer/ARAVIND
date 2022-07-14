import sqlite3 as sql
con=sql.connect('database3.sqlite3')
query2=con.execute(''' select avg(salary) from employee3 group by department_id having count(*)>=10 ''')
con.commit()
for i in query2:
    print(i)
