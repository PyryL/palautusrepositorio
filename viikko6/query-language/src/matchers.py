class QueryBuilder:
    def __init__(self, and_matchers = [], or_matchers = []):
        self._and_matchers = and_matchers
        self._or_matchers = or_matchers

    def playsIn(self, team):
        new_and_matchers = self._and_matchers[:]
        new_and_matchers.append(PlaysIn(team))
        return QueryBuilder(new_and_matchers)

    def hasAtLeast(self, value, attr):
        new_and_matchers = self._and_matchers[:]
        new_and_matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(new_and_matchers)

    def hasFewerThan(self, value, attr):
        new_and_matchers = self._and_matchers[:]
        new_and_matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(new_and_matchers)

    def oneOf(self, *matchers):
        return QueryBuilder(or_matchers=matchers)

    def build(self):
        if len(self._or_matchers) > 0:
            return Or(*self._or_matchers)
        return And(*self._and_matchers)

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value
