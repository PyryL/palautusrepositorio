import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []
    longestName = -1

    for player_dict in response:
        if player_dict['nationality'] != "FIN":
            continue
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['nationality'],
            player_dict['goals'],
            player_dict['assists']
        )
        players.append(player)
        if len(player_dict['name']) > longestName:
            longestName = len(player_dict['name'])
    
    players.sort(key=lambda p : p.points, reverse=True)

    for player in players:
        player.set_name_field_length(longestName)
        print(player)

if __name__ == "__main__":
    main()
