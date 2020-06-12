from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route('/')
def index() :
    cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO user VALUES(%s)",['MIKE'])
    # mysql.connection.commit()
    # fruits = ['Apple', 'Banana', 'Orange']
    # return render_template('index.html',fruits=fruits)
    # return redirect(url_for('about'))
    result = cur.execute("SELECT * FROM user")
    if result>0:
        users = cur.fetchall()
        print(users)
    return render_template('index.html')

@app.route('/about')
def about() :
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug=True)