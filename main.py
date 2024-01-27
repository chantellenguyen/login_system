acounts = [["channy", "hi"], ["levy", "nguyen"]]
status = []


def signup(username, password):
    canSignUp = True
    # loop the existing accounts

    for a in acounts:
        # a[0] repersents account names
        if username == a[0]:
            print("username exists - sign up failed")
            canSignUp = False

    if (canSignUp):
        acounts.append([username, password])

    menu()


def login(username, password):
    loggedin = False
    # loop the acount list
    for a in acounts:
        # check if username and password matches
        # a[0] reperssents username and a[1] repersents password
        if (a[0] == username and a[1] == password):
            print("succesfully logged in!!!!!!")
            loggedin = True
            submenu()

    if loggedin == False:
        print("login unsucessful")


def post():
    userquotes = input("write a status to post: ")
    status.append(userquotes)

    print("posting status: " + userquotes)
    submenu()


def submenu():
    print("choose an option")
    print("1. post a status")
    print("2. view all statuses")
    print("3. edit a  status")
    print("4.delete a status")
    userchoice = input("choose a status.")

    if (userchoice == "1"):
        print("post a status")
        post()
    elif (userchoice == "2"):
        print("view all statuses")
    elif (userchoice == "3"):
        print("edit a status")
    else:
        print("delete a status")


def menu():
    print("welcome to channyscord (discord but worse")
    userchoice = input("do you want to sign up or login. ")
    if (userchoice == "sign up"):
        print("sign up")
        username = input("plz give us your username: ")
        password = input("plz give password: ")
        signup(username, password)
    elif (userchoice == "login"):
        print("login")
        username = input("plz give us your username: ")
        password = input("plz give password: ")
        login(username, password)
    else:
        print("invalid choice")


menu()

