"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .forms import add_Profile
from datetime import date


###
# Routing for your application.
###

@app.route('/home', methods = ["GET, POST"])
def home():
    """Render website's home page."""
    form = add_Profile()
    form_name = "Add Profile"
    firstname = "First Name"
    lastname = "Last Name"
    gender = "Gender"
    email = "Email"
    example_mail = "e.g. naldoreginald@example.com"
    location = "Location"
    Firstname = form.Firstname.data
    Lastname = form.Lastname.data
    Gender = form.Gender.data
    Email = form.Email.data
    Location = form.Location.data
    if request.method == "POST" and form.validate():
        flash("Successfully Completed")
    return render_template('home.html', form_name = form_name, firstname = firstname, lastname = lastname, Firstname = Firstname, Lastname = Lastname, gender =gender, email = email, loaction = location, Gender = Gender, Email = Email, Location = Location)

app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Lord Reginald")


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/profile')
def profile():
    my_name = 'Lord Reginald'
    email = 'lord_reginald@gmail.com'
    res = 'Portland, Jamaica'
    story = 'One day I hope to achieve both small and great things such as a stable financial income and to a further extent provide perfor real estate investments in order to improve Jamaica welbeing in the long run'
    Post = 'Post'
    Following = 'Following'
    Followers = 'Followers'
    Post_num = '21'
    Followers_num = '210'
    Following_num = '21'
    return render_template('profile.html', my_name = my_name, email = email, res =res, story = story, getDate = getDate(), Post_num = Post_num, Following_num = Following_num, Followers_num = Followers_num, Post = Post, Followers = Followers, Following = Following)

@app.route('/profiles')
def profiles():
    my_name = 'Lord Reginald'
    email = 'lord_reginald@gmail.com'
    res = 'Portland, Jamaica'
    story = 'One day I hope to achieve both small and great things such as a stable financial income and to a further extent provide perfor real estate investments in order to improve Jamaica welbeing in the long run'
    Post = 'Post'
    Following = 'Following'
    Followers = 'Followers'
    Post_num = '21'
    Followers_num = '210'
    Following_num = '21'
    return render_template('profile.html', my_name = my_name, email = email, res =res, story = story, getDate = getDate(), Post_num = Post_num, Following_num = Following_num, Followers_num = Followers_num, Post = Post, Followers = Followers, Following = Following)
    
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def getDate():
    today = date.today().strftime('%m/%Y')
    return today

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
