import random

# array of goodRespone and errorResponse
goodResponse = ["Nice work!" , "Keep up the good work!", "Very good!",  "Excellent",]
errorResponse = ["Wrong. Try once more.", "No. Please try again.", "Don't give up!", "No. Keep trying."]

#addition function to add two numbers
def addition():
    correct = 0
    wrong = 0
    if (difficulty == "1"):
        rangeValue = 9
    if(difficulty=="2"):
        rangeValue = 99
    #get two numbers    
    num1 = random.randint(0,rangeValue)
    num2 = random.randint(0,rangeValue)
    
    print("\nHow much is ", num1, "+" , num2)
    #ask user to enter answer
    result = input("Enter your answer (-1 to exit): ")
    
    res = str(num1+num2)
    
    if(result == "-1"):
        return -1
    if(result == res):
        correct+=1
        print(goodResponse[random.randint(0,len(goodResponse)-1)])
    else:
        wrong+=1
        print(errorResponse[random.randint(0,len(errorResponse)-1)])
    return 0

#substraction function to subtract two numbers
def subtraction():
    correct = 0
    wrong = 0
    if (difficulty == "1"):
        rangeValue = 9
    if(difficulty=="2"):
        rangeValue = 99
        
    #get two numbers     
    num1 = random.randint(0,rangeValue)
    num2 = random.randint(0,rangeValue)
    
    if(num1<num2):
        num1,num2 = num2,num1
        
    print("\nHow much is ", num1, "-" , num2)
    #ask user to enter answer
    result = input("Enter your answer (-1 to exit): ")

    res = str(num1-num2)
    
    if(result == "-1"):
        return -1
    if(result == res):
        correct+=1
        print(goodResponse[random.randint(0,len(goodResponse)-1)])
    else:
        wrong+=1
        print(errorResponse[random.randint(0,len(errorResponse)-1)])
    return 0

#function to multiply two numbers
def multiplication():
    correct = 0
    wrong = 0
    if (difficulty == "1"):
        rangeValue = 9
    if(difficulty=="2"):
        rangeValue = 99
        
    #get two numbers     
    num1 = random.randint(0,rangeValue)
    num2 = random.randint(0,rangeValue)
    
    print("\nHow much is ", num1, "*" , num2)
    #ask user to enter answer
    result = input("Enter your answer (-1 to exit): ")

    res = str(num1*num2)
    
    if(result == "-1"):
        return -1
    if(result == res):
        correct+=1
        print(goodResponse[random.randint(0,len(goodResponse)-1)])
    else:         
        wrong+=1
        print(errorResponse[random.randint(0,len(errorResponse)-1)])
    return 0

#function to do division
def division():
    correct = 0
    wrong = 0
    if (difficulty == "1"):
        rangeValue=9
    if(difficulty=="2"):
        rangeValue = 99

    #get two numbers 
    num1 = random.randint(1,rangeValue)
    num2 = random.randint(1,rangeValue)
    
    print("\nHow much is ", num1, "/" , num2)
    #ask user to enter answer
    result = input("Enter your answer (-1 to exit): ")

    res = str(num1/num2)
    
    if(result == "-1"):
        return -1
    if(result == res):
        correct+=1
        print(goodResponse[random.randint(0,len(goodResponse)-1)])
    else:
        wrong+=1
        print(errorResponse[random.randint(0,len(errorResponse)-1)])
    return 0

def options(option):
    exitValue = 0
    if(option == 1):
        exitValue = addition()
    elif(option == 2):
        exitValue = subtraction()
    elif(option == 3):
        exitValue = multiplication()
    elif(option == 4):
        exitValue = division()
    else :
        option = random.randint(1,4) #for random operation
        options(option)
    return exitValue

# function for operation Menu
def operationMenu():
    print("\n1 : Addition")
    print("2 : Subtraction ")
    print("3 : Multiplication ")
    print("4 : Division ")
    print("5 : Random operation")
    
    # getting operation type from user
    option = int(input("Enter the operation (1 to 5):"))
    exitValue = options(option)
    if(exitValue == -1):
        return
    operationMenu()
    
#ask user to enter the difficulty level
difficulty = input("Enter difficulty Level(1 or 2) : ")
operationMenu()
print("Number of correct answers :",correct)
print("Number of wrong answers :",wrong)
print("Thanks for playing!")




