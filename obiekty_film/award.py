class AwardWinning:
    def __init__(self):
        self.awards = []

    def add_award(self,award:str):
        self.awards.append(award)

    def get_award(self)->list:
        return self.awards
