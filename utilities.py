import dbMethods as db
import sys
import Faker

# initiate faker to create dummy data
fake = Faker()


def create_users(qty):
    for i in range(qty):
        db.create_user({
            "title": fake.prefix(),
            'first_name': fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number()})

def find_user(id):
    user = db.find_user_id(id)
    print(user)

def update_user(id, first_name):
    db.update_user(user_id = id, first_name = first_name)

def delete_user(id):
    db.delete_user(id)

if __name__ == "__main__":
    # user can add a number of users as an argument
    if sys.argv[1] == "create":
        db.create_users(int(sys.argv[2]))
        
    elif sys.argv[1] == "find":
        db.find_user(sys.argv[2])
    
    elif sys.argv[1] == "update":
        db.update_user(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "delete":
        db.delete_user(sys.argv[2])

    elif sys.argv[1] == "create":
        db.create_table()

    elif sys.argv[1] == "make-table":
        db.make_table()

    else:
        print("No option selected")

