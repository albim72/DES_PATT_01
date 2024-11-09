class FootballTeamIterator:
    def __init__(self,members):
        self.members = members
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.members):
            val = self.members[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration()

class FootballTeam:
    def __init__(self,members):
        self.members = members

    def __iter__(self):
        return FootballTeamIterator(self.members)

def main():
    members = [f'gracz {str(x)}' for x in range(1,23)]
    members = members + ["trener 1", "trener 2", "trener 3", "fizjoterapeuta", "lekarz", "psycholog", "rzecznik"]
    team = FootballTeam(members)

    team_it = iter(team)

    try:
        while True:
            print(next(team_it))
    except StopIteration as si:
        print(si)


if __name__ == '__main__':
    main()
