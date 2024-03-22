
#user inputs  - Add password, delete password, show passwords



#maybe change them to 'add' so they ca be called from zsh in thw terminal



def main(): 
    user = input("Hi!, Enter an action to continue (A = Add passwords  S = Show passwords  D = Delete password  Q = Quit): ")
    while True: 
        if user == "A" or user == 'a':
            add_pass()
            break
        if user == "D" or user == 'd':
            #delete_pass()
            break
        if user == "S" or user == 's':
            #show_pass()
            break
        if user == "Q" or user == 'q':
            print("You have exited your Password Manager")
            break
        else:
            user = input("Hi!, Enter an action to continue (A = Add passwords  S = Show passwords  D = Delete password): ")


            







def add_pass(): 
    company = input("Enter the Company you are assigning credentials for: ")
    while True:
        #company = input("Enter the Company you are assigning credentials for: ")
        addition = input("Enter the (Username, Password) Credentials you want to add: ").strip()
        with open("pass_protect.txt", "a") as f:
            if addition == "q" or addition == "Q":
                break
            else:
                new = f.write(company + ": " + addition + "\n")
                print("Password has now been added to your Personal file")
    main()





if __name__ == '__main__': 
    main()
    