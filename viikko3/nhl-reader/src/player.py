class Player:
    def __init__(self, name, team, nationality, goals, assists):
        self._name = name
        self._team = team
        self._nationality = nationality
        self._goals = goals
        self._assists = assists
    
    @property
    def nationality(self):
        return self._nationality
    
    def __str__(self):
        return f"{self._name} team {self._team} goals {self._goals} assists {self._assists}"
