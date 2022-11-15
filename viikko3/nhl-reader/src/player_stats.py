
class PlayerStats:
    def __init__(self, player_reader):
        self._player_reader = player_reader
    
    def top_scorers_by_nationality(self, nationality):
        all_players = self._player_reader.get_players()
        players = list(filter(lambda p : p.nationality == nationality, all_players))
        players.sort(key=lambda p : p.points, reverse=True)
        return players
