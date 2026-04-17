import random

while True:
    print("Football Match Predictor")
    print("------------------------")
    home_team = input("Enter home team: ")
    away_team = input("Enter away team: ")
    print(home_team, "vs" , away_team, "prediction")
    home_goals = random.randint (0,5)
    away_goals = random.randint (0,5)

    print(home_team, home_goals, "-", away_goals, away_team)

    if home_goals > away_goals:
        print(home_team, "wins!")
    elif home_goals < away_goals:
        print(away_team, "wins!")
    else: 
        print("It's a draw!")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break