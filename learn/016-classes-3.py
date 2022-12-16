# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
from employee import *
# (self, username, name, passport, post, department, salary, office, email, date_employeed)
employee1 = employee("vasiliev.vv", "Vasiliev V.V.", 123456789, "CTO", "Administration", 1500, "2-5", "vasiliev.vv@somedomain.com", "22-12-2021")

employee1.show_employee_short()
employee1.index_salary(8)
employee1.new_post("CIO")
employee1.add_tel("555-55-55")
employee1.add_tel("666-66-66")
