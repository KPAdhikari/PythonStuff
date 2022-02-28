export FLASK_APP=project
export FLASK_DEBUG=1



The FLASK_APP environment variable instructs Flask on how to load the app. You would want this to point to where create_app is located. For this tutorial, you will be pointing to the project directory.

The FLASK_DEBUG environment variable is enabled by setting it to 1. This will enable a debugger that will display application errors in the browser.

Ensure that you are in the flask_auth_app directory and then run the project:

flask run
Now, in a web browser, you can navigate to the five possible URLs and see the text returned that was defined in auth.py and main.py.

For example, visiting localhost:5000/profile displays: Profile.
