import  sqlite3#import this to create database
conn = sqlite3.connect('password.sqlite')#creating a databasename
cur = conn.cursor()
try:
    cur.execute('CREATE TABLE pass (user VARCHAR,  pass VARCHAR, web VARCHAR)')#creates a table with columns
except:
    print("")
conn.commit()
conn.close()
