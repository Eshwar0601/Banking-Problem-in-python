

def main():
    userAccountBallence = 0
    user1Bal = 0
    user2Bal = 0
    DoMenu = True
    while DoMenu:
        print("========================================================================")
        print(" press 1 for deposit")
        print(" press 2 for withdraw")
        print(" press 3 for checking balence")
        print(" press 4 for money transfer")

        userTask = int(input(" what do you want to do?  :"))

#       depositing amount
        if(userTask == 1):
            depAmount = int(input("Enter the amount to be deposited :"))
            userAccountBallence += depAmount
            print("your available balence is", userAccountBallence, "rupees.")        

 #      withdrawing amount               
        elif(userTask == 2):
            withDrawAmount = int(input("enter the amount to be withdrawn! :"))
            if(userAccountBallence >= withDrawAmount):
                userAccountBallence -= withDrawAmount
                print(withDrawAmount,"has been withdrawed from your account!")
            else:
                print("Your balence is insufficient for withdrawal")    

#       checking ballence         
        elif(userTask == 3):
            print(" press 1 for checking Your ballence ")
            print(" press 2 for checking user1 ballence ")
            print(" press 3 for checking user2 ballence ")
            balCheck = int(input("Whose account ballence do you want to check ?"))
            if(balCheck == 1):
                print("your available balence is", userAccountBallence, "rupees.")
            elif(balCheck == 2):
                print("user1 available balence is", user1Bal, "rupees.")
            elif(balCheck == 3):
                print("user2 available balence is", user2Bal, "rupees.")
                
#       amount transfer
        elif(userTask == 4):
            print(" we have two active users to send the money ")
            print(" press 1 to send the money to User1")
            print(" press 2 to send the money to User2")
            transferUser = int(input(" to whome do you want to send ? "))
            transferAmount = int(input(" enter the amount to send :"))              
            if(transferUser == 1):
                #transferAmount = int(input(" enter the amount to send :"))
                if(userAccountBallence >= transferAmount):
                    userAccountBallence -= transferAmount
                    user1Bal += transferAmount
                else:
                    print(" Transaction cannot proceed due to insufficient balence ")
            elif(transferUser == 2):
                if(userAccountBallence >= transferAmount):
                    userAccountBallence -= transferAmount
                    user2Bal += transferAmount
                else:
                    print(" Transaction cannot proceed due to insufficient balence ")
                







main()