class PartyAnimal:
    def __init__(self, nam: str):
        self.x = 0
        self.name = nam
        print(f'{self.name} Constructed')

    def party(self):
        self.x += 1
        print(f'{self.name} party contains {self.x}')


