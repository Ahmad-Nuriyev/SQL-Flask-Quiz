from flask import Flask


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@localhost:3306/Testing"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


from controllers import *
from models import *
from extensions import *

if __name__ == '__main__' :
    app.run(debug=True, port=8000)
