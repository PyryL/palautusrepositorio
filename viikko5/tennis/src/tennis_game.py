
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.name1 = player1_name
        self.name2 = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.name1:
            self.score1 += 1
        else:
            self.score2 += 1
        
    def _score_to_text(self, score):
        if score > 3:
            return "Deuce"
        texts = ["Love", "Fifteen", "Thirty", "Forty"]
        return texts[score]
    
    def _deuce_text(self):
        difference = self.score1 - self.score2
        beginning = "Advantage" if abs(difference) == 1 else "Win for"
        player_name = self.name1 if difference > 0 else self.name2
        return f"{beginning} {player_name}"

    def get_score(self):
        if self.score1 == self.score2:
            if self.score1 > 3: return "Deuce"
            return self._score_to_text(self.score1) + "-All"
        elif self.score1 >= 4 or self.score2 >= 4:
            return self._deuce_text()
        else:
            return self._score_to_text(self.score1) + "-" + self._score_to_text(self.score2)
