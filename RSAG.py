import random
RSAG_list = ["Swimming", "Picnicing", "Biking", "Hiking", "Camping","Kiting"]
def RSAG():
    while True:
        rdm = "Sorry, there are no more activities available"
        if RSAG_list == []:
            print (rdm)
            break
        rdm = random.choice(RSAG_list)
        if rdm in RSAG_list:
            print("You got", rdm)
            print("\n")
            rdmC = input("Do you want to get a different activity?: ")
            if rdmC == "no":
                print("Have fun", rdm,"!")
                break
            elif rdmC == "yes":
                print("Rolling Another activity\nRemoving previous activity from list\n")
                if rdm == "Swimming":
                    RSAG_list.remove("Swimming")
                elif rdm == "Picnicing":
                    RSAG_list.remove("Picnicing")
                elif rdm == "Biking":
                    RSAG_list.remove("Biking")
                elif rdm == "Hiking":
                    RSAG_list.remove("Hiking")
                elif rdm == "Camping":
                    RSAG_list.remove("Camping")
                elif rdm == "Kiting":
                    RSAG_list.remove("Kiting")
                else:
                    print("sorry, there are no more activities available")
                    break
            else:
                print("Invalid input (yes / no)")
                print("\n")
                print("rolling different activity")
                print("\n")
RSAG()