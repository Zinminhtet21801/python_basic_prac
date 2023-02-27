class PlayerCharacter:
    membership = True

    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('zin')
player2 = PlayerCharacter('zain')
print(player1.run())
print(player2.adding_things(2, 3))
# help(player1)
