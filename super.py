class User:
    # def __init__(self, email):
    #     self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        # super().__init__(email)

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


# wizard = Wizard('Merlin', 50, 'merlin@gmail.com')
# wizard = Wizard('Merlin', 50,)
# print(wizard)

hybridBitch = HybridBorg('Borgie', 50, 100)

print(hybridBitch.name, hybridBitch.power, hybridBitch.num_arrows)