username = input("Enter user name:")
password=""
attempt=0
flag=0
while(attempt!=5):
    password=input("Enter password:")
    if (password=="changeme"):
        flag=1
        break
    else:
        attempt=attempt+1
        if(attempt==5):
            print("Incorect password")
            print("You have five maximum attempts,Access Denied")
if(flag==1):
    print("Password accepted")
    print("Welcome",username)
