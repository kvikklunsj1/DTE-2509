from flask import Flask, render_template
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'kark.uit.no'
app.config['MYSQL_USER'] = 'stud_v23_mki061'
app.config['MYSQL_PASSWORD'] = 'kaffekobberhaug'
app.config['MYSQL_DB'] = 'stud_v23_mki061'

mysql = MySQL(app)




@app.route('/')
def Home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM python")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('index.html', data = fetchdata)


if __name__ == "__main__":
    app.run(debug=True)