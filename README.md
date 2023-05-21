# Python_Git_Jenkins_CourseProject

**Release date: 21/05/2023**

**This project written in:**

python language

Groovy language for pipeline scripts

**It combined the following files:**

db_connector.py - This file connect to a remote MySql and implements a couple of methods (INSERT,SELECT,UPDATE,DELETE)

rest_app.py - This file defines routes with rest api for create, read, update, and delete user from/to the remote MySQL.
he start a flask server (localhost)

web_app.py - This file defines route that returns the userName from the remote MySQL DB by the given user id and show him in a user_data html template using render_template.
if the get_user_data didn't find the user according the given user id it will show an error in a user_error html template.
he start a flask server (localhost)

backend_testing.py - testing rest_app.py file

fronted_testing.py - testing web_app.py file using selenium

combined_testing.py - testing both rest_app.py file / web_app.py file as a single execution

clean_environment.py - This file stop flask servers (localhost) from rest_app.py and web_app.py files
it protected with error handling in case servers are not responding

templates - contains 3 html files for render_template in rest_app.py and web_app.py files

jenkinsfile - A jenkins pipeline script (in groovy) which connect to git repository and execute the above python files

jenkinsfileExtra - Do what jenkinsfile does with extra features such:
1. Send an email when failure occurred
2. add parameter to the pipline which will cause a specific test to run
3. add route error handler for non-existing routes - return page not found 404
