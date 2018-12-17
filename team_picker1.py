from random import choice


players = []
teams = []
team_b = []
team_a = []


print("####                   Random Team Generator                ####")
print("#### You will have to enter six different names for players ####")
print("#### then you will be prompted to insert two team names!    ####")
print("#### the two teams of three will be generated with the      ####")
print("#### with the information provided by the user!\n")


player_name1 = input("Insert First Player Name: \n")
players.append(player_name1)

player_name2 = input("Insert Second Player Name: \n")
players.append(player_name2)

player_name3 = input("Insert Third Player Name: \n")
players.append(player_name3)

player_name4 = input("Insert Fourth Player Name: \n")
players.append(player_name4)

player_name5 = input("Insert Fifth Player Name: \n")
players.append(player_name5)

player_name6 = input("Insert Sixth Player Name: \n")
players.append(player_name6)



print("#### Next please insert two team names ####\n")

team_name1 = input("Insert First Team Name: \n")
teams.append(team_a)

team_name2 = input("Insert Second Team Name: \n")
teams.append(team_b)
print("\n")



while len(players) > 3:
    player_1 = choice(players)
    team_a.append(player_1)
    players.remove(player_1)

    player_2 = choice(players)
    team_a.append(player_2)
    players.remove(player_2)

    player_3 = choice(players)
    team_a.append(player_3)
    players.remove(player_3)




print("Team",team_name1)
print(team_a)



while len(players) > 0:
    player_4 = choice(players)
    team_b.append(player_4)
    players.remove(player_4)

    player_5 = choice(players)
    team_b.append(player_5)
    players.remove(player_5)

    player_6 = choice(players)
    team_b.append(player_6)
    players.remove(player_6)

print("Team", team_name2)
print(team_b)
print("\n")

print("Thanks for using my program!")
print("Created by Garrett Johnson,2018")


