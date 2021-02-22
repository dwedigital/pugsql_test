import dbMethods as db
import sys


if __name__ == "__main__":
    # user can add a number of users as an argument
    if sys.argv[1] == "make_users":
        db.create_users(int(sys.argv[2]))
    elif sys.argv[1] == "find":
        db.find_user(sys.argv[2])
    
    elif sys.argv[1] == "update":
        db.update_user(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "delete":
        db.delete_user(sys.argv[2])

    elif sys.argv[1] == "create":
        db.create_table()

    else:
        print("No option selected")

