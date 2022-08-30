# Marca, Model, Price
class Game:
    def __init__(self, empresa, nome, preço):
        self.empresa = empresa
        self.nome = nome
        self.preço = preço

    def __repr__(self):
        return self.nome

    def bordao(self):
        print("It's Showdown")

    def bordao2(self):
        print("Become a champion of the Realm")

    def abertura(self):
        print("Hunters gotta Hunt")

    def abertura2(self):
        print("Welcome to Paladins")

    def show_info(self):
        print(self.empresa, self.nome, self.preço)

game1 = Game('Crytek', 'Hunt Showdown', '20 dollars')
#game2 = Game('Hi Rez', 'Paladins', 'Your Life')
game1.bordao()
game1.abertura()
game1.show_info()
#game2.abertura2()
#game2.bordao2()
#game2.show_info()





