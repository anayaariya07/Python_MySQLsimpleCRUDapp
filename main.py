from dbhelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print("********WELCOME************")
        print()
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()
        try:
            choice = int(input())
            if(choice == 1):
                uid = int(input("Enter userId :"))
                username = input("Enter userName :")
                userphone = int(input("Enter userPhone:"))
                db.insert_user(uid, username, userphone)
                #pass
            elif choice == 2: #display
                db.fetch_all()
                pass
            elif choice == 3: #delete
                userid= int(input("Enter uid to delete :"))
                db.delete_user(userid)
               # pass
            elif choice == 4: #update4
                uid = int(input("Enter userId :"))
                username = input(" new Name :")
                userphone = int(input(" new Phone :"))
                db.update_user(uid, username, userphone)
                
                #pass
            elif choice == 5:
                break
            else:
                print("invalid input ! try again")
        except Exception as e:
            print("e")
            print("Invalid details ! try again")

if __name__ == "__main__":
    main()

        



# main coding        
#helper = DBHelper()
#helper. insert_user(300,"Piya", "3452")
#helper. insert_user(301,"Siya", "3452")
#helper. insert_user(302,"Jiya", "3452")
#helper. insert_user(303,"Hiya", "3452")
#helper.fetch_all()
#helper.update_user(1423,"Yoho", '7481')
#helper.fetch_all()