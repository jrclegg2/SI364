from flask import Flask, request
import requests
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Task 2
# Write a return statement such that it displays 'Welcome to <course_name>'
# when you navigate to localhost:5000/course/<course_name>
# Remember to get rid of the pass statement
@app.route('/course/<course>')
def course(course):
   return 'Welcome to {}'.format(course)

# Task 3.1
# Edit the HTML form such that form data is sent to localhost:5000/result using POST method
@app.route('/form', methods = ['POST', 'GET'])
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<form method = "POST" action = "http://localhost:5000/result">
  INGREDIENT:<br>
  <input type="text" name="ingredient" value="eggs">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
# changed form tag to include method and action to send result to

# Note that by default eggs would be entered in the input field
    return s


## Task 3.2
## Modify the function code and return statement
## to display recipes for the ingredient entered
@app.route('/result',methods = ['POST', 'GET']) # get would add arguments into URL after / with ?= and such
def displayData():
  # use request.args when method is "GET" and use request.form when method is "POST"
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        requestURL = "http://www.recipepuppy.com/api"
        text = requests.get(requestURL, params = {'i' : ingredient}).text.encode('utf-8')
        return text


## Task 4
## Note : Since this is a dyanmic URL, recipes function should recieve a paramter called `ingrdient`
@app.route('/recipe/<ingredient>')
def recipes():
    pass

if __name__ == '__main__':
    app.run()
