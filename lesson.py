import sqlite3

conn= sqlite3.connect("datt.db")
curs=conn.cursor()
zap1="""CREATE TABLE IF NOT EXISTS USER (FullName TEXT, Degree TEXT, ScientificDirection TEXT, PlaceOfWork TEXT, Department TEXT, Position TEXT, Country TEXT, City TEXT, Address TEXT, WorkPhoneNumber TEXT, EMail TEXT, Type TEXT, Date1 TEXT,
 Date2 TEXT, Theme TEXT, Mark TEXT, Date3 TEXT, Hotel TEXT, Date4 TEXT, ConfName TEXT, Date TEXT, Place TEXT, Org TEXT, Spons 
 TEXT,Days INT, PartAmount INT, LectAmount INT);"""
curs.execute(zap1)
conn.commit()
tuple123 = ("Hazel Walsh", "Magister", "Scientist", "University","AAA", "BBB",
  "Germany", "Munich", "Street C", "+123456789", "FFF@mail.ru", "Lecturer", "21.01.2012", "23.01.2012", "Economy",
  "No", "15.05.2013", "No", "21.05.2013", "ABC", "12.01.78", "Paris", "F.n.L.", "Namess", 6, 15, 100)
s1 = """INSERT INTO USER values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
print(s1)
curs.execute(s1, tuple123)

conn.commit()
curs.close()
conn.close()