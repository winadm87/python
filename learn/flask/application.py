# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
from flask import Flask
application = Flask(__name__)

# create default web page
@application.route("/")
def index():
    return "Hello world from flask main page"
# once more page
@application.route("/help")
def helppage():
    return "<b><font color=yellow>There wont be any help, do it yourself</font></b>"
# and once more
@application.route("/user")
def usermain_page():
    return "user main page"
# set variable <username> in page
@application.route("/user/<username>")
def show_user_page(username):
    # show variable on page
    return "Hello " + username
# page with complex variable that can contain slash "/"
@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "Subpath is: " + subpath
# page to calculate square of the number
@application.route("/square/<int:x>")
def calc_square(x):
    return "square from: " + str(x) + " is equal to: " + str(x*x)
# lets create page from external html file
@application.route("/page1")
def show_page1():
    index1 = open("templates/page1.html", mode="r").read()
    return index1


#----------------------main-----------
if __name__ == "__main__":
    # debug for not restart server on every change, remove this string on production
    application.debug = True
    # run application itself
    application.run()
#-------------------------------------