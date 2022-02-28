from flask import Flask
#
#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
#
#First import the Flask object from the 'flask' package
#Then use that to create the Flask application instance named 'app'
#We pass the special variable '__name__' that holds the name of the
#current Python module. It's used to tell the instance where it's
#located - you need this because Flask sets up some paths behind the scenes.
#

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

#Once you create the app instance, you use it to handle incoming web requests and send responses to the user. @app.route is a decorator that turns a regular Python function into a Flask view function, which converts the function’s return value into an HTTP response to be displayed by an HTTP client, such as a web browser. You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL.
#
#The hello() view function returns the string 'Hello, World!' as a response.
#
#
#https://www.programiz.com/python-programming/decorator
# A decorator takes in a function, adds some functionality and returns it. In this tutorial, you will learn how you can create a decorator and why you should use it.
#
