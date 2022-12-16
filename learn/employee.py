# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
class employee():
    """class describe employees in some company"""
    def __init__(self, username, name, passport, post, department, salary, office, email, date_employeed):
        self.username = username
        self.name = name
        self.passport = passport
        self.post = post
        self.department = department
        self.salary = salary
        self.office = office
        self.tel = []
        self.email = email
        self.date_employeed = date_employeed
    def show_employee_short(self):
        """show all parameters of employee"""
        print(f"Internal systems ID: {self.username}, Full name: {self.name}, Passport N: {str(self.passport)}, working as: {self.post} at dept: {self.department}, email: {self.email}, got salary: {str(self.salary)}. Can be called by {self.tel}")
    def index_salary(self, index_percent):
        """index salary yearly"""
        self.salary = self.salary + (self.salary*index_percent/100)
        print(f"Employee {self.username}, {self.name} got new salary {str(self.salary)}")
    def new_post(self, newpost):
        self.post = newpost
        print(f"Employee {self.username}, {self.name} got new post: {self.post}")
    def add_tel(self, newtel):
        self.tel.append(newtel)
        print(f"Employee {self.username}, {self.name} got new tel: {self.tel}")