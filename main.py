import random


def enter_names():

    players = []
    print("SECRET SANTA MATCHUP SCRIPT")
    print("Three or more names required")
    print("How many names do you want to enter?: ")
    num_of_players = int(input())
    count = num_of_players - (num_of_players - 1)

    while num_of_players > 0:
        print(f"Please enter name {count}: ")
        name = input()
        players.append(name)
        count += 1
        num_of_players -= 1

    return players


def go(giver_list):

    #copy the list so that we can use one as the 'givers' list and the other as the 'receivers' list
    receiver_list = giver_list[:]

    #create an empty list to store all the matchups
    santas = []

    #while loop will remove a player from each list at random
    while len(giver_list)>0:
        print("giver list: ", giver_list)
        giver = giver_list.pop(random.randint(0, len(giver_list)-1))
        print(giver)
        print("receiver list: ", receiver_list)
        receiver = receiver_list.pop(random.randint(0, len(receiver_list)-1))
        print(receiver)

        #before confirming the matchup, check to make sure the giver and receiver isn't the same person
        #if they are the same, we add those players back to their respective lists and redraw above
        if giver == receiver:
            giver_list.append(giver)
            receiver_list.append(receiver)
            print("draw was equal here")
        #once duplicate check is passed, create the matchup and add said matchup to the santas list
        else:
            #one last check to ensure when we get to the end, that the last person on each list isnt the same person
            if len(giver_list) == 1 and giver_list[0] == receiver_list[0]:
                giver_list.append(giver)
                receiver_list.append(receiver)
                print("*****THE FINAL CHECK WORKS WOOHOO******")
            else:
                matchup = [giver, receiver]
                print("this is the matchup: ", matchup)
                santas.append(matchup)
                print("santa list so far: ",santas)

    return santas


players = enter_names()


santas = go(players)


print(santas)