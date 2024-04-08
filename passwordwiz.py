def password_checker(username,password):
 
    if(len(password)<8):
        
        return "weak:password should have more than 8 characters"
        
        
    elif not any(letter.isupper() for letter in password):
        
        return("weak:password should have atleast one capital letter")
        
    elif not any(letter.islower() for letter in password):
        
        return("weak:password should contain at leant on lower case letter")
        
    elif not any(letter.isdigit() for letter in password):
        
        return("weak:password should have atleast one digit")
        
    elif not all (letter.isalnum() for letter in password):
        
        return("weak:password should only have alphanumeric values and spaces")
         
    else:   
        with open("passwords.txt","a") as file:
            file.write("username:{}||password:{}\n".format(username,password))
        return("password has been saved under the username,'{}'".format(username))
        
#----------------------------------------------------------------------------#
def main():
    global count
    global count_N
    global password
    global username

    username=input("enter you username:")
    password=input("enter your password:")
    result=password_checker(username,password,)
    if("saved" in result):
        count+=1
    elif("weak" in result):
        count_N+=1
    print(result)
#----------------------------------------------------------------------------#
def password_generator(input1):
    if(input1=="1"):
        with open("passwords.txt","a") as file:
            file.write("username:{}||password:{}\n".format(username,username+".123"))
        print("password has been saved to {} under the username {}".format(username+".123",username))
    elif(input1=='2'):
        random_generator()
    elif(input1=='Quit'):
        pass
#----------------------------------------------------------------------------#
def random_generator():
    password_length=10
    password=(secrets.token_urlsafe(password_length))
    
    with open("passwords.txt","a") as file:
        file.write("username:{}||password:{}\n".format(username,password))
    print("A random password has been saved under the username {}".format(username))

#----------------------------------------------------------------------------#
def END():
    print("THANK YOU FOR USING PASSWORDWIZ :)")
#----------------------------------------------------------------------------#
print("----------WELCOME TO PASSWORDWIZ!!!-----------------")

import secrets
count_N=0
count=0
main()
while count==0:
    main()
    if(count_N==2):
        input1=input("You can also do:\n1.Use username as password \n2.Random password\n3.Quit")
        password_generator(input1)
        break
    else:
        END()
    
last=input("You can: \n1.view existing passwords \n2.clear all your passwords\n3.quit")
if(last=='1'):
    with open("passwords.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            print(line)
        print("These are all the saved passwords :)")
elif(last=='2'):
    file=open("passwords.txt","w")
    file.write("")
    print("cleared:)")
elif(last=='3'):
    END()


    
