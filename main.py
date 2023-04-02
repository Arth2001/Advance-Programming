import sqlite3
from flask import Flask,g,render_template,request,redirect,url_for


app = Flask(__name__,template_folder='template')


#Define the path to the database
DATABASE = 'travel_database.db'

#define function for connecting to the database
def get_db():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


#connection the html to flask
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    
    username = request.form['username']
    password = request.form['password']
    
    
    conn = sqlite3.connect(DATABASE)
    
    
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',(username,password))
    user = cursor.fetchone()
    
    conn.close()
    
    
    
    if user is None:
        return redirect('/index.html')
    
    else:
        error = 'Invalid username or password. Please try again.'
        return render_template('login.html',error=error)
    
    
    
    
    
    
# @app.route('/')
# def test_db():
#     db = get_db()
    
#     cur = db.execute('SELECT SQLITE_VERSION()')
#     data = cur.fetchone()
    
#     return f"SQLITE VERSON : {data[0]}"

if __name__ == '__main__':
    app.run(debug=True)