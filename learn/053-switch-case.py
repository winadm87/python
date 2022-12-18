# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# Switcher for implementing switch case options
def job_details(ID):
    switcher = {
        "100": "Job Description: Software Engineer",
        "200": "Job Description: Lawyer",
        "300": "Job Description: Graphics Designer",
    }
    # The first argument will be returned if the match found and
    # nothing will be returned if no match found
    return switcher.get(ID, "nothing")

# Take the job ID
job_id = input("Enter the job ID: \n")
# Print the output
print(job_details(job_id))