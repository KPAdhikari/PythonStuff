import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

###########
# kp: This app is made while going through this example tutorial:
#      https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
###########
#The flash() function stores flashed messages in the client’s browser session, which requires setting a secret key. This secret key is used to secure sessions, which allow Flask to remember information from one request to another, such as moving from the new post page to the index page. The user can access the information stored in the session, but cannot modify it unless they have the secret key, so you must never allow anyone to access your secret key. See the Flask documentation for sessions for more information.

#To set a secret key, you’ll add a SECRET_KEY configuration to your application via the app.config object. Add it directly following the app definition before defining the index() view function:

# Remember that the secret key should be a long random string.
############
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

### main view function
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


#########
#Here we create a new Flask route with a view function and correspondingly we'lll add
#    a new HTML template to display an individual blog post by its ID.
# By the end of this step, the URL http://127.0.0.1:5000/1 will be a page that displays the first post (because it has the ID 1). The http://127.0.0.1:5000/ID URL will display the post with the associated ID number if it exists.
#
# Or or make Flask respond with a 404 Not Found message if the blog post does not exist.
#  To respond with a 404 page, you need to import the abort() function from the Werkzeug library, which was installed along with Flask, at the top of the file:

#In this new view function, you add a variable rule <int:post_id> to specify that the part after the slash (/) is a positive integer (marked with the int converter) that you need to access in your view function. Flask recognizes this and passes its value to the post_id keyword argument of your post() view function. You then use the get_post() function to get the blog post associated with the specified ID and store the result in the post variable, which you pass to a post.html template that you’ll soon create.
##########
### Another view function
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

#########
# After setting a secret key, you’ll create a view function that will render a template that displays a form you can fill in to create a new blog post. Add the following new function at the bottom of the file.

#This creates a /create route that accepts both GET and POST requests. GET requests are accepted by default. To also accept POST requests, which are sent by the browser when submitting forms, you’ll pass a tuple with the accepted types of requests to the methods argument of the @app.route() decorator.

# To create the template, open a file called create.html inside your templates folder.
# ....
# You’ll handle the incoming POST request when a form is submitted. You’ll do this inside the create() view function. You can separately handle the POST request by checking the value of request.method. When its value is set to 'POST' it means the request is a POST request, you’ll then proceed to extract submitted data, validate it, and insert it into your database.
#
# For that, modify the create() view function adding the 'if request.method == 'POST':' block
#########
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        
    return render_template('create.html')


#########3
# For a blog to be up to date, you’ll need to be able to edit your existing posts. 

#First, you’ll add a new route to the app.py file. Its view function will receive the ID of the post that needs to be edited, the URL will be in the format /post_id/edit with the post_id variable being the ID of the post. Open the app.py file for editing
#Next, add the following edit() view function at the end of the file. Editing an existing post is similar to creating a new one, so this view function will be similar to the create() view function:
#########

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

###########
#Sometimes a post no longer needs to be publicly available, which is why the functionality of deleting a post is crucial. In this step you will add the delete functionality to your application.

#First, you’ll add a new /ID/delete route that accepts POST requests, similar to the edit() view function. Your new delete() view function will receive the ID of the post to be deleted from the URL.

#This view function only accepts POST requests. This means that navigating to the /ID/delete route on your browser will return an error because web browsers default to GET requests.

#However you can access this route via a form that sends a POST request passing in the ID of the post you want to delete. The function will receive the ID value and use it to get the post from the database with the get_post() function.

#Note that you don’t render a template file, this is because you’ll just add a Delete button to the edit page.
###########
# ....

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
