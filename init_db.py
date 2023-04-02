import sqlite3

#create connection to database
conn = sqlite3.connect('travel_database.db')


#create cursor object
cursor = conn.cursor()


#create  a table for storing credential 

table_create_query = """ 
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
"""
#Insert user data 

# user_data = [
#     ('arth','doshi'),
#     ('admin','password')
# ]


cursor.execute(table_create_query)
cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",('admin','password'))


#commit
conn.commit()
conn.close()