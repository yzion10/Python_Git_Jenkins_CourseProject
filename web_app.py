# This web_app.py defines route that returns the userName
# from the MySQL DB by the given user id and show him in a
# user_data html template using render_template.
# if the get_user_data didn't find the user according the given user id
# it will show an error in a user_error html template.

from flask import Flask, render_template
from db_connector import DBConnector
import os
import signal

host='devopsdb.cu3hwstmvfmq.eu-north-1.rds.amazonaws.com'
port=3306
user='admin'
password='oren123456'
database='test'

# initialize the DBConnector class
db = DBConnector(host,port,user,password,database)

# initialize the Flask (constructor)
app = Flask(__name__)

# returns the userName from the MySQL DB by the given user id
# and show him in a html template
@app.route("/users/get_user_data/<user_id>")
def getUserData(user_id):
    username = db.getUserName(user_id)
    if username is not None:
        return render_template("user_data.html", user_name=username)
    else:
        return render_template("user_error.html", user_id=user_id)

# Stop the flask server
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

# Extra
# route error handler for non-existing routes
# return page not found 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("PageNotFount.html")

# Run the Flask application
app.run(host='127.0.0.1', debug=True, port=5001)
