
#function to display the menu
def displayMenu():
    
    print("\nMenu")
    print("-----------------------------------")
    print("1.Look up an email address")   
    print("2.Add a new name and email address")
    print("3.Change an existing email address")
    print("4.Delete a name and email address")
    print("5.Quit the program")

    #ask user to enter the option
    option=int(input("\nEnter your choice: "))
    return option

#function for look up email address
def lookUpEmail(emailDict, name):
    if name in emailDict.keys():
        return emailDict[name]

#function to add name and email address    
def addNameEmail(emailDict, name, email):
    if name not in emailDict:
        emailDict[name] = email
        print("Name and address have been added")
    else:
        print("That name already exists\n")

#function for change an existing email
def changeEmail(emailDict, name, newemail):
    if name in emailDict.keys():
        emailDict[name] = newemail

#funtion to delete name and email address
def deleteNameEmail(emailDict, name):
    if name in emailDict.keys():
        emailDict[name]=None
        del emailDict[name]
        print("Information deleted")
    else:
        print("The specified name was not found\n")

#function for load and read information from the file
def loadFromFile():
    emailDict=dict()
    try:
        f = open('emails.txt', 'r') 
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            emailDict[lines[i].strip()] = lines[i+1].strip()
        f.close()
    except:
        pass
    return emailDict

#function to save all information in a file
def saveInFile(emailDict):   
    f = open('emails.txt', 'w')
    for key, value in emailDict.items():
        f.write(key+"\n")
        f.write(value+"\n")
    f.close()

#main function
def main():
    emailDict = loadFromFile()
    while True:
        choice = displayMenu()
        if choice==1:
            name=input("Enter a name: ")
            try:
                email=lookUpEmail(emailDict, name)
                if(email!=None):
                    print("Name:",name)
                    print("Email:",email)
                else:
                    print("The specified name was not found")
            except:
                print("The specified name was not found")
        elif choice==2:
            name=input("Enter name: ")
            email=input("Enter email Address: ")
            addNameEmail(emailDict, name, email)
            
        elif choice==3:
            name=input("Enter name: ")
            email=input("Enter new address: ")
            changeEmail(emailDict, name, email)
            print("Information updated")
        elif choice==4:
            name=input("Enter the name: ")
            try:
                deleteNameEmail(emailDict, name)
            except:
                print("Something went wrong!!! please try again later")
        elif choice==5:
            saveInFile(emailDict)
            print("Information saved")
            break;
        else:
            print("invalid input")


main()



