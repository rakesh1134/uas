from genericpath import exists
from operator import truediv
import sqlite3

class userdb:
    db_name = "users.db"
    def __init__(self):
        self.dbpath = ""
        self.conn = None
    
    def connect(self):
        dbexists = False
        if exists(self.db_name):
            dbexists = True

        usrs = {}
        if dbexists:

            self.conn = sqlite3.connect(self.db_name)
            cur = self.conn.cursor()
            for row in cur.execute('SELECT * FROM users'):
                usrs[row[0]]  = row[1]
            cur.close()
        else:
            self.conn = sqlite3.connect(self.db_name)
            cur = self.conn.cursor()
            cur.execute('''CREATE TABLE users(username text, password text)''')  
            cur.close()
        return usrs

    def insert(self,uname,pw):
        cur = self.conn.cursor()
        cur.execute("insert into users (username, password) values (?, ?)",(uname, pw)) 
        self.conn.commit()
        cur.close()

    def showrecords(self):
        cur = self.conn.cursor()
        for row in cur.execute('SELECT * FROM users'):
            print(row[0],row[1])
        cur.close()

    def update(self,uname,newpassw):
        pass
    
    def close(self):
        if not self.conn is None:
            self.conn.close()
        



