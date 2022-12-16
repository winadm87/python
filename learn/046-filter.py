# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# define email list
emails_list = [
    "aaa@bbb.cc",
    "info@domain.com",
    "some.name@domain.com",
    "info@intel.com",
    "virt@domain.com",
]
# define func to filter emails in emails list
def selected_email(emails_list):
    selected = [
        'info@domain.com',
        'virt@domain.com',
        'gmail@domain.com',
    ]
    if (emails_list in selected):
        return True
# run filter, apply func on email list
selectedlist = filter(selected_email, emails_list)
print('The selected emails are: \n')
for email in selectedlist:
    print(email)