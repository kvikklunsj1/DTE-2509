from flask import Flask
from views import views

from flaskext.mysql import MySQL
mysql = MySQL()
#mysql.init_app(app)


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
app.config['MYSQL_HOST'] = 
 
if __name__ == '__main__':
    app.run(debug=True)
