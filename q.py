import random

comp_wins = 0
player_wins = 0
while comp_wins < 3 and player_wins < 3:
    user = input("Ваш вариант:")
    comp = random.choice(["Камень", "Ножницы", "Бумага"])
    print("Комп выбрал:", comp)

    if user == comp:
        print("Ничья")
    elif user == "Камень":
        if comp == "Ножницы":
            print("Игрок победил")
            player_wins += 1
        else:
            print("Комп победил")
            comp_wins +=1

    elif user == "Ножницы":
        if comp == "Бумага":
            print("Игрок победил")
            player_wins += 1
        else:
            print("Комп победил")
            comp_wins +=1

    elif user == "Бумага":
        if comp == "Камень":
            print("Игрок победил")
            player_wins += 1
        else:
            print("Комп победил")
            comp_wins += 1
    print("Счёт:", player_wins, "-", comp_wins)
print("Счёт:", player_wins, "-", comp_wins)
if player_wins > comp_wins:
    print("Победил игрок")
else:
    print("Победил комп")
