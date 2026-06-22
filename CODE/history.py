import sqlite3
from datetime import datetime
mycon=sqlite3.connect('history.db')
mycur=mycon.cursor()
def create_database():
    mycur.execute("CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY AUTOINCREMENT , expression TEXT, result TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
    mycon.commit()
def history_add(expression,result):
    timestamp=datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    mycur.execute("INSERT INTO history(expression,result,timestamp) VALUES(?,?,?)", (expression, result, timestamp))
    mycon.commit()
def history_show(n):
    mycur.execute("SELECT * FROM history")
    data=mycur.fetchall()
    if n==0:
        if len(data)==0:
                print("no history found")
        else:
            for i in data:
                print("cal=",i[1],"=",i[2],"time=",i[3])
    elif n>len(data):
        print("not enough history found, showing all history")
        for i in data:
            print("cal=",i[1],"=",i[2],"time=",i[3])
    elif n<0:
        print("invalid input, negative number")
    else:
        for i in data[-n:]:
            print("cal=",i[1],"=",i[2],"time=",i[3])
def history_clear():
    mycur.execute('DELETE FROM history')
    mycon.commit()