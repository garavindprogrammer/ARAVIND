import sqlite3 as sql
con=sql.connect('database1.sqlite3')
max=con.execute(''' select max(salary) from employee2 ''')
min=con.execute(''' select min(salary) from employee2 ''')
sum=con.execute(''' select sum(salary) from employee2 ''')
avg=con.execute(''' select avg(salary) from employee2 ''')
con.commit()
print('maximum salary')
for i in max:
    print(i)
print('minimum salary')
for i in min:
    print(i)
print('sum of  salary')
for i in sum:
    print(i[0])
print('average salary')
for i in avg:
    print(i[0])    
