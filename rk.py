import sqlite3 as sql
con = sql.connect('kalyan')
cur = con.cursor()
q = 'select * from items where item_id = ?'
itemid = int(input('enter any itemid'))
t1 = (itemid,)
cur.execute(q,t1)
data = cur.fetchall()
if itemid == data:
    print("data available")
for i in data:
    for j in i:
        print(j,end="")
    print()
    cost = data[0][2]
    print(cost)
    q1 = int(input('enter a quality'))
    if q1>=1 and q1<=10:
        print(cost)
        bill = cost*q1
        print(bill)
    break
else:
    print('invalid item')
cur.close()