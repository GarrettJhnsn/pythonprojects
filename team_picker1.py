from random import choice

## -- players       ---- Holds the data value for inputed players
## -- teams         ---- Holds the data value for inputed teams
## -- team_b,team_a ---- Holds three players names in a and three player names in b

players = []
teams = []
team_b = []
team_a = []


print("####                   Random Team Generator                ####")
print("#### You will have to enter six different names for players ####")
print("#### then you will be prompted to insert two team names!    ####")
print("#### the two teams of three will be generated with the      ####")
print("#### with the information provided by the user!\n")


## User will be prompted to insert a player's name
## User will be prompted each time to insert a players name until he had inputed six different names
## When the user inputs the name the data is stored = players as a set of values
## This continues until the user has inputed all six names

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

## User will be prompted to insert a team name
## User will create two teams

print("#### Next please insert two team names ####\n")

team_name1 = input("Insert First Team Name: \n")
teams.append(team_a)

team_name2 = input("Insert Second Team Name: \n\n")
teams.append(team_b)

## After all inputs have be established the program will start randomly pulling a name
## Inserting it into team_a until there are three names left in the players set.
## Everytime a player is added to either team_a or team_b it is also being removed from the players set list
## Once it has assigned three players to team_a it will assign all remaining players to team_b
## Because team_a stops assigining when three players are left in the set and team_b stops once there are no remaining players
## Team_b will not start pulling names until team_a is completed its function

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

## After assiging names randomly to different teams the program will print the team name value given from the user
## Below the team name it will display all of the assigned players of that Team.

print("Team",team_name1)
print(team_a)

## Ref line 64-75 for explanation of team_b

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
print(team_b, "\n")

print("Thanks for using my program!")
print("Created by Garrett Johnson,2018")


