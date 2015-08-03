'''
Program created to learn sqlite3 
'''
import sqlite3

class Database:
	
	def __init__(self):
		self.conn = sqlite3.connect('UserInfo.db')
		self.cur  = self.conn.cursor()
		print("success")
	
	def createTable(self):
		table_exists = 'SELECT name FROM sqlite_master WHERE type="table" AND name="USERS"'
		sql = 'CREATE TABLE USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, CITY TEXT NOT NULL)'
		if not self.cur.execute(table_exists).fetchone():
			self.cur.execute(sql)
			self.conn.commit()
		
	def insertRecord(self, name, city):
		sql = 'INSERT INTO USERS (NAME, CITY) VALUES (?,?)'
		self.cur.execute(sql,(name, city))
		self.conn.commit()
	
	def getRecord(self):
		sql = 'SELECT * FROM USERS'
		for row in self.cur.execute(sql):
			print (row)
		self.conn.commit()
	
	def updateRecord(self, name, id):
		sql = 'UPDATE USERS SET NAME = ? WHERE ID = ?'
		self.cur.execute(sql,(name, id))
		self.conn.commit()
	
''' The SQLite ALTER TABLE statement is used to add, modify, or drop/delete columns in a table. 
    Also used to rename a table. Doesn't support AUTOINCREMENT'''	
	def deleteRecord(self, name):
		sql          = 'DELETE FROM USERS WHERE NAME = ?'
	#	sqlGetlMaxId = 'SELECT MAX(ID) FROM USERS'
	#	sqlResetId   = 'ALTER TABLE USERS AUTOINCREMENT = ?'
		self.cur.execute(sql, (name,))
	#	for maxId in self.cur.execute(sqlGetlMaxId):
	#		self.cur.execute(sqlResetId, (maxId[0],))
		self.conn.commit()
	
	def connClose(self):
		conn.close()
	
database = Database()
database.createTable()
database.insertRecord("Nirali", "NY")
database.getRecord()
database.updateRecord("KP", 2)
database.deleteRecord("Nirali")
database.connClose()