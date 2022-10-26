import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),    # 16
            Player("Lemieux", "PIT", 45, 54),   # 99
            Player("Kurri",   "EDM", 37, 53),   # 90
            Player("Yzerman", "DET", 42, 56),   # 98
            Player("Gretzky", "EDM", 35, 89)    # 124
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReaderStub()
        self.statistics = Statistics(self.reader)
    
    def test_search_player(self):
        # check that stats' player search returns the correct player
        result_player = self.statistics.search("Kurri")
        self.assertEqual(str(result_player), "Kurri EDM 37 + 53 = 90")
    
    def test_search_nonexistent_player(self):
        # check that stats' player search returns None when searching player that doesn't exist
        result_player = self.statistics.search("Lahtinen")
        self.assertEqual(result_player, None)
    
    def test_team_player_listing(self):
        # check that stats returns correct list of players in a specific team
        team_players = [str(player) for player in self.statistics.team("EDM")]
        edm_team_players = [str(player) for player in self.reader.get_players() if player.team == "EDM"]
        self.assertSequenceEqual(team_players, edm_team_players)
    
    def test_top_player(self):
        # check that stats return correct list of players based on their points
        # NOTE: parameter of `statistics.top` is zero-based, which I think is a feature, not a bug
        #       That is why parameter value 1 should return two top players.
        top_players = [str(player) for player in self.statistics.top(1)]
        correct_players = [
            str(self.reader.get_players()[4]),
            str(self.reader.get_players()[1])
        ]
        self.assertSequenceEqual(top_players, correct_players)
