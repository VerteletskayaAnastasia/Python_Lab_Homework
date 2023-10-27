list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
half_of_players = int(len(list_players)/2)
team_1 = list_players[:half_of_players]
team_2 = list_players[half_of_players::]
print(team_1)
print(team_2)