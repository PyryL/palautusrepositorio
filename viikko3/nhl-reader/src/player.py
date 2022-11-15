class Player:
    def __init__(self, name, team, nationality, goals, assists):
        self._name = name
        self._team = team
        self._nationality = nationality
        self._goals = goals
        self._assists = assists
        self._name_field_length = len(name)
    
    @property
    def nationality(self):
        return self._nationality
    
    @property
    def points(self):
        return self._goals + self._assists
    
    def set_name_field_length(self, length):
        self._name_field_length = length
    
    def __str__(self):
        return f"{self._name:<{self._name_field_length}} {self._team} {self._goals:>2} + {self._assists:>2} = {self.points:>2}"
