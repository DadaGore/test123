userReply = input("Do we need to ship a package? (Enter yes or no) : \n")

if userReply == "yes" :
    print("We can help you to ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
userReply1 = input("Would you like to buy stamps, buy an envelope, or make a copy? (enter stamp, envelope or copy) : \n")
if userReply1 == "stamp" : 
    print("We have many stamp design to choose from.")
elif userReply1 == "envelope" :
    print("We have many envelope to choose from.")
elif userReply1 == "copy":
    copies = input("How many copies do you like to take (Enter a number) : \n")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you. Please come again.")