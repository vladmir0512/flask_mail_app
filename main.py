
from flask_mail import Mail, Message
from flask import Flask 


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'

mail = Mail(app)


@app.route("/")
def index():

    msg = Message("Hello",
                  sender="vjgamer2001@gmail.com",
                  recipients=["papep15405@iunicus.com"])

    mail.send(msg)
    
    return msg

if __name__ == '__main__':
    app.run(host='localhost',port=5050)
