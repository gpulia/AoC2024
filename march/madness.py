import random as r
import math as m
with open('data.txt', 'r') as file:
    data = file.read()
    data_dict = {}
    for line in data.splitlines():
        parts = line.split()
        key = parts[0]
        values = list(map(int, parts[1:4]))  # Convert values to integers
        data_dict[key] = values
    while(True):
        team1 = input("Enter the first team: ")
        team2 = input("Enter the second team: ")
        if team1 in data_dict and team2 in data_dict:
            print(f'{team1} vs {team2}')
            print(f'{data_dict[team1]} vs {data_dict[team2]}')
            if data_dict[team1][0] - data_dict[team2][0] < 0:
                higherseed = team1
                lowerseed = team2
            else:
                higherseed = team2
                lowerseed = team1
            print(f'{higherseed=}')
            seed_diff = abs(data_dict[higherseed][0] - data_dict[lowerseed][0])
            attitude = (seed_diff * 20/15) / 100
            print(f'{attitude=}')
            offense = (data_dict[higherseed][1] * (1+attitude)) + data_dict[lowerseed][2]*(1+attitude)
            defense = (data_dict[higherseed][2] *(1-attitude)) + data_dict[lowerseed][1]*(1-attitude)
            print(f'{offense=} {defense=}')
            randOffense = (r.randint(0,40)-20)/100
            randDefense = (r.randint(0,40+round(seed_diff*1.5))-20)/100
            print(f'{randOffense=} {randDefense=}')
            calcOffense = offense * (1+randOffense)
            calcDefense = defense * (1+randDefense)
            print(f'{calcOffense=} {calcDefense=}')
            if calcOffense > calcDefense:
                print(f'{higherseed} wins by {calcOffense - calcDefense}!')
            else:
                print(f'{lowerseed} wins by {calcDefense - calcOffense}!')
        else:
            print("Invalid team names. Please try again.")
            continue
        
