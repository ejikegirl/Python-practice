#the if statement
userReply = int (input("How many bananas do you have?"))
if userReply >= 5:
    print("You have a bunch of bananas.")
elif userReply >= 1 and userReply <= 4:
    print("You have a small bunch of bananas.")
else:
    print("You do not have any bananas.")


