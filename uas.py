import kdf
import db
import sha256hasher


#g_hasher = kdf.hasher()
g_hasher = sha256hasher.sha256hasher()
g_db = db.userdb()
g_users = g_db.connect()

def showoptions():
    print("Choose an option...\n")
    print("1: Register new user\n")
    print("2: Login\n")
    print("3: Change password\n")
    print("4: Reset password\n")
    print("Any other key to exit\n")
    try:
        i_option = input()
        i_option = int(i_option)
    except ValueError:
        return -1
    return i_option

def showuserslist():
    #print(g_users)
    g_db.showrecords()

def userexists(uname):
    if uname in g_users:
        return True
    return False

def registeruser():
    print("Enter username")
    uname = input()
    print("Enter password")
    passw = input()

    uname = uname.strip()
    passw = passw.strip()
    if userexists(uname):
        print("ERROR: user name already exists")
        return

    hpassw = g_hasher.hashpassword(passw)
    g_users[uname] = hpassw
    g_db.insert(uname,hpassw)
    
def login():
    print("Enter username")
    uname = input()
    print("Enter password")
    passw = input()
    uname = uname.strip()
    passw = passw.strip()
    if not userexists(uname):
        print("User name doesn't exist.")
        return

    if g_users[uname] != g_hasher.hashpassword(passw):
        print("Password incorrect.")
        return

    print("Successfully loggedin")
    
def changepassword():
    print("change password\n")

    
def main():
   
    while True:
        option = showoptions()
        if option == 1:
            registeruser()
        elif option == 2:
            login()
        elif option == 3:
            changepassword()
        elif option == 4:
            #resetpassword()
            pass
        elif option == 5:
            showuserslist()
        else:
            break
        


def main1():
   
    #h = kdf.hasher()
    h = sha256hasher.sha256hasher()
    hp1 = h.hashpassword("password1")
    hp2 = h.hashpassword("password2")
    print(hp1)
    print(hp2)

    hp1 = h.hashpassword("password1")
    hp2 = h.hashpassword("password2")

    print(hp1)
    print(hp2)
    print(h.verifypassword(hp1,"password1"))
    print(h.verifypassword(hp1,"password2"))


# def main2():
#     h = kdf.hasher()
#     d = db.userdb()
#     d.connect()
#     d.insert("user1","password1")
#     d.insert("user2","password2")
#     d.showrecords()

if __name__ == "__main__":
    main()
    
