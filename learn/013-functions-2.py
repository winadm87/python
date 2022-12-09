# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# create fun to create dict
def create_record(name,tel,addr):
    """create record for db - dict"""
    record = {
        'name': name,
        "phone": tel,
        "address": addr
    }
    return record
user1 = create_record("vasya", "+7 911 12312312", "tunisia")
user2 = create_record("petka", "123123", "spb")
print(user1)
print(user2)

def give_award(medal,*persons):
    """award people"""
    for person in persons:
        print("someone " + person.title() + " take award " + medal)

give_award("za 5letky", "vasya", "petya")
give_award("za lyny", "masha", "lena")